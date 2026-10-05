"""Coleta um recorte explícito de patentes. Apenas biblioteca padrão Python."""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen
import uuid

NASA_BASE = "https://technology.nasa.gov/api/api/patent/"


def now():
    return datetime.now(timezone.utc).isoformat()


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def clean(value):
    parser = PlainText()
    parser.feed(str(value or ""))
    return " ".join("".join(parser.parts).split())


def request_json(url, headers=None, data=None):
    body = None if data is None else json.dumps(data).encode("utf-8")
    for attempt in range(3):
        try:
            req = Request(url, data=body, headers={"Accept": "application/json", **(headers or {})})
            with urlopen(req, timeout=35) as response:
                raw = response.read()
                if not raw:
                    return None
                if "json" not in response.headers.get("Content-Type", "").lower():
                    raise ValueError("Resposta não JSON; confira o endpoint.")
                return json.loads(raw)
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise RuntimeError(f"Falha HTTP {error.code}") from None
        except (URLError, TimeoutError):
            if attempt == 2:
                raise RuntimeError("Falha de conexão ou timeout") from None
        time.sleep(2 ** attempt)


def normalize(rows, term):
    unique = {}
    invalid = 0
    stamp = now()
    for row in rows:
        if not isinstance(row, list) or len(row) < 10 or not all(isinstance(row[i], str) and row[i].strip() for i in (0, 1, 2)):
            invalid += 1
            continue
        unique[row[0]] = {
            "nasa_id": row[0], "codigo": clean(row[1]), "titulo": clean(row[2]),
            "descricao": clean(row[3]), "categoria": clean(row[5]), "centro": clean(row[9]),
            "inventor": None, "status_licenciamento": None,
            "termo_busca": term, "fonte": NASA_BASE + quote(term, safe=""), "atualizado_em": stamp,
        }
    return list(unique.values()), invalid


def collect(term):
    payload = request_json(NASA_BASE + quote(term, safe=""))
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        raise ValueError("Formato da NASA mudou.")
    rows = payload["results"]
    # A resposta testada retorna todos os resultados apesar de perpage=10.
    # Nunca marcar como completa uma resposta truncada: revisar paginação se isso mudar.
    if int(payload.get("total", len(rows))) > len(rows):
        raise ValueError("Resposta paginada: implementar paginação antes de prosseguir.")
    if not rows:
        raise ValueError("Busca sem registros; confira o termo antes de atualizar.")
    return normalize(rows, term)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Consulta NASA sem escrever no banco")
    args = parser.parse_args(argv)
    term = os.getenv("NASA_SEARCH_TERM", "engine").strip()
    if not term:
        print("Configure um termo de busca não vazio.")
        return 1
    url = os.getenv("SUPABASE_URL", "").rstrip("/")
    key = os.getenv("SUPABASE_SERVICE_KEY", "")
    if not args.dry_run and (not key or urlparse(url).scheme != "https" or not urlparse(url).hostname):
        print("Configure SUPABASE_URL (HTTPS) e SUPABASE_SERVICE_KEY nos Secrets.")
        return 1
    headers = {"apikey": key, "Content-Type": "application/json", "Prefer": "resolution=merge-duplicates,return=minimal"}
    if key.startswith("eyJ"):
        headers["Authorization"] = "Bearer " + key
    log = {"id": str(uuid.uuid4()), "iniciado_em": now(), "registros_processados": 0,
           "lotes": 0, "erros": 0, "status": "erro_critico", "mensagem": "", "termo_busca": term}
    try:
        rows, invalid = collect(term)
        log["erros"] += invalid
        if args.dry_run:
            print(json.dumps({"termo": term, "registros_unicos": len(rows), "invalidos": invalid,
                              "amostra": rows[:1]}, ensure_ascii=False, indent=2))
            return 1 if invalid or not rows else 0
        for offset in range(0, len(rows), 100):
            batch = rows[offset:offset + 100]
            try:
                request_json(url + "/rest/v1/patentes?on_conflict=nasa_id", headers, batch)
                log["registros_processados"] += len(batch)
                log["lotes"] += 1
            except (RuntimeError, ValueError):
                log["erros"] += 1
        log["status"] = "concluido" if not log["erros"] else (
            "erro_parcial" if log["registros_processados"] else "erro_critico")
        log["mensagem"] = "Coleta finalizada." if not log["erros"] else "Registros inválidos ou falha no envio de lote."
    except (RuntimeError, ValueError, TypeError) as error:
        log["erros"] += 1
        # Não registrar URLs, headers ou corpos de erro que possam conter credenciais.
        log["mensagem"] = "Falha na coleta: " + type(error).__name__
    if args.dry_run:
        print(log["mensagem"])
        return 1
    log["finalizado_em"] = now()
    try:
        request_json(url + "/rest/v1/execucoes?on_conflict=id", headers, log)
    except (RuntimeError, ValueError):
        print("Falha ao gravar o log no banco; verifique Secrets, tabelas e permissões.")
        return 1
    print(json.dumps(log, ensure_ascii=False))
    return 0 if log["status"] == "concluido" else 1


if __name__ == "__main__":
    sys.exit(main())

