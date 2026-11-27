# [Toy] Check the smarter agent's best reply

**Label:** `ready` · **Role:** writer · **Separate copy (branch):** `toy/smarter-agent-check` · **Sub-agent:** `deviation-checker` · **Reviewer:** `acceptance-reviewer`

Start this card only after `toy/rules.py` is on `main`.

## Goal

`toy/best_reply.py` and its tests show that lookalike is the best reply to the naive bonus and that safe is the best reply to the audit.

## Allowed files

- `toy/best_reply.py` (create)
- `toy/tests/test_best_reply.py` (create)

## What to implement

`best_reply(rule, only_listed=False)` returns the action with the highest agent payoff from `toy.rules.payoffs`. When `only_listed` is true, rank only actions with `listed` true. If two agent payoffs are equal, return the name that comes last in alphabetical order. Do not return a hard-coded action name.

`format_report()` returns text that includes these lines:

```text
naive_bonus best_reply lookalike
naive_bonus listed_best_reply safe
audit_bonus best_reply safe
naive_bonus principal -8
audit_bonus principal 0
```

The principal lines are the principal's payoff at that rule's best reply over all actions, including `lookalike`.

## Acceptance criteria (done when)

- [ ] `best_reply("naive_bonus")` is `lookalike`, and `best_reply("naive_bonus", only_listed=True)` is `safe`.
- [ ] `best_reply("audit_bonus")` is `safe`, and the agent's audit payoff for `safe` is strictly higher than for `lookalike` and for `risky`.
- [ ] The principal's payoff at the naive best reply is -8 and at the audit best reply is 0, and `format_report()` contains the five lines in this card.
- [ ] The new tests call `best_reply` and `payoffs`, `best_reply.py` calls `payoffs` rather than returning a fixed name, only the two allowed files change, and the check command passes.

## Check command

```bash
python3 -m pytest tests toy/tests -q
```

## Not in this card

- Editing `toy/actions.py` or `toy/rules.py`.
- Any claim that the best reply is what a deployed system would do.
