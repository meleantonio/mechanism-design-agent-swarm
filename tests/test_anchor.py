"""The pin names the anchor commit and drops the synthetic toy."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "395802d996abe0ab54f7088aac0d0ca35e28f91b"


def test_anchor_note_pins_the_commit() -> None:
    """The status map names the repository, the commit, and the open packages."""
    text = (ROOT / "notes" / "anchor.md").read_text(encoding="utf-8")
    assert "meleantonio/smarter-agent-mechanism-design" in text
    assert PIN in text
    assert "Do not push" in text
    for label in ("R13", "R14", "R15"):
        assert label in text
    assert "Pull request #37" in text
    assert "Pull request #38" in text
    assert "Pull request #39" in text
    assert "Koh and Martinez-Bruera" in text
    assert "arXiv:2609.01595" in text


def test_instructions_share_the_pin() -> None:
    """The orchestrator files and the launch prompt use the same commit."""
    for rel in ("CLAUDE.md", "AGENTS.md", "README.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert PIN in text
        assert "A sub-agent does a piece of the work and hands back the result that job needs." in text


def test_synthetic_toy_is_gone() -> None:
    """The invented oversight table is not part of this swarm."""
    assert not (ROOT / "toy").exists()
    needles = ("look" + "alike", "naive_" + "bonus", "[Toy]")
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".py", ".yml"}:
            continue
        if ".git" in path.parts or "tests" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            assert needle not in text, path
