# Plan: GBV quiz model answer

This work exists because the gbv page asks the reader to name four forms of gender-based violence but offers no model answer, so the reader cannot confirm whether their list is complete or correct.

## Premise check

What exists: `gbv.html` contains a quiz question asking the reader to name four forms of GBV. The page also has findings RD1 D2 (core distinctions paragraph too long, Severity: medium, shared key: long-para) and RD2 D2 (Nepal context paragraph too long, Severity: medium, shared key: long-para), recorded in the audit ledger.

What is missing: The quiz asks for a list of four GBV forms but provides no way to verify the answer. The reader cannot check whether they have identified the correct forms. The audit ledger finding RD3 D3 (Severity: high, Confidence: medium) records that the quiz asks to name four GBV forms but offers no model answer, and the proposed change is to add a model answer mapping the four forms.

## What ships

1. Add a model answer to the gbv quiz that explicitly maps the four forms of gender-based violence.
2. The model answer should show each form with a brief definition or example, so the reader can see not only the correct names but also what distinguishes each form.
3. The model answer should follow the standard format used by other model answers on the site, keeping it consistent with the existing pattern.

## Cases and decisions

- Findings RD1 D2 and RD2 D2 are separate findings handled by the shared long-para root-cause finding and are not addressed by this plan.
- The four GBV forms must be grounded in the content already presented on the page and in verified WHO and Nepal-specific sources.
- Open decision: whether the model answer is shown inline or behind a collapsible element, and whether it includes Nepal-specific GBV prevalence data (which would require verification and is currently out of scope per the no-invented-prevalence rule).

## Security

GBV is sensitive content. The model answer must be factually accurate and must not re-traumatize the reader. The four forms must be clearly defined without graphic detail. No prevalence figures are invented for Nepal. The answer must align with WHO and Nepal legal definitions of gender-based violence.

## Validation

- The gbv quiz includes a model answer that maps the four GBV forms with brief definitions or examples.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The model answer forms are verified against WHO and Nepal legal sources.
- The ledger finding RD3 D3 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RD3 D3) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
