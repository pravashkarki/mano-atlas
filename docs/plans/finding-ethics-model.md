# Plan: Ethics quiz model reasoning

This work exists because the ethics page asks the reader to resolve four ethical dilemmas but offers no model reasoning, so the reader cannot check whether their ethical analysis follows the correct reasoning process.

## Premise check

What exists: `ethics.html` presents ethical dilemmas relevant to mental health practice in Nepal. The page has findings RD1 D2 (self-care paragraph too long, Severity: medium, shared key: long-para) and RD2 D2 (confidentiality ladder paragraph too long, Severity: medium, shared key: long-para), recorded in the audit ledger.

What is missing: The quiz asks the reader to work through four ethical dilemmas but provides no model answer or model reasoning. The reader cannot confirm whether their ethical analysis is sound. The audit ledger finding RD3 D3 (Severity: high, Confidence: medium) records that the quiz asks four ethical dilemmas but offers no model answer, and the proposed change is to add a composite scenario with model reasoning.

## What ships

1. Add a composite scenario to the ethics page that presents one or more of the quiz dilemmas with full model reasoning shown step by step.
2. The model reasoning must show the ethical framework applied, the reasoning steps, and the conclusion reached, so the reader can compare their own analysis.
3. Where possible, the model reasoning should reference the ethical standards relevant to Nepal mental health practice, consistent with the page content.

## Cases and decisions

- Findings RD1 D2 and RD2 D2 are separate findings handled by the shared long-para root-cause finding and are not addressed by this plan.
- The composite scenario must not present a real client case; it must use a fictional composite situation.
- Open decision: whether all four dilemmas receive model reasoning or whether one or two representative dilemmas receive full model reasoning and the others are left as practice prompts. The ledger proposes a composite scenario with model reasoning, which suggests a representative set rather than all four.

## Security

Ethical dilemmas in mental health carry real stakes for clients. The model reasoning must not suggest actions that would violate confidentiality, create dual relationships, or breach Nepal's ethical codes. The reasoning must align with the ACA ethical standards referenced on the page and Nepal-specific legal obligations. No fictional scenario should imply that a real practitioner made a specific ethical error.

## Validation

- The ethics page includes a composite scenario with model reasoning showing the ethical framework, reasoning steps, and conclusion.
- `python3 build.py` runs clean with no gate failures.
- Grep for em-dashes across content/, keypoints/, quizzes/ returns nothing.
- The model reasoning aligns with ACA ethical standards and Nepal legal obligations as presented in the source content.
- The ledger finding RD3 D3 is marked as addressed in this plan.

## Rollout

Accepted findings from the audit ledger become board cards through the existing process. This finding (RD3 D3) becomes an individual board card, is pair-reviewed, and is built on the dev branch before merging to main. The change ships through the standard content edit and rebuild cycle: edit the source, run `python3 build.py`, verify on the dev preview, then merge to main per the go-live process.

---
PLN, 2026-09-25
