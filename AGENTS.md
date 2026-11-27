# Agent instructions

Teaching exercise: a principal writes an oversight rule, and the agent knows an action the rule does not list. The numbers in `toy/actions.py` are synthetic. They are not a research result.

## Workflow

- One issue card, one branch, one pull request.
- At most two cards in progress, and those two must not share a file.
- Sub-agents do the writing. The orchestrator tracks labels and reviews.
- Run the check command before calling a card finished.

## Economics

- Document the actions, the record, the bonus, and the audit cost in the notes.
- Use relative paths.
- Do not edit `toy/actions.py`. It is the exercise data.
- Do not certify a theorem, an optimal mechanism, or a claim about real AI systems.

## Privacy

- Do not commit secrets, API keys, or a `.env` file.
- Do not read or copy `meleantonio/smarter-agent-mechanism-design`, and do not paste manuscript text into issues or notes.
- The public framing paper is Bergemann, Koh and Morris (2026), arXiv:2609.01595. This repository does not reproduce it.

## Verification

```bash
python3 -m pytest tests toy/tests -q
```
