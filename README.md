# Mechanism-design agent swarm

A Claude Code swarm for one teaching question: a principal writes an oversight rule, and the agent knows an action the rule does not list. The swarm picks up GitHub issues, writes a setting note, a two-rule sketch, and a best-reply check, and tracks each card from `ready` to `done`.

The numbers are synthetic. They are not a theorem and not a result copied from a research draft. The question is the one tracked in the private repository `meleantonio/smarter-agent-mechanism-design`. This repository stays private and does not contain that draft. The public framing paper is Bergemann, Koh and Morris (2026), *Mechanism Design for Alignment and Control*, arXiv:2609.01595. This exercise does not reproduce it.

## Layout

```text
CLAUDE.md                  orchestrator loop for Claude Code
AGENTS.md                  economics, privacy, check command
README.md                  this file
issues/                    cards: one goal and yes/no checks
.claude/agents/            sub-agents that write or review
.claude/skills/            repeatable steps for this conversation
notes/orchestration_log.md label log
scripts/open_issue_cards.py
toy/actions.py             exercise data (do not edit)
toy/show_actions.py
toy/README.md
tests/                     card and harness checks
.github/workflows/checks.yml
```

The swarm adds `notes/setting.md`, `notes/mechanism_sketch.md`, `toy/rules.py`, `toy/best_reply.py`, and `toy/tests/test_best_reply.py`.

A sub-agent is another agent you hand a piece of the work. It has its own conversation and its own instructions. Inside the bounds on the card, it can read, write, check, and decide, and it hands back the file or the review that job needs. A skill is a repeatable set of instructions in the same conversation.

## Setup

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest tests toy/tests -q
```

`gh` must be logged in to this repository, with permission to create issues, labels, and pull requests.

## Launch with Claude Code

From this directory:

```bash
claude
```

Paste this as the first prompt:

```text
Read CLAUDE.md and AGENTS.md. You are the orchestrator. Do not write the economics files yourself.

Follow the loop in CLAUDE.md. Open the issue cards with python3 scripts/open_issue_cards.py. Hand each writing card to its named sub-agent. Track ready, in-progress, needs-review, and done. At most two writing cards at once, and those two must not share a file. Start the best-reply card only after toy/rules.py is on main.

I authorize you to merge a pull request with gh pr merge NUMBER --merge only when the acceptance-check skill and the acceptance-reviewer both mark every criterion yes and python3 -m pytest tests toy/tests -q passes. Then move that card to done.

The numbers are synthetic teaching data. Do not call them a theorem. Do not open or copy meleantonio/smarter-agent-mechanism-design.
```
