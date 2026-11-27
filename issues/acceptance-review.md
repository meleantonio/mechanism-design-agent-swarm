# [Toy] Review the three cards

**Label:** `ready` · **Role:** checker · **Separate copy (branch):** none · **Sub-agent:** `acceptance-reviewer`

Start this card after the three writing cards have files on the checkout you are reviewing. This sub-agent reads and decides. It does not edit.

## Goal

The acceptance-reviewer answers every writing-card criterion yes or no from the files on this checkout.

## Allowed files

- None. Read only.

## Acceptance criteria (done when)

- [ ] The review answers every checkbox on the three writing cards with yes or no.
- [ ] Every no names the file that fails, and a review with no failures says that all three cards pass.
- [ ] The review says the numbers are synthetic teaching data and does not call them a theorem or a result from a research draft.
- [ ] No file in the checkout changes as part of this card.

## Check command

```bash
python3 -m pytest tests toy/tests -q
```

The orchestrator runs that command in the main conversation, using the `acceptance-check` skill, and pastes the output into the issue comment with the review. This sub-agent does not run the command.

## Not in this card

- Editing notes, rules, or tests.
- Merging a pull request. The orchestrator merges only when this review is all yes and the launch prompt allowed the merge.
