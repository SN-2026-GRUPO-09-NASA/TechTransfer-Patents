# Registro inicial de uso de IA

Rascunho factual. O template do professor ainda não foi fornecido. Preservar a conversa completa e transferir para esse template; este resumo não substitui todas as respostas integrais exigidas.

## 28/09/2026 - Leitura da atividade

Prompt do usuário: “oi chat amigo, le o pdf identifique os pontos da atividade e explique como fazer de forma simples, e tambem me ajude a fazer ela”.

Objetivo: entender requisitos, prazo e etapas. Resposta: leitura das 12 páginas, resumo dos entregáveis e pergunta sobre o grupo. Não foi realizada entrega ou publicação.

## Identificação do grupo

Prompt do usuário: “eh o grupo 9 dos nomes pra repositorio, eh Patentes NASA disponíveis para licenciamento: título, categoria, inventor e status” e referência a `api.nasa.gov/techtransfer/patent/`.

Resposta: confirmação das nomenclaturas e testes da NASA. O endereço de exemplo com DEMO_KEY retornou HTML após redirecionamento; a alternativa oficial retornou JSON. A consulta sem termo falhou com HTTP 500. Ajuste: recorte explícito por `engine`. Inventor e status não foram inventados.

## Conferência das contas e base inicial

Usuário informou que já tinha GitHub e Supabase e enviou o repositório `SN-2026-GRUPO-09-NASA/TechTransfer-Patents` e o projeto `avplmdbotkyhqhztattm`.

Constatações: repositório público vazio; conexão GitHub com leitura, sem escrita; projeto Supabase ativo em São Paulo com nome correto e sem tabelas públicas. O nome da organização Supabase não pôde ser confirmado na listagem disponível.

Arquivos locais preparados: esquema SQL, coletor Python, workflow, painel HTML, README e testes. O SQL foi aplicado ao projeto informado; RLS e permissões das duas tabelas foram conferidos. Quatro testes unitários passaram e a coleta em modo dry-run retornou 34 registros válidos. Secrets, primeira execução real com gravação e publicação do painel ainda dependem de configuração. Não afirmar que o projeto já está entregue.

## Pontos para o grupo avaliar

- Acerto: verificar a resposta real da API antes de assumir seu formato.
- Limitação: ainda não há inventor/status individual e o catálogo usado é um recorte.
- Correção técnica: remover marcação HTML do título e descrição; escapar dados no painel.
- Pendência: anexar respostas integrais, resultados dos testes e ajustes feitos pelos integrantes.
