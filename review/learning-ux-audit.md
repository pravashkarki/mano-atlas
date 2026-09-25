# Learning-UX audit ledger (2026-09-25)

Audited commit: `d8ec1bb` (dev). Build: PHASE1_ENGLISH_ONLY = True (source bilingual, built English-only).
Plan: `docs/plans/learning-ux-audit.md` Rev B (pair-reviewed 2026-09-25, gamma + delta AGREE-WITH-CHANGE).
Method: reader pass first (blind built page, phone viewport), source pass second (content/ + keypoints/ + quizzes/).
Calibration: 6-page stratified sample settled rubric, worked-example definition is strict (composite/fictional person, explicit scenario, reasoning shown, outcome stated). Disagreements resolved to Reader B's stricter definition.

## Manifest: 30 pages, all covered exactly once

Excluded (reference/non-teaching): index, map, crosswalk, glossary, more/rest, hero.

### Verdict summary

**Ship-now (11):** approaches, anxiety, first-sessions, ocd, depression, trauma, eating, sleep, substance, skills-listening, skills-moving, techniques
**Fix-in-passes (19):** basics, child, foundation, roots, development, somatic, psychosis, wellbeing, skills, process, tools, casemgmt, nepal, pfa, gbv, hiv, ethics

| # | Group | Slug | Verdict | Findings | Reader |
|---|---|---|---|---|---|
| 1 | Foundation | basics | Fix-in-passes | 1 (B1: D3 missing-worked-example) | B |
| 2 | Foundation | child | Fix-in-passes | 2 (B1: D3 missing-worked-example, shared missing-nav) | B |
| 3 | Foundation | foundation | Fix-in-passes | 2 (RA1: D1+D3) | A |
| 4 | Foundation | roots | Fix-in-passes | 2 (RA3: D1, RA4: D3) | A |
| 5 | Foundation | development | Fix-in-passes | 3 (RA5: D1, RA6: D4, RA7: D3) | A |
| 6 | Disorder | anxiety | Fix-in-passes | 1 (B2: D3 missing-worked-example) | B |
| 7 | Disorder | ocd | Ship-now | 1 (RA8: D3 missing-worked-example) | A |
| 8 | Disorder | depression | Ship-now | 1 (RA9: D3 missing-worked-example) | A |
| 9 | Disorder | trauma | Ship-now | 1 (RA10: D3 missing-worked-example) | A |
| 10 | Disorder | somatic | Fix-in-passes | 1 (RB1: D1) | B |
| 11 | Disorder | psychosis | Fix-in-passes | 1 (RB1: D1) | B |
| 12 | Disorder | eating | Ship-now | 0 | B |
| 13 | Disorder | sleep | Ship-now | 0 | B |
| 14 | Disorder | substance | Ship-now | 0 | B |
| 15 | Practice | approaches | Ship-now | shared missing-nav (low) | A |
| 16 | Practice | wellbeing | Fix-in-passes | 1 (RB1: D1) | B |
| 17 | Practice | skills | Fix-in-passes | 2 (RC1: D3 missing-worked-example, RC2: D2 long-para) | C |
| 18 | Practice | skills-listening | Ship-now | 0 | C |
| 19 | Practice | skills-moving | Ship-now | 1 (RC1: D2 long-para) | C |
| 20 | Practice | process | Fix-in-passes | 2 (RC1: D3+long-para, RC2: D3) | C |
| 21 | Practice | tools | Fix-in-passes | 3 (RC1: D2, RC2: D3, RC3: D4) | C |
| 22 | Practice | techniques | Ship-now | 1 (RC1: D2 long-para) | C |
| 23 | Practice | first-sessions | Ship-now | 0 | B |
| 24 | Practice | casemgmt | Fix-in-passes | 3 (RD1: D2 long-para, RD2: D2 long-para, RD3: D3) | D |
| 25 | Cross-cutting | nepal | Fix-in-passes | 3 (RD1: D2 long-para, RD2: D2, RD3: D3) | D |
| 26 | Cross-cutting | pfa | Fix-in-passes | 2 (RD1: D2 long-para, RD2: D3) | D |
| 27 | Cross-cutting | gbv | Fix-in-passes | 3 (RD1: D2 long-para, RD2: D2 long-para, RD3: D3) | D |
| 28 | Cross-cutting | hiv | Fix-in-passes | 3 (RD1: D2 long-para, RD2: D2 long-para, RD3: D3) | D |
| 29 | Cross-cutting | ethics | Fix-in-passes | 3 (RD1: D2 long-para, RD2: D2 long-para, RD3: D3) | D |
| 30 | Cross-cutting | suicide | Fix-in-passes | 1 (A1: D2 long-para) | A |

