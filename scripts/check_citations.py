"""Check that ``notes/literature.md`` cites records that resolve.

The literature card owns the note. This script re-fetches each arXiv or DOI
row and compares the title with the record. It does not decide whether a
paper is relevant.

Run from the repository root:

    python3 scripts/check_citations.py
    python3 scripts/check_citations.py --require
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

LOGGER = logging.getLogger("check_citations")

ROOT = Path(__file__).resolve().parents[1]
LITERATURE = ROOT / "notes" / "literature.md"

UNCONFIRMED_SENTENCE = (
    "Koh and Martinez-Bruera is not cited: the anchor records no stable public link."
)

REQUIRED_IDS = (
    "arXiv:2609.01595",
    "doi:10.2307/2297639",
    "doi:10.1111/j.1468-0262.2005.00638.x",
    "doi:10.1257/aer.20131159",
)

ARXIV_ID = re.compile(r"(?i)^arXiv:(\d{4}\.\d{4,5})(v\d+)?$")
DOI_ID = re.compile(r"(?i)^doi:(10\.\S+)$")
USER_AGENT = "mechanism-design-agent-swarm/citation-check"


@dataclass(frozen=True)
class Citation:
    """One row of the verified-records table."""

    authors: str
    year: str
    title: str
    identifier: str
    record_check: str


@dataclass(frozen=True)
class FetchResult:
    """What a record lookup returned."""

    ok: bool
    title: str
    url: str
    detail: str = ""


def canonical_id(identifier: str) -> str:
    """Return a comparable arXiv or DOI id.

    Args:
        identifier: Cell text such as ``arXiv:2609.01595`` or ``doi:10.2307/2297639``.

    Returns:
        The canonical id, or the stripped original when the cell is not an id.
    """
    text = identifier.strip()
    arxiv = ARXIV_ID.match(text)
    if arxiv:
        return f"arXiv:{arxiv.group(1)}"
    doi = DOI_ID.match(text)
    if doi:
        return f"doi:{doi.group(1).lower()}"
    return text


def titles_match(recorded: str, fetched: str) -> bool:
    """Return whether two titles are the same after light normalization.

    Args:
        recorded: Title cell from the note.
        fetched: Title returned by arXiv or Crossref.

    Returns:
        True when the normalized strings match or one contains the other.
    """
    left = _normalize_title(recorded)
    right = _normalize_title(fetched)
    if not left or not right:
        return False
    return left == right or left in right or right in left


def parse_verified_table(text: str) -> list[Citation]:
    """Parse the table under ``## Verified records``.

    Args:
        text: Full markdown of the literature note.

    Returns:
        One citation per data row.

    Raises:
        ValueError: The heading or the header row is missing, or a row is short.
    """
    heading = "## Verified records"
    start = text.find(heading)
    if start < 0:
        raise ValueError("missing heading '## Verified records'")
    rows: list[Citation] = []
    seen_header = False
    for line in text[start:].splitlines():
        if seen_header and line.startswith("## "):
            break
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not seen_header:
            if cells[:5] != ["Authors", "Year", "Title on the record", "Identifier", "Record check"]:
                continue
            seen_header = True
            continue
        if all(set(cell) <= set("-: ") for cell in cells):
            continue
        if len(cells) < 5:
            raise ValueError(f"short citation row: {line}")
        rows.append(Citation(cells[0], cells[1], cells[2], cells[3], cells[4]))
    if not seen_header:
        raise ValueError("verified-records table has no header")
    return rows


def evaluate(
    text: str | None,
    fetch,
    *,
    require: bool,
    min_rows: int = 8,
) -> list[str]:
    """Return human-readable failures. An empty list means the note passes.

    Args:
        text: Literature note, or None when the file is absent.
        fetch: Callable mapping a canonical id to a ``FetchResult``.
        require: When True, a missing note is a failure.
        min_rows: Minimum number of verified rows when ``require`` is True.

    Returns:
        Failure messages.
    """
    if text is None:
        if require:
            return ["notes/literature.md is absent"]
        return []
    failures: list[str] = []
    if UNCONFIRMED_SENTENCE not in text:
        failures.append("missing the sentence that Koh and Martinez-Bruera is not cited")
    try:
        rows = parse_verified_table(text)
    except ValueError as exc:
        return failures + [str(exc)]
    seen: set[str] = set()
    for row in rows:
        if "martinez-bruera" in row.authors.lower() or "martinez-bruera" in row.title.lower():
            failures.append(f"{row.identifier} cites Koh and Martinez-Bruera, which has no stable link")
            continue
        if not row.record_check:
            failures.append(f"{row.identifier} has an empty record-check cell")
        ident = canonical_id(row.identifier)
        if ident in seen:
            failures.append(f"duplicate identifier {ident}")
        seen.add(ident)
        if not (ident.startswith("arXiv:") or ident.startswith("doi:")):
            failures.append(f"unrecognized identifier {row.identifier!r}")
            continue
        try:
            result = fetch(ident)
        except (OSError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            LOGGER.exception("fetch failed for %s", ident)
            failures.append(f"{ident} could not be fetched: {exc}")
            continue
        if not result.ok:
            failures.append(f"{ident} did not resolve: {result.detail}")
            continue
        if not titles_match(row.title, result.title):
            failures.append(f"{ident} title {row.title!r} does not match record title {result.title!r}")
    if require and len(rows) < min_rows:
        failures.append(f"need at least {min_rows} verified rows, found {len(rows)}")
    if require:
        for ident in REQUIRED_IDS:
            if ident not in seen:
                failures.append(f"missing required identifier {ident}")
    return failures


def live_fetch(identifier: str, opener=urllib.request.urlopen, pause=time.sleep) -> FetchResult:
    """Fetch one arXiv or Crossref record.

    Args:
        identifier: Canonical id from ``canonical_id``.
        opener: URL opener, replaced in tests.
        pause: Sleep callable used between retries.

    Returns:
        The record title when the lookup succeeds.
    """
    if identifier.startswith("arXiv:"):
        arxiv_id = identifier.split(":", 1)[1]
        url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
        body = _read_bytes(url, opener, pause)
        if body is None:
            return FetchResult(False, "", url, "arXiv request failed")
        text = body.decode("utf-8", "replace")
        if arxiv_id not in text:
            return FetchResult(False, "", url, "arXiv id absent from the feed")
        title = _arxiv_title(text)
        if not title:
            return FetchResult(False, "", url, "arXiv feed has no title")
        return FetchResult(True, title, url)
    if identifier.startswith("doi:"):
        doi = identifier.split(":", 1)[1]
        url = f"https://api.crossref.org/works/{doi}"
        body = _read_bytes(url, opener, pause)
        if body is None:
            return FetchResult(False, "", url, "Crossref request failed")
        try:
            payload = json.loads(body.decode("utf-8", "replace"))
            titles = payload["message"]["title"]
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            LOGGER.error("crossref payload for %s: %s", doi, exc)
            return FetchResult(False, "", url, "Crossref payload has no title")
        title = " ".join(titles).strip()
        if not title:
            return FetchResult(False, "", url, "Crossref title is empty")
        return FetchResult(True, title, url)
    return FetchResult(False, "", "", f"unrecognized identifier {identifier}")


def main(argv: list[str] | None = None) -> int:
    """Check the literature note and print each failure.

    Args:
        argv: Optional argument list.

    Returns:
        Zero when the note passes or is absent without ``--require``.
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Re-fetch citation rows in notes/literature.md")
    parser.add_argument(
        "--require",
        action="store_true",
        help="Fail when the note is missing, short, or lacks the required ids",
    )
    parser.add_argument("--min-rows", type=int, default=8)
    args = parser.parse_args(argv)
    text = LITERATURE.read_text(encoding="utf-8") if LITERATURE.is_file() else None
    if text is None and not args.require:
        print("notes/literature.md is absent")
        return 0
    try:
        failures = evaluate(text, live_fetch, require=args.require, min_rows=args.min_rows)
    except (OSError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        LOGGER.error("%s", exc)
        return 1
    if failures:
        for failure in failures:
            print(failure)
        return 1
    print(f"verified {LITERATURE.relative_to(ROOT)}")
    return 0


def _normalize_title(text: str) -> str:
    """Lowercase a title and drop punctuation.

    Args:
        text: Raw title.

    Returns:
        Space-separated tokens.
    """
    cleaned = re.sub(r"<[^>]+>", " ", text.lower())
    cleaned = cleaned.replace("–", " ").replace("—", " ")
    cleaned = re.sub(r"[^a-z0-9]+", " ", cleaned)
    return " ".join(cleaned.split())


def _arxiv_title(feed: str) -> str:
    """Return the first entry title in an arXiv Atom feed.

    Args:
        feed: Atom XML text.

    Returns:
        The title, or an empty string.
    """
    match = re.search(r"<entry>.*?<title>(.*?)</title>", feed, re.S)
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()


def _read_bytes(url: str, opener, pause, attempts: int = 3) -> bytes | None:
    """GET a URL, retrying on rate limits.

    Args:
        url: Absolute URL.
        opener: URL opener.
        pause: Sleep callable.
        attempts: How many tries to make.

    Returns:
        Response bytes, or None when every try fails.
    """
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(attempts):
        try:
            with opener(request, timeout=30) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            LOGGER.error("HTTP %s for %s", exc.code, url)
            if exc.code == 429 and attempt + 1 < attempts:
                pause(1 + attempt)
                continue
            return None
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            LOGGER.error("request failed for %s: %s", url, exc)
            if attempt + 1 < attempts:
                pause(1)
                continue
            return None
    return None


if __name__ == "__main__":
    raise SystemExit(main())
