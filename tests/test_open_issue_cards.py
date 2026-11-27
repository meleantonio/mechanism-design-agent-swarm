"""Parser tests for the issue-card opener. They do not call GitHub."""

from __future__ import annotations

import pytest

import open_issue_cards


def test_parse_card_reads_the_h1() -> None:
    """The issue title is the H1, and the body keeps the card text."""
    title, body = open_issue_cards.parse_card("# [Toy] Example\n\nHello.\n")
    assert title == "[Toy] Example"
    assert body.startswith("# [Toy] Example")
    assert body.endswith("\n")


def test_parse_card_rejects_a_missing_title() -> None:
    """A card without an H1 cannot become an issue."""
    with pytest.raises(ValueError, match="H1"):
        open_issue_cards.parse_card("No title here.\n")


def test_repo_cards_parse() -> None:
    """Every card in issues/ has a title."""
    paths = open_issue_cards.card_paths()
    assert len(paths) == 4
    titles = [open_issue_cards.parse_card(path.read_text(encoding="utf-8"))[0] for path in paths]
    assert all(title.startswith("[Toy] ") for title in titles)
