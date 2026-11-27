# Orchestration log

Stages run in order: model setup, literature review, setups and extensions. Append one row when a card changes label. Do not delete earlier rows.

| When | Issue | From | To | Evidence |
| --- | --- | --- | --- | --- |
| 2026-11-27 | #1–#4 | — | ready | `python3 scripts/open_issue_cards.py` created #1 acceptance review, #2 extensions, #3 literature, #4 model setup; pytest 19 passed |
| 2026-11-27 | #4 | ready | in-progress | Handed `issues/model-setup.md` to `model-setter` on branch `theory/model-setup` |
| 2026-11-27 | #4 | in-progress | needs-review | https://github.com/meleantonio/mechanism-design-agent-swarm/pull/5 |
| 2026-11-27 | #4 | needs-review | ready | PR #5 failed criterion 4 (anchor prose near-copied at model.md l.11, 33, 35, 36, 52, 58, 61, 69, 81); comment on #4 |
| 2026-11-27 | #4 | ready | in-progress | Card returned to `model-setter` to reword on `theory/model-setup` / PR #5 |
| 2026-11-27 | — | — | — | User overruled the CLAUDE.md one-writing-card rule in chat: writing cards may run in parallel. Merges stay gated by the acceptance check, the reviewer, and the check commands |
| 2026-11-27 | #3 | ready | in-progress | Handed `issues/literature-review.md` to `literature-reader` in its own worktree on `theory/literature-review`; it reads the draft `notes/model.md` from PR #5 (not yet on `main`) |
| 2026-11-27 | #4 | in-progress | needs-review | PR #5 reworded at 048bfb3 |
| 2026-11-27 | #4 | needs-review | ready | Re-review of PR #5 at 048bfb3 failed criterion 4 (l.81 H6 clause near-verbatim); comment on #4 |
| 2026-11-27 | #4 | ready | in-progress | Returned to `model-setter` for l.81 (and l.9, 36, 52) |
| 2026-11-27 | #3 | in-progress | needs-review | https://github.com/meleantonio/mechanism-design-agent-swarm/pull/6 |
| 2026-11-27 | #4 | in-progress | needs-review | PR #5 reworked at 4247987 |
| 2026-11-27 | #2 | ready | in-progress | Handed `issues/extensions.md` to `extension-writer` in its own worktree; reads draft notes from PR #5 and PR #6 (user override on parallel writing) |
| 2026-11-27 | #3 | needs-review | ready | PR #6 failed criterion 3 (model note not on main; Holmström provenance l.29); comment on #3 |
| 2026-11-27 | #4 | needs-review | ready | Third review of PR #5 at 4247987 failed criterion 4 (l.10, 35, 81 term-by-term; l.81 Q mapping wrong); comment on #4 |
| 2026-11-27 | #4 | ready | in-progress | Returned to `model-setter` for structural rewrite |
| 2026-11-27 | #2 | in-progress | needs-review | https://github.com/meleantonio/mechanism-design-agent-swarm/pull/7 (drafted against unmerged PR #5/#6) |
| 2026-11-27 | #4 | in-progress | needs-review | PR #5 structural rewrite at bca1a27 |
| 2026-11-27 | #2 | needs-review | ready | PR #7 failed criteria 2, 4 (prerequisite notes not on main); Setup 3 Q8 framing; comment on #2 |
| 2026-11-27 | #4 | needs-review | done | Fourth review all yes; acceptance-check all yes; pytest 19 passed; merged https://github.com/meleantonio/mechanism-design-agent-swarm/pull/5 as e0b9fab |
| 2026-11-27 | #3 | ready | in-progress | Returned to `literature-reader`: rebase on main with merged `notes/model.md`, fix Holmström provenance |
| 2026-11-27 | #3 | in-progress | needs-review | PR #6 revised at 7a2d31f |
| 2026-11-27 | #3 | needs-review | done | Second review all yes; acceptance-check all yes; check_citations verified; pytest 19 passed; merged https://github.com/meleantonio/mechanism-design-agent-swarm/pull/6 as 821a202 |
| 2026-11-27 | #2 | ready | in-progress | Returned to `extension-writer`: merge main (model + literature now on main), re-check ids, fix Setup 3 Q8 framing |
| 2026-11-27 | #2 | in-progress | needs-review | PR #7 revised at d1b791f |
| 2026-11-27 | #2 | needs-review | done | Second review all yes; acceptance-check all yes; check_citations verified; pytest 19 passed; merged https://github.com/meleantonio/mechanism-design-agent-swarm/pull/7 as 705fd17 |
| 2026-11-27 | #1 | ready | in-progress | Final review handed to `acceptance-reviewer` on main at 705fd17 |
| 2026-11-27 | #1 | in-progress | done | Final review all yes on main 705fd17; pytest and check_citations --require outputs posted on #1 |