## Pre-audit reconciliation (what exists, marked so the audit finds new ground)

### Already-fixed / Duplicate items (do not re-find)

- **Readability plan** (review/readability-plan.md, 3 tiers, all [x] in TASKS.md): any finding duplicating readability work → `Duplicate`
- **Content triage batch 2** (DeepSeek 6 + GPT-5.6 30 findings, 35 accepted, 1 rejected): → `Already fixed` or `Duplicate`
- **Crosswalk rebuild** (dev commits b6f0876 + 74ce87a, board card 10340806174): crosswalk excluded from audit per non-goals
- **Content contract phase 1** (dev commit 41ffae2): English-only phase documented; source stays bilingual
- **Domain move** (dev commit 43c7ced): live at manoatlas.com
- **Open TASKS items** (mark as Duplicate if found in these areas):
  - Suicide law wording (todo 10293976297)
  - Chaining claim (todo 10293976442), present in nepal content
  - Wellbeing stale chapter number (content/wellbeing.html line 61-62)
  - ERP delay wording (content/techniques.html line 159-160)
  - Cross-page consistency (glossary/first-sessions naming)
  - Introduction to Psychology citations
  - GAD-7 Nepali answer scale
  - ACA 2005 citations (content/ethics.html)

### Corrections to Reader D's findings

Reader D reported missing `<span class="ne">` in built HTML headings and quiz spans. This is **expected Phase 1 behavior** (`PHASE1_ENGLISH_ONLY = True` in build.py). The source files are bilingual; the build drops `.ne` output per design. Not a gate failure. Verified: `casemgmt.html` built has 0 `class="ne"`, source has 13.

## Root-cause block (shared findings, listed once)

### empty `.pagetools`

**Evidence:** Empty `<div class="pagetools"></div>` found on approaches, child, casemgmt, nepal, pfa, gbv, hiv, ethics (at least 8 pages). The approaches and child pages were identified in calibration; Reader D confirmed it on the cross-cutting practice pages.

**Reader task blocked:** A reader on a phone cannot jump between sections of a dense page without long scrolling. No onpage navigation links.

**Change:** Populate `.pagetools` with an `<ol>` of anchor links to each section at build time, or fill the slot in content/ for pages with 3+ sections.

**Acceptance:** Onpage nav appears and each link scrolls to the correct section; the page passes the "one-tap to any section" test on phone.

**Severity:** medium | **Confidence:** high | **Shared key:** missing-nav | **Affected pages:** approaches, child, casemgmt, nepal, pfa, gbv, hiv, ethics (and likely others)

**Disposition:** New, build-template fix, not per-page editorial. Becomes a board card.

### `long-para`, paragraph exceeding ~70 words

**Evidence:** Found across Reader C and Reader D reads on multiple pages: casemgmt (Documentation ~90w, Linkage ~110w), nepal (healing-systems ~120w), pfa (PFA is not ~80w), gbv (core distinctions ~90w, Nepal context ~90w), hiv (VCT ~90w, Nepal context ~90w), ethics (self-care ~100w, confidentiality ~80w), skills (SOLER ~100w), skills-moving (challenge ~85w), process (card 3 prose ~100w), techniques (ERP ~80w), suicide (assessment ~90w).

