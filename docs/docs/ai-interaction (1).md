# Histórico de Interação com IA

> Preencha este arquivo ao longo do desenvolvimento do projeto.
> Registre TODOS os prompts utilizados — mesmo os que não funcionaram.
> Este documento é parte obrigatória da avaliação.

---

## Informações gerais

| Campo | Valor |
|-|-|
| **Grupo** | Grupo 09 |
| **Integrantes** | Leonardo, Esther, Yasmim L. |
| **API NASA escolhida** | TechTransfer / Patents |
| **IA utilizada** | [PREENCHER: IA usada nas interações 1 a 3; a interação 4 foi feita com Claude] |
| **Data de início** | 28-09-2026 |
| **Data de conclusão** | 13-11-2026 |

---

## Interação 1 — Leitura da atividade e explicação das etapas

**Data:** 28-09-2026
**Objetivo:** Entender requisitos, prazos e etapas da atividade.

**Prompt enviado à IA:**

```
oi chat amigo, le o pdf identifique os pontos da atividade e explique como fazer de forma simples, e tambem me ajude a fazer ela
```

**Resumo da resposta:**
A IA leu as 12 páginas do PDF, resumiu os entregáveis, o prazo e as etapas e perguntou qual era o grupo.

**O que funcionou:**
O resumo serviu como mapa das etapas (GitHub, Supabase, Secrets, pipeline, painel, documentação).

**O que precisou ajuste:**
Nada foi entregue ou publicado nesta etapa. [PREENCHER: algo que o grupo conferiu no PDF original]

---

## Interação 2 — Identificação da API e teste do endpoint

**Data:** 28-09-2026
**Objetivo:** Confirmar as nomenclaturas do grupo 09 e testar o endpoint de patentes.

**Prompt enviado à IA:**

```
eh o grupo 9 dos nomes pra repositorio, eh Patentes NASA disponíveis para licenciamento: título, categoria, inventor e status
```

(acompanhado da referência ao endpoint `api.nasa.gov/techtransfer/patent/`)

**Resumo da resposta:**
A IA confirmou os nomes (organização `SN-2026-GRUPO-09-NASA`, repositório `TechTransfer-Patents`, projeto `TechTransfer-Patents-DB`) e testou os endpoints.

**O que funcionou:**
A verificação da resposta real antes de escrever o código. O endpoint alternativo oficial, `https://technology.nasa.gov/api/api/patent/engine`, devolveu JSON.

**O que precisou ajuste:**
- O endereço do enunciado com `DEMO_KEY` redirecionou para uma página HTML. Solução: usar o endpoint alternativo documentado pela NASA.
- A consulta sem termo retornou HTTP 500. Solução: definir um recorte explícito (`engine`).
- Inventor e status de licenciamento não existem nessa resposta. Solução: manter os campos nulos e exibir "Não informado pela fonte", em vez de inventar valores.

---

## Interação 3 — Conferência das contas e geração da base do projeto

**Data:** 28-09-2026
**Objetivo:** Verificar GitHub e Supabase e gerar SQL, coletor, workflow, painel e testes.

**Prompt enviado à IA:**

```
[PREENCHER: colar o prompt exato em que o grupo informou o repositório SN-2026-GRUPO-09-NASA/TechTransfer-Patents e o projeto Supabase avplmdbotkyhqhztattm]
```

**Resumo da resposta:**
A IA constatou que o repositório estava vazio e o projeto Supabase ativo em São Paulo, sem tabelas. Gerou `sql/setup.sql`, `scripts/fetch_nasa.py`, `update-data.yml`, `index.html`, README e testes. Aplicou o SQL e conferiu RLS e permissões. Quatro testes unitários passaram e o `--dry-run` retornou 34 registros válidos.

**O que funcionou:**
Estrutura do pipeline, deduplicação por `nasa_id`, log em `execucoes`, saída 1 em falha parcial e testes unitários.

**O que precisou ajuste:**
- Títulos e descrições vinham com marcação HTML. Correção: limpeza no coletor e `escapeHtml()` no painel.
- [PREENCHER: erros que apareceram ao enviar ao GitHub, configurar Secrets e rodar o Actions, e como foram corrigidos]

---

## Interação 4 — Revisão do projeto contra a atividade e documentação final

**Data:** 13-11-2026
**Objetivo:** Comparar o repositório com os requisitos da atividade e gerar os arquivos de documentação pendentes.

**Prompt enviado à IA:**

```
Preciso que veja oq falta mexer no arquivo zip, em comparação com as atividades
```

```
Me ajude a fazer td
```

**Resumo da resposta:**
A IA comparou o zip com as seções 3, 5 e 7 do PDF e listou o que estava pronto (SQL, coletor, workflow, painel) e o que faltava (`tutorial.pdf`, `apresentacao.pdf`, `ai-interaction.md` no template, `reflexao.md`, README final, Secrets, execução verde, Pages, convites ao professor e PDF de entrega). Em seguida gerou rascunhos do README, deste arquivo, da reflexão, do tutorial e dos slides.

**O que funcionou:**
A lista de pendências serviu de checklist. Os rascunhos deram a estrutura dos documentos.

**O que precisou ajuste:**
[PREENCHER: o que o grupo revisou, corrigiu ou reescreveu nos rascunhos]

---

## Resumo final

**Total de interações:** 4 [ajustar se houver mais]

**Principais contribuições da IA:**

- Leitura e resumo do enunciado em etapas.
- Teste do endpoint real e descoberta do redirecionamento para HTML e do HTTP 500 sem termo.
- Geração do SQL, do coletor, do workflow, do painel e dos testes.
- Checklist de pendências e rascunho da documentação.

**Principais limitações encontradas:**

- O endpoint do enunciado não retornou JSON; foi preciso usar outro endpoint.
- A API não fornece inventor nem status de licenciamento; o catálogo coletado é só um recorte (`engine`).
- A IA não consegue criar Secrets, executar o Actions nem publicar o Pages; essas etapas dependeram do grupo.
- [PREENCHER: outras limitações observadas]

**Avaliação geral do uso da IA:**
[PREENCHER pelo grupo, em até 10 linhas. Sugestão de pontos: o que a IA acelerou, o que precisou ser verificado manualmente, o que cada integrante consegue explicar sem a IA.]
