# Plan: Nepal cultural concepts worked example

This work exists because the nepal page asks quiz scenario questions about cultural concepts but provides no model answer, so the reader cannot verify their understanding of how cultural framing applies in practice.

## Premise check

What exists: `nepal.html` covers Nepal-specific cultural concepts relevant to mental health. The page has three findings in the audit ledger: RD1 D2 (healing-systems paragraph too long, Severity: medium), RD2 D2 (dense clinical neighbour table cells, Severity: medium), and RD3 D3 (no composite scenario for cultural concepts, Severity: high).

What is missing: The quiz asks scenario questions about cultural concepts but offers no model answer. The reader cannot see how cultural concepts apply to a real situation. The audit ledger finding RD3 D3 (Severity: high, Confidence: medium) records that there is no composite scenario for cultural concepts and proposes adding a composite scenario where a client uses local expressions to describe their distress.

## What ships

1. Add a composite scenario to the nepal page that illustrates a cultural concept in a realistic clinical situation, using a client who describes distress in locally recognized terms alongside an English explanation.
2. Add a model answer to the quiz scenario questions so the reader can check their response against a concrete example.
3. The composite scenario must demonstrate the cultural concept with reasoning shown and an outcome stated, meeting the strict worked-example definition from the audit calibration.

## Cases and decisions

- The two shared long-para finding RD1 D2 and the dense-table finding RD2 D2 are separate findings and are not addressed by this plan.
- The scenario uses local terms as they appear in the source content, keeping the existing convention of transliteration for everyday spoken terms alongside the English explanation.
- Open decision: whether the composite scenario should appear inside a details expander or inline on the page, and whether the model answer should be a separate section or embedded in the quiz itself.

## Security

The scenario must not invent Nepal-specific prevalence figures or misrepresent cultural practices. All terms and situations must be grounded in verified source content. The composite person is clearly fictional and must not be confused with a real client case study.

## Validation

- The nepal page includes a composite scenario with a named fictional person, an explicit cultural situation, reasoning shown, and an outcome stated.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The quiz scenario questions now have model answers that the reader can compare against.
- The ledger finding RD3 D3 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RD3 D3) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
