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
| **IA utilizada** | Claude (interações 1 a 12) |
| **Data de início** | 28-09-2026 |
| **Data de conclusão** | 13-11-2026 |

---

## Interação 1 — Leitura da atividade

**Data:** 28-09-2026
**Objetivo:** Entender o que a atividade pedia, o prazo e as etapas.

**Prompt enviado à IA:**

```
Le o pdf identifique os pontos da atividade e explique como fazer de forma simples, e tambem me ajude a fazer ela
```

**Resumo da resposta:**
A IA leu as 12 páginas do PDF e explicou o que precisava ser entregue, o prazo e as etapas. No final, perguntou qual era o nosso grupo.

**O que funcionou:**
O resumo ajudou a entender as etapas: GitHub, Supabase, Secrets, pipeline, painel e documentação.

**O que precisou ajuste:**
Nada foi publicado nessa etapa. Usamos o PDF original para conferir prazos, nomes e o que entregar.

---

## Interação 2 — Descobrir a API do grupo e testar o endpoint

**Data:** 28-09-2026
**Objetivo:** Confirmar os nomes do grupo 09 e testar o endereço da API de patentes.

**Prompt enviado à IA:**

```
É o grupo 9 dos nomes pra repositorio, e Patentes NASA disponíveis para licenciamento: título, categoria, inventor e status
```

(Junto com a referência ao endereço `api.nasa.gov/techtransfer/patent/`.)

**Resumo da resposta:**
A IA confirmou os nomes (organização `SN-2026-GRUPO-09-NASA`, repositório `TechTransfer-Patents` e projeto `TechTransfer-Patents-DB`) e testou os endereços da API.

**O que funcionou:**
Testar a API antes de escrever o código. O endereço alternativo `https://technology.nasa.gov/api/api/patent/engine` devolveu JSON.

**O que precisou ajuste:**
- O endereço do enunciado (com `DEMO_KEY`) abriu uma página HTML e não JSON. Usamos o endereço alternativo da própria NASA.
- A busca sem termo deu erro HTTP 500. Por isso usamos um recorte: a palavra `engine`.
- A API não traz inventor nem status de licenciamento. Deixamos esses campos vazios e o painel mostra "Não informado pela fonte", em vez de inventar.

---

## Interação 3 — Conferência das contas e criação da base do projeto

**Data:** 28-09-2026
**Objetivo:** Verificar o GitHub e o Supabase e criar os arquivos do projeto.

**Prompt enviado à IA:**

```
SN-2026-GRUPO-09-NASA/TechTransfer-Patents e o projeto Supabase avplmdbotkyhqhztattm.
```

**Resumo da resposta:**
A IA viu que o repositório estava vazio e que o projeto do Supabase estava ativo em São Paulo, sem tabelas. Criou `sql/setup.sql`, `scripts/fetch_nasa.py`, o workflow, o `index.html`, o README e os testes. Aplicou o SQL e conferiu o RLS e as permissões. Os 4 testes passaram e o `--dry-run` achou 34 registros.

**O que funcionou:**
A estrutura do pipeline, a deduplicação por `nasa_id`, o log na tabela `execucoes`, a saída com erro (`sys.exit(1)`) e os testes.

