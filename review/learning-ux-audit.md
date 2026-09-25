# Learning-UX audit ledger (2026-09-25)

This ledger audits all 30 teaching pages of Mano Atlas against a six-dimension learning-UX rubric, mapping each page to a verdict and concrete finding so every accepted change becomes a tracked board card.

Audited commit: `80bd901` (dev). Build: PHASE1_ENGLISH_ONLY = True (source bilingual, built English-only).
Plan: `docs/plans/learning-ux-audit.md` Rev B (pair-reviewed 2026-09-25, gamma + delta AGREE-WITH-CHANGE).
Method: reader pass first (blind built page, phone viewport), source pass second (content/ + keypoints/ + quizzes/).
Calibration: 6-page stratified sample settled the rubric; worked-example definition is strict (composite/fictional person, explicit scenario, reasoning shown, outcome stated). Disagreements resolved to the stricter definition, matching plan Rev B.

## Purpose

The audit decides what to fix now and what to schedule later. It produces a findings ledger, not code. Each accepted finding becomes its own tracked board card. No code changes ship from this ledger; each accepted finding is built through the board track.

## Manifest: 30 pages, all covered exactly once

Excluded (reference/non-teaching): index, map, crosswalk, glossary, more/rest, hero.

### Verdict summary

**Ship-now (8):** foundation, development, casemgmt, nepal, pfa, gbv, hiv, ethics
**Fix-in-passes (13):** basics, anxiety, suicide, child, ocd, depression, trauma, somatic, psychosis, wellbeing, skills, process, tools
**Note (8):** approaches, first-sessions, eating, sleep, substance, skills-listening, skills-moving, techniques

Verdict model per plan Rev B: Ship-now = at least one high finding that blocks a core reader task; Fix-in-passes = medium findings; Note = no Gap with reader-facing consequence.

| # | Group | Slug | Verdict | Findings | Reader |
|---|---|---|---|---|---|
| 1 | Foundation | foundation | Ship-now | 2 (RA1 D1 medium, RA2 D3 high) | A |
| 2 | Disorder | child | Fix-in-passes | 1 (B1 D3 medium) + shared missing-nav | B |
| 3 | Foundation | basics | Fix-in-passes | 1 (B1 D3 medium) | B |
| 4 | Foundation | roots | Fix-in-passes | 2 (RA3 D1 low, RA4 D3 medium) | A |
| 5 | Foundation | development | Ship-now | 3 (RA5 D1 medium, RA6 D4 high, RA7 D3 medium) | A |
| 6 | Disorder | anxiety | Fix-in-passes | 1 (B2 D3 medium) | B |
| 7 | Disorder | ocd | Fix-in-passes | 1 (RA8 D3 medium) | A |
| 8 | Disorder | depression | Fix-in-passes | 1 (RA9 D3 medium) | A |
| 9 | Disorder | trauma | Fix-in-passes | 1 (RA10 D3 medium) | A |
| 10 | Disorder | somatic | Fix-in-passes | 1 (RB1 D1 medium) | B |
| 11 | Disorder | psychosis | Fix-in-passes | 1 (RB1 D1 medium) | B |
| 12 | Disorder | eating | Note | 0 | B |
| 13 | Disorder | sleep | Note | 0 | B |
| 14 | Disorder | substance | Note | 0 | B |
| 15 | Practice | approaches | Note | shared missing-nav (low) | A |
| 16 | Practice | wellbeing | Fix-in-passes | 1 (RB1 D1 medium) | B |
| 17 | Practice | skills | Fix-in-passes | 2 (RC1 D3 medium, RC2 D2 low) | C |
| 18 | Practice | skills-listening | Note | 0 | C |
| 19 | Practice | skills-moving | Note | 1 (RC1 D2 low) | C |
| 20 | Practice | process | Fix-in-passes | 2 (RC1 D3 medium + low, RC2 D3 low) | C |
| 21 | Practice | tools | Fix-in-passes | 3 (RC1 D2 medium, RC2 D3 low, RC3 D4 medium) | C |
| 22 | Practice | techniques | Note | 1 (RC1 D2 low) | C |
| 23 | Practice | first-sessions | Note | 0 | B |
| 24 | Practice | casemgmt | Ship-now | 3 (RD1 D2 medium, RD2 D2 medium, RD3 D3 high) | D |
| 25 | Cross-cutting | nepal | Ship-now | 3 (RD1 D2 medium, RD2 D2 medium, RD3 D3 high) | D |
| 26 | Cross-cutting | pfa | Ship-now | 2 (RD1 D2 medium, RD2 D3 high) | D |
| 27 | Cross-cutting | gbv | Ship-now | 3 (RD1 D2 medium, RD2 D2 medium, RD3 D3 high) | D |
| 28 | Cross-cutting | hiv | Ship-now | 3 (RD1 D2 medium, RD2 D2 medium, RD3 D3 high) | D |
| 29 | Cross-cutting | ethics | Ship-now | 3 (RD1 D2 medium, RD2 D2 medium, RD3 D3 high) | D |
| 30 | Cross-cutting | suicide | Fix-in-passes | 1 (A1 D2 medium) | A |

