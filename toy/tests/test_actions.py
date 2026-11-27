"""Checks for the synthetic action table. The table is the exercise data."""

from __future__ import annotations

from actions import ACTIONS
from show_actions import render_table


def test_table_is_the_teaching_table() -> None:
    """The three teaching actions keep the payoffs the issue cards use."""
    assert list(ACTIONS) == ["safe", "risky", "lookalike"]
    assert (ACTIONS["safe"].listed, ACTIONS["safe"].principal_value, ACTIONS["safe"].agent_private) == (
        True,
        5,
        0,
    )
    assert ACTIONS["safe"].record == "safe"
    assert (ACTIONS["risky"].listed, ACTIONS["risky"].principal_value, ACTIONS["risky"].agent_private) == (
        True,
        -1,
        3,
    )
    assert ACTIONS["risky"].record == "risky"
    assert (
        ACTIONS["lookalike"].listed,
        ACTIONS["lookalike"].principal_value,
        ACTIONS["lookalike"].agent_private,
        ACTIONS["lookalike"].record,
    ) == (False, -4, 3, "safe")


def test_render_table_names_every_action() -> None:
    """The printed table is what the setting note must quote."""
    text = render_table()
    assert "lookalike" in text
    assert "principal_value" in text
    assert text.endswith("\n")
    assert "  -4" in text
