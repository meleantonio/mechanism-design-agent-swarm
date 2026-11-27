"""Structural checks for the issue cards. They do not judge economics."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WRITING = (
    "issues/model-setup.md",
    "issues/literature-review.md",
    "issues/extensions.md",
)
PIN = "395802d996abe0ab54f7088aac0d0ca35e28f91b"


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
        assert "python3 -m pytest tests -q" in text
        assert PIN in text


def test_writing_cards_do_not_share_files() -> None:
    """The three writing cards edit different paths."""
    used: dict[str, str] = {}
    for rel in WRITING:
        paths = _paths((ROOT / rel).read_text(encoding="utf-8"))
        assert paths, rel
        for path in paths:
            assert path not in used, f"{path} is on {used[path]} and {rel}"
            used[path] = rel
    assert used == {
        "notes/model.md": "issues/model-setup.md",
        "notes/literature.md": "issues/literature-review.md",
        "notes/extensions.md": "issues/extensions.md",
    }


def test_later_cards_wait_for_earlier_notes() -> None:
    """Literature waits for the model, and extensions wait for the literature."""
    literature = (ROOT / "issues/literature-review.md").read_text(encoding="utf-8")
    extensions = (ROOT / "issues/extensions.md").read_text(encoding="utf-8")
    assert "after the model-setup card is done" in literature
    assert "after the literature-review card is done" in extensions
    assert "arXiv:2609.01595" in literature
    assert "doi:10.2307/2297639" in literature
    assert "python3 scripts/check_citations.py --require" in literature


def test_cards_are_not_the_synthetic_toy() -> None:
    """Issue titles name the theorist stages."""
    titles = []
    for path in (ROOT / "issues").glob("*.md"):
        first = path.read_text(encoding="utf-8").splitlines()[0]
        titles.append(first)
        assert "[Toy]" not in first
        assert "lookalike" not in path.read_text(encoding="utf-8")
    assert "# Set up the model" in titles
    assert "# Review the related literature" in titles
    assert "# Propose setups and extensions" in titles
    assert "# Review the three stages against the anchor" in titles
