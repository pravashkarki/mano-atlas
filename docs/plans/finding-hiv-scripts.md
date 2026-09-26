# Plan: HIV pre and post-test counselling scripts

This work exists because the hiv page has no composite scenario for pre and post-test counselling, so the reader cannot see how the counselling process unfolds in a real situation or practice the conversation steps.

## Premise check

What exists: `hiv.html` covers HIV testing and counselling in Nepal. The page has findings RD1 D2 (VCT paragraph too long, Severity: medium, shared key: long-para) and RD2 D2 (Nepal context paragraph too long, Severity: medium, shared key: long-para), recorded in the audit ledger.

What is missing: The page has no composite scenario showing a pre or post-test counselling interaction. The quiz asks the reader to perform counselling steps but offers no model showing how those steps sound in practice. The audit ledger finding RD3 D3 (Severity: high, Confidence: medium) records that there is no composite scenario for pre and post-test counselling, and the proposed change is to add composite pre/post-test scripts with reasoning and outcome.

## What ships

1. Add a composite scenario to the hiv page showing a pre-test counselling conversation between a counsellor and a client.
2. Add a composite scenario showing a post-test counselling conversation, with reasoning shown for each step and an outcome stated.
3. The scripts must demonstrate the counselling process step by step, not just list the steps in abstract form.

## Cases and decisions

- Findings RD1 D2 and RD2 D2 are separate findings handled by the shared long-para root-cause finding and are not addressed by this plan.
- The scripts must use a fictional composite person and a realistic Nepal healthcare setting, consistent with the existing content on the page.
- Open decision: whether the scripts are shown inline on the page or behind a collapsible element such as an accordion or details block, and whether both pre and post-test scripts are in one section or two.

## Security

HIV counselling carries specific safety obligations. The scripts must not imply that testing is mandatory or stigmatizing, must include the option of informed consent, and must not invent test result scenarios that could cause distress. The scripts must be consistent with Nepal national HIV guidelines and WHO counselling standards. No prevalence figures are invented.

## Validation

- The hiv page includes composite pre and post-test counselling scripts with reasoning shown for each step and an outcome stated.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The scripts are verified against Nepal national HIV testing guidelines and WHO counselling standards.
- The ledger finding RD3 D3 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RD3 D3) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
