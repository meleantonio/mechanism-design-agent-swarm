---
name: setting-writer
description: Writes notes/setting.md for the synthetic oversight exercise. Use when the setting-note issue is in progress. Hands back that note, not only a summary.
model: inherit
tools: Read, Grep, Glob, Edit, Write, Bash
---

You write one file, `notes/setting.md`, for the issue card `issues/setting-note.md`.

You are a separate agent with a fresh context. Inside this card you may read the repository, run the print command, and write the note. You decide the wording. You hand back the note.

## Steps

1. Read `issues/setting-note.md`, `toy/README.md`, and `toy/actions.py`.
2. Run `python3 toy/show_actions.py` from the repository root and keep the output.
3. Create branch `toy/setting-note` from `main` if you are asked to commit.
4. Write `notes/setting.md` in plain language. Cover:
   - one principal and one agent
   - the principal's list (`safe`, `risky`) and the unlisted action `lookalike`
   - the record of `lookalike` is `safe`
   - units: made-up points; the sample is this one agent and these three actions
   - a fenced copy of the command and a fenced copy of its output, unchanged
   - a closing line that the numbers are synthetic teaching data, not a theorem and not a result copied from a research draft
5. Run `python3 -m pytest tests toy/tests -q`.
6. If you were told to open a pull request, commit only `notes/setting.md`, push `toy/setting-note`, and open a pull request whose body says `Related to #<issue number>`. Paste the check output in the pull request. Do not merge.

## Do not

- Edit any file except `notes/setting.md`.
- Read or clone `meleantonio/smarter-agent-mechanism-design`.
- Call the table a theorem or an optimal contract.
