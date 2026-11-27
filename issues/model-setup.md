# Set up the model

**Label:** `ready` · **Role:** writer · **Separate copy (branch):** `theory/model-setup` · **Sub-agent:** `model-setter` · **Reviewer:** `acceptance-reviewer`

## Goal

`notes/model.md` states players, timing, information, and instruments for a principal overseeing a more capable agent, using the anchor commit recorded in `notes/anchor.md`.

## Allowed files

- `notes/model.md` (create)

## Acceptance criteria (done when)

- [ ] The note has the headings Players, Timing, Information, Instruments, What more capable means, Settled on the pin, Still open, and Sources opened, and Sources opened lists `README.md`, `notes/00-seed.md`, `notes/03-open-questions.md`, `notes/04-theoretical-framework.md`, `notes/05-results-index.md`, `docs/research-roadmap.md`, and `docs/research-roadmap-next.md` with `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- [ ] What more capable means names four distinct readings and the anchor note for each, and it says they are not one constraint.
- [ ] Settled on the pin says R1–R12 are complete at their stated scope and that H1–H6 stay speculative, and Still open names R13, R14, R15, issues #33–#35, and pull requests #37–#39 as in flight.
- [ ] `git diff --stat` shows only `notes/model.md`, the note does not paste anchor prose or display mathematics, and the check command passes.

## Check command

```bash
python3 -m pytest tests -q
```

## Not in this card

- Writing the literature note or the extensions note.
- Any new theorem, payoff, or invented paper.
- A push to `meleantonio/smarter-agent-mechanism-design`.
