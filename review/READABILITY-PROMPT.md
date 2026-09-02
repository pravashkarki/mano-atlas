# Readability and learnability review: Mano Atlas (pcs.pravashkarki.com)

Work only inside this repository; do not read files outside it. Read README.md, then content/*.html, quizzes/*.html, build.py (SHELL template, PAGES, CARELINES) and assets/style.css. The root *.html files are generated; you may open one (e.g. anxiety.html) to see the final page shell (sidebar, pager, quick check, resources, footer).

The site is a free bilingual (English/Nepali) mental-health education site for CTEVT Psychosocial Counselor students, community health workers, and family members of people who are unwell. Body text 19px Literata; Nepali in Mukta. Every string exists in both languages. Pages: 29 chapters in four groups. Each disorder page follows a fixed order: definition, DSM-5 criteria, international, Nepal, diagram, "a skill to try", quick check, learn more.

Your job: propose changes that would make the site EASIER TO READ AND UNDERSTAND for a first-time learner, especially one reading on a phone in Nepali with no clinical background. Judge the actual text and structure, not hypotheticals. Consider:

1. TEXT DENSITY: paragraphs or table cells that pack too many ideas; sentences over ~30 words; lists of 8+ items with no grouping; where a summary line, a bolded lead, or a split would help.
2. PROGRESSION: does each page open with the one idea a beginner needs first? Is jargon defined before it is used? Are cross-references ("page 03") usable on a phone? Is there an on-ramp for non-students (the two curriculum tags, DSM-5 codes, ICD codes, ACA section numbers)?
3. RETENTION AIDS: what is missing that helps a student remember: a "key points" box, a glossary, worked mini-examples, mnemonics, a per-page "one thing to try", a printable summary, spaced review of the quick-check questions.
4. NAVIGATION & FINDABILITY: sidebar of 29 items, the search, the pager, the home grid; what a reader looking for "my son will not go to school" or "my wife cries every day" would need that is not there.
5. NEPALI READER: anything about the Nepali layout, line length, term glosses (English term in brackets), digits, or register that costs a Nepali-first reader effort.
6. TABLES ON PHONES: which tables would read better as stacked cards or short lists.
7. TONE FOR A WORRIED FAMILY MEMBER: where clinical detail should be preceded by a plain-language reassurance or a "when to seek help now" line.

House rules for any suggestion: no em-dashes; nothing ships in one language; crimson colour is reserved for crisis content; quizzes reassure, never judge; complexity is opt-in (advanced detail layered on top of a simple default, never the default).

OUTPUT FORMAT, exactly this, nothing else:
- One line per suggestion: `AREA (one of the 7 above) | FILE or "site-wide" | the problem in one sentence with a short quoted example | the concrete change | EFFORT (S/M/L) | IMPACT (1-5)`
- Highest impact first. Maximum 30 suggestions. Do not praise. Do not restate the house rules. Do not propose changing the fact content.
