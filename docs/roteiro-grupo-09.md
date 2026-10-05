# Roteiro do grupo 09 - TechTransfer / Patents

## Nomes exigidos pelo enunciado

- Organização no GitHub e no Supabase: `SN-2026-GRUPO-09-NASA`
- Repositório público: `TechTransfer-Patents`
- Projeto Supabase: `TechTransfer-Patents-DB`
- Integrantes listados no PDF: Leonardo, Esther e Yasmim L.
- Entrega: 13/11/2026, às 23h59.

## O que estamos construindo

Um catálogo de tecnologias patenteadas da NASA, com busca por título e filtro por categoria. O Python coleta os dados, o Supabase armazena, o GitHub Actions atualiza e o GitHub Pages exibe o painel.

## Descoberta na verificação de 28/09/2026

A consulta de exemplo `https://api.nasa.gov/techtransfer/patent/?engine&api_key=DEMO_KEY` redirecionou para `https://technology.nasa.gov/api/` e retornou HTML, não JSON.

A alternativa documentada pela própria NASA, `https://technology.nasa.gov/api/api/patent/engine`, retornou JSON com registros reais. Esse teste consultou o termo `engine`; não é prova de coleta de todo o catálogo. Precisaremos conferir paginação e definir o recorte da coleta antes de implementar o pipeline definitivo.

Fonte: https://technology.nasa.gov/api/

Na resposta observada, os registros são listas posicionais. Foram reconhecidos identificador, código de referência, título, descrição, categoria e centro NASA. Inventor e status individual de licenciamento não estão identificados na documentação consultada. Não interpretar campos vazios ou o centro NASA como inventor, nem atribuir automaticamente um status individual. Se esses campos não estiverem disponíveis, mostrar “Não informado pela fonte” e documentar a limitação; se forem obrigatórios para o grupo, verificar uma fonte complementar oficial e alinhar com o professor.

Títulos e descrições podem conter marcação HTML de destaque. O coletor deve convertê-la em texto e o painel deve escapar valores externos com `escapeHtml()`.

## Ordem prática

1. Conferir os links existentes do GitHub e Supabase e os nomes acima. Não recriar estruturas que já funcionam.
2. Conferir a API e decidir o recorte de dados, paginação e identificador para deduplicação.
3. Criar `sql/setup.sql`: tabela `patentes`, tabela `execucoes`, UNIQUE, RLS e permissões explícitas. A chave natural precisa ser validada nos dados.
4. Criar `scripts/fetch_nasa.py`: consulta, limpeza, deduplicação, envio em lotes, upsert e registro de execução. Sinalizar falha parcial ou crítica com saída diferente de zero.
5. Configurar Secrets `SUPABASE_URL`, `SUPABASE_SERVICE_KEY` e a chave NASA quando exigida pelo endpoint efetivamente usado. Nunca colocar a chave privada no painel ou em mensagens.
6. Criar `.github/workflows/update-data.yml` com cron, execução manual, `permissions: contents: read`, `concurrency` e `timeout-minutes`.
7. Criar `index.html` com leitura da REST API, busca, categoria, última atualização lida de `execucoes` e tratamento dos estados de carregamento, vazio e erro.
8. Ativar Pages na branch `main`, pasta raiz. Testar leitura pública e bloqueio de escrita pública.
9. Executar o workflow e verificar dados reais no banco, log e status verde.
10. Finalizar README, tutorial de até 15 páginas, slides, histórico de IA e reflexão real dos integrantes.
11. Adicionar o professor conforme enunciado, atualizar as colunas G/H da planilha e reunir links e prints no PDF de entrega.

## Situação atual

- PDF lido e grupo identificado.
- Dois endereços oficiais testados; alternativa JSON encontrada.
- Links recebidos e conferidos: repositório público vazio e projeto Supabase ativo em São Paulo.
- Tabelas patentes e execucoes criadas; RLS e permissões verificadas. Repositório remoto, convites e publicação não foram alterados.
- Coletor, workflow e painel preparados localmente. Testes unitários e consulta dry-run passaram; envio ao GitHub, Secrets, execução real e publicação ainda pendentes.

## Uso de IA

Preservar esta conversa e usar o template `ai-interaction.md` do professor quando ele estiver disponível. Registrar também o problema do redirecionamento e sua solução efetivamente adotada. A reflexão deve ser escrita ou revisada pelos integrantes, sem inventar experiências, testes ou resultados.
