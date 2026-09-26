# Plan: Development page quiz feedback mechanism

This work exists because the development page asks three application questions and provides no way for the reader to confirm whether their answers are correct, which blocks the core learning task of self-checking understanding.

## Premise check

What exists: `development.html` contains a `<details class="quiz">` block with three application questions. The page is part of the Ship-now group in the learning-ux audit ledger.

What is missing: Unlike every other teaching page on the site, this quiz block has no feedback mechanism. The reader submits answers with no way to know if they are right or wrong. The audit ledger finding RA6 D4 (Severity: high, Confidence: high) records that `<details class="quiz">` has no feedback mechanism, and the proposed change is to convert it to the standard Quick check format with qz-fb hidden answers.

## What ships

1. Convert the `<details class="quiz">` block on the development page to the standard Quick check format used by every other quiz on the site.
2. Add qz-fb hidden answer elements behind each question so the reader can reveal whether their answer is correct.
3. Preserve the existing three application questions and their content exactly as written.

## Cases and decisions

- The development page also has RA5 D1 (practitioner-facing opening, Severity: medium) and RA7 D3 (abstract Erikson table, Severity: medium). Those are separate findings and are not addressed by this plan. This plan covers only RA6 D4.
- The standard Quick check format is already proven on the site; no new interactivity pattern is introduced.
- Open decision: whether the quiz questions should also be revised to fit the exact qz-fb markup structure, or whether the existing question text is sufficient and only the answer-reveal mechanism is added.

## Security

The risk is limited to content accuracy: if the hidden answers are incorrect or misleading, the reader receives wrong feedback on a developmental psychology application task. All answer text must be verified against the source content before shipping.

## Validation

- The development page quiz uses the same `qz-fb` pattern as all other Quick checks on the site.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The quiz is functional: each question has a hidden answer that reveals on the standard Quick check interaction, tested in light and dark themes.
- The ledger finding RA6 D4 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RA6 D4) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
