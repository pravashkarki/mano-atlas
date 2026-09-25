# Curriculum page plan: rebuild the crosswalk as the PSC curriculum overview

Status: PLAN v2, approved via pair review (DeepSeek v4 Pro + GPT-5.6, 2026-09-25). Reviews: `gpt-curriculum-page-review.md`, `deepseek-curriculum-page-review.md`; decisions in `review/curriculum-page-triage.md`. v1 archived as `curriculum-page-plan-v1.md`. Nothing changed yet.

## Decision (pair-reviewed)

**Rebuild `crosswalk.html` in place.** Both reviewers confirmed: the crosswalk is already the single "For PSC students" entry point (hero card, sidebar, sitemap, llms.txt); two curriculum pages split one audience and drift.

## Page structure (v2, after triage)

1. **Lead**: one short "For PSC students" paragraph each language; everyone else can skip.
2. **You are here**: module → sub-module → site-page map. Statuses are short bilingual phrases, not audit jargon: "covered here" / "partly" / "not yet on the site". Hours and marks sit on every module row so status reads against exam weight (Module 2 = 150 marks / 60 h; Module 4 = 50 marks / 73 h). No coverage percentages, ever.
3. **Course at a glance**: 780 h total · 620 in-house + 160 OJT · 600 marks (Th 100 / Pr 500) · 60% pass · 90% attendance · OJT 100 marks. One compact block, not a section.
4. **Course table**: Module / Hours / Marks using only the official values (the source PDF's arithmetic does not reconcile for Modules 3 and 4; print official totals, never derived sums). Sub-module hours live in an expander. The PDF's two-numbering note is a one-line bilingual footnote beside this table, stating the site follows the course-structure numbering.
5. **Why the site order differs**: one short bilingual paragraph (the site is a reading order; the curriculum is a duty framework; they differ by design).
6. **Footer**: sources (no handbook or roadmap pointers), the not-a-diagnostic line.

Beyond-curriculum pages (OCD, eating, sleep, deep-dives, techniques) stay on their own pages with the existing beyond pill; none appear as module rows and there is no separate beyond-curriculum section.

## Scope notes

- **Keypoints and quiz are in scope** (DeepSeek catch): crosswalk is not in NO_QUIZ/NO_KEYPOINTS, so `keypoints/crosswalk.html` and `quizzes/crosswalk.html` must be re-authored in en+ne to match the new page, or the build fails.
- **Nepali terminology reuses what exists**: केस व्यवस्थापन, क्षमता विकास, परामर्श, मनोसामाजिक; no forked module names.
- **No links to the private study handbook, roadmap, or the internal coverage doc.** Gaps appear honestly in the map; links go only to on-site pages.

## House rules the page must respect

No em-dashes; both languages for every string; no invented figures; crimson only for crisis; quizzes reassure; no client case studies; complexity opt-in; the page must be self-explanatory (documentation is a failure state).

## Data assurance

Hours/marks and all statuses come from `review/curriculum-coverage.md` (read-only audit of curriculum.pdf, 56 pages, Drive folder, checked 2026-09-11). Note: `drive-source/curriculum.pdf` in this repo is a failed-download 404 stub; the real document lives in the Drive folder only.

## Build steps after approval

1. Draft `content/crosswalk.html` (en+ne) with the structure above, using `{{page:slug}}` cross-references and the existing group/pill vocabulary.
2. Re-author `keypoints/crosswalk.html` and `quizzes/crosswalk.html` (en+ne).
3. `python3 build.py` clean; no em-dashes; both themes in the browser.
4. Commit to dev, push, preview check, one card comment.