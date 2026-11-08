# bks-daiwl (categoria: backside)

BKS-DAIWL — *Don't Accept It Without Learning*. Skill de manutenibilidade pessoal: compara o código
gerado por IA com o que o desenvolvedor domina e ensina a diferença. Repositório público, fonte da
verdade da skill; o `bks-sdd-kit` carrega uma cópia fixada numa versão.

## O projeto é autossuficiente

Tudo que uma sessão precisa está neste repositório. Nenhum comando lê o vault para funcionar.

## Boot da sessão — carregar nesta ordem

| # | Arquivo | Para que |
|---|---|---|
| 1 | `./STATUS.md` | onde o projeto parou, o que trava, próximo passo |
| 2 | `./WORKFLOW.md` | o fluxo de comandos deste projeto |
| 3 | `./decisions/` | as decisões fechadas |
| 4 | `./skills/bks-daiwl/SKILL.md` | o contrato da skill |

O perfil do usuário vive no vault (`workbench/profile.md`) e é carregado pelo ambiente, não por
este arquivo.

## Onde cada coisa está

| O que | Onde |
|---|---|
| A skill — o que se publica | `./skills/bks-daiwl/` |
| Pontuação determinística | `./skills/bks-daiwl/scripts/daiwl.py` |
| Adaptadores Copilot e Cursor | `./skills/bks-daiwl/adapters/` |
| Specs | `./specs/{features,tests,tasks}/` |
| Decisões | `./decisions/ADR-NNN.md` |
| Material bruto | `./docs/input/` |
| Página pública | `./README.md` (inglês) e `./README.pt-BR.md` |

## Regras de publicação

- A versão mora em três lugares que andam juntos: `skills/bks-daiwl/VERSION`, `metadata.version`
  no `SKILL.md` e o `CHANGELOG.md`.
- Mudança de peso ou fator da fórmula sobe o `formula_version`.
- O `scripts/daiwl.py` usa só a biblioteca padrão do Python 3.9+.
- Nenhum vault, nota ou relatório real entra no repositório: é dado pessoal.
- Release no kit: copiar `skills/bks-daiwl/` para o `bks-sdd-kit` e registrar a versão no
  `THIRD_PARTY.md` dele.

## Idioma

Documentação de projeto em português do Brasil. A página pública é bilíngue (inglês e português).
Código, chaves internas, nomes de tipo, método e variável em inglês.
