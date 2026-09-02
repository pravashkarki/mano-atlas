# Content pair-review triage, batch 2 (2026-09-02)

Brief: `review/BATCH2-CONTENT-REVIEW-PROMPT.md`. Reviewers: DeepSeek v4 Pro (`deepseek-content-review.md`, 6 findings) and GPT-5.6 (`gpt-content-review.md`, 30 findings; the first GPT run hung for two hours in a sub-agent and was killed, rerun with sub-agents disabled, `gpt-content-review-hung.err`). Fix commits: ce3300b (DeepSeek round), next commit (GPT round).

Verdict key: ACCEPT = changed both languages; PARTIAL = part taken; REJECT = checked and does not hold or conflicts with a site rule.

## DeepSeek

| # | Finding | Verdict | Note |
|---|---|---|---|
| D1 | Glossary intro said thirty terms, table has 37 | ACCEPT | Count removed from the intro so it cannot drift again |
| D2 | Techniques pointed task 12 at process; "pros-and-cons page" had no target | ACCEPT | Now first-sessions and the brainstorming weighing step |
| D3 | Child-abuse reporting duty stated as fact | VERIFIED, kept and sharpened | Act Relating to Children 2075 (2018), Section 68(1): caregiver, teacher, health worker or any other person who learns of violence or sexual abuse against a child shall inform the nearest police office; 68(3) and (4) protect the informant. Section 50(1): any person with information about a child in need of special protection shall inform the child welfare authority. Read from the Law Commission text. Section cited on the page |
| D4 | "साक्षी-आत्म" coined | ACCEPT | English term kept |
| D5 | "ईआरपी" in Devanagari | ACCEPT | Latin ERP on techniques, keypoints and ocd |
| D6 | Iceberg aria-label did not match the drawing | ACCEPT | Label describes the drawing; caption notes the simplification (see G11) |

## GPT-5.6

| # | Finding | Verdict | Note |
|---|---|---|---|
| G1, G8, G9 | ERP ladder, delay schedule and "repeat until boring" form a self-run kit | ACCEPT | Ladder labelled one clinician-built example; delay schedule replaced by an agreed, shortened delay at the clinician's judgement; progression by learning and readiness, practice varied |
| G2 | Psychoeducation vignette rules out a medical cause | ACCEPT | Doctor's check first, in the vignette and the phrase bank |
| G3 | "Even then I would tell you first" cannot be guaranteed | ACCEPT | "wherever it is safe and lawful" |
| G4 | Danger-to-self and danger-to-others stated as automatic duties | PARTIAL | "serious danger" in the script; the precaution line already ties the limits to law, agency protocol and supervision; child duty kept (Section 68) |
| G5 | Fever or head injury with psychotic symptoms needs urgent medical assessment | ACCEPT | Same-day medical check named, delirium named |
| G6 | "OCD is not dangerous" | ACCEPT | A thought is not an action; OCD can cost skin, sleep, work and mood |
| G7 | Restructured thought could discourage hygiene | ACCEPT | Ordinary washing continues; the extra washing is the OCD |
| G10 | I-message can escalate danger at home | ACCEPT | Only where safe; violence or control means safety first, link to GBV |
| G11 | Iceberg: ego and superego both reach the unconscious | ACCEPT | Caption sentence; the drawing stays as the classroom simplification |
| G12 | Electra complex is Jung's term | ACCEPT | Attributed |
| G13 | Fixed-interval example wrong | ACCEPT | Checking the post as delivery time nears |
| G14, G16, G17, G18 | "feared outcome does not follow" is too absolute | ACCEPT | "less likely or more bearable than predicted, and the not-knowing can be carried" on approaches, techniques, keypoints, glossary; ocd urge-surfing no longer promises the wave falls |
| G15 | Generic exposure framing for PTSD | ACCEPT | PTSD only as trauma-focused therapy by a trained provider |
| G19 | "SUDS anchors every exposure" | ACCEPT | Optional, when it helps (pre-existing line) |
| G20 | Process table and track diagram used different stage names | ACCEPT | Diagram relabelled Formulate, Plan, Intervene, Close with matching sub-labels (pre-existing) |
| G21 | "You cannot change predisposing factors" | ACCEPT | History cannot be changed; its present effects can (pre-existing caption) |
| G22 | "Filed under a code number, never a name" not in the deck | REJECT | It is the site's case-management rule from Module 2 (casemgmt.html) and stays consistent across pages |
| G23 | "Fixed beliefs others call strange" pathologises culture | ACCEPT | Not shared by family or faith, held against evidence, causing distress or harm |
| G24 | Keypoint "its four limits" | ACCEPT | Limits set by law and agency |
| G25 | ACT evidence for OCD overstated | ACCEPT | ERP first-line, ACT an addition |
| G26 | "यहाँ कसैले जाँच्दैन" means nobody checks | ACCEPT | दोष लगाउँदैन वा फैसला गर्दैन |
| G27 | Duplicated glossary phrase | ACCEPT | Introduced by the D1 fix; removed |
| G28 | "रुन्चे स्वरमा" can belittle | ACCEPT | रुन लागेजस्तो स्वरमा |
| G29 | तिमी inside a quoted mistake | ACCEPT | तपाईं; the arrogance is in the content, not the pronoun |
| G30 | Crosswalk Nepali row missing GBV | ACCEPT | Pre-existing parity gap |

Open after both rounds: the native Nepali proofread remains the gate for idioms; ERP, ACT and the first-session scripts are the pages to send first.
