# Review the related literature

**Label:** `ready` · **Role:** writer · **Separate copy (branch):** `theory/literature-review` · **Sub-agent:** `literature-reader` · **Reviewer:** `acceptance-reviewer`

Start this card only after the model-setup card is done and `notes/model.md` is on `main`.

## Goal

`notes/literature.md` records related papers whose arXiv or DOI records resolve, read against `notes/model.md`.

## Allowed files

- `notes/literature.md` (create)

## Acceptance criteria (done when)

- [ ] The note contains the sentence `Koh and Martinez-Bruera is not cited: the anchor records no stable public link.` and a Verified records table of at least eight rows.
- [ ] The table includes `arXiv:2609.01595`, `doi:10.2307/2297639`, `doi:10.1111/j.1468-0262.2005.00638.x`, and `doi:10.1257/aer.20131159`, and every title matches the fetched record.
- [ ] Reading has a paragraph for each row that names its identifier and relates the paper to `notes/model.md`, and Sources opened lists `notes/02-literature-map.md`, `notes/LIT-MAP.md`, and `docs/source-evidence.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- [ ] `python3 scripts/check_citations.py --require` passes, `git diff --stat` shows only `notes/literature.md`, and the check command passes.

## Check command

```bash
python3 -m pytest tests -q
```

## Not in this card

- Editing `notes/model.md`.
- A citation without an arXiv id or a DOI.
- A citation of Koh and Martinez-Bruera, or a paper whose record does not resolve.
