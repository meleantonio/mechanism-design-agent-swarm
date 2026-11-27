"""The Claude Code harness files exist and name the sub-agents."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

AGENTS = {
    ".claude/agents/setting-writer.md": "setting-writer",
    ".claude/agents/mechanism-sketcher.md": "mechanism-sketcher",
    ".claude/agents/deviation-checker.md": "deviation-checker",
    ".claude/agents/acceptance-reviewer.md": "acceptance-reviewer",
}


def test_subagent_frontmatter_names() -> None:
    """Each sub-agent file declares the name Claude Code calls."""
    for rel, name in AGENTS.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert text.startswith("---\n")
        assert f"name: {name}\n" in text
        assert "description:" in text


def test_skills_are_named_like_their_folders() -> None:
    """A skill is instructions for this conversation, with a matching name."""
    for folder in ("issue-board", "acceptance-check"):
        text = (ROOT / ".claude" / "skills" / folder / "SKILL.md").read_text(encoding="utf-8")
        assert f"name: {folder}\n" in text


def test_claude_md_drives_the_loop() -> None:
    """The root instructions name the loop, the labels, and the sub-agents."""
    text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    for phrase in (
        "setting-writer",
        "mechanism-sketcher",
        "deviation-checker",
        "acceptance-reviewer",
        "ready",
        "in-progress",
        "needs-review",
        "done",
        "python3 scripts/open_issue_cards.py",
    ):
        assert phrase in text
