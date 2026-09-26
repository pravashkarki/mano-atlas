# Plan: PFA quiz model answer

This work exists because the pfa page asks the reader to write five PFA sentences but offers no model answer, leaving the reader unable to confirm whether their sentences follow the correct approach.

## Premise check

What exists: `pfa.html` contains a quiz that asks for five PFA (Psychological First Aid) sentences. The page also has finding RD1 D2 (a paragraph too long at roughly 80 words, Severity: medium, shared key: long-para), recorded in the audit ledger.

What is missing: The quiz prompt asks for output but provides no example of the correct form. The reader cannot check their five sentences against a model. The audit ledger finding RD2 D3 (Severity: high, Confidence: medium) records that the quiz asks for five PFA sentences but offers no model answer, and the proposed change is to add a collapsible model answer with verb-marking.

## What ships

1. Add a collapsible model answer section to the pfa page quiz area.
2. The model answer must show five correctly-formed PFA sentences, each with verb-marking so the reader can see which action verbs are used and why.
3. The collapsible element keeps the page clean by default and reveals the model only when the reader chooses to check their work.

## Cases and decisions

- Finding RD1 D2 (long-para on the PFA page) is a separate finding handled by the shared long-para root-cause finding and is not addressed by this plan.
- The verb-marking approach is the specific proposal in the ledger; it means each sentence in the model answer is annotated to show the action verb, giving the reader a clear pattern to imitate.
- Open decision: whether the collapsible element uses the existing `<details>` pattern already used elsewhere on the site or a new component specific to this page type.

## Security

PFA is crisis-response content, and the model answer must use accurate, non-harmful language consistent with WHO PFA guidelines. No step in the model answer should imply a technique that could cause harm if applied incorrectly. The sentences must not invent crisis protocols.

## Validation

- The pfa quiz includes a collapsible model answer showing five PFA sentences with verb-marking.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The model answer sentences are verified against WHO PFA guidelines and the existing source content.
- The ledger finding RD2 D3 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RD2 D3) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
