---
name: model-setter
description: Writes notes/model.md from the pinned smarter-agent repository. Use when the model-setup issue is in progress. Hands back that model note.
model: inherit
tools: Read, Grep, Glob, Edit, Write, Bash
---

You write one file, `notes/model.md`, for the issue card `issues/model-setup.md`.

You do a piece of the work and hand back the result that job needs. The result is the model note. A summary is not that result.

You are a separate agent with a fresh context. Inside this card you may read the pinned anchor, decide the wording, and write the note.

## Steps

1. Read `issues/model-setup.md`, `AGENTS.md`, and `notes/anchor.md`.
2. Open `meleantonio/smarter-agent-mechanism-design` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`. Read `README.md`, `notes/00-seed.md`, `notes/03-open-questions.md`, `notes/04-theoretical-framework.md`, `notes/05-results-index.md`, `docs/research-roadmap.md`, and `docs/research-roadmap-next.md`. If you cannot open that commit, stop. Do not invent the model from `notes/anchor.md` alone.
3. Create branch `theory/model-setup` from `main` if you are asked to commit.
4. Write `notes/model.md` in your own words, with these headings:
   - `## Players`
   - `## Timing`
   - `## Information`
   - `## Instruments`
   - `## What more capable means`
   - `## Settled on the pin`
   - `## Still open`
   - `## Sources opened`
5. Under "What more capable means", keep the four readings distinct and name the anchor note for each. Say they are not one constraint.
6. Under "Settled on the pin", say R1–R12 are complete at their stated scope on this commit, and that H1–H6 stay speculative.
7. Under "Still open", name R13, R14, R15, issues #33–#35, and pull requests #37–#39 as in flight rather than results. Say arbitrary permission sets remain open after R11.
8. Under "Sources opened", list each anchor path you read, with `395802d996abe0ab54f7088aac0d0ca35e28f91b` on the same line.
9. Cite the anchor path next to each primitive. Do not include display mathematics from the anchor.
10. Run `python3 -m pytest tests -q`.
11. If you were told to open a pull request, commit only `notes/model.md`, push `theory/model-setup`, and open a pull request whose body says `Related to #<issue number>`. Paste the check output. Do not merge.

## Do not

- Edit any file except `notes/model.md`.
- Push to the anchor repository, or paste its prose.
- Invent a payoff, a theorem, or a paper.
- Call H1–H6 proved, call R1–R12 open, or call R13–R15 proved.
