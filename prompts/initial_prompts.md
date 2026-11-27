# Initial prompts

These are the prompts that created this swarm example. They are copied as given.

## 1. Create the swarm

Create a new GitHub repository with a complete, working example of full agent-swarm orchestration using GitHub Issues, following the patterns described in the EIEF Workshop material (the sub-agent definition and orchestration approach from PR #57 and the workshop content). The example should be about the user's project on mechanism design for agents that are smarter than the principal. Set it up so it can be run via Claude Code — include a CLAUDE.md (or equivalent) with clear instructions so Claude Code can drive the whole swarm orchestration loop: creating issues, spawning sub-agents, tracking progress through issue state, and completing the workflow end to end. Come back with the repo URL, its structure, and how to launch it with Claude Code.

## 2. Ground it in the existing project

Update to the in-flight repo setup job: the source material for this project lives locally at dropbox/github/smarter agent mechanics design on the user's computer. Read from that path to ground the new repository's content — the mechanism design for agents smarter than the principal material, examples, and any orchestration patterns — rather than relying only on the workshop chat history. Keep everything else from the original request unchanged: new GitHub repo, full swarm orchestration via GitHub Issues per the EIEF workshop material, runnable via Claude Code with a CLAUDE.md.

Further update: there is also a GitHub repository with the same name as the local project (smarter agent mechanics design), so the material can be found on GitHub as well. Use whichever source is more convenient or cross-check both. Everything else from the original request stays the same.

## 3. Rework it around the theory project

Rework the mechanism-design agent swarm example in the private repo meleantonio/mechanism-design-agent-swarm (main 7623715) so its objective is his own theoretical work on mechanism design for agents smarter than the principal.

1. Find the existing GitHub repo(s) in the meleantonio account on that theory problem (the smarter-agent mechanism design project, which has made real progress). Read it and treat it as the anchor. The swarm starts from that repo's model, results and open directions, not a blank slate. Cite the source repo, files and commit in the swarm.
2. Make the orchestration mirror the standard workflow of a theorist on a new paper: (a) set up the model, (b) literature review and reading the related papers, (c) generate possible setups and extensions. Map the four sub-agents and the issue cards onto those stages, keeping an acceptance or review step that checks each stage's output against the anchor repo. Literature citations must be verifiable (no invented papers).
3. Update CLAUDE.md, AGENTS.md, the sub-agents and issue cards. Keep the swarm executable: tests pass, `python3 scripts/open_issue_cards.py` still works. Replace the synthetic toy where it no longer fits.
4. Keep the repo private. Do not change the anchor research repo. Push to main of mechanism-design-agent-swarm only (it is a new example repo Antonio asked for); if anything protects main, open a PR instead.

Report back: which anchor repo you used, what changed (files), the commit, test results, the exact Claude Code opening prompt, and any open questions.
