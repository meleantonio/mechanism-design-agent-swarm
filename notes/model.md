# Model: a principal overseeing a more capable agent

This note sets out the model the swarm works from. It is written from the anchor `meleantonio/smarter-agent-mechanism-design` at commit `395802d996abe0ab54f7088aac0d0ca35e28f91b` (pinned in `notes/anchor.md`). Every anchor path below refers to that commit. The wording here is a paraphrase. It adds no payoff, no theorem, and no paper. Formulas stay in the anchor and are not reproduced.

The anchor keeps one model per instrument. It does not combine them into one general model. The setup below lists the shared parts and says which parts belong to which instrument. It is not a single game that contains every restriction at once (`notes/05-results-index.md` and `docs/research-roadmap.md`, both at `395802d996abe0ab54f7088aac0d0ca35e28f91b`).

## Players

- **Principal (designer, deployer).** What the principal values is what the agent physically does, not the score an evaluation records, and it commits to an oversight mechanism before the agent acts. Q15 asks whether this principal has to be a person at all: a person might fix only the top-level goal, leaving the capability gap that matters to run from a stronger AI down to the AI that supervises it. Sources: `notes/04-theoretical-framework.md` (sections 2 and 4.7), `notes/03-open-questions.md` (Q15), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Agent (the AI).** Has a private type made up of feasible actions (execution capability), a preference or bias (alignment), a belief, and an information experiment (information capability). This follows the Bergemann, Koh and Morris type, arXiv:2609.01595. Sources: `notes/04-theoretical-framework.md` (section 2.1), `notes/00-seed.md`, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Strategic monitor or evaluator (in some models only).** A separate player who sees evidence and may or may not reveal it. Getting this player to report truthfully is its own requirement, imposed on top of getting the acting agent to follow its recommendation. Sources: `notes/05-results-index.md` (note 12 entry and the H3 row), `notes/12-strategic-monitor.md` as indexed there, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Coalition of agents (in the audit models only).** Several agents who can act together to make an evaluation record look obedient. Sources: `docs/research-roadmap-next.md` (R9, R12, R14), `notes/05-results-index.md` (note 15 entry), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## Timing

The baseline order is a static, committed, single-agent mechanism. Sources: `notes/04-theoretical-framework.md` (sections 2.3 and 4.4), `README.md`, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

1. The principal commits to the mechanism: which tests to run, which permissions or caps go with each test result, how actions are measured, how rewards depend on measured outcomes, and how much monitoring or audit to buy.
2. The agent learns its type, and in the detection models it forms a private belief about whether it is being evaluated.
3. The agent sends a report. In practice this means passing or failing evaluations the principal can grade. It can claim only what its capability lets it substantiate.
4. The mechanism assigns permissions and recommends a plan.
5. The agent observes a private signal about the state, then picks an action. It may disobey, and it may combine a misreport with later disobedience (a double deviation).
6. The principal sees a measured outcome, and possibly a monitor's report or an audit signal. Rewards and penalties are paid within their bounds.

Departures from the baseline, each in its own model:

