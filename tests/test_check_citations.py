"""Citation checks use a stand-in fetcher. They do not call arXiv or Crossref."""

from __future__ import annotations

from check_citations import (
    REQUIRED_IDS,
    UNCONFIRMED_SENTENCE,
    FetchResult,
    canonical_id,
    evaluate,
    titles_match,
)

HEADER = (
    "| Authors | Year | Title on the record | Identifier | Record check |\n"
    "| --- | --- | --- | --- | --- |\n"
)


def _note(rows: list[tuple[str, str, str, str]], extra: str = "") -> str:
    body = ["# Literature", "", UNCONFIRMED_SENTENCE, "", "## Verified records", "", HEADER]
    for authors, year, title, ident in rows:
        body.append(f"| {authors} | {year} | {title} | {ident} | 200 https://example.test |")
    body.append("")
    body.append(extra)
    return "\n".join(body) + "\n"


def _core_rows() -> list[tuple[str, str, str, str]]:
    rows = [
        ("Bergemann, Koh and Morris", "2026", "Mechanism Design for Alignment and Control", "arXiv:2609.01595"),
        ("Green and Laffont", "1986", "Partially Verifiable Information and Mechanism Design", "doi:10.2307/2297639"),
        ("Bergemann and Morris", "2005", "Robust Mechanism Design", "doi:10.1111/j.1468-0262.2005.00638.x"),
        ("Carroll", "2015", "Robustness and Linear Contracts", "doi:10.1257/aer.20131159"),
        ("Myerson", "1981", "Optimal Auction Design", "doi:10.1287/moor.6.1.58"),
        ("Irving, Christiano and Amodei", "2018", "AI safety via debate", "arXiv:1805.00899"),
        (
            "Christiano, Shlegeris and Amodei",
            "2018",
            "Supervising strong learners by amplifying weak experts",
            "arXiv:1810.08575",
        ),
        ("Greenblatt and coauthors", "2024", "Alignment faking in large language models", "arXiv:2412.14093"),
    ]
    assert len(rows) >= 8
    return rows


def _fetch_ok(identifier: str) -> FetchResult:
    titles = {
        "arXiv:2609.01595": "Mechanism Design for Alignment and Control",
        "doi:10.2307/2297639": "Partially Verifiable Information and Mechanism Design",
        "doi:10.1111/j.1468-0262.2005.00638.x": "Robust Mechanism Design",
        "doi:10.1257/aer.20131159": "Robustness and Linear Contracts",
        "doi:10.1287/moor.6.1.58": "Optimal Auction Design",
        "arXiv:1805.00899": "AI safety via debate",
        "arXiv:1810.08575": "Supervising strong learners by amplifying weak experts",
        "arXiv:2412.14093": "Alignment faking in large language models",
    }
    title = titles.get(identifier, "")
    if not title:
        return FetchResult(False, "", "", "unknown in this test")
    return FetchResult(True, title, f"https://example.test/{identifier}")


def test_titles_match_ignores_case_and_punctuation() -> None:
    """A record title with a colon still matches the cell."""
    assert titles_match("Robust Mechanism Design", "robust mechanism design")
    assert titles_match("Commitment vs. Flexibility", "Commitment vs Flexibility")


def test_canonical_id_strips_an_arxiv_version() -> None:
    """The version suffix is not part of the required id."""
    assert canonical_id("arXiv:2609.01595v1") == "arXiv:2609.01595"
    assert canonical_id("DOI:10.1257/AER.20131159") == "doi:10.1257/aer.20131159"


def test_required_note_passes() -> None:
    """Eight resolving rows and the unconfirmed sentence pass."""
    failures = evaluate(_note(_core_rows()), _fetch_ok, require=True)
    assert failures == []
    for ident in REQUIRED_IDS:
        assert ident


def test_missing_note_is_reported_only_when_required() -> None:
    """An absent literature note fails the literature card and not the harness."""
    assert evaluate(None, _fetch_ok, require=False) == []
    assert evaluate(None, _fetch_ok, require=True) == ["notes/literature.md is absent"]


def test_title_mismatch_and_unconfirmed_author_fail() -> None:
    """A wrong title, a missing id, and the unconfirmed item are failures."""
    rows = _core_rows()
    rows[0] = (rows[0][0], rows[0][1], "A paper that does not exist", rows[0][3])
    mismatches = evaluate(_note(rows), _fetch_ok, require=True)
    assert any("does not match record title" in item for item in mismatches)

    invented = _note(rows[:7] + [("Someone", "2024", "Untitled", "forthcoming")])
    bad_id = evaluate(invented, _fetch_ok, require=True)
    assert any("unrecognized identifier" in item for item in bad_id)

    leaked = _note(
        _core_rows()
        + [("Koh and Martinez-Bruera", "2025", "Coupled rewards", "doi:10.0000/not-a-paper")]
    )
    leaked_failures = evaluate(leaked, _fetch_ok, require=True)
    assert any("Martinez-Bruera" in item for item in leaked_failures)


def test_missing_unconfirmed_sentence_fails() -> None:
    """The note must say the unlinked item is not cited."""
    text = _note(_core_rows()).replace(UNCONFIRMED_SENTENCE, "")
    failures = evaluate(text, _fetch_ok, require=True)
    assert any("Koh and Martinez-Bruera" in item for item in failures)
