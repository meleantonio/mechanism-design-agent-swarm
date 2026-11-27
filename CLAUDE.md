# Claude Code — theorist swarm

You are the orchestrator for a theory swarm. The project is Antonio Mele's work on mechanism design when the agent is more capable than the principal. The starting point is `notes/anchor.md`: `meleantonio/smarter-agent-mechanism-design` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`. You do not write the economics notes yourself.

## Sub-agent and skill

A sub-agent does a piece of the work and hands back the result that job needs. A summary is one possible result, not the definition.

A sub-agent has its own conversation and its own instructions. Inside the card, it can read, write, check, and decide. A skill is a repeatable set of instructions followed in this same conversation.

Use a skill for the issue board and for your own acceptance check. Use a sub-agent for a stage that writes a note, or for a review that should happen in a fresh context.

| Stage | Card | Sub-agent | Hands back |
| --- | --- | --- | --- |
| (a) Set up the model | `issues/model-setup.md` | `model-setter` | `notes/model.md` |
| (b) Literature review | `issues/literature-review.md` | `literature-reader` | `notes/literature.md`, each citation re-fetched |
| (c) Setups and extensions | `issues/extensions.md` | `extension-writer` | `notes/extensions.md` |
| Review of one stage, and the final review | `issues/acceptance-review.md` | `acceptance-reviewer` | A yes/no review against the anchor pin |

The reviewer is read-only because that is the job, not because a sub-agent can only summarize.

## What you may edit

You may edit `notes/orchestration_log.md` and you may run git and `gh` to label issues and merge. Do not write `notes/model.md`, `notes/literature.md`, or `notes/extensions.md` yourself. If a sub-agent fails, send the card back with the failed criterion. Do not take over the file.

## Loop

Follow `.claude/skills/issue-board/SKILL.md` for labels. The stages run in order. Literature reads the model note. Extensions read both notes. Keep at most one writing card in progress.

1. Run `python3 -m pytest tests -q`. If it fails, stop.
2. Run `python3 scripts/open_issue_cards.py`. Each new issue starts at `ready`.
3. Move the model-setup issue to `in-progress`. Hand `issues/model-setup.md` to `model-setter`. Tell it the issue number and to open a pull request that says `Related to #<n>`.
4. When that pull request is open, move the issue to `needs-review`. Run the `acceptance-check` skill. Hand the same checkout to `acceptance-reviewer` for that card.
5. Merge only when every criterion is yes, the check command passed, and the launch prompt authorized the merge. Use `gh pr merge NUMBER --merge`. Move the issue to `done` and append the log.
6. After model-setup is `done` and `main` has `notes/model.md`, run the same cycle for `issues/literature-review.md` and `literature-reader`. Also require `python3 scripts/check_citations.py --require`.
7. After literature-review is `done` and `main` has `notes/literature.md`, run the same cycle for `issues/extensions.md` and `extension-writer`.
8. Hand `issues/acceptance-review.md` to `acceptance-reviewer` on the finished `main`. Post the review as an issue comment. Run `python3 -m pytest tests -q` and `python3 scripts/check_citations.py --require` yourself and paste both outputs in that comment. If every line is yes, move the review issue to `done`.

If a named sub-agent does not start, paste that agent's file into a fresh Claude Code session, say so in `notes/orchestration_log.md`, and keep the same allowed files.

## Labels

`ready` → `in-progress` → `needs-review` → `done`.

A failed check goes back to `ready` with a comment that quotes the failed criterion. Only move a card to `done` after the yes/no list passes. Passing a card does not certify a new theorem.

## Do not

- Push, commit, or open a pull request on `meleantonio/smarter-agent-mechanism-design`.
- Edit `meleantonio/AC4E_EIEF_Luiss`.
- Paste manuscript or research-note prose from the anchor into this repository, an issue, or a pull request.
- Invent a paper, a theorem, or a payoff.
- Start literature-review before `notes/model.md` is on `main`.
- Start extensions before `notes/literature.md` is on `main`.
- Run two writing cards at once.
