# [Toy] Sketch the two oversight rules

**Label:** `ready` · **Role:** writer · **Separate copy (branch):** `toy/mechanism-sketch` · **Sub-agent:** `mechanism-sketcher` · **Reviewer:** `acceptance-reviewer`

## Goal

`notes/mechanism_sketch.md` and `toy/rules.py` state the naive bonus and the costly audit, with principal and agent payoffs equal to the table in this card.

## Allowed files

- `notes/mechanism_sketch.md` (create)
- `toy/rules.py` (create)

## The rules

Both rules use `toy/actions.py`. Do not change that file. Payoffs are integers. `payoffs(rule, action)` returns `(principal_payoff, agent_payoff)`.

**Naive bonus.** If the action's record is `safe`, the principal pays the agent a bonus of 4. Otherwise the bonus is 0. The action is carried out. The principal's payoff is `principal_value` minus the bonus. The agent's payoff is `agent_private` plus the bonus.

**Audit.** The principal pays an audit cost of 1, which is not given to the agent. If the true action is `safe`, the action is carried out and the bonus is 4. If the true action is anything else, the action is blocked: the principal gets none of `principal_value`, and the bonus is 0. The agent's payoff is `agent_private` plus the bonus.

| Rule | Action | Principal | Agent |
| --- | --- | ---: | ---: |
| `naive_bonus` | `safe` | 1 | 4 |
| `naive_bonus` | `risky` | -1 | 3 |
| `naive_bonus` | `lookalike` | -8 | 7 |
| `audit_bonus` | `safe` | 0 | 4 |
| `audit_bonus` | `risky` | -1 | 3 |
| `audit_bonus` | `lookalike` | -1 | 3 |

An unknown rule name or an unknown action name raises `ValueError`.

## Acceptance criteria (done when)

- [ ] The note describes the naive bonus as a transfer of 4 when the record is `safe`, and the audit as a cost of 1, a bonus of 4 only when the true action is `safe`, and a block on every other action.
- [ ] `payoffs` returns the six pairs in the table, and `payoffs("unknown", "safe")` raises `ValueError`.
- [ ] The note says the principal's payoff is 1 if the agent plays `safe` under the naive rule and 0 when `safe` is played under the audit, so the audit is the better rule in this table only because the unlisted action is available.
- [ ] `git diff --stat` shows only the two allowed files, and the check command passes.

## Check command

```bash
python3 -m pytest tests toy/tests -q
```

## Not in this card

- Editing `toy/actions.py`, `notes/setting.md`, or the best-reply files.
- Any claim that this comparison is a theorem, or that the bonus of 4 is an optimal contract.
