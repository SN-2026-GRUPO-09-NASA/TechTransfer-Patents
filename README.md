# TechTransfer-Patents - Grupo 09

Base inicial do trabalho sobre patentes NASA. As tabelas já foram criadas no projeto informado em 28/09/2026. Ainda requer configurar os Secrets, publicar os arquivos e validar o fluxo completo.

- Organização: `SN-2026-GRUPO-09-NASA`
- Projeto Supabase: `TechTransfer-Patents-DB`, região São Paulo
- Repositório: https://github.com/SN-2026-GRUPO-09-NASA/TechTransfer-Patents
- Painel previsto (ainda não confirmado publicado): https://sn-2026-grupo-09-nasa.github.io/TechTransfer-Patents/
- Supabase: https://avplmdbotkyhqhztattm.supabase.co

## Como funciona

GitHub Actions executa Python → API NASA → limpeza e deduplicação → Supabase → painel no GitHub Pages.

Usamos inicialmente o recorte `engine`, com 34 registros na consulta de 28/09/2026. Não é o catálogo completo. A API retorna listas: posição 0 = identificador de origem, 1 = referência, 2 = título, 3 = descrição, 5 = categoria e 9 = centro NASA. A chave UNIQUE é `nasa_id`, identificador da origem; a deduplicação usa a mesma chave antes do upsert. A tabela guarda a última observação, sem apagar registros antigos automaticamente.

Inventor e status individual de licenciamento ficam nulos quando não fornecidos. Não confundir o status do pipeline com o status da patente. Esses campos exigem investigação complementar caso o professor exija seu preenchimento.

## 1. Criar as tabelas

No projeto indicado, abrir **SQL Editor**, colar o conteúdo de `sql/setup.sql` e executar. O script cria `patentes` e `execucoes`, permite leitura pública e reserva escrita ao serviço. A Data API deve estar habilitada e expor o schema `public`. Não executar em outro projeto sem revisar a configuração.

## 2. Enviar os arquivos ao GitHub

Enviar os arquivos deste projeto ao repositório do grupo, na branch `main`, preservando as pastas e principalmente `.github/workflows/update-data.yml`. Não enviar `tmp`, `output`, `.env` ou `__pycache__`. Se o envio pelo navegador não incluir a pasta oculta `.github`, criar o arquivo pelo botão **Add file → Create new file**, digitando o caminho completo.

## 3. Configurar os Secrets

No repositório: **Settings → Secrets and variables → Actions → New repository secret**.

| Nome | Valor |
|---|---|
| `SUPABASE_URL` | `https://avplmdbotkyhqhztattm.supabase.co` |
| `SUPABASE_SERVICE_KEY` | Chave secreta/backend do projeto, copiada diretamente do Supabase |

Não enviar a chave secreta por chat nem colocá-la no site. O site já contém somente a chave pública obtida do projeto. O coletor aceita chave moderna `sb_secret_...` ou chave legada `service_role`.

**Diferença em relação ao enunciado:** o endpoint `api.nasa.gov/techtransfer/patent/?engine&api_key=DEMO_KEY` redirecionou para uma página HTML no teste. Foi usada a alternativa oficial documentada em https://technology.nasa.gov/api/, que retornou JSON sem chave. A chave `NASA_API_KEY` não é utilizada nesta versão; registrar e alinhar essa adaptação com o professor. A consulta sem termo retornou HTTP 500 no teste, por isso o recorte está explícito.

## 4. Rodar a coleta

Em **Actions → Atualizar patentes NASA → Run workflow**. Conferir status verde, linhas na tabela `patentes` e um registro em `execucoes`. O cron está definido para 09h17 UTC diariamente (06h17 em São Paulo); execuções agendadas podem sofrer atraso.

Sem escrever no banco, testar localmente com Python 3.12 ou superior:

```sh
python scripts/fetch_nasa.py --dry-run
python -m unittest discover -s tests -v
```

Não há dependências Python externas. Requisições têm timeout e até três tentativas. Os lotes contêm até 100 registros. Um erro parcial produz saída 1 para o Actions mostrar falha. Se a resposta vier paginada/truncada, o coletor falha explicitamente em vez de fingir uma coleta completa. A paginação da NASA deve ser implementada caso o comportamento mude.

## 5. Publicar o painel

Em **Settings → Pages**, selecionar publicação por branch, `main` e `/(root)`. Abrir o link fornecido pelo GitHub, testar busca e categoria e conferir a última execução. O botão Atualizar painel relê o banco; não executa o pipeline.

Endpoint REST para entrega: `https://avplmdbotkyhqhztattm.supabase.co/rest/v1/patentes?select=codigo,titulo,categoria&limit=5`. Para consumir, enviar a chave pública no cabeçalho `apikey`. Abrir só a URL sem esse cabeçalho pode resultar em erro de autenticação.

## Verificação pendente nas contas

- SQL executado; RLS, SELECT público, ausência de INSERT para anon/authenticated e INSERT para service_role confirmados no banco. A função preexistente `rls_auto_enable()` gerou avisos no advisor por permissões EXECUTE; sua assinatura é `event_trigger`. Ela não foi alterada. Referência: https://supabase.com/docs/guides/database/database-linter?lint=0028_anon_security_definer_function_executable
- Configurar os Secrets, executar Actions e confirmar dados reais e log.
- Publicar Pages e verificar o painel no navegador e no celular.
- Confirmar nome da organização Supabase: a conexão não permitiu confirmar a organização associada ao projeto na listagem disponível.
- Adicionar o professor no GitHub (`GilFerques`) e no Supabase (`rafael.ferques@ifpr.edu.br`, Developer).
- Divisão de responsabilidades entre Leonardo, Esther e Yasmim L.: preencher pelo grupo.
- Produzir `docs/tutorial.pdf` (até 15 páginas) e `docs/apresentacao.pdf` após validar o funcionamento.
- Completar histórico de IA no template do professor e escrever a reflexão do grupo.
- Atualizar colunas G/H da planilha e montar o PDF único de entrega com links e prints reais.

O prazo do enunciado é 13/11/2026 às 23h59. Esta base ainda não representa a entrega concluída.

## Testes realizados

Quatro testes unitários passaram: deduplicação/limpeza/campos ausentes, resposta incompleta, falha parcial e falha de gravação do log. `--dry-run` consultou a NASA e normalizou 34 registros sem inválidos, sem escrever dados no banco. Sintaxe JavaScript conferida. O painel ainda precisa de teste visual e funcional no navegador; não houve execução real no GitHub Actions.
