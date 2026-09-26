# Plan: Case management referral letter model answer

This work exists because the casemgmt page asks the reader to draft a three-line referral letter but offers no model answer, which blocks the core learning task of producing a correct referral letter.

## Premise check

What exists: `casemgmt.html` contains a quiz question asking the reader to draft a three-line referral letter. The page has the shared missing-nav finding (empty `.pagetools`) and two long-para findings (RD1 D2, RD2 D2), all recorded in the audit ledger.

What is missing: The quiz prompt is a request without a demonstration. The reader cannot perform a referral letter because no worked example or model answer exists on the page. The audit ledger finding RD3 D3 (Severity: high, Confidence: medium) records that there is no composite scenario and the quiz asks for a referral letter with no model answer. The proposed change is to add a composite scenario with a 3-line referral letter.

## What ships

1. Add a composite scenario (a named fictional person and situation) to the casemgmt page, placed before the quiz that asks for a referral letter.
2. Add a model three-line referral letter as the worked example, showing the correct format and content.
3. The composite scenario and model answer together give the reader a concrete template to imitate when answering the quiz prompt.

## Cases and decisions

- The casemgmt page has two shared long-para findings (RD1 D2, RD2 D2) at Severity: medium. Those are separate findings handled by the shared long-para root-cause finding and are not addressed by this plan.
- The referral letter model must use a fictional composite person, never a real client case study.
- Open decision: whether the composite scenario should be a full paragraph context or a brief setup of two to three sentences, and whether the model letter should be inside a collapsible element or shown inline.

## Security

Content-risk is the primary concern: a referral letter is a professional document, and the model answer must reflect accurate referral practice consistent with Nepal's mental health system. No fabricated institutional addresses or phone numbers are introduced. The composite person must be clearly fictional.

## Validation

- The casemgmt page includes a composite scenario and a model three-line referral letter before the quiz prompt.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The model answer matches the standard format of a referral letter and is verified against real Nepal mental health referral practice.
- The ledger finding RD3 D3 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RD3 D3) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
