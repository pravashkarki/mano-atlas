# Plan: Learning-UX audit across all pages

Status: REV B (pair review, 2026-09-25, two fresh readers both AGREE-WITH-CHANGE). Founder's go pending. Nothing ships from this plan itself.

Card 10341164031 (Shaping). Big appetite, up to 14 days. Deliverable on the card: a findings ledger in `review/` mapping every page to a learning-UX verdict with routable findings, interactivity research naming proven options that fit a calm mental-health reader, verdicts on the card, and each accepted change tracked as its own card or todo.

## What this plan is

An audit, not a rebuild. It decides the ship-now fixes and flags the broader interactive layer. No code changes ship from this plan; each accepted finding becomes its own tracked item built later through the board track.

## Manifest: the audited pages

Thirty teaching pages, frozen by slug so each is included exactly once and reference pages are excluded consistently (excluded: index, map, crosswalk, glossary, more/rest, hero):

- Foundation: foundation, basics, roots, development
- Disorder pages: anxiety, ocd, depression, trauma, somatic, psychosis, child, eating, sleep, substance
- Practice: wellbeing, approaches, skills, skills-listening, skills-moving, process, first-sessions, tools, techniques, casemgmt
- Cross-cutting: nepal, suicide, pfa, gbv, hiv, ethics

Excluded, and why: index (root shell), map, crosswalk, glossary, more (reference pages with no teaching text; the crosswalk already reviews itself at build). The audit row for a page records its current language mode (bilingual source; English-only rendered in the current phase) and prior-work links (readability items, triage rows) so nothing is quietly re-found.

## Baseline gates (checked once, not per page)