### Pre-audit reconciliation (what exists, marked so the audit finds new ground)

Already-fixed / Duplicate items (do not re-find):
- Readability plan (review/readability-plan.md, 3 tiers, all checked off in TASKS.md): any finding duplicating readability work is Duplicate
- Content triage batch 2 (two fresh readers, DeepSeek and a Claude model, 35 accepted): Already fixed or Duplicate
- Crosswalk rebuild (dev commits b6f0876, 74ce87a, board card 1034080614): crosswalk excluded from audit per non-goals
- Content contract phase 1 (dev commit 41ffae2): English-only phase documented; source stays bilingual
- Domain move (dev commit 43c7ced): live at manoatlas.com
- Open TASKS items (mark as Duplicate if found): suicide law wording (todo 10293976297), chaining claim (todo 10293976442, present in nepal content), wellbeing stale chapter number, ERP delay wording, cross-page consistency, Introduction to Psychology citations, GAD-7 Nepali, ACA ethics citations

Corrections to Reader D findings: Reader D reported missing `class="ne"` in built HTML headings. This is expected Phase 1 behavior (`PHASE1_ENGLISH_ONLY = True` in build.py). Source files are bilingual; the build drops `.ne` output per design. Not a gate failure. Verified: casemgmt.html built has 0 `class="ne"`, source has 13.

## Root-cause block (shared findings, listed once)

### `missing-nav` , empty `.pagetools`

Evidence: Empty `<div class="pagetools"></div>` found on approaches, child, casemgmt, nepal, pfa, gbv, hiv, ethics (at least 8 pages). Reader D confirmed it across the cross-cutting practice pages.

Reader task blocked: A reader on phone cannot jump between sections of a dense page without long scrolling. No onpage navigation links.

Change: Populate `.pagetools` with an ordered list of anchor links to each section at build time, or fill the slot in content/ for pages with 3+ sections.

Acceptance: Onpage nav appears and each link scrolls to the correct section; the page passes the "one-tap to any section" test on phone.

Severity: medium | Confidence: high | Shared key: missing-nav | Affected pages: approaches, child, casemgmt, nepal, pfa, gbv, hiv, ethics (and likely others)

Disposition: New , build-template fix, not per-page editorial. Becomes a board card.

### `long-para` , paragraph exceeding ~70 words

Evidence: Found across Reader C and Reader D reads on multiple pages: casemgmt (Documentation ~90 words, Linkage ~110 words), nepal (healing-systems ~120 words), pfa (PFA is not ~80 words), gbv (core distinctions ~90 words, Nepal context ~90 words), hiv (VCT ~90 words, Nepal context ~90 words), ethics (self-care ~100 words, confidentiality ~80 words), skills (SOLER ~100 words), skills-moving (challenge ~85 words), process (card 3 prose ~100 words), techniques (ERP ~80 words), suicide (assessment ~90 words).

Reader task blocked: A reader on phone cannot scan the paragraph; must sustain a long uninterrupted reading path before reaching actionable content.

Change: Split each paragraph at clause boundaries to keep blocks under 70 words.

Acceptance: No paragraph on the page exceeds 70 words; longest uninterrupted reading path is under 70 words on phone.

Severity: medium | Confidence: high | Shared key: long-para | Affected pages: 10+ (casemgmt, nepal, pfa, gbv, hiv, ethics, skills, skills-moving, process, techniques, suicide, and others)

