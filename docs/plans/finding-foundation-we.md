# Plan: Foundation page worked example

This work exists because the foundation page presents two SVG diagrams but offers no worked example showing how the concepts apply to a real situation, leaving the reader unable to bridge the diagram to practice.

## Premise check

What exists: `foundation.html` contains two SVG diagrams illustrating core concepts of the foundation chapter. The page also has finding RA1 D1 (opening uses a section header rather than a reader question, Severity: medium), recorded in the audit ledger.

What is missing: The page relies on diagrams alone to convey its teaching points, but diagrams are not worked examples. A worked example requires a named fictional or composite person, an explicit scenario, reasoning or action shown, and an outcome stated. The audit ledger finding RA2 D3 (Severity: high, Confidence: high) records that there are two SVGs only with no worked example, and the proposed change is to add a two to three sentence composite scenario after the loop figure.

## What ships

1. Add a two to three sentence composite scenario after the loop figure on the foundation page.
2. The scenario must feature a named fictional or composite person in an explicit situation, with reasoning or action shown and an outcome stated.
3. The scenario must be clearly framed as fictional and must not present a real client case study.

## Cases and decisions

- Finding RA1 D1 (practitioner-facing opening) is a separate finding and is not addressed by this plan.
- The composite scenario is placed after the loop figure as specified in the ledger finding RA2 D3.
- Open decision: whether the worked example appears inline after the loop figure or inside a collapsible details element. The ledger proposal specifies "after the loop figure," suggesting inline placement, but a collapsible option could keep the page scannable.

## Security

The foundation page establishes core mental health concepts. The worked example must use accurate, non-stigmatizing language and must not invent prevalence figures or misrepresent psychological concepts. The composite person must be fictional and the scenario must be educational, not clinical or alarming.

## Validation

- The foundation page includes a two to three sentence composite scenario after the loop figure, with a named fictional person, explicit scenario, reasoning or action shown, and outcome stated.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The scenario meets the strict worked-example definition from the audit calibration (composite person, explicit scenario, reasoning shown, outcome stated).
- The ledger finding RA2 D3 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RA2 D3) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
