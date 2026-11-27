---
name: deviation-checker
description: Writes toy/best_reply.py and toy/tests/test_best_reply.py, showing the unlisted action beats the naive bonus. Use after toy/rules.py is on main. Hands back the module and the tests.
model: inherit
tools: Read, Grep, Glob, Edit, Write, Bash
---

You implement the issue card `issues/smarter-agent-check.md`. You are a separate agent with a fresh context. You may read, write the two allowed files, run pytest, and decide the ranking code. You hand back the module and the tests.

## Steps

1. Read `issues/smarter-agent-check.md`, `toy/rules.py`, and `toy/actions.py`. If `toy/rules.py` is missing, stop and say the mechanism-sketch card is not on this branch.
2. Write `best_reply(rule: str, only_listed: bool = False) -> str`. Rank actions by the agent payoff from `payoffs`. Restrict to `listed` actions when `only_listed` is true. On a tie, pick the name that comes last in alphabetical order. Do not return a fixed action name.
3. Write `format_report() -> str` so it contains the five lines in the card. The principal figures are the principal payoff at the best reply over all actions.
4. Write `toy/tests/test_best_reply.py` that calls `best_reply` and `payoffs` and checks the acceptance criteria, including `payoffs("unknown", "safe")` raising `ValueError`.
5. Create branch `toy/smarter-agent-check` from current `main` if you are asked to commit.
6. Run `python3 -m pytest tests toy/tests -q` and keep the output.
7. If you were told to open a pull request, commit only the two allowed files, push, and open a pull request whose body says `Related to #<issue number>`. Do not merge.

## Do not

- Edit `toy/actions.py` or `toy/rules.py`.
- Read or clone `meleantonio/smarter-agent-mechanism-design`.
- Say the best reply describes a real AI system.