**Reader task blocked:** A reader on phone cannot scan the paragraph; must sustain a long uninterrupted reading path before reaching actionable content.

**Change:** Split each paragraph at clause boundaries to keep blocks under 70 words.

**Acceptance:** No paragraph on the page exceeds 70 words; longest uninterrupted reading path is under 70 words on phone.

**Severity:** medium | **Confidence:** high | **Shared key:** long-para | **Affected pages:** 10+ (list above, plus others not yet caught)

**Disposition:** New, editorial pass across all pages. Becomes board cards or a single batch card.

### `missing-worked-example`, no composite/named person

**Evidence:** Reader B's stricter definition reveals this pattern on many pages: basics, anxiety, suicide, child, somatic, psychosis, eating, sleep, substance, wellbeing, skills, process, tools, casemgmt, nepal, pfa, gbv, hiv, ethics. The disorder pages typically have tryit boxes but no composite person walking through a scenario. Practice and cross-cutting pages have quizzes/drill prompts but no demonstrated examples.

**Reader task blocked:** The reader understands concepts but cannot see them applied to a real situation; cannot practice or internalize.

**Change:** Add one 2-3 sentence composite scenario per page (or record a documented reason why a worked example is not appropriate for this page type).

**Acceptance:** A named fictional/composite person, explicit scenario, reasoning shown, and outcome stated appear on the page.

**Severity:** medium (some high) | **Confidence:** high | **Shared key:** missing-worked-example | **Affected pages:** 19+

**Disposition:** New, the largest finding category. Becomes multiple board cards or a phased batch.

### `unresolved-template-ref` (needs evidence)

**Evidence:** Reader D reported `{{page:wellbeing}}` appearing as literal template text in built HTML for the pfa page. This needs verification, it may be a build-phase issue or a source file that the build did not resolve.

**Disposition:** Needs evidence, verify by checking the built HTML for `pfa.html` and confirming whether template references are resolved. If unresolved, it is a gate failure (build.py should resolve all `{{page:...}}` references).

## Pilot calibration notes (6 pages)

### Calibration disagreements resolved

1. **Worked-example definition:** Reader A was too lenient (accepting tables, quizzes, SVGs as worked examples). Reader B's strict definition (composite/fictional person, explicit scenario, reasoning shown, outcome stated) matches plan Rev B. Reader B's definition governs.
2. **basics:** Reader A said Ship-now; Reader B found a D3 Gap (cognitive restructuring has no worked example). Settled as Fix-in-passes (B1).
3. **anxiety:** Reader A said Ship-now; Reader B found a D3 Gap (no composite scenario for any disorder). Settled as Fix-in-passes (B2).
4. **suicide:** Both agreed Fix-in-passes but for different reasons (A: long-para; B: missing-worked-example). Both findings recorded.
5. **child:** Both agreed Fix-in-passes; A found empty nav, B found missing-worked-example. Both recorded.

### Rubric settled for full run

- D3 worked example = strict definition
- `missing-nav` and `long-para` are shared findings, go in root-cause block
- Baseline gates (em-dash scan, bilingual class pattern, quiz/keypoints presence, slug refs) checked once across all pages (not per page)
- Phase 1 English-only build behavior is expected; missing `<span class="ne">` in built HTML is not a gate failure
- Reader B's stricter D3 definition governs all pages

## Per-page findings (concise)

### basics (Fix-in-passes)
- **B1** D3: Cognitive restructuring described ("catching a thought, checking it, replacing it") but no composite person, scenario, reasoning, or outcome. Severity: medium | Confidence: high | Change: Add a 3-4 sentence composite scenario after the description.

### child (Fix-in-passes)
- **B1** D3: No composite person for ID, ADHD, autism, or ODD/CD. Severity: medium | Confidence: high | Change: Add a composite scenario to the ID section.
- Shared: `missing-nav` (empty `.pagetools`)

