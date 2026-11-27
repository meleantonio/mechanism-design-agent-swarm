# Extensions: three setups inside the anchor's open directions

This note proposes three setups for later work. It reads `notes/model.md` and `notes/literature.md` as they stand on `main` in this repository (model note merged through PR #5, literature note through PR #6). The anchor is `meleantonio/smarter-agent-mechanism-design` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`, pinned in `notes/anchor.md`. Package status comes from `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`, paraphrased.

Each setup changes one part of one instrument's model and keeps the rest of that model as the anchor states it. R1–R12 are treated as complete at their stated scope. None of the setups below is a result. No payoff function, theorem, or paper is introduced here; every literature identifier is copied from the Verified records table in `notes/literature.md`.

## Setup 1

**Open direction:** R14 (anchor issue #34): a coalition that learns which trusted sensor was selected before it chooses an attack. This setup asks for the ground between the two timings the roadmap names. The coalition does not see the sensor identity outright. It receives a signal about the identity, and the precision of that signal is a primitive. The hidden-sensor benchmark of R12 is the case of an uninformative signal, and the fully observed sensor of R14 is the case of a perfectly informative one.

**Primitives changed:** The coalition's information at the attack stage. In the R12 timing it knows only the principal's sensor lottery; here it also observes the realization of a fixed experiment on the selected sensor before members decide whether to consent to an attack. Two versions are kept apart. In the first, the experiment is exogenous (leakage the principal cannot control). In the second, the principal chooses the experiment together with the sensor lottery, which turns part of the audit problem into an information-design problem about the sensor identity. The sensor menu, sensor costs, the attack set, the enforceable sanction after detection, and the split between coalitions with and without transfers stay as in R9 and R12.

**Completed package left in place:** R12 (issue #32), finite trusted-sensor investment and its certificates, is the hidden-information endpoint and is not redone. R9 (issue #29), the coalition record semantics and the voluntary-audit thresholds with and without transfers, is used as given.

**Anchor issue or pull request:** Issue #34. The fully observed endpoint of this setup matches the R14 work in pull request #37, which is in flight on the anchor and is not a result. This swarm is not merging pull request #37, does not review it, and does not rely on anything it states.

**Literature identifiers:** doi:10.1257/jel.20181489; doi:10.3982/ecta14991; doi:10.3982/TE6266; arXiv:2412.14093.

**Result this setup would need later:** A statement of the minimum audit cost that deters every attack, written as a function of the coalition's signal, for both the transfer and the no-transfer regime. The first open question is whether that cost moves monotonically when the coalition's signal becomes more informative in the Blackwell sense, or whether a counterexample exists. The second is whether, in the version where the principal picks the experiment, revealing nothing is always optimal, or whether some partial disclosure can lower cost. Either answer would need the feasible one-shot deviations to be written down explicitly, in the way R9 does for records, and would need to recover R12 and the R14 endpoint as limit cases.

**Not claimed:** This card does not prove the setup. It does not claim that the cost is monotone, that concealment is optimal, or anything about what pull request #37 shows. It does not estimate how much a real AI system can infer about oversight.

## Setup 2

**Open direction:** Arbitrary permission sets after R11. R11 settles one fully traversed interior gap; optimality over general, possibly disconnected, permission sets is still open on the pin. This setup also touches R13 (anchor issue #33), multiple and boundary gaps, because finite unions of intervals are a subclass of the sets considered here.

**Primitives changed:** Two primitives of the permission model. First, the class of feasible permission sets is enlarged from intervals and single-gap sets to every closed subset of the action line. Second, the bias uncertainty is allowed to be lopsided: the designer knows the bias lies in an interval that need not be centred at zero, so a floor and a cap no longer face mirror-image risks. The agent's choice rule inside a set with infinitely many components needs a stated tie-breaking convention, which becomes part of the model. The state distribution, the quadratic physical loss, and the absence of transfers are kept as the anchor's R10 and R11 models fix them, and a change to the distribution is listed as a separate variant rather than folded in.

**Completed package left in place:** R10 (issue #30), interval permissions at every bias radius, and R11 (issue #31), the single interior gap, are both used as stated and are not redone. The symmetric-bias interval solution of R10 is the benchmark this setup must recover when the bias interval is centred.

**Anchor issue or pull request:** Issue #33 for the finite-union part. The finite-union, symmetric-bias part of this setup overlaps the R13 work in pull request #38, which is in flight on the anchor and is not a result. This swarm is not merging pull request #38 and does not take any of its statements as settled. The parts that go beyond it here are closed sets that are not finite unions, and an off-centre bias interval.

**Literature identifiers:** doi:10.1111/j.1467-937X.2007.00471.x; doi:10.1111/j.1468-0262.2006.00666.x; doi:10.1111/j.1468-0262.2005.00638.x.

**Result this setup would need later:** Either an approximation argument showing that the designer's worst-case loss over all closed sets is approached by finite unions of intervals, so that nothing is lost by stopping at finite unions, or an explicit closed set that does strictly better. Separately, a statement of how the optimal floor and cap shift when the bias interval is moved off centre, and whether a gap ever becomes worthwhile purely because of that asymmetry. The comparison with Alonso and Matouschek on when interval delegation loses nothing would have to be stated, not assumed.

**Not claimed:** This card does not prove the setup. It does not claim that intervals stay optimal, that gaps help, or that the approximation argument goes through. It does not identify the bias of any real AI system.

## Setup 3

**Open direction:** Q8 in `notes/03-open-questions.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`. `notes/model.md` lists Q8 among the questions with no general answer on the pin and glosses it as whether the instruments keep their order of strength when the stronger agent can tamper with the party that watches it. Q8 has two parts: that ranking question, and what the mechanism-design counterpart is of a weak monitor whose channel the strong agent corrupts or obscures. This setup builds a model of the second part and uses it to pose the first part as the result it would need later (see below); it does not answer either part.

**Primitives changed:** The monitor's evidence. In the strategic-monitor model of R6 the evidence the monitor sees is generated by the agent's action alone. Here the agent chooses two things: a physical action and a costly concealment effort that garbles the evidence the monitor receives, without changing the measured cell. The monitor stays a strategic player whose honest reporting is its own incentive constraint, scores stay bounded, and the principal still pays only on what it observes. The cost of concealment, and whether the principal can see that concealment took place, are new primitives that must be stated; the setup does not supply a functional form for either.

**Completed package left in place:** R6 (strategic monitor, one of the R1–R8 packages that `notes/anchor.md` and `notes/model.md` record as complete) is the zero-concealment case and is not redone. R5 (constrained awareness and detection) is used as background and is not reopened.

**Anchor issue or pull request:** No anchor issue or pull request on the pin tracks this setup. It does not match pull request #37, #38, or #39.

**Literature identifiers:** arXiv:2609.01595; arXiv:2503.11926; arXiv:1805.00899; arXiv:2312.09390; doi:10.1257/jel.20181489; doi:10.2307/3003320.

**Result this setup would need later:** Three pieces. First, a characterization of which bounded monitor scores and agent rewards stay incentive compatible once concealment is available, with a comparison to the R6 benchmark that says when concealment strictly shrinks the set of implementable outcomes. Second, the ranking part of Q8: holding concealment fixed, a comparison of what the principal attains with permissions, with delegation sets, and with reward schedules, stating whether the order these instruments have in the Bergemann, Koh and Morris benchmark (arXiv:2609.01595) without tampering survives, and if not, which pair switches. Third, a condition under which buying a second, independent monitor restores what concealment removes. Holmström (1979) is the starting point for this third piece: in a moral-hazard model, an extra signal about a hidden action is worth paying on exactly when the existing output is not a sufficient statistic for the action given both signals. Here the analogue would ask when the second monitor's evidence stays informative about the physical action after the agent has chosen its concealment. Holmström's signals are not strategic and cannot be garbled by the agent, so that condition does not carry over without a separate argument. All three pieces need the timing of concealment relative to the monitor's disclosure choice fixed in advance.

**Not claimed:** This card does not prove the setup. It does not claim that concealment hurts the principal, that the instrument ranking changes or survives, that a second monitor helps, or that the empirical findings in arXiv:2503.11926 measure the concealment cost of any deployed system.

## Sources opened

- `notes/model.md` on `main` in this repository
- `notes/literature.md` on `main` in this repository
- `notes/anchor.md` in this repository
- `docs/research-roadmap-next.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`
- `notes/03-open-questions.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b`, to read both parts of Q8
- Anchor pull requests #37, #38, and #39, viewed read-only with `gh pr view` to decide which setups overlap them

`README.md`, `notes/00-seed.md`, `notes/04-theoretical-framework.md`, `notes/05-results-index.md`, and `docs/research-roadmap.md` at `395802d996abe0ab54f7088aac0d0ca35e28f91b` were fetched only for a mechanical check that this note shares no run of eight or more words with them; they were not used as sources. No other anchor file was opened for this card.
