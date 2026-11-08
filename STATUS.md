# STATUS — bks-daiwl

> Ponto de entrada do projeto. Leia só este arquivo para saber onde as coisas estão e o que fazer
> a seguir. Atualizado pelo `/bks:save` ao fim de cada sessão; lido pelo `/bks:brain`.
>
> Última atualização: 2026-11-08

---

## Em uma frase

A skill está na `1.0.1`, com estrutura de repositório público, 23 testes verdes, CI e release
automático do `.skill` por tag. Falta só criar o repositório no GitHub e fazer o primeiro push.

---

## Fase atual

**Empacotamento** — a fase termina com o repositório publicado e o primeiro release `.skill`
anexado pelo workflow.

---

## O que trava

| Bloqueio | Espera | Quem destrava |
|---|---|---|
| Push inicial | criar o repositório `fabiobackside-code/bks-daiwl` no GitHub | Fabio |

---

## Próximo passo

Criar o repositório vazio no GitHub (`bks-daiwl`, público, sem README) e rodar:

```
git remote add origin https://github.com/fabiobackside-code/bks-daiwl.git
git push -u origin main
```

Depois, publicar o primeiro release: `git tag v1.0.1 && git push origin v1.0.1`. O workflow
`release.yml` roda os testes, gera o `.skill` e anexa ao release.

---

## Decisões que valem

| # | Decisão | Onde |
|---|---|---|
| 1 | Repositório próprio; skill em `skills/bks-daiwl/`; o kit carrega uma cópia fixada | `decisions/ADR-001.md` |
| 2 | Licença MIT, a mesma do kit | `LICENSE` |

---

## Aberto

- Os testes cobrem pontuação, normalização, `init` e `score`; `render`, `rescore`, `sources` e `inventory` seguem sem teste
- O `fundamentals-catalog.md` cita fontes primárias; falta conferir uma a uma antes da divulgação
- Sobreposição com o `/bks:maintainability` do kit: os critérios por stack de lá poderiam alimentar
  a extração de fundamentos daqui

---

## Mapa dos documentos

| Documento | Para que |
|---|---|
| este arquivo | onde parei, o que trava, próximo passo |
| `WORKFLOW.md` | o fluxo de comandos deste projeto |
| `JOURNAL.md` | marcos e sessões, do mais recente ao mais antigo |
| `decisions/` | as decisões, com contexto e alternativas descartadas |
| `skills/bks-daiwl/` | a skill publicada |
| `README.md`, `README.pt-BR.md` | a página pública |
| `CHANGELOG.md` | o histórico de versões da skill |
