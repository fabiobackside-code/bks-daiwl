# STATUS — bks-daiwl

> Ponto de entrada do projeto. Leia só este arquivo para saber onde as coisas estão e o que fazer
> a seguir. Atualizado pelo `/bks:save` ao fim de cada sessão; lido pelo `/bks:brain`.
>
> Última atualização: 2026-11-08

---

## Em uma frase

A skill 1.0.0 virou projeto próprio com estrutura de repositório público (licença MIT, README
bilíngue, CHANGELOG, CONTRIBUTING, SECURITY), versionada localmente, ainda sem remoto no GitHub e
sem nenhum teste.

---

## Fase atual

**Empacotamento** — o conteúdo veio pronto do pacote `.skill`. A fase termina com o repositório
publicado, o primeiro release `.skill` anexado e o `daiwl.py` coberto por teste.

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

Depois, abrir sessão nesta pasta e escrever os testes do `daiwl.py`: `score` e `rescore`
determinísticos sobre um `findings.json` de exemplo, normalização do esquema antigo em português e
recusa de delta quando o `formula_version` muda.

---

## Decisões que valem

| # | Decisão | Onde |
|---|---|---|
| 1 | Repositório próprio; skill em `skills/bks-daiwl/`; o kit carrega uma cópia fixada | `decisions/ADR-001.md` |
| 2 | Licença MIT, a mesma do kit | `LICENSE` |

---

## Aberto

- Nenhum teste. O `daiwl.py` (23 KB) só passa no `py_compile`
- Sem `.github/` (templates de issue e PR, CI); entra junto com os testes
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