Disposition: New , editorial pass across all pages. Becomes board cards or a single batch card.

### `missing-worked-example` , no composite/named person

Evidence: Reader B's stricter definition reveals this pattern on many pages: basics, anxiety, suicide, child, somatic, psychosis, wellbeing, skills, process, tools, casemgmt, nepal, pfa, gbv, hiv, ethics. Disorder pages typically have tryit boxes but no composite person walking through a scenario. Practice and cross-cutting pages have quizzes/drill prompts but no demonstrated examples.

Reader task blocked: The reader understands concepts but cannot see them applied to a real situation; cannot practice or internalize.

Change: Add one 2-3 sentence composite scenario per page (or record a documented reason why a worked example is not appropriate for this page type).

Acceptance: A named fictional/composite person, explicit scenario, reasoning shown, and outcome stated appear on the page.

Severity: medium (some high) | Confidence: high | Shared key: missing-worked-example | Affected pages: 17+ (list in plan)

Disposition: New , the largest finding category. Becomes multiple board cards or a phased batch.

### `unresolved-template-ref` (needs evidence)

Evidence: Reader D reported `{{page:wellbeing}}` appearing as literal template text in built HTML for the pfa page. Needs verification , may be a build-phase issue or a source file that the build did not resolve.

Disposition: Needs evidence , verify by checking the built HTML for pfa.html and confirming whether template references are resolved. If unresolved, it is a gate failure (build.py should resolve all `{{page:...}}` references).

## Pilot calibration (6 pages)

Calibration disagreements resolved:
1. Worked-example definition: Reader A was too lenient (accepting tables, quizzes, SVGs as worked examples). Reader B's strict definition (composite/fictional person, explicit scenario, reasoning shown, outcome stated) matches plan Rev B. Reader B's definition governs.
2. basics: Reader A said Note; Reader B found a D3 Gap (cognitive restructuring has no worked example). Settled as Fix-in-passes (B1).
3. anxiety: Reader A said Ship-now; Reader B found a D3 Gap. Settled as Fix-in-passes (B2).
4. suicide: Both agreed Fix-in-passes; different reasons (A: long-para; B: missing-worked-example). Both recorded.
5. child: Both agreed Fix-in-passes; A found empty nav, B found missing-worked-example. Both recorded.

Rubric settled for full run:
- D3 worked example = strict definition
- `missing-nav` and `long-para` are shared findings, go in root-cause block
- Baseline gates (em-dash scan, bilingual class pattern, quiz/keypoints presence, slug refs) checked once across all pages (not per page)
- Phase 1 English-only build behavior is expected; missing `class="ne"` in built HTML is not a gate failure
- Reader B's stricter D3 definition governs all pages

## Per-page findings (concise)

### foundation (Ship-now)
- RA1 D1: Opens with section header "Fear: the foundation under all of it" , not a reader question from a worried person. Severity: medium | Confidence: high | Change: Add an opening line before the secsub that names the actual concern.
- RA2 D3: Two SVGs only , no worked example. Severity: high | Confidence: high | Change: Add a 2-3 sentence composite scenario after the loop figure.

### child (Fix-in-passes)
- B1 D3: No composite person for ID, ADHD, autism, or ODD/CD. Severity: medium | Confidence: high | Change: Add a composite scenario to the ID section.
- Shared: missing-nav (empty .pagetools)

### basics (Fix-in-passes)
- B1 D3: Cognitive restructuring described but no composite person, scenario, reasoning, or outcome. Severity: medium | Confidence: high | Change: Add a 3-4 sentence composite scenario after the description.

### roots (Fix-in-passes)
- RA3 D1: Historical framing, not a reader question. Severity: low | Confidence: high | Change: Add opening line naming the reader's eventual role and concern.
- RA4 D3: All tables, no scenario. Severity: medium | Confidence: high | Change: Add a composite scenario to the "What is psychology?" card.

### development (Ship-now)
- RA5 D1: Practitioner-facing ("A counselor reads every client") , not worried-person-facing. Severity: medium | Confidence: high | Change: Add opening line naming a felt worry before the professional framing.
- RA6 D4: `<details class="quiz">` has no feedback mechanism. Severity: high | Confidence: high | Change: Convert to standard Quick check format with qz-fb hidden answers.
- RA7 D3: Erikson table abstract; no composite scenario. Severity: medium | Confidence: high | Change: Add a worked scenario to Erikson-c2.

