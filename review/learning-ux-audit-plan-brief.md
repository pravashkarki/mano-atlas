# Pair-review brief: learning-UX audit plan

Read `~/Work/PCS/CLAUDE.md`, `~/Work/PCS/docs/VOICE-TONE.md`, and `~/Work/PCS/docs/plans/learning-ux-audit.md` first. This brief is what the plan answers to; VOICE-TONE and the repo notes set the rules the audit must respect.

## What you are reviewing

A plan to audit all 29 teaching pages of Mano Atlas (an English/Nepali mental-health education site, static zero-framework build, bilingual in source, English-only in the current shipped phase) against a six-dimension learning-UX rubric. The audit produces a findings ledger, not code. Each accepted finding becomes its own board card later, so the audit must produce concrete, routable, per-page changes and must not double-report questions.

Check the plan against:

1. **Fit with the goal.** The project goal is "learning made easy and user-friendly" and the card it serves says: audit content formatting, scannability, worked examples, reader-question structure, and how far each page teaches instead of just informs; research interactivity options that respect the calm-reader brief (no animations, auto-play, countdowns, scores; quizzes reassure); produce a ledger mapping each page to its verdict and concrete change; keep existing conventions (care elements dismissible, examples real, no invented Nepali figures, external links only when verified).

2. **Coverage.** Does the six-dimension rubric cover what the card asks? Is anything in the card left out? Is any dimension redundant with the house gates (em-dash scan, bilingual class pattern, quiz/keypoints presence)?

3. **Method quality.** Is the method (fresh-reader sessions per page, built page + source, shared patterns cross-checked once, merged ledgers) sound for an audit of this size? Is the per-page verdict scale (Ship-now / Fix-in-passes / Note) clear enough to route to cards? Will the ledger avoid per-page noise for site-wide issues?

4. **Respect for the rules.** The audit must not invent Nepali prevalence or unverified links, must not recommend breaking the calm-reader brief, must not suggest interactivity the static build cannot do, and must not drift into language-fidelity or content-correction territory owned by other tracks (native Nepali proofread, known content fixes already logged in TASKS.md).

5. **Concreteness.** Audits that end in "this page is dense" are noise. Is the plan shaped so each finding lands as an actionable change someone can pick up and build?

Do NOT spawn sub-agents, run builds, or edit files. Read and return a verdict in one message.

## Return format

- VERDICT: AGREE / AGREE-WITH-CHANGE / DISAGREE.
- MUST-FIX: numbered, only things that would make the audit wrong or worse (not style).
- SHOULD-FIX: numbered, things that would make the audit better.
- NITS: numbered, trivial.

Sign with your model name. Date: today.