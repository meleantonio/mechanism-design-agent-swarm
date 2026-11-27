# Propose setups and extensions

**Label:** `ready` · **Role:** writer · **Separate copy (branch):** `theory/extensions` · **Sub-agent:** `extension-writer` · **Reviewer:** `acceptance-reviewer`

Start this card only after the literature-review card is done and `notes/literature.md` is on `main`.

## Goal

`notes/extensions.md` proposes three setups or extensions that stay inside the open directions recorded in `notes/anchor.md`.

## Allowed files

- `notes/extensions.md` (create)

## Acceptance criteria (done when)

- [ ] The note has Setup 1, Setup 2, and Setup 3, and each setup has the labels Open direction, Primitives changed, Completed package left in place, Anchor issue or pull request, Literature identifiers, Result this setup would need later, and Not claimed.
- [ ] At least one open direction is R13, R14, or R15, and every literature identifier appears in `notes/literature.md`.
- [ ] Each completed-package line names an R1–R12 package the setup does not redo, and a setup that matches pull request #37, #38, or #39 names that pull request and says this swarm is not merging it.
- [ ] Sources opened lists `notes/model.md`, `notes/literature.md`, `notes/anchor.md`, and `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`, only `notes/extensions.md` changes, and the check command passes.

## Check command

```bash
python3 -m pytest tests -q
```

## Not in this card

- A claim that the setup is already proved.
- Redoing a completed R1–R12 package as if it were open.
- An identifier that is not in `notes/literature.md`.