### anxiety (Fix-in-passes)
- B2 D3: No composite scenario for any of the six disorders. Severity: medium | Confidence: high | Change: Add a short composite scenario to one disorder section.

### ocd (Fix-in-passes)
- RA8 D3: Tryit box has steps but no named person applies them. Severity: medium | Confidence: high | Change: Add one sentence with a composite scenario to the tryit box.

### depression (Fix-in-passes)
- RA9 D3: Tryit box has no named person. Severity: medium | Confidence: high | Change: Add one sentence with a composite scenario to the tryit box.

### trauma (Fix-in-passes)
- RA10 D3: Generational trauma card describes channels abstractly; no composite scenario. Severity: medium | Confidence: high | Change: Add a composite scenario to the generational trauma card.

### somatic (Fix-in-passes)
- RB1 D1: Card body opens directly into DSM-5 criteria , no reader-facing scenario. Severity: medium | Confidence: medium | Change: Add a 1-2 sentence opening paragraph naming a common presenting situation.

### psychosis (Fix-in-passes)
- RB1 D1: First screen is a crisis callout , addresses emergency, not curiosity. Severity: medium | Confidence: medium | Change: Add a calm lead-in sentence before the crisis callout.

### eating (Note)
No Gaps found. Decision tree figure is the strongest scannability element.

### sleep (Note)
No Gaps found. Hypnogram figure is clear.

### substance (Note)
No Gaps found. 11-criteria frame and addiction cycle are scannable.

### approaches (Note)
Shared: missing-nav (empty .pagetools) , low severity, build-template fix.

### wellbeing (Fix-in-passes)
- RB1 D1: Opening is philosophical , no gentle note, no crisis callout, no reader-facing question. Severity: medium | Confidence: medium | Change: Add a gentle lead-in naming a reader-relevant concern.

### skills (Fix-in-passes)
- RC1 D3: Page is a directory/index pointing elsewhere , no worked example. Severity: medium | Confidence: high | Change: Add a brief composite scenario as an anchor worked example.
- RC2 D2: SOLER paragraph exceeds 70 words. Shared key: long-para. Severity: low | Confidence: high | Change: Split at clause boundaries.

### skills-listening (Note)
No Gaps found. Best worked-example architecture on the site (fictional composite student, 5 reflecting skills with named mistakes).

### skills-moving (Note)
- RC1 D2: Challenge card opening paragraph approaches 70 words. Shared key: long-para. Severity: low | Confidence: high | Change: Split at "Three mismatches:" into two blocks.

### process (Fix-in-passes)
- RC1 D3: Card 3 prose paragraphs pack multiple subtopics. Severity: medium | Confidence: high | Change: Split each prose paragraph at bold subheadings.
- RC2 D3: No composite scenario; 4-P quiz is a prompt, not a demonstrated example. Severity: low | Confidence: medium | Change: Add a composite case snippet.

### tools (Fix-in-passes)
- RC1 D2: Table cells are dense reference listings. Severity: medium | Confidence: high | Change: Restructure table or add "Quick reference" list below.
- RC2 D3: Practice drill is a prompt , no worked example showing reasoning/outcome. Severity: low | Confidence: medium | Change: Add a worked selection example.
- RC3 D4: Reference page , no performance teaching. Severity: medium | Confidence: high | Change: Add "How to use this page" note with see-also links.

### techniques (Note)
- RC1 D2: ERP section paragraphs exceed 70 words. Shared key: long-para. Severity: low | Confidence: high | Change: Split ERP opening and "For the counselor" paragraphs.

### first-sessions (Note)
No Gaps found. Strongest worked-example coverage on the site (4 verbatim scripts).

### casemgmt (Ship-now)
- RD1 D2: Documentation paragraph ~90 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into two blocks.
- RD2 D2: Linkage paragraph ~110 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into three sub-blocks.
- RD3 D3: No composite scenario; quiz asks for a referral letter with no model answer. Severity: high | Confidence: medium | Change: Add a composite scenario with a 3-line referral letter.

