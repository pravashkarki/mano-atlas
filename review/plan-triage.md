# Plan pair-review triage (2026-09-02)

Reviewers: GPT-5.6 (`review/gpt-plan-review.md`, 25 findings) and DeepSeek v4 Pro (`review/deepseek-plan-review.md`, 17 findings), both via opencode against `review/PLAN-REVIEW-PROMPT.md`. Plan under review: `review/pdf-batch-2-plan-v1.md`. Result: `review/pdf-batch-2-plan.md` (v2).

Verdict key: ACCEPT = plan v2 changed; PARTIAL = part taken; REJECT = checked and does not hold, or conflicts with a decision Pravo already made.

## Where both reviewers agreed

| # | Finding | Verdict | What v2 does |
|---|---|---|---|
| 1 | Full ERP/ACT protocol on a public page invites self-treatment; ocd.html itself says "full ERP belongs with a professional" | ACCEPT | Techniques chapter is written to the trainee ("what the counselor does in supervised sessions"), carries the curriculum tag, opens with a plain line for family readers. ERP keeps the cycle, the hierarchy idea and the response-prevention principle; no homework sheet, no "do this at home" steps. Urge surfing stays the public skill. |
| 2 | Chapter numbers are also hand-written as a `secbadge` in every content fragment (29 of them); position-derived numbering leaves stale badges | ACCEPT (verified) | Build strips authored badges and injects the number; build fails if a fragment still carries one. |
| 3 | A git-ignored intake ledger is not a durable audit trail | PARTIAL | Pravo decided (1a7958c) that docs/ and TASKS.md stay untracked. The ledger stays in `review/` and is mirrored to `~/Obsidian/Mano/sources/intake.md` in the vault, which is git-backed. Not committed to the site repo unless Pravo reverses that decision. |
| 4 | The running vignette (village student) is fine only if explicitly fictional; one long narrative risks stereotyping | ACCEPT | Card one states "a fictional composite student, not a client". The four layered skills (paraphrase, feeling, meaning, summary) keep the one thread because they build on each other; the other five use short, different situations. |
| 5 | Aversion therapy in the behavioural applications is dated and ethically contested; plan did not flag it | ACCEPT | Listed as historical, one sentence, not taught as a technique. |
| 6 | Nepali: font-garbling affects all five decks, not just the verbal one; metaphors and technical calques need Nepali-familiar equivalents; a fluent counselling-language review is still needed | ACCEPT | "Render, never extract" applies to every deck. Metaphors (quicksand, traffic light, on one hand) get a Nepali-natural equivalent, not a coin. Glossary and Nepali text keep the English term where no natural Nepali exists (house rule). Native proofread stays the gate (already an open task). |
| 7 | Returning students cannot see what changed | ACCEPT (small) | Build stamps each page with its last content change from git, and the home page gets a short "Recently added" strip fed from PAGES. Kept minimal. |
| 8 | Word budgets for the new chapters were never estimated; they could breach the ceiling on day one | ACCEPT | Budgets in v2. Life skills shrinks to a six-area map plus links (both reviewers: it duplicates existing chapters). |

## GPT-only findings

