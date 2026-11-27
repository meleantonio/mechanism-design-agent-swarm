# Mechanism-design agent swarm

A Claude Code swarm for Antonio Mele's theoretical work on mechanism design when the agent is more capable than the principal. The swarm sets up the model, reads the related papers, and proposes setups and extensions. Each stage is checked against the anchor repository.

The anchor is the private repository [`meleantonio/smarter-agent-mechanism-design`](https://github.com/meleantonio/smarter-agent-mechanism-design) at commit [`395802d996abe0ab54f7088aac0d0ca35e28f91b`](https://github.com/meleantonio/smarter-agent-mechanism-design/commit/395802d996abe0ab54f7088aac0d0ca35e28f91b) (29 October 2026, merge of pull request #36). `notes/anchor.md` records that pin, the results already on it, and the open directions. This repository stays private. It does not contain the manuscript.

The public starting paper is Bergemann, Koh and Morris (2026), *Mechanism Design for Alignment and Control*, [arXiv:2609.01595](https://arxiv.org/abs/2609.01595).

A sub-agent does a piece of the work and hands back the result that job needs. A summary is one possible result, not the definition. A skill is a repeatable set of instructions in the same conversation.

## Stages

| Stage | Sub-agent | Hands back |
| --- | --- | --- |
| (a) Set up the model | `model-setter` | `notes/model.md` |
| (b) Literature review | `literature-reader` | `notes/literature.md` |
| (c) Setups and extensions | `extension-writer` | `notes/extensions.md` |
| Review against the anchor | `acceptance-reviewer` | A yes/no review |

## Layout

```text
CLAUDE.md                  orchestrator loop for Claude Code
AGENTS.md                  economics, privacy, check command
README.md                  this file
notes/anchor.md            pin, results, and open directions
issues/                    cards: one goal and yes/no checks
.claude/agents/            sub-agents that write or review
.claude/skills/            repeatable steps for this conversation
notes/orchestration_log.md label log
scripts/open_issue_cards.py
scripts/check_citations.py
tests/                     card, pin, and citation checks
.github/workflows/checks.yml
```

The swarm adds `notes/model.md`, `notes/literature.md`, and `notes/extensions.md`.

## Setup

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest tests -q
python3 scripts/check_citations.py
```

`gh` must be logged in to this repository, with permission to create issues, labels, and pull requests, and able to read the private anchor. The citation check prints that the literature note is absent until that stage has been merged.

## Launch with Claude Code

From this directory:

```bash
claude
```

Paste this as the first prompt:

```text
Read CLAUDE.md and AGENTS.md. You are the orchestrator. Do not write the economics notes yourself.

Follow the loop in CLAUDE.md. Open the issue cards with python3 scripts/open_issue_cards.py. Hand each writing card to its named sub-agent, in order: model setup, then the literature review, then setups and extensions. After each writing pull request, run the acceptance-check skill and hand the same checkout to acceptance-reviewer. Track ready, in-progress, needs-review, and done. Keep at most one writing card in progress. Start the next writing card only after the previous card is done and its note is on main.

I authorize you to merge a pull request with gh pr merge NUMBER --merge only when the acceptance-check skill and the acceptance-reviewer both mark every criterion yes and python3 -m pytest tests -q passes. When the card is the literature review or the final review, python3 scripts/check_citations.py --require must pass as well. Then move that card to done.

Read meleantonio/smarter-agent-mechanism-design at commit 395802d996abe0ab54f7088aac0d0ca35e28f91b. Do not push to that repository, and do not paste its manuscript or research-note prose into this one. Cite paths and that commit. A literature row needs an arXiv id or a DOI whose record resolves. Do not invent papers.
```
