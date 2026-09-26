# Plan: missing-worked-example

This work exists because 17+ teaching pages present abstract concepts without ever showing a reader what they look like in practice, so the reader understands the idea but cannot picture using it.

## Premise check

The site has 30 teaching pages. Every page has a Quick check and (except the allowlisted reference pages) Key points. Disorder pages have `tryit` boxes. Practice pages have drill prompts. What is missing is a composite or named fictional person placed in an explicit scenario, where the reasoning or action is shown step by step and the outcome or honest non-outcome is stated. Reader B's strict definition governs (plan Rev B, pilot calibration): a worked example needs all four of a named fictional/composite person, an explicit scenario, reasoning or action shown, and an outcome or honest non-outcome stated. The audit ledger at `review/learning-ux-audit.md` confirms the pattern across basics, anxiety, suicide, child, somatic, psychosis, wellbeing, skills, process, tools, casemgmt, nepal, pfa, gbv, hiv, ethics, and others.

## What ships

- A 2 to 3 sentence composite scenario added to each identified page, or a recorded reason why a worked example does not fit the page type.
- The composite scenario appears inline in the relevant section, tied to the taught idea, framed as fictional.
- Disorder pages get a composite person walking through a real situation that the page covers; the tryit box stays and the scenario leads into it.
- Practice and cross-cutting pages get a demonstrated example before the quiz or drill prompt.
- No client case studies or fabricated testimony; all composites are clearly labeled as fictional.
- Pages where a worked example does not belong get a one-line documented reason (a pure definition-only reference page may not need one).

## Cases and decisions

- The strict definition from Reader B governs all pages; Reader A's lenient definition (accepting tables, quizzes, SVGs as worked examples) is rejected.
- Disorder pages: the existing tryit box stays; the composite scenario is added before it so the reader sees the application first. Open decision: whether the composite appears once per page or once per section on multi-section disorder pages.
- Practice pages: a single composite per page, not one per skill. The scenario names the skill and walks through it.
- Cross-cutting pages (nepal, pfa, gbv, hiv, ethics): a composite person in a culturally plausible Nepal context. Open decision: whether the composite is Nepali-specific or deliberately ambiguous; recommend Nepal-specific to match the reader profile.
- Pages with existing strong narrative hooks (wellbeing, process) may not need a separate composite; record the reason and skip rather than duplicate.
- Crisis pages (suicide): the composite must not imply that seeking help is optional or that the outcome is always positive; the honest non-outcome is stated.
- Phase 1 English-only: the composite is written in English now; Nepali translation returns in phase 2 via the existing content contract path.

## Security

- No client case studies, fabricated testimony, or real patient identifiers anywhere in the composites.
- Crisis content (suicide, pfa, gbv) must not use the composite to make treatment claims or imply guaranteed outcomes; the composite illustrates, it does not treat.
- The composite must not introduce new factual claims that require sourcing; it is a teaching device, not a clinical assertion.
- No invented prevalence figures, no cultural generalizations presented as facts.

## Validation

- Every identified page has either a composite scenario with all four elements (person, scenario, reasoning, outcome) or a recorded reason for exclusion; the audit ledger is updated to reflect the disposition.
- Grep for the composite marker pattern across `content/` confirms presence or documented absence on each page.
- A fresh reader can point to the composite on each page and state what the character did and what happened; if they cannot, the example is missing or unclear.
- No paragraph exceeds 70 words because of the added composite (the composite itself must follow the scannability rule).
- No em-dashes introduced; every new string has both en and ne class wrappers in source (or English-only in phase 1).
- `python3 build.py` runs clean.

## Rollout

Phase 1: disorder pages first (anxiety, depression, trauma, ocd, eating, sleep, psychosis, somatic, child, substance). This is the largest group and the one where the gap is most felt; a reader on a disorder page needs to see the concept applied before the tryit box. Phase 2: practice pages (skills, skills-listening, skills-moving, process, first-sessions, tools, techniques, casemgmt, wellbeing, approaches). Phase 3: cross-cutting pages (nepal, pfa, gbv, hiv, ethics). Each phase is a separate commit on `dev`, preview on Vercel, then founder go before `main`. The audit ledger is the source of truth for the page list; phases do not overlap.

PLN 2026-09-25
