# TechTransfer-Patents — Grupo 09

Pipeline de dados com a API de **patentes da NASA (Technology Transfer)**: GitHub Actions coleta os dados, o Supabase (PostgreSQL) armazena e o GitHub Pages publica um painel de consulta.

**Integrantes:** Leonardo, Esther e Yasmim L.

## Links

| Item | Endereço |
|---|---|
| Organização GitHub | https://github.com/SN-2026-GRUPO-09-NASA |
| Repositório | https://github.com/SN-2026-GRUPO-09-NASA/TechTransfer-Patents |
| Painel (GitHub Pages) | https://sn-2026-grupo-09-nasa.github.io/TechTransfer-Patents/ |
| Projeto Supabase | `TechTransfer-Patents-DB` (região South America – São Paulo) |
| API REST do Supabase | https://avplmdbotkyhqhztattm.supabase.co/rest/v1/patentes |

## Sobre a API

O catálogo **NASA Technology Transfer** lista tecnologias e patentes da NASA disponíveis para licenciamento. Este projeto coleta o recorte de busca `engine` (motores) e guarda, por patente: identificador de origem, código de referência, título, descrição, categoria e centro NASA.

- Endpoint usado: `https://technology.nasa.gov/api/api/patent/engine` (não exige chave).
- Cada registro chega como **lista posicional**: posição 0 = identificador, 1 = código, 2 = título, 3 = descrição, 5 = categoria, 9 = centro NASA.
- Títulos e descrições podem trazer marcação HTML; o coletor converte para texto e o painel escapa tudo com `escapeHtml()`.

**Diferença em relação ao enunciado.** O endereço `api.nasa.gov/techtransfer/patent/` redirecionou para uma página HTML nos testes de 28/09/2026, e a consulta sem termo retornou HTTP 500. Por isso foi usada a alternativa oficial documentada em https://technology.nasa.gov/api/, que retorna JSON. A chave `NASA_API_KEY` não é utilizada nesta versão.

**Limitações conhecidas.** O recorte `engine` tinha 34 registros na consulta de 28/09/2026 e não representa o catálogo completo. *Inventor* e *status de licenciamento* não são fornecidos por este endpoint; ficam nulos no banco e o painel exibe "Não informado pela fonte". O status do pipeline (`execucoes.status`) não é o status da patente.

## Arquitetura

```
GitHub Actions (cron diário + manual)
        |  python scripts/fetch_nasa.py
        v
API NASA Technology Transfer  -->  limpeza + deduplicação (nasa_id)
        |  upsert em lotes de 100 (REST, service key via Secret)
        v
Supabase PostgreSQL: patentes + execucoes (RLS, leitura pública)
        |  REST com chave publicável (somente leitura)
        v
index.html no GitHub Pages
```

**Modelagem.** `patentes` tem a restrição `UNIQUE (nasa_id)`, a chave natural do registro, usada no upsert (`on_conflict=nasa_id`). A deduplicação ocorre antes do envio, o que evita o erro PostgreSQL 21000. `execucoes` registra cada rodada: registros processados, lotes, erros, status (`concluido`, `erro_parcial`, `erro_critico`) e mensagem.

**Segurança.** RLS ativo nas duas tabelas com política de leitura pública. `anon` e `authenticated` só têm SELECT; `service_role` tem ALL. A chave secreta existe apenas nos Secrets do GitHub. O `index.html` contém somente a chave publicável.

## Resultados da execução

- O workflow **Atualizar patentes NASA** foi executado manualmente (execução #44, disparada na branch `main`) e terminou com sucesso em 13 s.
- A tabela `execucoes` tem 41 registros. As execuções conferidas têm status `concluido`, 1 lote, 0 erros e 32 ou 33 registros processados.
- A tabela `patentes` guarda 37 registros do recorte `engine`: ela mantém a última observação de cada patente e não apaga registros antigos, por isso o total pode ser maior que o de uma única rodada.
- O painel publicado no GitHub Pages carrega os dados do Supabase pela API REST com a chave publicável.
- O Actions mostra um aviso sobre a descontinuação do Node.js 20 nas ações `checkout@v4` e `setup-python@v5`. É apenas um aviso e não afeta a execução.

## Estrutura do repositório

```
index.html                      painel (GitHub Pages)
scripts/fetch_nasa.py           coleta, deduplicação, upsert e log
scripts/inspecionar_api.py      inspeção da resposta da NASA (sem gravar)
sql/setup.sql                   tabelas, UNIQUE, RLS e GRANTs
tests/test_pipeline.py          testes unitários
.github/workflows/update-data.yml   agendamento do pipeline
docs/tutorial.pdf               guia completo para replicar o projeto
docs/apresentacao.pdf           slides do seminário
docs/ai-interaction.md          histórico de uso de IA
docs/reflexao.md                análise crítica do uso de IA
```

## Divisão de responsabilidades

| Área | Responsável |
|---|---|
| Pipeline (Python e workflow) | [PREENCHER: Leonardo e Esther] |
| Banco de dados (Supabase) | [PREENCHER: Leonardo e Esther] |
| Painel (index.html) | [PREENCHER: Leonardo e Esther] |
| Documentação e apresentação | [PREENCHER: Yasmim Lima] |

## Uso de IA generativa

O grupo utilizou IA generativa como apoio (leitura da atividade, inspeção da API, geração e revisão de código e documentação). Os prompts e a avaliação crítica estão em `docs/ai-interaction.md` e `docs/reflexao.md`.

## Como configurar do zero

O passo a passo detalhado está em `docs/tutorial.pdf`. Resumo:

1. **Supabase:** criar o projeto `TechTransfer-Patents-DB` (São Paulo), abrir o SQL Editor e executar `sql/setup.sql`. Confirmar que a Data API expõe o schema `public`.
2. **Secrets (GitHub → Settings → Secrets and variables → Actions):**

   | Nome | Valor |
   |---|---|
   | `SUPABASE_URL` | URL do projeto, por exemplo `https://avplmdbotkyhqhztattm.supabase.co` |
   | `SUPABASE_SERVICE_KEY` | chave secreta do Supabase (nunca no código, em commits ou prints) |

3. **Pages:** Settings → Pages → branch `main`, pasta `/(root)`.
4. **Coleta:** Actions → *Atualizar patentes NASA* → *Run workflow*. O cron diário roda às 09h17 UTC (06h17 em São Paulo).

Testes locais, sem dependências externas (Python 3.12+):

```sh
python scripts/fetch_nasa.py --dry-run     # consulta a NASA sem gravar no banco
python -m unittest discover -s tests -v    # testes unitários
```

## Boas práticas do workflow

`permissions: contents: read`, `concurrency` (sem execuções simultâneas) e `timeout-minutes: 10`. Falha parcial ou crítica encerra o script com `sys.exit(1)`, e o erro fica visível no Actions.

## Painel

Mostra cards das patentes, busca por título ou código, filtro por categoria e a data, o status e a quantidade de registros da última execução, lidos da tabela `execucoes`. O botão *Atualizar painel* relê o banco; não executa o pipeline.

Dados: [NASA Technology Transfer](https://technology.nasa.gov/). Projeto acadêmico — Atividade Avaliativa do 3º Trimestre (2026).
