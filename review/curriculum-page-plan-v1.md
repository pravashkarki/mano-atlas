# Curriculum page plan: rebuild the crosswalk as the PSC curriculum overview

Status: PLAN, nothing changed yet. Decision to review with DeepSeek v4 Pro and GPT-5.6, triage in `review/curriculum-page-triage.md`.

## Context

A free bilingual mental-health education site for CTEVT Psychosocial Counselor (PSC) students. The site is ordered as a **learning path** (overview → disorders → practice → reference), not as the curriculum. Students arrive with one question: "which curriculum unit am I covering, and what will the exam ask?" The page that should answer this, `content/crosswalk.html` ("For PSC students"), is stale, not a curriculum-to-page map, and points at a private study handbook not on the site. Full error list: `review/curriculum-coverage.md` section 10.

## The decision under review

**Rebuild `crosswalk.html` in place** (recommended) vs create a new separate page.

Rebuild in place because:
- It is already the "For PSC students" page (`reference` group, sidebar and home route both call it that).
- The URL is stable and already linked from hero (`PSC student?` card), nepal, rest, and search.
- Two curriculum pages would split one audience and age out of sync.
- Its nav slots are the last "reference" row; nothing depends on its internal table shape.

## Proposed page structure (outline only, content to be drafted after approval)

1. **What this page is**: one paragraph for PSC students; everyone else can skip.
2. **The course in one table**: the official four-module structure with hours and marks (source: curriculum-coverage.md section 1). State clearly that the PDF uses two numberings and which one the site follows (section 10.7).
3. **Site order vs curriculum order**: a short section that says, plainly: the site is a reading order, the curriculum is a duty framework; they differ by design; here is how to use both.
4. **Coverage by module**: for each module and sub-module, which site page(s) cover it, and a clear PARTLY / MISSING marker where the curriculum unit is not yet taught. Uses the existing curriculum-coverage.md statuses (COVERED / PARTLY / MISSING).
5. **Beyond-curriculum content**: one line each for the disorder and practice pages that are NOT in the curriculum (OCD, eating, sleep, approaches detail, techniques), so students are not confused about where they belong.
6. **What students can do about gaps**: point to the ranked gaps list (coverage doc section 9) and to the study handbook only where it is genuinely public or in-class.

## House rules the page must respect

No em-dashes; both languages for every string; no invented Nepali figures; crimson styling only for crisis content; quizzes reassure; no client case studies; complexity is opt-in; a page that needs a manual is a failure (make the page self-explanatory, not documented).

## Data assurance

The hours/marks module table and the per-unit statuses come from `review/curriculum-coverage.md`, which was built by a read-only audit of `curriculum.pdf` (Drive folder, 56 pages) on 2026-09-11. Note: `drive-source/curriculum.pdf` in this repo is a failed-download 404 stub, not the real document; the real one lives in the Drive folder only.

## Review ask

Two questions, judged in priority order:

1. **In place vs new page**: is rebuilding crosswalk.html the right call, or should the curriculum overview be its own page (new slug, own nav slot)? Consider URL stability, the hero route, search, and the risk of two pages ageing out of sync.
2. **Page design**: does the proposed outline (course table → order explanation → coverage by module → beyond-curriculum → gaps) answer a student's real questions in the right order? What is missing, what would you cut, and what would confuse a first-time reader?

House rules the review must apply: no em-dashes anywhere on the site; documentation is a failure state (page must be self-explanatory); complexity opt-in; no invented figures. The page lives within the bilingual pattern: every string exists in both `en` and `ne`.