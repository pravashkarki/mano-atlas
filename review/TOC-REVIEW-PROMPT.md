# Review brief: the full table of contents (draft v1)

Work only inside this repository; do not read files outside it. Do the whole review yourself in this session: do NOT spawn sub-agents or delegate tasks. You are reviewing a PLAN, not content. Nothing on the site has changed.

Read, in this order:
1. `review/toc-plan.md` (the plan under review: 86 entries in 12 parts plus Reference).
2. `review/curriculum-coverage.md` (the 2010 CTEVT PSC curriculum, task by task, and what the site covers).
3. `review/beyond-curriculum.md` (research: 65 topics a counsellor needs beyond the curriculum, priorities, rejected practices).
4. `build.py` (the PAGES list and GROUPS) and `CLAUDE.md` (house rules). Skim `content/*.html` only to check a claim about a live chapter.

Context: a free bilingual (English/Nepali) mental-health education site for CTEVT Psychosocial Counselor students, health workers and families in Nepal, plus anyone learning. Goal: cover the whole curriculum AND what a psychologist or counsellor needs beyond it. The site grows through a six-month course: instructor decks arrive about weekly; chapters are built as we go. This table of contents is the map everything is built against.

Your job: find the real problems with the table of contents. Judge, in priority order:

1. COMPLETENESS: is any curriculum task unit (see curriculum-coverage.md) left without a home? Is any CORE or IMPORTANT research topic dropped or buried? Is anything a Nepali psychosocial counsellor must know missing from both inputs?
2. READER JOURNEY: does the order make sense for a first-time reader, start to finish? Is each chapter one reader question? Where would you move, merge or split, and why? Answer the draft's five open questions directly.
3. SCOPE AND SAFETY: does any chapter push a psychosocial counsellor beyond scope (diagnosis, medicines, specialist trauma therapy) or invite self-treatment from a public page? Is the "not recommended" page the right handling of rejected practices?
4. NAVIGATION: 13 sidebar groups and 86 entries. What breaks first for a reader on a phone? Propose a concrete grouping if you would change it.
5. BUILD ORDER: which 10 new chapters should be built first, and why (marks weight, CORE priority, safety, dependency between chapters)?

House rules the plan must respect: no em-dashes anywhere; never invent Nepali prevalence figures; crimson styling only for crisis content; quizzes reassure, never judge; no client case studies; coping-skill boxes are skills, never treatment claims; complexity is opt-in; documentation is a failure state; English term in the Nepali text when no natural Nepali equivalent exists.

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `AREA (1 to 5) | entry or part (short quote) | VERDICT (DISAGREE / RISK / MISSING / AGREE-WITH-CHANGE) | your recommendation, concrete, one or two sentences`
- Most important first. Maximum 25 findings. No praise, no restating the plan.
- Then one line: `OPEN-QUESTIONS: 1=<answer> 2=<answer> 3=<answer> 4=<answer> 5=<answer>`
- Then one line: `FIRST-TEN: <slug, slug, ...>`
