# Synthetic oversight table

One principal writes an oversight rule. One agent can take an action the principal did not write down.

The principal's list has two actions, `safe` and `risky`. The agent also knows `lookalike`. The principal's record cannot tell `lookalike` from `safe`. Carrying out `lookalike` is worse for the principal. Once a bonus is paid whenever the record says `safe`, `lookalike` is better for the agent than `safe`.

This folder fixes that table. The issue cards ask the swarm to write the setting note, the two rules, and the best-reply check. The numbers are made up for the exercise. They are not a theorem and not a result from a research draft.

Bergemann, Koh and Morris (2026), *Mechanism Design for Alignment and Control* (arXiv:2609.01595), is the public paper that frames oversight of a more capable agent. This table does not reproduce that paper.

## Already here

- `actions.py` holds the three actions.
- `show_actions.py` prints the table: `python3 toy/show_actions.py`.

## The cards add

- `notes/setting.md`
- `notes/mechanism_sketch.md`
- `rules.py`
- `best_reply.py`
- `tests/test_best_reply.py`

Do not edit `actions.py`. It is the exercise data.
