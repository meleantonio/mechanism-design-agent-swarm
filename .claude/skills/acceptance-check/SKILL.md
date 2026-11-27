---
name: acceptance-check
description: Use in this conversation when judging a stage card against its yes/no criteria and against the anchor pin.
---

# Acceptance check

Use this skill in the orchestrator conversation when you need to judge a card yourself. Use the `acceptance-reviewer` sub-agent when the same judgment should happen in a fresh context. The skill does not replace that sub-agent.

1. Read the issue card. List its checkboxes.
2. Read `notes/anchor.md` and the files the card names.
3. Run `python3 -m pytest tests -q` and keep the full output.
4. When the card is literature-review, extensions, or acceptance-review, also run `python3 scripts/check_citations.py --require` and keep the full output.
5. When `gh` can read `meleantonio/smarter-agent-mechanism-design` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`, open the paths listed under `## Sources opened` and check the note against them. If `gh` cannot read that private repository, the anchor-agreement criterion is no. Do not pass it on the pin file alone.
6. For each checkbox, write `yes` or `no` and the evidence: a heading, a cited path, an identifier, or the command's summary line.
7. If any checkbox is `no`, leave the card at `needs-review` and comment with the failed check. Do not merge.

## Do not

- Edit the economics notes while you are only checking.
- Treat a green pytest run, or a resolved citation, as a new theorem.
- Mark the card done before the yes/no list is complete.
- Paste anchor prose into the review comment. Cite the path and the commit.
