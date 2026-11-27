"""The Claude Code harness files exist and name the sub-agents."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AGENTS = {
    ".claude/agents/model-setter.md": "model-setter",
    ".claude/agents/literature-reader.md": "literature-reader",
    ".claude/agents/extension-writer.md": "extension-writer",
    ".claude/agents/acceptance-reviewer.md": "acceptance-reviewer",
}

PIN = "395802d996abe0ab54f7088aac0d0ca35e28f91b"


def test_subagent_frontmatter_names() -> None:
    """Each sub-agent file declares the name Claude Code calls."""
    for rel, name in AGENTS.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert text.startswith("---\n")
        assert f"name: {name}\n" in text
        assert "description:" in text
        assert "Hands back" in text or "hands back" in text


def test_skills_are_named_like_their_folders() -> None:
    """A skill is instructions for this conversation, with a matching name."""
    for folder in ("issue-board", "acceptance-check"):
        text = (ROOT / ".claude" / "skills" / folder / "SKILL.md").read_text(encoding="utf-8")
        assert f"name: {folder}\n" in text


def test_claude_md_drives_the_loop() -> None:
    """The root instructions name the stages, the labels, and the sub-agents."""
    text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    for phrase in (
        "model-setter",
        "literature-reader",
        "extension-writer",
        "acceptance-reviewer",
        "ready",
        "in-progress",
        "needs-review",
        "done",
        "python3 scripts/open_issue_cards.py",
        "python3 scripts/check_citations.py --require",
        PIN,
        "A sub-agent does a piece of the work and hands back the result that job needs.",
        "A summary is one possible result, not the definition.",
    ):
        assert phrase in text
