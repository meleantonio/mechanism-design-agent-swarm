"""Synthetic actions for a teaching exercise.

One principal can write down ``safe`` and ``risky``. The agent also knows
``lookalike``, which the principal's record cannot tell apart from ``safe``.

The numbers are invented for the exercise. They are not estimates and not a
result from a research draft.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Action:
    """One action the agent can take.

    Attributes:
        name: Short name used in the code and the notes.
        listed: True when the action is on the principal's list.
        principal_value: Principal's payoff if this action is carried out,
            before any bonus or audit cost.
        agent_private: Agent's payoff before any bonus.
        record: What the principal's list records. ``lookalike`` is recorded
            as ``safe``.
    """

    name: str
    listed: bool
    principal_value: int
    agent_private: int
    record: str


ACTIONS: dict[str, Action] = {
    "safe": Action("safe", True, 5, 0, "safe"),
    "risky": Action("risky", True, -1, 3, "risky"),
    "lookalike": Action("lookalike", False, -4, 3, "safe"),
}


def action_names() -> list[str]:
    """Return action names in table order.

    Returns:
        The names ``safe``, ``risky``, and ``lookalike``.
    """
    return list(ACTIONS)
