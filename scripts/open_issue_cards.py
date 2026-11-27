"""Open one GitHub issue per card in ``issues/``.

The script is idempotent: a title that already exists is left as it is.
Run from a checkout of this repository, with ``gh`` authenticated for it:

    python3 scripts/open_issue_cards.py
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
from pathlib import Path

LOGGER = logging.getLogger("open_issue_cards")

ROOT = Path(__file__).resolve().parents[1]
ISSUES = ROOT / "issues"

LABELS: dict[str, tuple[str, str]] = {
    "ready": ("1D76DB", "Goal and acceptance criteria are written; an agent may start"),
    "in-progress": ("FBCA04", "An agent is working on its own branch"),
    "needs-review": ("D93F0B", "A pull request or a review comment is waiting"),
    "done": ("0E8A16", "A human checked every acceptance criterion"),
}


def parse_card(text: str) -> tuple[str, str]:
    """Return the H1 title and the issue body.

    Args:
        text: Full markdown of one issue card.

    Returns:
        The title without the leading ``#``, and the body including a
        trailing newline.

    Raises:
        ValueError: The card has no H1 title.
    """
    title = ""
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    if not title:
        raise ValueError("card has no H1 title")
    body = text if text.endswith("\n") else text + "\n"
    return title, body


def card_paths(folder: Path = ISSUES) -> list[Path]:
    """Return card paths in alphabetical order.

    Args:
        folder: Directory of ``*.md`` cards.

    Returns:
        Sorted paths.
    """
    return sorted(folder.glob("*.md"))


def _run(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run a command and log it.

    Args:
        args: Command and arguments.
        check: When True, raise if the exit code is not zero.

    Returns:
        The completed process.

    Raises:
        subprocess.CalledProcessError: The command failed and ``check`` is True.
    """
    LOGGER.info("run %s", " ".join(args))
    completed = subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.stdout:
        LOGGER.info(completed.stdout.strip())
    if completed.returncode != 0:
        LOGGER.error(completed.stderr.strip())
        if check:
            raise subprocess.CalledProcessError(completed.returncode, args, completed.stdout, completed.stderr)
    return completed


def ensure_labels() -> None:
    """Create the four swarm labels when they are missing."""
    for name, (color, description) in LABELS.items():
        completed = _run(
            ["gh", "label", "create", name, "--color", color, "--description", description],
            check=False,
        )
        if completed.returncode != 0 and "already exists" not in completed.stderr.lower():
            raise subprocess.CalledProcessError(
                completed.returncode,
                ["gh", "label", "create", name],
                completed.stdout,
                completed.stderr,
            )


def existing_titles() -> dict[str, int]:
    """Map issue titles to numbers, open and closed.

    Returns:
        Title to issue number.
    """
    completed = _run(
        ["gh", "issue", "list", "--state", "all", "--limit", "200", "--json", "number,title"],
    )
    rows = json.loads(completed.stdout or "[]")
    return {row["title"]: int(row["number"]) for row in rows}


def open_cards() -> list[tuple[str, int, str]]:
    """Create any missing issues.

    Returns:
        Tuples of title, issue number, and ``created`` or ``exists``.
    """
    ensure_labels()
    found = existing_titles()
    results: list[tuple[str, int, str]] = []
    for path in card_paths():
        title, body = parse_card(path.read_text(encoding="utf-8"))
        if title in found:
            LOGGER.info("exists #%s %s", found[title], title)
            results.append((title, found[title], "exists"))
            continue
        body_path = path
        completed = _run(
            ["gh", "issue", "create", "--title", title, "--body-file", str(body_path), "--label", "ready"],
        )
        url = (completed.stdout or "").strip()
        found = existing_titles()
        number = found.get(title, 0)
        LOGGER.info("created #%s %s %s", number, title, url)
        results.append((title, number, "created"))
    return results


def main() -> int:
    """Open the cards and print one line per issue.

    Returns:
        Zero when every card exists or was created.
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    try:
        for title, number, status in open_cards():
            print(f"{status}\t#{number}\t{title}")
    except (subprocess.CalledProcessError, OSError, ValueError) as exc:
        LOGGER.error("%s", exc)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
