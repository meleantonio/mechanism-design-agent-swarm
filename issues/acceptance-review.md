# Review the three stages against the anchor

**Label:** `ready` · **Role:** checker · **Separate copy (branch):** none · **Sub-agent:** `acceptance-reviewer`

Start this card after the three writing cards have notes on the checkout you are reviewing. This sub-agent reads and decides. It does not edit.

## Goal

The acceptance-reviewer answers every writing-card criterion yes or no by comparing the three notes with `notes/anchor.md`.

## Allowed files

- None. Read only.

## Acceptance criteria (done when)

- [ ] The review answers every checkbox on the three writing cards with yes or no, and it names the commit `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- [ ] Every no names the file that fails, and a review with no failures says that all three notes agree with the pin on what is settled and what is open.
- [ ] The review does not call R13–R15 proved, does not call R1–R12 open, and does not add a paper that is absent from `notes/literature.md`.
- [ ] No file in the checkout changes as part of this card.

## Check command

```bash
python3 -m pytest tests -q
```

The orchestrator runs that command, and `python3 scripts/check_citations.py --require`, in the main conversation, using the `acceptance-check` skill, and pastes both outputs into the issue comment with the review. This sub-agent does not run the commands.

## Not in this card

- Editing notes.
- Merging a pull request. The orchestrator merges only when this review is all yes and the launch prompt allowed the merge.