**O que precisou ajuste:**
- Os títulos e descrições vinham com marcação HTML. Corrigimos limpando no coletor e usando `escapeHtml()` no painel.
- Depois de subir os arquivos e criar os Secrets, rodamos o workflow à mão (execução #44) e deu certo. O Actions só mostrou um aviso sobre o Node.js 20, que não atrapalha, e deixamos como está.

---

## Interação 4 — O que falta no projeto em relação à atividade

**Data:** 13-11-2026
**Objetivo:** Comparar o zip do projeto com o que a atividade pede.

**Prompt enviado à IA:**

```
Preciso que veja oq falta mexer no arquivo zip, em comparação com as atividades
```

**Resumo da resposta:**
A IA abriu o zip e comparou com as seções 3, 5 e 7 do PDF. Disse que o SQL, o coletor, o workflow e o painel estavam prontos. Faltavam `docs/tutorial.pdf`, `docs/apresentacao.pdf`, o `ai-interaction.md` no modelo do professor, a reflexão, o README final, os Secrets, a execução verde, o Pages, os convites do professor e o PDF de entrega. Também avisou que o endpoint usado era diferente do enunciado.

**O que funcionou:**
A lista virou nosso checklist do que fazer antes do prazo.

**O que precisou ajuste:**
Nada precisou ser refeito. Só tivemos que conferir na prática o que dependia das nossas contas.

---

## Interação 5 — Criação dos documentos que faltavam

**Data:** 13-11-2026
**Objetivo:** Gerar os arquivos de documentação do repositório.

**Prompt enviado à IA:**

```
Me ajude a fazer tudo
```

**Resumo da resposta:**
A IA criou o README novo, o `ai-interaction.md` no modelo, o rascunho da reflexão, o `tutorial.pdf` (11 páginas), o `apresentacao.pdf` (slides) e um checklist de entrega. Tudo veio num zip.

**O que funcionou:**
Os arquivos deram a estrutura de todos os documentos e o tutorial usou o código real do projeto.

**O que precisou ajuste:**
Alguns trechos ficaram em branco para o grupo completar, porque só o grupo sabe a divisão de tarefas e quem usou qual IA. Eles foram completados por nós.

---

## Interação 6 — O que colocar no GitHub

**Data:** 13-11-2026
**Objetivo:** Saber quais arquivos subir e se o zip gerado era igual ao nosso.

**Prompt enviado à IA:**

```
Oq eu preciso colocar no github
```

```
O zip que mandou está igual oq eu mandei?
```

**Resumo da resposta:**
A IA explicou quais arquivos subir para a branch `main`, quais substituir (README, `ai-interaction.md`, `reflexao.md`) e quais não subir. Avisou sobre a pasta oculta `.github`. Sobre o zip, disse que o dela tinha só os arquivos novos, e não uma cópia do nosso.

**O que funcionou:**
A lista de arquivos e a explicação de como subir pelo navegador ou pelo Git.

**O que precisou ajuste:**
Nada. Só tivemos o cuidado de não subir o `.zip` inteiro nem o checklist.

---

## Interação 7 — O que falta além dos arquivos

**Data:** 13-11-2026
**Objetivo:** Descobrir o que mais precisava ser feito além dos arquivos do repositório.

**Prompt enviado à IA:**

```
Oq eu preciso colocar a mais no trabalho, além daqueles arquivos
```

**Resumo da resposta:**
A IA listou: ativar o GitHub Pages, convidar o professor no GitHub e no Supabase, atualizar as colunas G e H da planilha e montar o PDF único do Classroom. Antes disso, ela olhou o nosso print do workflow verde e disse que ele podia entrar no PDF.

**O que funcionou:**
A lista com a ordem do PDF de entrega (links, print do workflow, Table Editor, API REST e planilha).

**O que precisou ajuste:**
Nada.

---

## Interação 8 — URL da API REST (Console e aba Network)

**Data:** 13-11-2026
**Objetivo:** Conseguir o print da URL da API do Supabase retornando JSON.

**Prompt enviado à IA:**

```
O que seria a URL
```

```
Eu não copiei, pois falava que não tinha como colar
```

```
Tem dois patentes
```

**Resumo da resposta:**
A IA explicou que a URL é o endereço da API REST do Supabase que devolve os dados em JSON. Passou um comando para o Console do navegador, mas deu erro de sintaxe. Aí sugeriu a aba **Network** do DevTools. Ela também explicou que apareciam duas requisições `patentes` porque o painel lê em blocos: a de `offset=0` traz os dados e a de `offset=37` volta vazia.

**O que funcionou:**
A aba Network funcionou. Conseguimos o print da requisição com status 200 OK e do JSON com registros reais (por exemplo `TOP2-271`).

**O que precisou ajuste:**
- O Console do Chrome bloqueou a colagem e o comando digitado à mão deu erro. Trocamos para a aba Network.
- Tivemos que escolher a requisição certa (`offset=0`), porque a outra vinha vazia.

---

## Interação 9 — Revisão do PDF de entrega

**Data:** 13-11-2026
**Objetivo:** Ver o que faltava no PDF do Classroom.

**Prompt enviado à IA:**

```
O que falta fazer?
```

(Com o print do rascunho do PDF. Depois enviamos o print da planilha e a versão atualizada do PDF.)

**Resumo da resposta:**
A IA viu que os itens 1 a 4 estavam prontos e que faltavam o 5 (URL da API) e o 6 (planilha). Depois apontou três problemas: o link do repositório com `.git` no final, a URL escrita que não batia com o print e o print da planilha com o link cortado.

**O que funcionou:**
Essas correções deixaram o PDF de acordo com os itens da atividade.

**O que precisou ajuste:**
Tiramos o `.git` do link, colocamos a URL real que aparece no print e refizemos o print da planilha com a coluna alargada.

---

## Interação 10 — Conferência dos zips do repositório

**Data:** 13-11-2026
**Objetivo:** Ver se os arquivos novos já estavam no zip do repositório.

**Prompt enviado à IA:**

```
Está td certo?
```

```
Esse zip, tem todas as alterações?
```

(Com os zips do repositório e o zip gerado pela IA.)

**Resumo da resposta:**
O primeiro zip do repositório era idêntico ao original, e o segundo tinha só os PDFs e a reflexão novos. A IA avisou que o README e o `ai-interaction.md` continuavam antigos. No zip final, conferiu todos os arquivos.

**O que funcionou:**
A comparação arquivo por arquivo mostrou exatamente o que ainda estava desatualizado.

**O que precisou ajuste:**
Subimos de novo o README e o `ai-interaction.md` novos para o GitHub.

---

## Interação 11 — Terminar os arquivos que faltavam

**Data:** 13-11-2026
**Objetivo:** Completar os documentos que ainda tinham trechos em branco.

**Prompt enviado à IA:**

```
Quero que termine todos os arquivos que ainda tem que ter ajuste
```

**Resumo da resposta:**
A IA completou o README (com uma seção de resultados), o histórico de IA, a reflexão e os slides, e atualizou o roteiro. Usou só fatos que apareceram nos prints, como a execução #44, as 41 execuções e os 37 registros. Deixou em branco só o que depende do grupo: a divisão de responsabilidades e o nome da IA das interações 1 a 3.

**O que funcionou:**
Os documentos ficaram completos e conferidos com o que o painel e o Supabase mostram.

**O que precisou ajuste:**
Nós completamos a divisão de responsabilidades e o nome da IA, e lemos a reflexão para ver se ela refletia o que aconteceu.

---

## Interação 12 — Reescrever este histórico em linguagem de aluno

**Data:** 13-11-2026
**Objetivo:** Deixar este arquivo completo, com os prompts, em linguagem simples.

**Prompt enviado à IA:**

```
Quero que escreva no `ai-interaction.md` tudo as coisas certas, com o prompt e tudo mais, coloque o que você acha que um aluno do terceiro ano do ensino médio escreveria
```

**Resumo da resposta:**
A IA recusou inventar prompts que não foram enviados, porque este arquivo é um registro do que foi usado de verdade. Em vez disso, reescreveu o arquivo com os prompts reais desta conversa, copiados do jeito que foram escritos, e com as explicações em linguagem simples.

**O que funcionou:**
O arquivo ficou mais completo e verdadeiro, com 12 interações.

**O que precisou ajuste:**
Falta o nome da IA das interações 1 a 3, que o grupo deve preencher.

---

## Resumo final

**Total de interações:** 12

**Principais contribuições da IA:**

- Leu o enunciado e explicou as etapas.
- Testou a API de verdade e achou o problema do endereço do enunciado.
- Criou o SQL, o coletor, o workflow, o painel e os testes.
- Comparou o projeto com a atividade e fez o checklist do que faltava.
- Criou os documentos: README, tutorial, slides, reflexão e este histórico.
- Ajudou a corrigir o PDF de entrega e a conseguir o print da API.

**Principais limitações encontradas:**

- O endereço do enunciado não devolveu JSON e foi preciso usar outro.
- A API não traz inventor nem status de licenciamento, e a coleta é só um recorte (`engine`).
- A IA não consegue criar Secrets, rodar o Actions, ativar o Pages nem convidar o professor. Isso foi feito por nós.
- O comando passado para o Console do navegador não funcionou, e foi preciso usar a aba Network.

**Avaliação geral do uso da IA:**
A IA ajudou bastante a entender a atividade e a montar o projeto mais rápido, principalmente o código e os documentos.
Mas ela errou ao partir de um endereço de API que não funcionava, e só descobrimos isso quando testamos de verdade.
Também precisamos conferir tudo na prática: o workflow rodou verde, o Supabase recebeu as execuções e o painel carregou os dados.
O que depende das nossas contas (Secrets, Pages, convites, planilha e prints) foi feito por nós.
Aprendemos como funciona o fluxo completo e que sempre é preciso testar o que a IA sugere antes de confiar.
