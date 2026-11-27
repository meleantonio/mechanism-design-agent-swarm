# Agent instructions

Theory swarm for mechanism design when the agent is more capable than the principal. The anchor is `meleantonio/smarter-agent-mechanism-design` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`, mapped in `notes/anchor.md`.

A sub-agent does a piece of the work and hands back the result that job needs. A summary is one possible result, not the definition.

## Workflow

- One issue card, one branch, one pull request.
- Stages run in order: model, literature, extensions. At most one writing card is in progress.
- Sub-agents write the notes. The orchestrator tracks labels and runs the acceptance check.
- Run the check command before calling a card finished.
- After the literature note exists, `python3 scripts/check_citations.py --require` must pass before that card is finished.

## Economics

- Set up the model from the pinned files: players, timing, information, and instruments. Keep the four readings distinct.
- Keep H1–H6 speculative. Keep R1–R12 completed at their stated scope. Keep R13–R15, and arbitrary permission sets, open. In-flight pull requests #37, #38, and #39 are not results.
- Literature rows need an arXiv id or a DOI. Copy the title from the record you fetched. Do not cite Koh and Martinez-Bruera.
- An extension proposes a setup. It does not claim a new theorem.
- Use relative paths for files in this repository. Cite an anchor path with the commit.

## Privacy

- This repository stays private.
- Do not commit secrets, API keys, or a `.env` file.
- Do not push to the anchor repository, and do not paste its manuscript or research-note prose.
- Do not edit `meleantonio/AC4E_EIEF_Luiss`.

## Verification

```bash
python3 -m pytest tests -q
python3 scripts/check_citations.py --require
```

The second command waits until `notes/literature.md` exists. Until then it is expected to fail under `--require`, and to print that the note is absent without `--require`.
