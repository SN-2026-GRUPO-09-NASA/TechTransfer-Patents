# Reflexão do grupo sobre o uso de IA

> RASCUNHO. Os fatos abaixo estão documentados em `ai-interaction.md`. Os trechos marcados com [PREENCHER] dependem da experiência real do grupo e devem ser escritos pelos integrantes antes da entrega.

## Onde a IA ajudou

- Resumiu o enunciado em etapas e reduziu o tempo para entender o que era exigido.
- Testou o endpoint real antes de escrever o código, o que revelou cedo que o endereço do enunciado não devolvia JSON.
- Gerou a primeira versão do SQL, do coletor em Python, do workflow e do painel, com testes unitários e modo `--dry-run`.
- Sugeriu práticas pedidas pela atividade: deduplicação antes do upsert, log em `execucoes`, `sys.exit(1)` em falha parcial e `escapeHtml()` no painel.

## Onde a IA errou ou foi limitada

- Partiu do endpoint indicado no enunciado, que redirecionou para HTML. A alternativa oficial só apareceu depois do teste.
- A consulta sem termo de busca retornou HTTP 500, então o catálogo completo não pôde ser coletado de uma vez. Foi necessário um recorte (`engine`).
- Inventor e status de licenciamento não existem na resposta da API. A IA não inventou esses valores, mas o painel ficou sem eles.
- Não consegue configurar Secrets, rodar o Actions nem ativar o Pages por conta própria.
- [PREENCHER: erros reais que apareceram ao subir o código, rodar o workflow ou abrir o painel]

## O que o grupo corrigiu, decidiu e revisou

- Decidiu usar o endpoint alternativo da NASA e documentar a diferença em relação ao enunciado.
- Decidiu mostrar "Não informado pela fonte" em vez de preencher inventor e status.
- Manteve a chave secreta apenas nos Secrets e a chave publicável no painel.
- [PREENCHER: partes do código que cada integrante leu, testou ou modificou]

## Respostas às perguntas orientadoras

1. **O que entendemos melhor com a explicação da IA?** [PREENCHER]
2. **Como confirmamos o problema do endpoint e a alternativa oficial?** Testamos os dois endereços; o do enunciado devolveu HTML após redirecionamento e o de `technology.nasa.gov/api/` devolveu JSON. [PREENCHER: quem testou e como]
3. **Como tratamos inventor e status ausentes?** Campos nulos no banco e texto "Não informado pela fonte" no painel, com a limitação registrada no README.
4. **Quais partes do código revisamos e modificamos?** [PREENCHER]
5. **Quais erros apareceram nos testes reais e como foram corrigidos?** [PREENCHER]
6. **O que cada integrante consegue explicar sem consultar a IA?** Leonardo: [PREENCHER]. Esther: [PREENCHER]. Yasmim: [PREENCHER].

## Conclusão

[PREENCHER: avaliação do grupo sobre se a IA ajudou ou atrapalhou, e o que faria diferente.]
