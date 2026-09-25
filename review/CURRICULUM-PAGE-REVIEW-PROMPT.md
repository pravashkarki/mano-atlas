# Review brief: curriculum page decision (crosswalk rebuild vs new page)

Work only inside this repository. You are reviewing a PLAN and a page-decisions question. Nothing has been changed yet. The site is currently mid-change (English-first build landed on dev; do not treat the English-only output as the design baseline — the bilingual pattern is still the house rule this page must satisfy).

Read, in this order:
1. `review/curriculum-page-plan.md` (the plan under review; the DECISION is in section "The decision under review").
2. `review/curriculum-coverage.md` (the audit that is the data source; pay attention to the module/hours/marks table in section 1, section 7 "hours/marks table" recommendation, and section 10 "Crosswalk errors").
3. `content/crosswalk.html` (the current page this plan wants to rebuild in place).
4. `build.py` (only the PAGES list and how groups/nav are produced; the root `*.html` are generated, do not review them).
5. `content/hero.html` and `content/nepal.html` and `content/rest.html` (where crosswalk is linked from).

Context: a free bilingual (English/Nepali) mental-health education site for CTEVT Psychosocial Counselor (PSC) students. The site's sidebar order is a READING order (overview → disorders → practice → reference). The CTEVT curriculum is a DUTY framework (Module 1 Psychosocial Intervention → 2 Case Management → 3 Counseling Skill and Process → 4 Capacity Building). They deliberately differ; students are confused because the one page that should explain the relationship, crosswalk, is stale and not a real curriculum-to-page map.

Your job: find the real problems with the plan. Judge, in priority order:

1. DECISION — IN PLACE VS NEW PAGE. The plan recommends rebuilding `crosswalk.html` in place (same slug, same reference-group nav slot) rather than a new separate page. Is that right? Consider: the hero "PSC student?" card and nepal/rest links; URL stability for students who bookmark it; the risk that a second page ages out of sync with the first; whether "curriculum overview" deserves its own nav entry. Give a firm verdict with the reasoning, and the one condition under which you would flip the decision.
2. PAGE ORDER. Does the proposed outline (course table → order explanation → coverage by module → beyond-curriculum → gaps) answer a PSC student's real questions in the right sequence? What opens first for a student: "where am I in the curriculum" or "what does the curriculum look like as a whole"? What is missing (e.g. OJT, pass marks, the two-numbering note placement, exam weight of skills practice), what would you cut, and what would confuse a first-time reader?
3. DATA TRUTH. The hours/marks numbers and COVERED/PARTLY/MISSING statuses come from `review/curriculum-coverage.md`. Sanity-check them against each other (Module 2 carries 150 marks for 60 h; Module 4 carries 50 marks/73 h). Flag anything in the plan's outline that would present these numbers misleadingly (e.g. per-module "coverage" percentages that ignore marks weight).
4. BEYOND-CURRICULUM. The plan says the page must label which site pages are NOT in the curriculum (OCD, eating, sleep, deep-dives) so students are not confused. Is a "beyond-curriculum" section the right mechanism, or does it create a second taxonomy? Would a per-module table with a "beyond curriculum" marker per row be cleaner?
5. BILINGUAL + HOUSE RULES. Anything in the outlined page that is hard to carry in Nepali: module names, the terms "hours and marks", COVERED/PARTLY/MISSING labels, the two-numberings note. Keep the house rule: English term in the Nepali text when no natural Nepali equivalent; transliteration for everyday loans. Note the site-wide rule that metatext (badges, section labels) is short.

House rules the plan must respect (flag any violation): no em-dashes anywhere; never invent Nepali prevalence figures; crimson styling reserved for crisis content; quizzes reassure, never judge; no client case studies; complexity is opt-in; documentation is a failure state — this page must be self-explanatory, not documented.

Do the whole review yourself in this session: do NOT spawn sub-agents or delegate tasks.

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `AREA (1 to 5) | what the plan says (short quote) | VERDICT (DISAGREE / RISK / MISSING / AGREE-WITH-CHANGE) | your recommendation, concrete, one or two sentences`
- Most important first. Maximum 15 findings. No praise, no restating the plan.
- Then one line: `DECISION-VERDICT: <rebuild crosswalk in place / new separate page> <one-clause reason>`
- Then one line: `PAGE-ORDER-VERDICT: <the one change to the proposed outline you would insist on>`