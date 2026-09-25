# Triage: curriculum page plan (crosswalk rebuild vs new page)

Plan: `review/curriculum-page-plan.md` (v1). Reviews: `gpt-curriculum-page-review.md`, `deepseek-curriculum-page-review.md` (both run 2026-09-25 via opencode). Nothing built yet.

## Decision

**Rebuild crosswalk.html in place.** Both reviewers AGREE-WITH-CHANGE on the in-place decision (the only question was presentation, covered below). The hero "PSC student?" card, every sidebar nav, sitemap and llms.txt already point at crosswalk.html; a second page splits one audience and drifts.

## Accepted actions (both reviews agree)

| # | Finding | Decision |
|---|---|---|
| 1 | No coverage percentages per module | Show hours+marks on every module row so status reads against exam weight (Module 2 = 150 marks/60 h vs Module 4 = 50 marks/73 h); never print a "% covered" figure (PARTLY hides weight). |
| 2 | Use official module totals only | The source PDF arithmetic does not reconcile (M3 320 vs 322; M4 75 vs 73). Print the official table values; do not derive totals or per-sub-module sums; footnote the numbered-inconsistencies only where a student would hit them. |
| 3 | Include the course facts a student asks about | 780 h total · 620 in-house + 160 OJT · 600 marks (Th 100 / Pr 500) · 60% pass · 90% attendance · OJT = 100 marks. Compact one-block, not a new section. |
| 4 | Reuse the existing `pill beyond` tag | No separate "beyond-curriculum" section or second taxonomy. The site already tags non-curriculum pages (hero + clipboard); keep OCD/eating/sleep/deep-dives tagged and visibly outside the module table. |
| 5 | Statuses in teaching words, not audit jargon | Use short bilingual phrases: "covered here" / "partly" / "not yet on the site"; never "COVERED / PARTLY / MISSING" (audit vocabulary; "MISSING" reads as learner failure). |
| 6 | Reuse existing Nepali module names | केस व्यवस्थापन, क्षमता विकास, परामर्श, मनोसामाजिक already in use; do not fork the terminology. |
| 7 | Course table is Module/Hours/Marks visible, sub-module hours behind an expander | Five-column table stacks badly on phone cards; complexity opt-in. |
| 8 | Two-numbering note is a footnote beside the table | One bilingual sentence: the PDF's detail pages use a different module numbering; the site follows the course-structure table. Not a separate section. |
| 9 | No pointing at the study handbook / roadmap / internal coverage doc | The rebuild exists to purge those pointers. Gaps appear honestly in the map; links go only to on-site pages. |
| 10 | Re-author keypoints and quiz (DeepSeek catch) | crosswalk is NOT in NO_QUIZ/NO_KEYPOINTS; the build fails without keypoints/crosswalk.html and quizzes/crosswalk.html. Both must be rewritten for the new content in en+ne. |

## Resolved disagreement: page order

GPT: open with the whole course, then order explanation, then coverage; insert OJT/assessment right after the course table.
DeepSeek: open with the module-to-page coverage mapping ("where am I" is the first question), demote the full course table behind it.

Resolution: lead with a compact **"You are here"** sub-module-to-page map (the coverage core), because a student arrives asking which unit they are in. Then a compact course-facts block (hours/marks/OJT/pass). The order-explanation and full course table come after, per the coverage-doc §7 note that the hours/marks table is "USEFUL as reference" but not the lead.

## Accepted structure (v2)

1. Lead: "For PSC students" intro (one short paragraph each language; everyone else skips).
2. **You are here**: module → sub-module → site page map, with "covered here / partly / not yet on the site" statuses in both languages, hours+marks on each module row.
3. Course at a glance: 780 h · 620+160 · 600 marks (Th 100 / Pr 500) · 60% pass · 90% attendance · OJT 100 marks.
4. Course table: Module / Hours / Marks (official values), sub-module hours in an expander, two-numbering footnote beside it.
5. Why the site order differs: one short bilingual paragraph (reading order vs duty framework).
6. Footer: sources (minus handbook/roadmap pointers), the not-a-diagnostic line.

Beyond-curriculum items (OCD, eating, sleep, deep-dives, techniques) stay on their existing pages with the beyond pill; none appear as module rows.

## Data guarantees

All numbers from `review/curriculum-coverage.md` section 1 (the 2026-09-11 read-only audit of curriculum.pdf). The drive-source/curriculum.pdf in the repo is a 404 stub; the real 56-page PDF lives in the Drive folder only. If the page ships the hours/marks table, the reviewer-confirmed caveats (arithmetic does not reconcile in the source for M3/M4) are handled by printing official values only.

## Blocked on

Nothing. Ready to draft once Pravo approves v2.