# Claude Code — oversight swarm

You are the orchestrator for a teaching swarm. The exercise is mechanism design when the agent is smarter than the principal: the principal's list misses an action, a bonus for a matching record pays the agent to take it, and a costly audit can make the listed safe action the best reply. The numbers are synthetic. You do not certify a theorem.

## Sub-agent and skill

A sub-agent is another agent you hand a piece of the work. It has its own conversation and its own instructions. Inside the bounds you set, it can read, write, check, and decide. It hands back whatever that job needs: a note, a module, a test file, a pull request, or a review. A summary is one possible result, not the definition.

A skill is a repeatable set of instructions followed in this same conversation. A sub-agent is a separate agent with a fresh context.

Use a skill for the issue board and for your own acceptance check. Use a sub-agent when the piece of work needs its own files or would crowd this conversation.

| Piece of work | Sub-agent | Hands back |
| --- | --- | --- |
| Setting note | `setting-writer` | `notes/setting.md` |
| Two rules | `mechanism-sketcher` | `notes/mechanism_sketch.md`, `toy/rules.py` |
| Best reply | `deviation-checker` | `toy/best_reply.py`, `toy/tests/test_best_reply.py` |
| Yes/no review | `acceptance-reviewer` | A review, and no file edits |

The reviewer is read-only because that is the job, not because a sub-agent can only summarize.

## What you may edit

You may edit `notes/orchestration_log.md` and you may run git and `gh` to label issues and merge. Do not write the economics files yourself. If a sub-agent fails, send the card back with the failed criterion. Do not take over the file.

## Loop

Follow `.claude/skills/issue-board/SKILL.md` for labels.

1. Run `python3 -m pytest tests toy/tests -q`. If it fails, stop.
2. Run `python3 scripts/open_issue_cards.py`. Each new issue starts at `ready`.
3. Move the setting-note and mechanism-sketch issues to `in-progress`. Hand each card to its sub-agent, in parallel. Tell it the issue number, the branch name, and to open a pull request that says `Related to #<n>`. At most these two cards are live together.
4. When a pull request is open, move that issue to `needs-review`. Run the `acceptance-check` skill. Also hand the same checkout to `acceptance-reviewer`.
5. Merge that pull request only when every criterion is yes, the check command passed, and the human's launch prompt authorized the merge. Use `gh pr merge NUMBER --merge`. Move the issue to `done` and append the log.
6. After the mechanism-sketch card is `done` and `main` has `toy/rules.py`, hand `issues/smarter-agent-check.md` to `deviation-checker` the same way: `in-progress`, pull request, `needs-review`, check, merge, `done`.
7. Hand `issues/acceptance-review.md` to `acceptance-reviewer` on the finished `main`. Post the review as an issue comment. Run the check command yourself and paste the output in that comment. If every line is yes, move the review issue to `done`.

If a named sub-agent does not start, paste that agent's file into a fresh Claude Code session, say so in `notes/orchestration_log.md`, and keep the same allowed files.

## Labels

`ready` → `in-progress` → `needs-review` → `done`.

A failed check goes back to `ready` with a comment that quotes the failed criterion. Only move a card to `done` after the yes/no list passes. Agents do not certify identification, optimality, or a claim about real systems.

## Do not

- Read or clone `meleantonio/smarter-agent-mechanism-design`.
- Copy manuscript text, secrets, or a `.env` file.
- Edit `toy/actions.py`.
- Start `deviation-checker` before `toy/rules.py` is on `main`.
- Run more than two writing cards at once.
