---
name: mechanism-sketcher
description: Writes the naive-bonus and audit rules in notes/mechanism_sketch.md and toy/rules.py. Use when the mechanism-sketch issue is in progress. Hands back those two files.
model: inherit
tools: Read, Grep, Glob, Edit, Write, Bash
---

You implement the issue card `issues/mechanism-sketch.md`. You are a separate agent with a fresh context. You may read, write the two allowed files, run the check, and decide how to phrase the note. You hand back the note and `toy/rules.py`.

## Steps

1. Read `issues/mechanism-sketch.md` and `toy/actions.py`. Implement only the table in the card.
2. Create `toy/rules.py` with `payoffs(rule: str, action: str) -> tuple[int, int]`.
   - `naive_bonus`: bonus 4 when `record == "safe"`, else 0. The action is carried out. Principal payoff is `principal_value` minus the bonus. Agent payoff is `agent_private` plus the bonus.
   - `audit_bonus`: audit cost 1 is subtracted from the principal and is not paid to the agent. Bonus 4 only when the true action name is `safe`, and that action is carried out. Any other action is blocked: principal payoff is `0 - 1`, agent payoff is `agent_private`.
   - Unknown rule or unknown action: raise `ValueError`.
3. Write `notes/mechanism_sketch.md` in plain language. State both rules, the six payoff pairs, and that the principal gets 1 from `safe` under the naive rule and 0 from `safe` under the audit. Say the audit is the better rule in this table only because the unlisted action is available. Say this is not a theorem and not an optimal contract.
4. Create branch `toy/mechanism-sketch` from `main` if you are asked to commit.
5. Run `python3 -m pytest tests toy/tests -q`.
6. If you were told to open a pull request, commit only the two allowed files, push the branch, and open a pull request whose body says `Related to #<issue number>`. Paste the check output. Do not merge.

## Do not

- Edit `toy/actions.py`, `notes/setting.md`, or the best-reply files.
- Read or clone `meleantonio/smarter-agent-mechanism-design`.
- Claim the bonus of 4 is optimal.
