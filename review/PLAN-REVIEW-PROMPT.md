# Plan review brief: PDF batch 2 placement and six-month content strategy

Work only inside this repository; do not read files outside it. You are reviewing a PLAN, not content. Nothing has been changed yet.

Read, in this order:
1. `review/pdf-batch-2-plan.md` (the plan under review).
2. `review/sources/*.txt` (text extracted from the five new instructor decks; Nepali may be garbled by font encoding, the English structure is reliable).
3. `README.md`, `build.py` (PAGES, SHELL, `link_page_refs`), and these content sources: `content/skills.html`, `content/process.html`, `content/approaches.html`, `content/tools.html`, `content/basics.html`, `content/roots.html`, `content/ocd.html`, `content/depression.html`, `content/crosswalk.html`. Skim the other `content/*.html` only to check for overlap. The root `*.html` files are generated; do not review them.

Context: a free bilingual (English/Nepali) mental-health education site for CTEVT Psychosocial Counselor students, health workers and family members. Every string exists in both languages. 30 chapters in four sidebar groups. New instructor decks will arrive about once a week for the next six months; the plan proposes where this batch goes AND three build changes so that later inserts stay cheap.

Your job: find the real problems with the plan. Judge, in priority order:

1. PLACEMENT: for each of the five decks, is the proposed home (expand vs new chapter, and which page) the one a first-time reader needs? Where would you place it differently, and why? Is anything in the decks that the plan drops or misplaces? Is anything already on the site that the plan duplicates instead of linking?
2. INFORMATION ARCHITECTURE FOR SIX MONTHS: will the proposed rules (slug cross-refs, position-derived numbering, intake ledger, 1800-word ceiling, "go deeper" expanders, sub-grouping the practice group by CTEVT module later) hold up across about 25 weekly intakes? What breaks first? What is missing (e.g. versioning, a "what changed" page for returning students, a per-module landing page, a way to mark curriculum-required vs beyond-curriculum depth)?
3. SOURCE CAUTIONS: the plan lists claims it will not import (Mehrabian 60 to 80 percent, "10 percent conscious", seating distance, Freudian typology framed as history, Little Albert ethics, Rogers six conditions, SUDS scale). Are these right? What else in the decks is wrong, dated, or unsafe to teach as fact (check the ACT, behavioural activation, ERP, life-skills steps and the process scripts)?
4. PEDAGOGY AND SAFETY: does moving ERP and ACT protocols onto a public page risk self-treatment? Is the proposed framing ("done with a trained person", skill boxes stay skills) enough? Does the Verbal-skills chapter's single running case (a student from the village alone in Kathmandu) breach the site's "no client case studies" rule, or is a fictional teaching vignette acceptable? Say which and why.
5. BILINGUAL: anything in the plan that will be hard to carry in Nepali (terminology, the phrase banks, the scripts), and how to handle it given the house rule: English term in the Nepali text when no natural Nepali equivalent exists, transliteration for everyday loans.

House rules the plan must respect: no em-dashes anywhere; never invent Nepali prevalence figures; crimson styling reserved for crisis content; quizzes reassure, never judge; no client case studies; coping-skill boxes are skills, never treatment claims; complexity is opt-in; documentation is a failure state (if a reader needs a manual, fix the page).

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `AREA (1 to 5) | what the plan says (short quote) | VERDICT (DISAGREE / RISK / MISSING / AGREE-WITH-CHANGE) | your recommendation, concrete, one or two sentences`
- Most important first. Maximum 25 findings. No praise, no restating the plan.
- Then one line: `PLACEMENT-VERDICT: <for each deck: deck short name = keep / move to X>`
- Then one line: `STRATEGY-VERDICT: <the one change to the six-month rules you would insist on>`