- **Two periods with re-optimization.** The principal may later be tempted to revise permissions, so the value of commitment is something to work out, not something assumed. Sources: `notes/05-results-index.md` (note 13 entry), `docs/research-roadmap.md` (R7), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Monitor stage.** A strategic evaluator decides whether to disclose before enforcement. Source: `notes/05-results-index.md` (note 12 entry) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Attack after sensor choice.** The principal picks trusted sensors, then the coalition picks an attack. In the open R14 package the coalition sees which sensor was picked before it attacks. Source: `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## Information

- **The agent knows more about the state.** Once its private signal arrives, the AI is better informed about the state than the designer, so the designer lacks full knowledge in the Bergemann–Morris sense. Source: `notes/04-theoretical-framework.md` (section 2.4) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **The designer holds a prior** over states and agent types and grades reports through a verification order: one type can pass every test another type passes. Source: `notes/04-theoretical-framework.md` (section 2.2) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Two orders, kept apart.** One order is physical (true nested action sets and a more informative experiment). The other comes only from the checks the principal is able to design and score, anti-sandbagging meta-checks included. This test-based order may lump together types that the physical order separates. Sources: `notes/04-theoretical-framework.md` (section 3), `notes/03-open-questions.md` (Q2), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Claim sets.** Knowing which claims each type can back up under the tests (its claim set) is necessary but does not settle behaviour. The model must also specify how imitation runs between the classes of that partition, and even inside one class, types that share all available reports may separate because their preferences differ. Source: `notes/05-results-index.md` (common-structure section) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Measurement is a partition of actions into cells.** The principal rewards cells, not physical actions. Source: `notes/05-results-index.md` (note 06 entry) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Private awareness.** In the detection models the agent's posterior about monitoring is private. The contract can depend only on what the designer observes, so it cannot condition on that posterior. Source: `notes/05-results-index.md` (notes 08, 09 and 14 entries) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Records versus welfare.** A coalition that controls every observed label can produce an obedient-looking record while the physical outcome differs. Score and welfare are different objects. Source: `docs/research-roadmap-next.md` (findings section) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## Instruments

Each instrument comes with the model that uses it. The anchor does not claim the instruments are equivalent to one another.

- **Capability tests (threshold tests, costly to buy).** Their outcome determines claim sets and tiers. Sources: `notes/05-results-index.md` (notes 05 and 10), `docs/research-roadmap.md` (R3), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Enforced permissions.** Caps per tier, intervals with a floor and a cap for two-sided bias, and permission sets with gaps. Sources: `notes/05-results-index.md` (notes 05 and 16), `docs/research-roadmap-next.md` (R10, R11, R13), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Measured rewards.** Unrestricted and costless in the measurement-design model; bounded in the monitoring models. Sources: `notes/05-results-index.md` (notes 06, 09, 11), `docs/research-roadmap.md` (R4), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Measurement design.** Choosing how actions are aggregated into measured cells, jointly with test investment. Source: `notes/05-results-index.md` (note 11 entry) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Monitoring and detection experiments.** Bounded penalties, posterior experiments, and constrained posterior bands. Sources: `notes/05-results-index.md` (notes 08, 09, 14), `docs/research-roadmap.md` (R5), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Monitor incentives.** Bounded scores given to a strategic evaluator. Sources: `notes/05-results-index.md` (note 12), `docs/research-roadmap.md` (R6), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Commitment.** Treated as a choice whose value has to be derived, compared with re-optimization. Sources: `notes/04-theoretical-framework.md` (section 4.4), `notes/05-results-index.md` (note 13), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Trusted audits and sensors, with or without transfers.** Whether coalition members can make side payments decides what an audit has to beat. With them, a reluctant member can be compensated, so the binding test is the coalition's combined surplus; without them, an attack that needs unanimous consent fails as soon as one member declines. In both cases an audit moves payoffs only when detection leads to a sanction the principal can enforce. Sources: `docs/research-roadmap-next.md` (R9, R12 and the economic interpretation), `notes/05-results-index.md` (notes 15 to 17), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## What more capable means

The anchor separates four readings of an agent that is more capable than its principal. They are **not one constraint**. Each changes a different part of the model, and a result about one does not carry over to another. Sources: `notes/04-theoretical-framework.md` (section 3), `notes/03-open-questions.md` (Q1), `notes/05-results-index.md`, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

1. **Coarse tests and caps.** The principal's tests cannot tell apart types that physically differ. Larger claim sets force the designer to respect more incentive constraints, so, other ingredients held fixed, the principal's attainable value cannot rise. This is the reading closest to sandbagging in the public paper. Anchor note: `notes/05-results-nested-capability.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
2. **Unlisted actions.** The agent can take or combine actions the designer did not list. A measured reward then controls which cell the agent lands in, but not which physical action it takes inside that cell. Anchor note: `notes/06-results-unlisted-actions.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
3. **A richer model of the mechanism.** The agent understands the designer, the designer's prior, or how the designer picks the mechanism better than the designer understands the agent. This is a different object from a coarser test, and the anchor does not reduce it to one in general. Anchor note: `notes/07-results-mechanism-modeling.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
4. **Evaluation detection.** The agent's own signals separate a test episode from real use more sharply than the principal is able to disguise. Its private awareness of being monitored changes which rewards actually deter. Anchor notes: `notes/08-results-evaluation-detection.md`, `notes/09-results-quadratic-detection.md`, and `notes/14-constrained-detection.md`, all at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