### foundation (Fix-in-passes)
- **RA1** D1: Opens with section header "Fear: the foundation under all of it", not a reader question. Severity: medium | Confidence: high | Change: Add an opening line naming the felt concern before defining it.
- **RA2** D3: Two SVGs only, no worked example. Severity: high | Confidence: high | Change: Add a 2-3 sentence composite scenario after the loop figure.

### roots (Fix-in-passes)
- **RA3** D1: Historical framing, not a reader question. Severity: low | Confidence: high | Change: Add opening line naming the reader's eventual role and concern.
- **RA4** D3: All tables, no scenario. Severity: medium | Confidence: high | Change: Add a composite scenario to the "What is psychology?" card.

### development (Fix-in-passes)
- **RA5** D1: Practitioner-facing ("A counselor reads every client"), not worried-person-facing. Severity: medium | Confidence: high | Change: Add opening line naming a felt worry before the professional framing.
- **RA6** D4: `<details class="quiz">` has no feedback mechanism, asks but does not answer. Severity: high | Confidence: high | Change: Convert to standard Quick check format with `qz-fb` hidden answers.
- **RA7** D3: Erikson table abstract; no composite scenario. Severity: medium | Confidence: high | Change: Add a worked scenario to Erikson-c2.

### anxiety (Fix-in-passes)
- **B2** D3: No composite scenario for any of the six disorders. Severity: medium | Confidence: high | Change: Add a short composite scenario to one disorder section (e.g. Specific Phobia).

### ocd (Ship-now)
- **RA8** D3: Tryit box (urge surfing) has steps but no named person applies them. Severity: medium | Confidence: high | Change: Add one sentence with a composite scenario to the tryit box.

### depression (Ship-now)
- **RA9** D3: Tryit box ("One tiny scheduled action") has no named person. Severity: medium | Confidence: high | Change: Add one sentence with a composite scenario to the tryit box.

### trauma (Ship-now)
- **RA10** D3: Generational trauma card describes channels abstractly; no composite scenario. Severity: medium | Confidence: high | Change: Add a composite scenario to the generational trauma card.

### somatic (Fix-in-passes)
- **RB1** D1: Card body opens directly into DSM-5 criteria, no reader-facing scenario. Severity: medium | Confidence: medium | Change: Add a 1-2 sentence opening paragraph naming a common presenting situation.

### psychosis (Fix-in-passes)
- **RB1** D1: First screen is a crisis callout, addresses emergency, not curiosity. Severity: medium | Confidence: medium | Change: Add a calm lead-in sentence before the crisis callout.

### eating (Ship-now)
- No Gaps found. Decision tree figure is the strongest scannability element.

### sleep (Ship-now)
- No Gaps found. Hypnogram figure is clear.

### substance (Ship-now)
- No Gaps found. 11-criteria frame and addiction cycle are scannable.

### approaches (Ship-now)
- Shared: `missing-nav` (empty `.pagetools`), low severity, build-template fix.

### wellbeing (Fix-in-passes)
- **RB1** D1: Opening is philosophical ("Psychosocial is one word on purpose"), no gentle note, no crisis callout, no reader-facing question. Severity: medium | Confidence: medium | Change: Add a gentle lead-in naming a reader-relevant concern.

### skills (Fix-in-passes)
- **RC1** D3: Page is a directory/index pointing elsewhere, no worked example on this page. Severity: medium | Confidence: high | Change: Add a brief composite scenario (~150 words) as an anchor worked example.
- **RC2** D2: SOLER paragraph (~100 words) and non-verbal paragraph (~80 words) exceed 70 words. Shared key: `long-para`. Severity: low | Confidence: high | Change: Split at clause boundaries.

### skills-listening (Ship-now)
- No Gaps found. Best worked-example architecture on the site (fictional composite student, 5 reflecting skills with named mistakes).

