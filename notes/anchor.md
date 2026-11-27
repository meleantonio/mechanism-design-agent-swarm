# Anchor

The swarm starts from Antonio Mele's private research repository. This file is a pin and a status map. It is not a substitute for opening those files, and it is not the model note.

## Pin

| Field | Value |
| --- | --- |
| Repository | `meleantonio/smarter-agent-mechanism-design` |
| URL | https://github.com/meleantonio/smarter-agent-mechanism-design |
| Commit | `395802d996abe0ab54f7088aac0d0ca35e28f91b` |
| Date | 2026-10-29 |
| Subject | Merge pull request #36: robust permissions and trusted audit design |
| Visibility | Private |

Search of the `meleantonio` account for this theory problem found that repository. `meleantonio/mit-ai-ed-alignment` is a different project and is not a source. Do not push, commit, or open a pull request on the anchor. Do not edit `meleantonio/AC4E_EIEF_Luiss`.

Read the pinned commit. Cite a path together with `395802d996abe0ab54f7088aac0d0ca35e28f91b`. Do not paste prose from `paper/` or from `notes/04-theoretical-framework.md` through `notes/19-audit-investment.md`. File paths, issue numbers, package labels, and bibliographic ids are fine.

## Question the pin is already working on

The public starting paper is Bergemann, Koh and Morris (2026), *Mechanism Design for Alignment and Control*, [arXiv:2609.01595](https://arxiv.org/abs/2609.01595). That paper treats a more capable agent largely as a private type that can hide capability inside a one-sided verification order.

The anchor asks what changes when the agent is more capable than the principal in a stronger sense: the agent can out-plan, out-measure, or out-model the principal's tests and oversight, rather than only sandbag inside a type space the principal already wrote down. The manuscript title in `paper/README.md` is *Costly oversight of more capable agents*. Historical seed questions live in `notes/00-seed.md` and `notes/03-open-questions.md`. Hypotheses H1–H6 in the seed note are labeled speculative there. They are not theorems on this commit.

`notes/05-results-index.md` treats each later note as a result about one instrument. It does not present those notes as a general account of an intelligence gap, and it does not present them as a replacement for the public paper's revelation argument. Separate models use separate instruments. A numerical check or a Lean build does not identify real AI preferences and does not establish deployment safety.

## Where the work sits on this commit

`docs/research-roadmap.md` records R1–R8 (issues #13–#20) as complete at their stated scope. `docs/research-roadmap-next.md` records R9–R12 as proved and reviewed, landed by the merge above. A theorem count is not acceptance evidence. Inherited Bergemann–Koh–Morris boundaries stay visible in `docs/theorem-ledger.md`.

| Package | Issue | On this commit | What it is about |
| --- | --- | --- | --- |
| R1–R8 | #13–#20 | Complete at stated scope | Contribution ledger, semantic proofs, costly tests, measurement, constrained awareness, strategic monitor, dynamic commitment, research package |
| R9 | #29 | Landed | Coalition records and voluntary audit thresholds |
| R10 | #30 | Landed | Permission interval at every bias radius |
| R11 | #31 | Landed for one interior gap | A fully traversed interior permission gap; arbitrary permission sets stay open |
| R12 | #32 | Landed | Finite trusted-sensor investment and certificates |
| R13 | #33 | Open | Multiple and boundary permission gaps. Pull request #38 is in flight and is not a result |
| R14 | #34 | Open | A coalition that sees the selected sensor before it attacks. Pull request #37 is in flight and is not a result |
| R15 | #35 | Open | An executable rational certificate checker. Pull request #39 is in flight and is not a result |

## Files that carry the model, the results, and the open directions

Open these at the pin. Paraphrase.

| Path | Role |
| --- | --- |
| `README.md` | Project question and file map |
| `notes/00-seed.md` | Question and speculative H1–H6 |
| `notes/01-bkm-summary.md` | Reading note on the public paper |
| `notes/02-literature-map.md` | Seed bibliography with links |
| `notes/LIT-MAP.md` | Later literature map |
| `notes/03-open-questions.md` | Questions Q1–Q18 |
| `notes/04-theoretical-framework.md` | How the primitives change. Paraphrase only |
| `notes/05-results-index.md` | Index of notes 05–15 |
| `notes/05-results-nested-capability.md` through `notes/19-audit-investment.md` | Result notes. Cite the path; do not paste |
| `docs/research-roadmap.md` | R1–R8 completion record |
| `docs/research-roadmap-next.md` | R9–R15 status |
| `docs/theorem-ledger.md` | Statement-level evidence and remaining obligations |
| `docs/positioning-memo.md` | What the selected results add to published theory |
| `docs/source-evidence.md` | Literature boundaries used in the paper |
| `paper/README.md` | What the draft covers. Do not paste `paper/main.tex` |
| `verify/README.md` | Which checks exist, and what they do not certify |

The results index organizes four readings of a more capable agent, then the design notes:

1. Coarse tests and caps (`notes/05-results-nested-capability.md`): a coarser test adds incentive constraints.
2. Unlisted actions (`notes/06-results-unlisted-actions.md`): a measured reward controls cells, not every physical action inside a cell.
3. A richer model of the mechanism (`notes/07-results-mechanism-modeling.md`): this is not the same object as a coarser test.
4. Evaluation detection (`notes/08-results-evaluation-detection.md`, `notes/09-results-quadratic-detection.md`, `notes/14-constrained-detection.md`): private awareness of monitoring changes which rewards deter.

Design notes after those readings: costly tests (`notes/10-costly-tests.md`), measurement (`notes/11-measurement-design.md`), a strategic monitor (`notes/12-strategic-monitor.md`), dynamic commitment (`notes/13-dynamic-commitment.md`), coalition enlargement (`notes/15-coalition-enlargement.md`), robust intervals (`notes/16-robust-interval.md`), trusted audit (`notes/17-trusted-audit-design.md`), disconnected permissions (`notes/18-disconnected-permissions.md`), and audit investment (`notes/19-audit-investment.md`).

## Citation candidates

These ids are the ones printed in `notes/02-literature-map.md` at the pin. They were re-resolved while this pin was written (arXiv Atom and Crossref, 27 November 2026). The literature stage fetches them again and copies the title from the record. An id in this table is not yet a reading note.

| Identifier | Record title observed while pinning |
| --- | --- |
| `arXiv:2609.01595` | Mechanism Design for Alignment and Control |
| `doi:10.1287/moor.6.1.58` | Optimal Auction Design |
| `doi:10.2307/2297639` | Partially Verifiable Information and Mechanism Design |
| `doi:10.2307/1913096` | Full Extraction of the Surplus in Bayesian and Dominant Strategy Auctions |
| `doi:10.1111/j.1468-0262.2006.00666.x` | Commitment vs. Flexibility |
| `doi:10.1016/j.jet.2012.01.017` | Implementation with partial provability |
| `doi:10.3982/ecta14991` | Mechanisms With Evidence: Commitment and Robustness |
| `doi:10.1111/j.1468-0262.2005.00638.x` | Robust Mechanism Design |
| `doi:10.1257/aer.20131159` | Robustness and Linear Contracts |
| `doi:10.1007/BF01770224` | Formulation of Bayesian analysis for games with incomplete information |
| `arXiv:1606.03137` | Cooperative Inverse Reinforcement Learning |
| `arXiv:1805.00899` | AI safety via debate |
| `arXiv:1810.08575` | Supervising strong learners by amplifying weak experts |
| `arXiv:2312.09390` | Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision |
| `arXiv:1706.03741` | Deep reinforcement learning from human preferences |
| `arXiv:2406.07358` | AI Sandbagging: Language Models can Strategically Underperform on Evaluations |
| `arXiv:2412.14093` | Alignment faking in large language models |
| `arXiv:2503.11926` | Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation |
| `arXiv:2209.00626` | The Alignment Problem from a Deep Learning Perspective |
| `doi:10.1257/jel.20181489` | Information Design: A Unified Perspective |

Do not cite Koh and Martinez-Bruera. The anchor names that coupled-reward item and says to add it only after a stable public link exists. Holmström on delegation, Alonso and Matouschek (2008), and Rochet (1987) are named there without links. Cite one of them only after an arXiv id or a DOI resolves, and mark the row as added after verification.
