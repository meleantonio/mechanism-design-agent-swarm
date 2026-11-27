"""Print the synthetic action table.

Run from the repository root:

    python3 toy/show_actions.py
"""

from __future__ import annotations

from actions import ACTIONS, action_names


def render_table() -> str:
    """Render the action table as aligned text.

    Returns:
        A trailing-newline string with one header and one row per action.
    """
    header = f"{'action':<12}{'listed':<8}{'principal_value':>16}{'agent_private':>16}{'record':>10}"
    rows = [header]
    for name in action_names():
        item = ACTIONS[name]
        listed = "yes" if item.listed else "no"
        rows.append(
            f"{item.name:<12}{listed:<8}{item.principal_value:>16}{item.agent_private:>16}{item.record:>10}"
        )
    return "\n".join(rows) + "\n"


def main() -> None:
    """Print the table to standard output."""
    print(render_table(), end="")


if __name__ == "__main__":
    main()