The build gates already hold: no em-dashes, bilingual class pattern present in source, quiz and keypoints per page, slug cross-references, no hand-written chapter numbers. The audit runs these once across `content/`, `keypoints/`, `quizzes/` as a release gate (results in the ledger's shared section, not repeated per page).

## Rubric: six dimensions, scored per page

Each page gets a verdict per dimension: Pass / Pass-with-note / Gap, each with a one-line evidence note. Every Gap becomes a routable finding (model below).

1. **Reader-question shape.** Does the page answer one reader question, from a worried person first? Does the opening path name the reader's actual concern and what the page resolves, without a formulaic audience label (professional and practice pages are read by students; the worried-person framing is not forced there)? Fixed page order where required (disorder pages: definition → DSM-5 → international → Nepal → diagram → skill box → Quick check → Learn more). The ledger records the page's actual reader question and whether the first screen makes the page's job clear.
2. **Scannability.** One idea per paragraph, wall-of-text ceiling (roughly 70 words per paragraph from VOICE-TONE), subject and verb early, headings that jump, lists in parallel form with a chosen count, no dumps over seven items (split into groups). Measured, not line-counted: word count, block count, longest uninterrupted reading path, time to the first reader action.
3. **Worked examples.** Abstract skills and processes get a worked illustration: a named fictional or composite person in an explicit scenario, with the reasoning or action shown and the outcome or honest non-outcome stated, tied to the taught idea. Clearly framed as fictional where used; never client case studies or fabricated testimony. A page without a worked example needs a recorded reason (a definition-only reference page may not need one).
4. **Teaching depth beyond informing.** Beyond the presence of a skill box: can the reader explain the idea, distinguish it from a near neighbour, perform or retrieve a safe step, and know when to seek help? Crisis pages are not forced into generic self-help or formulaic reassurance; early reassurance on heavy pages is a safety rule, not counted as evidence of teaching.
5. **Interactivity and the calm pattern.** What interactivity exists today and what does it DO for learning (purpose, reader action, feedback, accessibility, mobile and print fallback, static-build feasibility, calm-reader fit): Quick checks, expanders, tables, diagrams, search. Tables and diagrams are not interactivity just because a reader can inspect them. No animation, auto-play, countdown, or score leaks anywhere (out by house rules; confirmed, not assumed). Care elements stay dismissible; teal/crimson split stays strict.
6. **Formatting and flow.** Heading hierarchy, block placement, section boundaries, list and table shape, callouts, diagram captions (explain the figure in one line, never describe the art), emphasis restraint, and the phone presentation. The opening-to-task path: how many scrolls or taps before a reader reaches something they can do.

## Finding model (routable, not "this page is dense")

A finding, not a note. A page can carry several findings; a shared finding lists its affected pages once.

Fields: finding ID, page slug, exact section or line evidence, reader task the finding blocks, proposed change, acceptance test, severity (high = blocks a reader's core task; medium = slows it; low = polish), confidence, dependencies, disposition. Worded so someone can pick it up and build it.

Dispositions, resolved from reconciliation before posting: New (becomes a board card) · Duplicate (already in TASKS.md, readability plan, or an existing board card; linked, not re-created) · Already fixed (verified, closed) · Out of scope (factual correction, source claim, or native Nepali quality: handed to the content-proofread / intake tracks, not new cards from this audit) · Needs evidence (unverified claim; recorded, not shipped).

## Verdict model

Per page: Ship-now (at least one high finding that blocks a core reader task) · Fix-in-passes (medium findings, build into the existing intake cadence) · Note (no Gap with a reader-facing consequence; Pass-with-note that names no consequence does not create work). Overall verdict derives from the finding severities; the ledger shows the derivation, and Note cannot hide unresolved questions (those get the Needs-evidence disposition).

## Method

1. Reconcile pre-audit: read TASKS.md, readability plan, the board, intake and triage records; mark every known page item so the audit finds new ground, not reopened work.
2. Pilot and calibrate the rubric on a fixed stratified sample first: one ordinary foundation page (e.g. basics), one dense practice page (approaches), one disorder page (anxiety), one crisis-heavy page (suicide), one English-only-phase page (crosswalk if it carried teaching text, else a recent batch-2 chapter), one criteria-dense page (child). Record disagreements, settle the rubric, then run the remaining pages.
3. Reader pass first, source pass second. A fresh reader sees the BUILT page first on a phone viewport with the recorded theme and visible language (English-only phase) and reads it as a visitor: does scanning and the opening-to-task path work blind? Only then does a second pass open the source and the gates. Disagreement across readers resolves to a third read or the Needs-evidence disposition.
4. Shared patterns found once: root-cause block with the affected-page list, not repeated per page (e.g. a recurring missing reused block, a repeated over-seven-item list).
5. Interactivity research as its own pass: options named only when they are proven in self-directed learning, fit the calm-reader brief, work on the zero-framework static build with both languages, keep crisis safety, and have resolving external references. Each option records evidence, target finding, accessibility, static and bilingual feasibility, cost, and a keep or skip decision. Existing interactions are audited separately from future options.
6. Ledger lands in `review/learning-ux-audit.md`; one commit on `dev`; verdicts posted on the card; accepted findings become board cards (ship-now first, then the interactive layer).
7. The audited commit is recorded in the ledger. If `dev` changes during the pass, affected pages are re-read before posting.

## Audit output and follow-up routing

The ledger is the deliverable; its accepted changes become board cards, each with its own plan and pair review per the board track. This plan ships no page changes itself.

## Language rule (governing)

Source is bilingual (en/ne class pattern, gate-held). The current phase renders English-only by build flag with the toggle hidden; the audit judges the rendered surface against learning-UX shape in the visible language, and confirms structurally that the source keeps the en/ne pattern. Nepali fidelity and idioms are owned by the native-proofread track; nothing in this audit creates Nepali-language cards.

## Non-goals

- No framework, no runtime, no interactivity added by this plan (only named as options on cards).
- No per-page noise for shared patterns (they live in the root-cause block).
- No invented prevalence, no links that do not resolve, no scores or shame in anything the audit recommends.
- No language-fidelity or factual-correction cards from this audit: those hand off to their existing tracks.
- The crosswalk page and reference pages are out of scope (the crosswalk reviewed itself; reference pages have no teaching text).

## Validation

- Grep for em-dashes across content/keypoints/quizzes returns nothing (gate).
- The ledger's page rows cover all 30 manifest slugs exactly once; dispositions resolve every finding.
- Pilot pass on the six-page calibration sample lands before the full run; its disagreements and rubric fixes are recorded.
- Interactivity options carry evidence and a keep/skip decision; external references verified to resolve.
- Verdicts posted on the card; every New finding is a board card or todo with a plan, per the founder's later choice of order.