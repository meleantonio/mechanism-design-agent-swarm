---
name: issue-board
description: Use when opening the swarm cards on GitHub or moving a card among ready, in-progress, needs-review, and done.
---

# Issue board

A skill is a repeatable set of instructions followed in this conversation. Follow it here. Hand a card to a sub-agent when the work needs its own files and a fresh context.

1. From the repository root, run `python3 scripts/open_issue_cards.py`.
2. Run `gh issue list --state open --json number,title,labels` and keep the output.
3. To move a card, run `gh issue edit NUMBER --remove-label OLD --add-label NEW`.
4. Append one row to `notes/orchestration_log.md` with the issue number, the old label, the new label, and the pull-request URL when there is one.
5. Use `Related to #N` on a pull request. Add `Closes #N` only when you merge after every acceptance criterion is yes.

## Labels

| Label | Meaning |
| --- | --- |
| `ready` | The goal and the yes/no checks are written |
| `in-progress` | A sub-agent is working on its own branch |
| `needs-review` | A pull request, or the review comment, is waiting |
| `done` | Every acceptance criterion was yes and the card was accepted |

## Do not

- Open a second issue for a title that already exists.
- Mark a card `done` because the sub-agent said it was finished. Mark it `done` only after the acceptance criteria are yes.
- Put confidential data, secrets, or manuscript text on an issue.