The result notes named above are cited by path as listed in `notes/05-results-index.md` and `notes/anchor.md`. This card did not open them (see Sources opened).

## Settled on the pin

- **R1–R12 are complete at their stated scope on this commit.** R1–R8 (issues #13–#20) are recorded as complete in `docs/research-roadmap.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`. R9–R12 (issues #29–#32) are recorded as proved and independently reviewed in `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`. R11 is settled only for a single, fully traversed interior permission gap.
- "Complete at stated scope" covers the selected results inside their own models and instruments. It does not cover a general theory of an agent smarter than its principal, a new revelation principle, or every inherited statement from Bergemann, Koh and Morris. Those inherited boundaries stay visible in the anchor's theorem ledger. A theorem count, a numerical check, or a Lean build is not acceptance evidence on its own. None of these results identifies real AI preferences or establishes that a deployment is safe. Sources: `notes/05-results-index.md`, `docs/research-roadmap.md`, `docs/research-roadmap-next.md`, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **H1–H6 stay speculative.** The seed note labels them working hypotheses. According to the results index, the scoped results settle nothing, for or against, about the broad claim that an AI smarter than its overseer behaves in some general way. None of H1–H6 is a theorem on this commit. Sources: `notes/00-seed.md`, `notes/05-results-index.md` (hypothesis status table), `notes/04-theoretical-framework.md` (marked as historical working notes), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## Still open

These items are in flight. They are not results.

- **R13 (issue #33).** Permission design with multiple gaps and gaps at the boundary. Open. Source: `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **R14 (issue #34).** A coalition that sees the selected sensor before it attacks, compared with the case where the sensor is hidden. Open. Source: `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **R15 (issue #35).** A Lean program that checks certificates over the rationals, built so that a passing check entails the corresponding claim over the reals. Open. Source: `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Issues #33–#35** are the open tracking issues for R13–R15. None of R13, R14 or R15 is proved.
- **Pull requests #37, #38 and #39** are in flight and are not results: #37 for R14, #38 for R13, #39 for R15. The pinned roadmap file does not list these pull request numbers. Their status comes from the swarm's pin map, `notes/anchor.md`.
- **Arbitrary permission sets remain open after R11.** R11 settles one fully traversed interior gap. Whether that result extends to optimality over arbitrary, possibly disconnected, permission sets is still a research question. Sources: `docs/research-roadmap-next.md`, `notes/05-results-index.md` (Q10 row), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- Also open on the pin, for context only. The index lists the commitment-or-modelling question behind H2 as open in general. Nothing in the model lets the agent itself take an oversight step, for instance triggering retraining, a shutdown, or a change of permissions (H6). The index gives no general answer to Q6, Q8, Q9 or Q13–Q15, which concern control of many agents at once, collusive behaviour, rival experts, and which institution plays the principal. Source: `notes/05-results-index.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## Sources opened

Each anchor path below was read with `gh api` at the pinned commit for this card.

- `README.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `notes/00-seed.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `notes/03-open-questions.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `notes/04-theoretical-framework.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `notes/05-results-index.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `docs/research-roadmap.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`

This card did not open the result notes `notes/05-results-nested-capability.md` through `notes/19-audit-investment.md`, `docs/theorem-ledger.md`, or `paper/`. They are cited above only as `notes/05-results-index.md` and `notes/anchor.md` describe them. The local pin map `notes/anchor.md` in this repository was also read.
