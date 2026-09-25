# Learning-UX audit plan: pair-review ledger (2026-09-25)

Plan: `docs/plans/learning-ux-audit.md` (Rev B). Brief: `review/learning-ux-audit-plan-brief.md`. Reviewers: gamma and delta, two fresh readers, both AGREE-WITH-CHANGE.

All must-fixes from both are in Rev B:

1. Dimension 6 rewrote as Formatting and flow (heading hierarchy, block placement, opening-to-task path) instead of House rules; baseline gates (em-dash, bilingual pattern, quiz/keypoints, slug refs) run once as a release gate.
2. Freeze a 29-slug manifest with exclusions and reasons; language mode and prior-work links recorded per page.
3. Language rule made explicit and phase-aware: source stays bilingual (gate-held), the audit judges the rendered English surface; Nepali fidelity hands to the native-proofread track, no Nepali cards from this audit.
4. Pre-audit reconciliation against TASKS.md, readability plan, board, intake/triage; every finding gets a disposition (New / Duplicate / Already fixed / Out of scope / Needs evidence) with links.
5. Finding model is routable: finding ID, page slug, section evidence, reader task blocked, proposed change, acceptance test, severity, confidence, dependencies, disposition; shared findings list affected pages once.
6. Verdict model defined with a derivation rule (Ship-now / Fix-in-passes / Note); Note cannot hide unresolved questions.
7. Reader pass first (built page, phone viewport, recorded theme/language), source and gate pass second; disagreement handling defined.
8. Grep replaced by manual built-page review plus targeted code checks; shared patterns in a root-cause block.
9. Fixed stratified pilot (basics, approaches, anxiety, suicide, a phase-1 page, child) before the full run (gamma asked a Founder question for the first five; delta's fixed pilot won, so the plan no longer needs the Founder to pick pages).

Should-fixes actioned in Rev B: worked-example definition (fictional/composite framing, reasoning shown, recorded reason when absent); teaching-depth test beyond skill box (explain / distinguish / perform / when to seek help, crisis pages not forced into self-help); actual reader question recorded per page with no formulaic audience label; current-interaction audit separated from future-option research (each option carries evidence, accessibility, static/bilingual feasibility, cost, keep/skip); audited commit recorded and re-checked if dev moves; factual corrections and native language hand to existing tracks, not new cards.

## Reproduced verdicts

### Gamma (verdict in full)

MUST-FIX
1. The rubric misses the card's content-formatting ask. The sixth dimension is House rules compliance, while Scannability mostly measures prose rhythm. Replace the sixth dimension with Content formatting, covering heading hierarchy, section boundaries, lists and tables, emphasis, diagrams and captions, and phone presentation. Run em-dash, bilingual, quiz/keypoint, and cross-reference checks as a separate release gate.
2. Freeze an exact 29-page manifest with canonical slugs, page type, current language mode, and prior-work links. The current category list does not prove that every page is included exactly once or that reference pages are excluded consistently.
3. Make the bilingual criterion phase-aware. A blanket "every string bilingual" check will flag expected English-only Phase 1 pages and pull the audit into native proofreading.
4. Add a pre-audit reconciliation against TASKS.md, the readability plan, the board, and relevant intake and triage records. Every finding needs a disposition.
5. Replace the inconsistent finding model. The plan asks for one change per dimension but records one change per page. Give every actionable Gap a finding ID, exact target, evidence, reader impact, proposed action, acceptance test, severity, confidence, dependencies, and disposition. A shared finding should list affected pages once.
6. Define what Ship-now, Fix-in-passes, and Note mean, including how uncertainty and cross-page scope affect routing.
7. Separate the reader and source passes. A fresh reader who sees source markup and the prescribed section order is not testing discovery.
8. Replace the "grep for walls" method. Grep cannot identify paragraph walls, missing reused blocks, or scannability failures. Use manual built-page review plus targeted code checks.

SHOULD-FIX
1. Define what qualifies as a worked example.
2. Make "teaching versus informing" more than checking for a skill box.
3. Record the actual reader question for each page and whether the first screen makes the page's job clear.
4. Separate current-interaction auditing from future-option research.
5. Run a calibration sample before auditing all 29.
6. Record the audited commit and recheck affected pages if dev changes.
7. State explicitly that factual corrections, source claims, and native language quality are handoffs.

NITS
1. Link or define the techniques pattern. 2. Standardize Pass-with-note versus the overall Note verdict. 3. Replace "What ships per page" with "Audit output and follow-up routing".

### Delta (verdict in full, typos cleaned)

MUST-FIX
1. Replace dimension 6, House rules compliance, with Formatting and flow: heading hierarchy, block placement, lists, tables, callouts, and the opening-to-task path.
2. Define a routable finding, not just a one-line note and one change. Require the page slug, exact section or evidence, reader task blocked, proposed change, expected outcome, acceptance check, priority, shared-issue key, and existing or proposed card.
3. Give Ship-now / Fix-in-passes / Note explicit entry criteria and explain how they derive from the six dimensions. Every Gap needs a destination. A Pass-with-note should not create work unless it names a reader-facing consequence.
4. Resolve the language contradiction. The rubric requires bilingual strings, while the voice standard and brief allow English-only output during the current phase. State the governing rule.
5. Add reconciliation against current tasks and the prior readability work. Every finding should resolve to Fixed, Existing item, New learning-UX card, or Content-track handoff.
6. Make the interactivity work evaluate learning, not inventory features. For each current or proposed interaction, record its learning purpose, reader action, feedback, accessibility, mobile and print fallback, static-build feasibility, calm-reader fit, and supporting evidence.

SHOULD-FIX
1. Do not require every opening to say who the page is for. Test whether the first screen names the reader's actual concern.
2. Define a worked example as situation + reasoning or action + outcome, tied to the taught idea. Require clearly fictional or composite framing and forbid client case studies.
3. Separate teaching depth from reassurance. A skill box is not proof of learning.
4. Have reviewers inspect the built page first on a phone viewport, then open the source. Record viewport, theme, and visible language.
5. Replace the Founder question with a fixed, stratified pilot. Include an ordinary foundation or basics page alongside the long, practice-heavy, and crisis-heavy cases, then calibrate the rubric before the remaining pages.

NITS
1. Line count is a weak proxy for density. Record word count, block count, longest uninterrupted reading path, and time to the first reader action.
2. "The quiet pattern" is undefined. Rename it "interactivity fit" or define the term.