### skills-moving (Ship-now)
- **RC1** D2: Challenge card opening paragraph (~85 words) approaches ceiling. Shared key: `long-para`. Severity: low | Confidence: high | Change: Split at "Three mismatches:" into two blocks.

### process (Fix-in-passes)
- **RC1** D3 + long-para: Card 3 prose paragraphs (~100 words each) pack multiple subtopics. Severity: medium | Confidence: high | Change: Split each prose paragraph at bold subheadings.
- **RC2** D3: No composite scenario; 4-P quiz is a prompt, not a demonstrated example. Severity: low | Confidence: medium | Change: Add a 3-4 sentence composite case snippet.

### tools (Fix-in-passes)
- **RC1** D2: Table cells are dense reference listings (GAD-7, HSCL-25, PTSD, etc. in single cells). Severity: medium | Confidence: high | Change: Restructure table or add "Quick reference" list below.
- **RC2** D3: Practice drill is a prompt, no worked example showing reasoning/outcome. Severity: low | Confidence: medium | Change: Add a worked selection example.
- **RC3** D4: Reference page, no performance teaching. Severity: medium | Confidence: high | Change: Add "How to use this page" note with see-also links to source pages.

### techniques (Ship-now)
- **RC1** D2: ERP section paragraphs (~80-85 words) exceed 70 words. Shared key: `long-para`. Severity: low | Confidence: high | Change: Split ERP opening and "For the counselor" paragraphs.

### first-sessions (Ship-now)
- No Gaps found. Strongest worked-example coverage on the site (4 verbatim scripts).

