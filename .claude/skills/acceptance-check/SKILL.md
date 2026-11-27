---
name: acceptance-check
description: Use in this conversation when judging a writing card against its yes/no acceptance criteria, including the pytest command.
---

# Acceptance check

Use this skill in the orchestrator conversation when you need to judge a card yourself. Use the `acceptance-reviewer` sub-agent when the same judgment should happen in a fresh context. The skill does not replace that sub-agent.

1. Read the issue card. List its checkboxes.
2. Read only the files the card allows, plus the files those checks name.
3. Run `python3 -m pytest tests toy/tests -q` and keep the full output.
4. For each checkbox, write `yes` or `no` and the evidence: a payoff pair, a quoted line, or the pytest summary line.
5. If any checkbox is `no`, leave the card at `needs-review` and comment with the failed check. Do not merge.

## Do not

- Edit the economics files while you are only checking.
- Treat a green pytest run as a theorem.
- Mark the card done before the yes/no list is complete.
