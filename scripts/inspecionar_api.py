"""Inspeção pública da NASA; não grava no Supabase e não usa credenciais."""
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def main():
    termo = sys.argv[1] if len(sys.argv) > 1 else "engine"
    url = "https://technology.nasa.gov/api/api/patent/" + quote(termo, safe="")
    req = Request(url, headers={"Accept": "application/json"})
    try:
        with urlopen(req, timeout=30) as response:
            if "json" not in response.headers.get("Content-Type", "").lower():
                raise ValueError("O servidor não retornou JSON.")
            data = json.load(response)
        if not isinstance(data, dict) or not isinstance(data.get("results"), list):
            raise ValueError("Formato inesperado: não há lista results.")
        print("Metadados:")
        print(json.dumps({k: v for k, v in data.items() if k != "results"}, ensure_ascii=False, indent=2))
        print("Registros nesta resposta:", len(data["results"]))
        if data["results"]:
            print("Primeiro registro, com posições para análise:")
            print(json.dumps(dict(enumerate(data["results"][0])), ensure_ascii=False, indent=2))
        print("Esta consulta é um recorte; ainda não valida a coleta completa nem inventor/status.")
        return 0
    except (HTTPError, URLError, ValueError, TimeoutError) as error:
        print("Falha na inspeção:", type(error).__name__, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
