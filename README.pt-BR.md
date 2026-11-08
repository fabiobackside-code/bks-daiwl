# BKS-DAIWL — Don't Accept It Without Learning (Não aceite sem aprender)

![versão](https://img.shields.io/badge/vers%C3%A3o-1.0.0-informational) ![idiomas](https://img.shields.io/badge/idiomas-en%20%7C%20pt--BR-blue)

🇺🇸 [Read in English](README.md)

Skill de **manutenibilidade pessoal** para agentes de código. Mede o quanto *você* vai conseguir manter um código
gerado por IA (Claude Code, Copilot, Cursor, agentes MCP), comparando os fundamentos que a IA aplicou com os que você
domina, aprendeu ou decidiu por experiência — e ensina a diferença usando o próprio código gerado como exemplo.

## O ciclo

```
 suas fontes ──indexar──▶ Índice de Cânone
 (vault, repositórios, papers, links)  │
 código da IA ──analisar───────────────┤──▶ score.md/html         (SMP 0–100, divergências, lacunas)
                                       │──▶ fundamentals.md/html  (cada fundamento com trecho real,
                                       │                           como estudar, fontes primárias)
                                       ▼
          aprendi <conceito>     ──▶ .daiwl/learnings/   ──▶ score sobe
          experiencia "<nota>"   ──▶ fundamentada, negociada, gravada como ADR leve ──▶ usada na próxima
```

A LLM **classifica**; o `skills/bks-daiwl/scripts/daiwl.py` **pontua** — mesma entrada, mesmo score, auditável.

## Instalação

**Claude Code** — `git clone https://github.com/fabiobackside-code/bks-daiwl && cp -r bks-daiwl/skills/bks-daiwl ~/.claude/skills/` (global) ou `.claude/skills/` (projeto).
**Claude.ai / Desktop** — instale o arquivo `.skill` publicado em [Releases](https://github.com/fabiobackside-code/bks-daiwl/releases).
**GitHub Copilot (modo agente)** — `cp -r bks-daiwl/skills/bks-daiwl .bks-daiwl && mkdir -p .github/prompts && cp bks-daiwl/skills/bks-daiwl/adapters/copilot/daiwl.prompt.md .github/prompts/` → `/daiwl`.
**Cursor** — `cp -r bks-daiwl/skills/bks-daiwl .bks-daiwl && mkdir -p .cursor/rules && cp bks-daiwl/skills/bks-daiwl/adapters/cursor/daiwl.mdc .cursor/rules/`.

Python 3.9+ (só biblioteca padrão) para o score determinístico; sem Python o agente calcula à mão e mostra a conta.

## Primeira configuração

Não tem vault? A skill cria um, compatível com Obsidian, com pastas em português, e faz uma entrevista curta:
```bash
python skills/bks-daiwl/scripts/daiwl.py init --vault ~/DAIWL-Vault --criar --idioma pt-BR
```
Já tem? Aponte tudo:
```bash
python skills/bks-daiwl/scripts/daiwl.py init --vault ~/Obsidian/Dev --idioma pt-BR \
  --fonte repositorio:~/src/wallet-apis:propria \
  --fonte repositorio:~/src/poc-copilot:ia \
  --fonte artigos:~/Documentos/papers \
  --fonte links:~/Obsidian/Dev/Referencias/links.md
python skills/bks-daiwl/scripts/daiwl.py fontes ls
```
Tipos: `vault`, `notas`, `repositorio` (autoria `propria` | `mista` | `ia` obrigatória), `artigos`, `links`, `url`.
A skill **só lê** as fontes e grava apenas em `<vault>/.daiwl/`. Repositório de autoria `ia` nunca conta como prova de domínio.

## Comandos

| Comando | Exemplo |
|---|---|
| `init` | `daiwl init` |
| `fontes` | `daiwl fontes add artigos:~/papers` |
| `indexar` | `daiwl indexar` |
| `analisar` | `daiwl analisar ./src` |
| `aprendi` | `daiwl aprendi "Outbox Pattern" "Result Pattern"` |
| `experiencia` | `daiwl experiencia "Repository genérico vazou IQueryable em outro projeto; prefiro um repository por aggregate"` |
| `versao` | `daiwl versao` |

Os comandos em inglês também funcionam (`index`, `analyze`, `learned`, `experience`, `sources`, `version`).
Os arquivos internos em `.daiwl/` usam nomes em inglês para o vault ser portável entre pessoas; o conteúdo das notas e
dos relatórios sai em português.

## Score

`SMP = Σ(impacto × fator) / Σ(impacto) × 100`, impacto = peso estrutural × (1 + ln ocorrências).
Conceito só declarado vale 0,70; lacuna 0; divergência −0,5; improviso da IA sem fundamento −0,25. Ver `skills/bks-daiwl/references/score.md`.

## Versionamento

SemVer, ver `CHANGELOG.md`. Cada relatório grava a versão da skill e a versão da fórmula; variação entre versões
diferentes da fórmula não é mostrada como progresso.

## Limites conhecidos

- A classificação é feita por LLM; duas execuções podem divergir em um ou dois fundamentos. O `findings.json` fica salvo
  para você revisar antes do score.
- O índice só enxerga o que está escrito. Se você domina algo que nunca registrou, use `aprendi` ou escreva uma nota.
- "Fundamentado" depende do catálogo e, com acesso à web, de fontes primárias. Estenda o catálogo com seus livros.

## Contribuir

Entradas no catálogo, traduções e novos leitores de fonte são bem-vindos. Ver [CONTRIBUTING.md](CONTRIBUTING.md).
Falha de segurança: [SECURITY.md](SECURITY.md).

## Relacionado

A BKS-DAIWL também vai, como cópia fixada numa versão, dentro do [bks-sdd-kit](https://github.com/fabiobackside-code/bks-sdd-kit).
O `/bks:maintainability` do kit pontua o código contra uma rubrica fixa de dev pleno; a DAIWL pontua contra *você*.
Este repositório é a fonte da verdade.

## Licença

[MIT](LICENSE)