| # | Finding | Verdict | Reasoning |
|---|---|---|---|
| 9 | "Stay until anxiety falls" teaches outdated habituation; modern ERP stresses expectancy violation and tolerating uncertainty; breathing during exposure can become a safety behaviour | ACCEPT | Correct. The existing approaches.html exposure row already says "stay until anxiety falls" and gets fixed in this batch too. Techniques chapter says: stay long enough to learn the feared outcome does not follow, and that anxiety is survivable whether or not it drops. |
| 10 | ACT deck is a teaching sequence, not a validated protocol; disorder-benefit list too broad | ACCEPT | Teach the six ACT processes plus the deck's sequence as one worked illustration; benefits limited to anxiety, depression, OCD with "adjunct" wording for the rest. |
| 11 | Confidentiality limits differ by law and setting; verify against Nepal law before publishing scripts | ACCEPT | Script carries the three limits the curriculum teaches (danger to self, danger to others, abuse of a child or vulnerable person, court order), with one line that mandatory reporting in Nepal is defined in law (Act Relating to Children 2018 for children) and that the counselor follows their agency's protocol. Verify wording against ethics.html, which already covers consent. |
| 12 | Disperse techniques into anxiety / depression / OCD / tools instead of one chapter | REJECT | Disorder pages have a fixed section order and anxiety is already the longest page (2700 words). The curriculum teaches these as Module 3 techniques together. One chapter, with one cross-link line on each disorder page, keeps the disorder pages calm. DeepSeek also voted keep. |
| 13 | Process page cannot absorb scripts + assessment table + six cards; make a first-session-and-assessment chapter | ACCEPT | Budget for the expanded page came to about 1600 words with a 10-row table and four scripts on the shortest practice page. v2: process.html keeps the map and adds stages 3 to 6 (formulation, goals, evaluation, follow-up, termination, alliance). New chapter "The first sessions: what to say, what to ask" carries stage 1 scripts and the stage 2 table. |
| 14 | Curriculum-required material must not become optional in closed expanders | PARTIAL | Expanders stay closed by default (complexity is opt-in, and the table is the map a first-time reader needs). But every expander summary line carries the existing CTEVT curriculum tag, and the print stylesheet opens them. |
| 15 | Sub-grouping the sidebar by CTEVT module serves students, not family readers | ACCEPT | Growth rule changed: when the practice group needs splitting, split by reader question; the curriculum view lives on the crosswalk page. |
| 16 | Plan promises search aliases with no mechanism | REJECT (verified) | `assets/search.js` already has an `ALIASES` list; each intake adds to it. |
| 17 | Weekly renumbering invalidates printed notes and memory; slugs are the identity, numbers are positions | ACCEPT | Slugs are stable identities; numbers are reading-order positions. Printed pages carry the slug in the footer URL already. |
| 18 | 4-7-8 "physical override" claim unsupported; breath holds can cause dizziness | ACCEPT | Skill box uses gentle longer-exhale breathing (already the site's convention) with an opt-out and no promised result. |
| 19 | Mirroring "builds subconscious rapport" and touch as routine skill | ACCEPT | Mirroring claim dropped; touch stays "only if culturally safe and asked for", as skills.html says today. |
| 20 | Follow-up intervals are examples, not a schedule | ACCEPT | Worded as "for example". |
| 21 | Psychosis questions must be non-leading; not every symptom is an emergency | ACCEPT | Row says: ask plainly, then assess safety, function, substances and medical causes; urgency decides referral speed. Consistent with psychosis.html. |
| 22 | Cognitive restructuring: do not import "thoughts cause distress" or emotion drop as proof | ACCEPT | Framed as thoughts, body, behaviour and context interacting; the aim is a fairer thought, not a positive one. |
| 23 | Maslow as heuristic, not universal sequence | ACCEPT | One clause. |
| 24 | Ceiling by word count alone misses tables, scripts, Nepali length | PARTIAL | Ceiling stays at about 1800 English words as the trigger, plus "one coherent reader question per chapter" as the test. Reading time already reflects Nepali length. |
| 25 | Build should fail on authored numbers or unresolved reference tokens, duplicate slugs, missing quiz or keypoints | ACCEPT | Added to the build changes. |
| 26 | Side-by-side Nepali/English phrases conflict with the language toggle | ACCEPT | Normal en/ne pattern; English technical term in brackets inside the Nepali only where the house rule says so. |

## DeepSeek-only findings

| # | Finding | Verdict | Reasoning |
|---|---|---|---|
| 27 | Nine deep-dived skills vs the table's seventeen: say what happens to the other eight | ACCEPT | Chapter intro says the remaining eight stay in the table on the skills page. |
| 28 | basics.html teaches two distortions, the CBT expander five: reconcile | ACCEPT | basics.html gets "two of the five named on page {{page:approaches}}". |
| 29 | A fourth avoidance-loop diagram fights "one mind" | ACCEPT | No new loop figure; techniques chapter links the foundation loop and the OCD loop. |
| 30 | ACT benefit claims for PTSD and substance use passed unqualified | ACCEPT | Merged with #10. |
| 31 | "CBT = Beck and Ellis" is loose; Ellis founded REBT | ACCEPT | One clause in the CBT expander; roots.html row already says "Cognitive · Beck · Ellis", fine as the school. |
| 32 | Renumber map in v1 was off by one | ACCEPT | With derived numbering there is no hand map; v2 lists the resulting order once. |
| 33 | "Re-file, not just insert" rule | ACCEPT | Added to growth rules. |

Both PLACEMENT verdicts: non-verbal, verbal, approaches = keep. Process: GPT split, DeepSeek keep; split taken (#13). Techniques: GPT disperse, DeepSeek keep; keep taken (#12).
