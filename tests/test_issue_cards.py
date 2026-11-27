"""Structural checks for the issue cards. They do not judge economics."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WRITING = (
    "issues/setting-note.md",
    "issues/mechanism-sketch.md",
    "issues/smarter-agent-check.md",
)
PARALLEL = (
    "issues/setting-note.md",
    "issues/mechanism-sketch.md",
)


def _section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.index(marker)
    rest = text[start + len(marker) :]
    nxt = rest.find("\n## ")
    body = rest if nxt < 0 else rest[:nxt]
    return body.strip()


def _paths(text: str) -> set[str]:
    return set(re.findall(r"`([^`]+\.[a-z]+)`", _section(text, "Allowed files")))


def test_each_card_has_one_goal_and_yes_no_checks() -> None:
    """Each card has one goal sentence and at least three checkboxes."""
    for rel in (*WRITING, "issues/acceptance-review.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        goal = re.sub(r"`[^`]+`", "FILE", _section(text, "Goal"))
        sentences = [part for part in goal.replace("\n", " ").split(".") if part.strip()]
        assert len(sentences) == 1, rel
        boxes = [line for line in text.splitlines() if line.strip().startswith("- [ ]")]
        assert len(boxes) >= 3, rel
        assert "## Check command" in text
        assert "python3 -m pytest tests toy/tests -q" in text


def test_parallel_cards_do_not_share_files() -> None:
    """The two cards that may run together edit different paths."""
    used: dict[str, str] = {}
    for rel in PARALLEL:
        for path in _paths((ROOT / rel).read_text(encoding="utf-8")):
            assert path not in used, f"{path} is on {used[path]} and {rel}"
            used[path] = rel
    assert "notes/setting.md" in used.values() or "notes/setting.md" in used
    assert "toy/rules.py" in used
