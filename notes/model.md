# Model: a principal overseeing a more capable agent

This note sets out the model the swarm works from. It is written from the anchor `meleantonio/smarter-agent-mechanism-design` at commit `395802d996abe0ab54f7088aac0d0ca35e28f91b` (pinned in `notes/anchor.md`). Every anchor path below refers to that commit. The wording here is a paraphrase. It adds no payoff, no theorem, and no paper. Formulas stay in the anchor and are not reproduced.

The anchor keeps one model per instrument. It does not combine them into one general model. The setup below lists the shared parts and says which parts belong to which instrument. It is not a single game that contains every restriction at once (`notes/05-results-index.md` and `docs/research-roadmap.md`, both at `395802d996abe0ab54f7088aac0d0ca35e28f91b`).

## Players

- **Principal (designer, deployer).** What the principal values is what the agent physically does, not the score an evaluation records, and it commits to an oversight mechanism before the agent acts. Q15 asks whether this principal has to be a person at all: a person might fix only the top-level goal, leaving the capability gap that matters to run from a stronger AI down to the AI that supervises it. Sources: `notes/04-theoretical-framework.md` (sections 2 and 4.7), `notes/03-open-questions.md` (Q15), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Agent (the AI).** The swarm reads the agent's private type through three questions. What does it know? It holds a belief about the state and has access to a signal that can sharpen that belief. What does it want? It has its own preference, which need not match the principal's. What can it do? It has a set of actions that are physically open to it, and that set may be larger than the designer expects. This way of building a type comes from Bergemann, Koh and Morris, arXiv:2609.01595. Sources: `notes/04-theoretical-framework.md` (section 2.1), `notes/00-seed.md`, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
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
- **Two orders, kept apart.** The swarm keeps apart what one type could imitate in principle and what the principal's grading can catch. Ranking types by the actions they really have and by how good their information is gives one ordering. Ranking them by which of the principal's own checks they pass gives another. Because those checks are limited, the second ordering can treat as interchangeable two types that the first ranks apart. Sources: `notes/04-theoretical-framework.md` (section 3), `notes/03-open-questions.md` (Q2), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Claim sets.** Knowing which claims each type can back up under the tests (its claim set) is necessary but does not settle behaviour. The model must also specify how imitation runs between the classes of that partition, and even inside one class, types that share all available reports may separate because their preferences differ. Source: `notes/05-results-index.md` (common-structure section) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Measurement is a partition of actions into cells.** The principal rewards cells, not physical actions. Source: `notes/05-results-index.md` (note 06 entry) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Private awareness.** In the detection models the agent's posterior about monitoring is private. The contract can depend only on what the designer observes, so it cannot condition on that posterior. Source: `notes/05-results-index.md` (notes 08, 09 and 14 entries) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Records versus welfare.** The score is computed from labels, while welfare depends on what physically happens. If a coalition writes every label the principal gets to see, the two can split: the record shows compliance and the outcome need not. Source: `docs/research-roadmap-next.md` (Economic interpretation section) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## Instruments

Each instrument comes with the model that uses it. The anchor does not claim the instruments are equivalent to one another.

- **Capability tests (threshold tests, costly to buy).** Their outcome determines claim sets and tiers. Sources: `notes/05-results-index.md` (notes 05 and 10), `docs/research-roadmap.md` (R3), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Enforced permissions.** Caps per tier, intervals with a floor and a cap for two-sided bias, and permission sets with gaps. Sources: `notes/05-results-index.md` (notes 05 and 16), `docs/research-roadmap-next.md` (R10, R11, R13), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Measured rewards.** Unrestricted and costless in the measurement-design model; bounded in the monitoring models. Sources: `notes/05-results-index.md` (notes 06, 09, 11), `docs/research-roadmap.md` (R4), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Measurement design.** Choosing how actions are aggregated into measured cells, jointly with test investment. Source: `notes/05-results-index.md` (note 11 entry) at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Monitoring and detection experiments.** Bounded penalties, posterior experiments, and constrained posterior bands. Sources: `notes/05-results-index.md` (notes 08, 09, 14), `docs/research-roadmap.md` (R5), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Monitor incentives.** Bounded scores given to a strategic evaluator. Sources: `notes/05-results-index.md` (note 12), `docs/research-roadmap.md` (R6), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Commitment.** Treated as a choice whose value has to be derived, compared with re-optimization. Sources: `notes/04-theoretical-framework.md` (section 4.4), `notes/05-results-index.md` (note 13), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
- **Trusted audits and sensors, with or without transfers.** The swarm frames the audit question from the coalition's side: what does a group of agents have to overcome before it attacks? The first hurdle exists only if a detected attack can be followed by a sanction the principal is able to enforce; otherwise the audit changes nothing. Beyond that, the answer turns on side payments. When members can pay one another, the group goes ahead whenever its pooled gain is large enough. When they cannot, each member holds a veto over any attack that relies on voluntary participation. Sources: `docs/research-roadmap-next.md` (R9, R12 and the Economic interpretation section), `notes/05-results-index.md` (notes 15 to 17), at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

## What more capable means

The anchor separates four readings of an agent that is more capable than its principal. They are **not one constraint**. Each changes a different part of the model, and a result about one does not carry over to another. Sources: `notes/04-theoretical-framework.md` (section 3), `notes/03-open-questions.md` (Q1), `notes/05-results-index.md`, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

1. **Coarse tests and caps.** Here the gap is one of measurement. Types that really differ produce the same test results, so the mechanism has to offer them a pooled set of reports. Pooling of this kind can only add to the incentive constraints the mechanism must respect, so with the rest of the model held fixed it never helps the principal. Of the four readings, this is the one the public paper treats as sandbagging. Anchor note: `notes/05-results-nested-capability.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
2. **Unlisted actions.** The agent can take or combine actions the designer did not list. A measured reward then controls which cell the agent lands in, but not which physical action it takes inside that cell. Anchor note: `notes/06-results-unlisted-actions.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
3. **A richer model of the mechanism.** The agent understands the designer, the designer's prior, or how the designer picks the mechanism better than the designer understands the agent. This is a different object from a coarser test, and the anchor does not reduce it to one in general. Anchor note: `notes/07-results-mechanism-modeling.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.
4. **Evaluation detection.** Here the gap is one of self-location. The agent can work out whether it is in a test or in deployment, and the principal cannot make the two settings look alike enough to prevent this. The agent's belief about being watched is private, so which rewards deter it depends on something the principal cannot see. Anchor notes: `notes/08-results-evaluation-detection.md`, `notes/09-results-quadratic-detection.md`, and `notes/14-constrained-detection.md`, all at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

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
- Also open on the pin, for context only. Apart from R13–R15, three groups of questions stay unresolved in general. (a) H2: the index records the commitment-or-modelling question behind it as open. (b) H6: the model gives the agent no oversight moves of its own, such as triggering retraining, a shutdown, or a change of permissions. (c) Six questions from `notes/03-open-questions.md` that the index says have no general answer: whether honesty about capability or honesty about alignment gives way first as capability grows (Q6); whether the instruments keep their order of strength when the stronger agent can tamper with the party that watches it (Q8); whether, with free and unbounded rewards, a more sophisticated agent helps or hurts the case for full surplus extraction of the Crémer–McLean kind (Q9); whether making strong agents compete can make up for the principal's weaker capability (Q13); how varied the beliefs of frontier models really are when they grade one another (Q14); and whether the principal is a person or another AI (Q15). Sources: `notes/05-results-index.md`, `notes/03-open-questions.md`, at `395802d996abe0ab54f7088aac0d0ca35e28f91b`.

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
