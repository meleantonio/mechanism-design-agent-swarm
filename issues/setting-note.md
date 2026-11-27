# [Toy] Write the setting note

**Label:** `ready` · **Role:** writer · **Separate copy (branch):** `toy/setting-note` · **Sub-agent:** `setting-writer` · **Reviewer:** `acceptance-reviewer`

## Goal

`notes/setting.md` records who the principal and the agent are, the three synthetic actions, and that lookalike is missing from the principal's list.

## Allowed files

- `notes/setting.md` (create)

## Acceptance criteria (done when)

- [ ] The note names one principal and one agent, lists `safe`, `risky`, and `lookalike`, and says `lookalike` is not on the principal's list while the record of `lookalike` is `safe`.
- [ ] A fenced block in the note is byte-for-byte the output of `python3 toy/show_actions.py`, and the note quotes that command.
- [ ] The note says the payoffs are synthetic teaching numbers, not a theorem, and not a result copied from a research draft.
- [ ] `git diff --stat` shows only `notes/setting.md`, and the check command passes.

## Check command

```bash
python3 -m pytest tests toy/tests -q
```

## Not in this card

- Editing `toy/actions.py` or any other Python file.
- Writing the bonus rules or the best-reply code.
- Any claim that the table is a theorem or a result from a research draft.
