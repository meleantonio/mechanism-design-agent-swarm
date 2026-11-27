# Literature: papers read against the model note

This note lists related papers whose arXiv or Crossref record resolved when this card fetched it on 27 November 2026, and reads each one against the model note `notes/model.md` (the draft on branch `theory/model-setup`, PR #5, at commit `048bfb33ad2dde925029675ccf674337d3a68fc6`). Rows were chosen with the anchor bibliography at `395802d996abe0ab54f7088aac0d0ca35e28f91b`. Every title below was copied from the fetched record. A row is a pointer to a record, not a claim about what the swarm has proved.

Koh and Martinez-Bruera is not cited: the anchor records no stable public link.

## Verified records

| Authors | Year | Title on the record | Identifier | Record check |
| --- | --- | --- | --- | --- |
| Bergemann, Koh, Morris | 2026 | Mechanism Design for Alignment and Control | arXiv:2609.01595 | HTTP 200, https://export.arxiv.org/api/query?id_list=2609.01595 |
| Myerson | 1981 | Optimal Auction Design | doi:10.1287/moor.6.1.58 | HTTP 200, https://api.crossref.org/works/10.1287/moor.6.1.58 |
| Green, Laffont | 1986 | Partially Verifiable Information and Mechanism Design | doi:10.2307/2297639 | HTTP 200, https://api.crossref.org/works/10.2307/2297639 |
| Ben-Porath, Lipman | 2012 | Implementation with partial provability | doi:10.1016/j.jet.2012.01.017 | HTTP 200, https://api.crossref.org/works/10.1016/j.jet.2012.01.017 |
| Ben-Porath, Dekel, Lipman | 2019 | Mechanisms With Evidence: Commitment and Robustness | doi:10.3982/ecta14991 | HTTP 200, https://api.crossref.org/works/10.3982/ecta14991 |
| Bergemann, Morris | 2005 | Robust Mechanism Design | doi:10.1111/j.1468-0262.2005.00638.x | HTTP 200, https://api.crossref.org/works/10.1111/j.1468-0262.2005.00638.x |
| Carroll | 2015 | Robustness and Linear Contracts | doi:10.1257/aer.20131159 | HTTP 200, https://api.crossref.org/works/10.1257/aer.20131159 |
| Amador, Werning, Angeletos | 2006 | Commitment vs. Flexibility | doi:10.1111/j.1468-0262.2006.00666.x | HTTP 200, https://api.crossref.org/works/10.1111/j.1468-0262.2006.00666.x |
| Bergemann, Morris | 2019 | Information Design: A Unified Perspective | doi:10.1257/jel.20181489 | HTTP 200, https://api.crossref.org/works/10.1257/jel.20181489 |
| Irving, Christiano, Amodei | 2018 | AI safety via debate | arXiv:1805.00899 | HTTP 200, https://export.arxiv.org/api/query?id_list=1805.00899 |
| Burns, Izmailov, Kirchner, Baker, Gao, Aschenbrenner, et al. | 2023 | Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision | arXiv:2312.09390 | HTTP 200, https://export.arxiv.org/api/query?id_list=2312.09390 |
| van der Weij, Hofstätter, Jaffe, Brown, Ward | 2024 | AI Sandbagging: Language Models can Strategically Underperform on Evaluations | arXiv:2406.07358 | HTTP 200, https://export.arxiv.org/api/query?id_list=2406.07358 |
| Greenblatt, Denison, Wright, Roger, MacDiarmid, Marks, et al. | 2024 | Alignment faking in large language models | arXiv:2412.14093 | HTTP 200, https://export.arxiv.org/api/query?id_list=2412.14093 |
| Baker, Huizinga, Gao, Dou, Guan, Madry, et al. | 2025 | Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation | arXiv:2503.11926 | HTTP 200, https://export.arxiv.org/api/query?id_list=2503.11926 |
| Alonso, Matouschek | 2008 | Optimal Delegation | doi:10.1111/j.1467-937X.2007.00471.x | HTTP 200, https://api.crossref.org/works/10.1111/j.1467-937X.2007.00471.x; added after verification |
| Holmstrom | 1979 | Moral Hazard and Observability | doi:10.2307/3003320 | HTTP 200, https://api.crossref.org/works/10.2307/3003320; added after verification |
| Ball, Kattwinkel | 2025 | Probabilistic verification in mechanism design | doi:10.3982/TE6266 | HTTP 200, https://api.crossref.org/works/10.3982/TE6266; added after verification |

The last three rows are not in the seed list's linked tables. Alonso and Matouschek, and Holmström, are named there without a link; their identifiers were taken from `notes/LIT-MAP.md` and `docs/source-evidence.md` at the pin and then resolved here. Ball and Kattwinkel comes from `docs/source-evidence.md` at the pin. Rochet (1987) is not cited: this card did not resolve a record for it.

## Reading

**arXiv:2609.01595 (Bergemann, Koh and Morris).** This is the base the model note builds on. The note borrows its agent type (feasible actions, bias, belief, experiment), its one-sided verification order, and its report-then-act timing with double deviations. Where the model note departs is in keeping two orders apart, physical capability versus what the principal's tests can grade, and in treating that gap through four separate readings. Only the first reading, coarse tests and caps, stays close to the concealment story in this paper; the other three change objects the paper takes as given.

**doi:10.1287/moor.6.1.58 (Myerson).** The revelation and incentive-compatibility toolkit that the base paper extends. In the model note the direct-mechanism logic is used inside each instrument's model, but the note does not claim a revelation principle for an agent that out-models the designer (reading 3), and it lists a new revelation principle as outside what the pin settles.

**doi:10.2307/2297639 (Green and Laffont).** The source of the idea that a type's feasible reports depend on its true type, with a nesting condition for truthful implementation. The model note's claim sets, what a type can substantiate under the tests, are this object. The note's coarse-test reading asks what happens when the grading order is coarser than the physical one, which is a comparative static on that nested structure rather than a new structure.

**doi:10.1016/j.jet.2012.01.017 (Ben-Porath and Lipman).** Implementation when agents can prove some facts but not others. In the model note, passing a test is the proof channel. The paper's evidence is a primitive; in the model note the principal buys tests at a cost and so chooses how fine the provable partition is, which places this paper as a fixed-evidence benchmark for the costly-test instrument.

**doi:10.3982/ecta14991 (Ben-Porath, Dekel and Lipman).** Gives conditions under which, with hard evidence, commitment adds nothing for the principal. The model note's baseline assumes commitment, and its two-period departure treats the value of commitment as something to derive. This paper is the benchmark that departure has to be compared with: the model note's tests are bought and its audits may come after a report, so the paper's equivalence conditions must be checked rather than assumed.

**doi:10.1111/j.1468-0262.2005.00638.x (Bergemann and Morris, 2005).** Robust design when the designer does not know agents' beliefs or higher-order beliefs. The model note's agent knows more about the state than the designer and, in reading 3, may hold a better model of the designer than the designer holds of it. This paper relaxes the designer's knowledge of beliefs within a type space; the model note's reading 3 is a different and stronger asymmetry, and the note does not reduce it to belief robustness.

**doi:10.1257/aer.20131159 (Carroll).** A principal who knows only part of the agent's action set picks a contract that is robust to unknown actions, and a linear contract is optimal. This is the closest classical neighbour to the model note's reading 2, unlisted actions. The model note's measured reward pays on cells of a partition, and a new action inside a cell is invisible to it; that is a different observability assumption from Carroll's observed output, so the linear-contract result does not transfer without a separate argument.

**doi:10.1111/j.1468-0262.2006.00666.x (Amador, Werning and Angeletos).** Rules versus discretion when a privately informed decision maker has a bias, without transfers. The model note's enforced permissions (caps by tier, floor-and-cap intervals for two-sided bias) are this kind of delegation set. The model note adds the tests that sort the agent into tiers before permissions bind, and the measurement layer that follows, neither of which is in this paper.

**doi:10.1257/jel.20181489 (Bergemann and Morris, 2019).** Unifies persuasion and information design through obedience constraints for a designer who controls signals. The model note's detection models let the principal choose monitoring experiments, which is an information-design problem. The model note also restricts the contract to one common reward that cannot condition on the agent's private posterior about monitoring, so the unrestricted obedience program here is a comparator and not the feasible set.

**arXiv:1805.00899 (Irving, Christiano and Amodei).** A protocol in which two strong agents argue and a weak judge decides. The model note's strategic monitor and its oversight reading, where the gap may be between a strong AI and a weaker overseer AI, sit next to this. Debate is a protocol whose guarantees rest on the zero-sum game; the model note instead treats the monitor as a player whose honesty is its own incentive constraint.

**arXiv:2312.09390 (Burns et al.).** Empirical study of training a strong model with labels from a weaker one. It motivates the model note's premise that the overseer is weaker than the overseen. It makes no incentive assumption: the strong model is not modelled as choosing to sandbag, which is exactly what the model note's private-type agent can do.

**arXiv:2406.07358 (van der Weij et al.).** Shows language models can deliberately underperform on evaluations. This is the empirical behaviour behind the model note's coarse-test reading and its report stage, where the agent passes or fails graded tests. The paper is evidence that the deviation is feasible; it does not estimate preferences, and the model note likewise claims nothing about real AI preferences.

**arXiv:2412.14093 (Greenblatt et al.).** Documents a model behaving differently when it infers it is being trained than when it is not. This is the behaviour behind the model note's fourth reading, evaluation detection, where the agent's private belief about being monitored changes which rewards deter. The model note treats that belief as an unobserved posterior; this paper is an elicited example, not a measurement of how common it is.

**arXiv:2503.11926 (Baker et al.).** Reports that monitoring a model's reasoning can catch misbehaviour, and that optimizing against the monitor can push the model to hide intent. In the model note's terms, the reward moves which measured cell the agent lands in without fixing the physical action within it (reading 2), and pressure on the score separates record from welfare. The model note keeps score and welfare as different objects for this reason.

**doi:10.1111/j.1467-937X.2007.00471.x (Alonso and Matouschek), added after verification.** Characterizes optimal delegation sets for an informed, biased agent without contingent transfers, including when intervals are optimal. The model note's permission instrument restricts attention to caps and intervals in some models and to sets with gaps in others; this paper is the benchmark for when such restrictions lose nothing. The model note's open question on arbitrary, possibly disconnected permission sets is the place where this comparison is still unsettled.

**doi:10.2307/3003320 (Holmström), added after verification.** Shows when an extra signal about a hidden action has incentive value, through a sufficiency condition on the existing output. The model note's measurement-design instrument chooses how actions are aggregated into cells, which also governs how informative the measurement is. The model note's object is different: physical actions hidden inside a measured cell, chosen jointly with test spending, so the informativeness criterion here is a starting point rather than a result the note can reuse.

**doi:10.3982/TE6266 (Ball and Kattwinkel), added after verification.** The principal picks a test that may depend on the report, and the agent can fail on purpose. This is close to the model note's capability tests and to sandbagging as deliberate failure. The model note's addition is that tests are costly and are chosen together with permissions and measurement downstream; this paper is the comparator any claim about the costly-test instrument has to address.

## Sources opened

- `notes/model.md` (draft on `origin/theory/model-setup`, PR #5; read with `git show`, re-fetched before finishing)
- `notes/02-literature-map.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `notes/LIT-MAP.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `docs/source-evidence.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`

The local pin map `notes/anchor.md` was also read. No other anchor file was opened for this card.