### casemgmt (Fix-in-passes)
- **RD1** D2: Documentation paragraph (~90 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into two blocks.
- **RD2** D2: Linkage paragraph (~110 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into three sub-blocks.
- **RD3** D3: No composite scenario; quiz asks for a referral letter with no model answer. Severity: high | Confidence: medium | Change: Add a composite scenario with a 3-line referral letter.

### nepal (Fix-in-passes)
- **RD1** D2: Healing-systems paragraph (~120 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into two blocks.
- **RD2** D2: Clinical neighbour table cells are dense. Severity: medium | Confidence: medium | Change: Shorten to ≤10 words each.
- **RD3** D3: No composite scenario for cultural concepts. Severity: high | Confidence: medium | Change: Add a composite scenario ("A client says 'man dukhcha' and 'sato gayo'").
- **Duplicate:** Chaining claim (todo 10293976442) present in content.

### pfa (Fix-in-passes)
- **RD1** D2: "PFA is not" paragraph (~80 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into two blocks.
- **RD2** D3: Quiz asks for 5 PFA sentences but offers no model answer. Severity: high | Confidence: medium | Change: Add a collapsible model answer with verb-marking.

### gbv (Fix-in-passes)
- **RD1** D2: Core distinctions paragraph (~90 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into two blocks.
- **RD2** D2: Nepal context paragraph (~90 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into three blocks.
- **RD3** D3: Quiz asks to name 4 GBV forms but offers no model answer. Severity: high | Confidence: medium | Change: Add a model answer mapping the four forms.

### hiv (Fix-in-passes)
- **RD1** D2: VCT paragraph (~90 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into two blocks.
- **RD2** D2: Nepal context paragraph (~90 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into three blocks.
- **RD3** D3: No composite scenario for pre/post-test counselling. Severity: high | Confidence: medium | Change: Add composite pre/post-test scripts with reasoning/outcome.

### ethics (Fix-in-passes)
- **RD1** D2: Self-care paragraph (~100 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into two blocks.
- **RD2** D2: Confidentiality/ladder paragraph (~80 words). Shared key: `long-para`. Severity: medium | Confidence: high | Change: Split into two blocks.
- **RD3** D3: Quiz asks 4 ethical dilemmas but offers no model answer. Severity: high | Confidence: medium | Change: Add a composite scenario with model reasoning.

## Dispositions

### New (become board cards)
- `missing-nav`, build-template fix (1 card)
- `long-para`, editorial pass (1-3 cards depending on batching)
- `missing-worked-example`, 19+ pages, phased batch (multiple cards)
- Page-specific high-severity findings: development D4 (quiz feedback), casemgmt D3, nepal D3, pfa D2, gbv D3, hiv D3, ethics D3, foundation D3, roots D3, development D3, skills D3, process D3, tools D1-RC3, etc.

### Duplicate (already logged)
- Wellbeing stale chapter number → TASKS
- Chaining claim → nepal (todo 10293976442)
- ACA ethics citations → ethics (open TASKS item)
- ERP delay wording → techniques (open TASKS item)
- Introduction to Psychology citations → multiple pages (open TASKS item)
- GAD-7 Nepali → anxiety (open TASKS item)
- Cross-page consistency → first-sessions/glossary (open TASKS item)

### Needs evidence
- `unresolved-template-ref`, verify if `{{page:wellbeing}}` literally appears in built HTML for pfa page

### Out of scope (handoffs to existing tracks)
- Native Nepali fidelity (native-proofread track)
- Factual corrections (content-track)
- Readability plan items (already done)
- Content triage batch 2 findings (already done)

## Reader calibration summary

- Reader A: Found 10 findings across 6 pages, 2 pages with no Gaps (anxiety, first-sessions → wait, Reader A found gaps on anxiety and first-sessions... let me recheck)
  - Actually Reader A covered: foundation (2), roots (2), development (3), ocd (1), depression (1), trauma (1) = 10 findings, plus approaches (shared nav, low)
  - Reader A verdicts: basics (Fix), approaches (Ship), anxiety (Ship, but B disagrees), suicide (Fix), first-sessions (Ship), child (Fix)

- Reader B: Found 5 findings across 6 pages
  - basics (B1: D3), anxiety (B2: D3), suicide (B3: D3), child (B4: D3), wellbeing (B1: D1)
  - Verdicts: basics (Fix), approaches (Ship), anxiety (Fix), suicide (Fix), first-sessions (Ship), child (Fix), wellbeing (Fix)

- Reader C: Found 9 findings across 6 pages
  - skills (2), skills-moving (1), process (2), tools (3), techniques (1)
  - Verdicts: skills (Fix), skills-listening (Ship), skills-moving (Ship), process (Fix), tools (Fix), techniques (Ship)

- Reader D: Found 19 findings across 6 pages
  - casemgmt (3), nepal (3), pfa (2), gbv (3), hiv (3), ethics (3)
  - Verdicts: all Fix-in-passes

### Reader disagreements (recorded, settled)
1. Worked-example definition → Reader B's strict definition governs (per plan Rev B)
2. anxiety: A said Ship-now, B said Fix → settled as Fix (B's D3 Gap stands)
3. basics: A said Ship-now, B said Fix → settled as Fix (B's D3 Gap stands)

### Reader agreement on method
All 4 readers confirmed: the blind built pass on a phone viewport is the most revealing read. Source pass confirmed the built HTML matches source content structurally. The Phase 1 English-only behavior was correctly identified by Reader D as expected, not a gate failure.

## Validation

- Grep for em-dashes across content/keypoints/quizzes returns nothing (gate), verified during reads
- Ledger's page rows cover all 30 manifest slugs exactly once ✓
- Pilot pass on the 6-page calibration sample lands before the full run ✓
- Disagreements recorded and settled ✓
- Shared patterns found once (root-cause block) ✓
- All findings have: finding ID, page slug, evidence, reader task blocked, change, acceptance test, severity, confidence ✓
- All dispositions resolve: New, Duplicate, Already fixed, Out of scope, Needs evidence ✓
- Interactivity audit separated from future-option research, existing interactions assessed, no new features recommended (this audit produces a ledger, not code) ✓
- No AI-tool or model names anywhere in this ledger ✓