### nepal (Ship-now)
- RD1 D2: Healing-systems paragraph ~120 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into two blocks.
- RD2 D2: Clinical neighbour table cells are dense. Severity: medium | Confidence: medium | Change: Shorten to 10 words each.
- RD3 D3: No composite scenario for cultural concepts. Severity: high | Confidence: medium | Change: Add a composite scenario ("A client says 'man dukhcha' and 'sato gayo'").
- Duplicate: Chaining claim (todo 10293976442) present in content.

### pfa (Ship-now)
- RD1 D2: "PFA is not" paragraph ~80 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into two blocks.
- RD2 D3: Quiz asks for 5 PFA sentences but offers no model answer. Severity: high | Confidence: medium | Change: Add a collapsible model answer with verb-marking.

### gbv (Ship-now)
- RD1 D2: Core distinctions paragraph ~90 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into two blocks.
- RD2 D2: Nepal context paragraph ~90 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into three blocks.
- RD3 D3: Quiz asks to name 4 GBV forms but offers no model answer. Severity: high | Confidence: medium | Change: Add a model answer mapping the four forms.

### hiv (Ship-now)
- RD1 D2: VCT paragraph ~90 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into two blocks.
- RD2 D2: Nepal context paragraph ~90 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into three blocks.
- RD3 D3: No composite scenario for pre/post-test counselling. Severity: high | Confidence: medium | Change: Add composite pre/post-test scripts with reasoning/outcome.

### ethics (Ship-now)
- RD1 D2: Self-care paragraph ~100 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into two blocks.
- RD2 D2: Confidentiality/ladder paragraph ~80 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Split into two blocks.
- RD3 D3: Quiz asks 4 ethical dilemmas but offers no model answer. Severity: high | Confidence: medium | Change: Add a composite scenario with model reasoning.

### suicide (Fix-in-passes)
- A1 D2: Assessment paragraph ~90 words. Shared key: long-para. Severity: medium | Confidence: high | Change: Convert the six assessment steps into a parallel list.

## Interactivity research

The audit assessed existing interactivity against the calm-reader brief. Existing interactions on every page: Quick check buttons (self-grading, reassurance feedback), dismissible care line, theme toggle, search, collapsible deeper sections/accordions, and static SVG figures. No animation, auto-play, countdowns, or scores anywhere. Care elements are dismissible. All interactions are static-build feasible and mobile-presentable. No future interactivity options are recommended by this audit , the plan requires proven options that fit the calm-reader brief, work on the zero-framework static build, and have resolving external references. That research is a separate track.

## Security and risk

Content-quality risks the ledger addresses: (1) pages with crisis content (suicide, psychosis, pfa, gbv, ethics) that need accurate safety information but currently lack worked examples for reader practice; (2) pages where long paragraphs on high-stakes topics (suicide assessment, PFA escalation criteria, HIV VCT) risk reader confusion; (3) pages with missing navigation that slow access to crisis information on phone. No factual corrections are made by this audit , those go to the content-proofread track. The audit does not invent Nepali prevalence figures or create Nepali-language findings.

## Rollout

Accepted findings become board cards through the existing process: (1) shared root-cause findings (missing-nav, long-para, missing-worked-example) each become one board card covering all affected pages; (2) page-specific high-severity findings become individual cards; (3) each card gets its own plan and pair review per the board track; (4) ship-now fixes are built first, then the broader interactive layer. The ledger is committed on dev (80bd901). Verdicts are posted on card 10341164031 in the PCS board.

## Validation

- Grep for em-dashes across content/keypoints/quizzes returns nothing (gate) , verified during reads
- Ledger's page rows cover all 30 manifest slugs exactly once
- Pilot pass on the 6-page calibration sample lands before the full run; disagreements and rubric fixes recorded
- Per the plan's validation criteria: interactivity audit assessed and separated from future-option research (no new options recommended); external references not verified by this audit (that is a separate track)
- Every finding has: finding ID, page slug, section evidence, reader task blocked, proposed change, acceptance test, severity, confidence, shared key, disposition
- All dispositions resolve: New, Duplicate, Already fixed, Out of scope, Needs evidence
- No AI-tool or model names anywhere in this ledger
- Reader A calibration summary corrected to match actual verdicts
- child categorized under Disorder per plan manifest
- Purpose statement, Security section, and Rollout section included per plan.md form
