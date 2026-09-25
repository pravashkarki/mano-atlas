14 findings, most important first, then the two verdict lines.

```
AREA 1 | "Rebuild crosswalk.html in place (recommended) vs create a new separate page" | AGREE-WITH-CHANGE | Rebuild in place: the hero "PSC student?" card, the sidebar nav on every page, the sitemap and llms.txt all already point at crosswalk.html, and a second page splits one audience and will drift. The one flip condition: if the hours/marks course table is judged useful to a non-student reader (trainers, accreditors) as a standalone reference, give that its own reference entry; otherwise in-place wins.

AREA 3 | "for each module and sub-module, which site page(s) cover it, and a clear PARTLY / MISSING marker" | RISK | Unit-count statuses hide exam weight: Module 2 reads "mostly PARTLY" yet carries 150 marks for 60 h (the highest marks-per-hour) on a single 849-word page, while Module 4 (50 marks / 73 h) reads "mostly MISSING" but barely counts. Put hours and marks on every module row so status is read against weight, not against the number of task units.

AREA 3 | "Uses the existing curriculum-coverage.md statuses (COVERED / PARTLY / MISSING)" | RISK | Any per-module "coverage percentage" (e.g. "M1 ~67% covered") would be more misleading than silence, since PARTLY means "named, not taught" and it ignores marks weight. Show per-unit statuses or raw counts, never a single percentage.

AREA 3 | "The course in one table: the official four-module structure with hours and marks (source: curriculum-coverage.md section 1)" | RISK | That source table's arithmetic does not reconcile (M3 totals 320 vs 322; M4 75 vs 73; theory 286 vs 284). Publishing the raw numbers verbatim ships figures that do not add up; reconcile and print clean totals, or footnote the discrepancy.

AREA 2 | "1. What this page is... 2. The course in one table... 4. Coverage by module" | DISAGREE | A student arrives asking "which unit am I in / what will the exam ask", but the outline answers that fourth. Open with the module-to-page mapping (item 4) and demote the full course table, so the page leads with "you are here", not reference material.

AREA 2 | "(outline lists no OJT, pass mark, or skills-practice weight)" | MISSING | OJT (160 h, 100 marks), the 60% pass / 90% attendance bar, and that practical marks are 500 of 600 are curriculum facts a student asks about, and none appear. Add them as the compact one-line logistics note coverage-doc §7 already prescribes, not as a new section.

AREA 2 | "State clearly that the PDF uses two numberings and which one the site follows (section 10.7)" | AGREE-WITH-CHANGE | The two-numbering note only matters when a student cross-references their own printed PDF, so place it as a one-line footnote on the module table, not as a lead caveat before the reader has seen either numbering.

AREA 2 | "Its nav slots are the last 'reference' row" | RISK | Crosswalk is the second-to-last reference row (glossary follows it); harmless but wrong. The bigger risk is granularity: rebuilt at 159 task-unit level the page drowns a first-time reader; show the four modules' sub-modules mapped to pages, and push task-level detail into the ranked-gaps list.

AREA 2 | "Rebuild crosswalk.html... nothing has been changed yet" | MISSING | quizzes/crosswalk.html and keypoints/crosswalk.html are build-walled (crosswalk is not in NO_QUIZ / NO_KEYPOINTS), so the rebuild must re-author both in en and ne, or the page ships a stale Quick-check and Key-points box that no longer match its content.

AREA 4 | "5. Beyond-curriculum content: one line each for the... pages that are NOT in the curriculum" | AGREE-WITH-CHANGE | The site already carries a `pill beyond` tag and "Beyond curriculum" wording in the hero and info popover; a full new section invents a second taxonomy for the same idea. Reuse the existing pill, keep these items visibly outside the module table (they map to no module), and do not slot them into a module row the way the stale crosswalk did.

AREA 5 | "a clear PARTLY / MISSING marker" | DISAGREE | "COVERED / PARTLY / MISSING" is audit vocabulary, not teaching words; repeated in a table it becomes long metatext (against the metatext-is-short rule) and "MISSING" reads as a learner's failure. Use short bilingual phrases ("covered here" / "partly" / "not yet on the site") with the quizzes-reassure-never-judge warmth.

AREA 5 | module names carried into Nepali | MISSING | The plan is silent on Nepali module names, but translations already exist and are in use (kasgmt nav "केस व्यवस्थापन" = Case Management; "क्षमता विकास" = Capacity Building in the current crosswalk). Reuse those exact strings so the rebuilt page does not fork the terminology.

AREA 5 | "The course in one table... with hours and marks" | AGREE-WITH-CHANGE | "घण्टा र अंक" carries fine, but a five-column module + sub-module + hours + marks table stacks poorly on phone cards. Keep the visible table to Module / Hours / Marks and push the sub-module hourly breakdown behind an opt-in expander (complexity opt-in).

AREA 2 | "6. What students can do about gaps: point to... the study handbook only where it is genuinely public" | AGREE-WITH-CHANGE | Gating the private handbook is right, but the rebuild exists precisely to purge the handbook/roadmap (coverage-doc §10.1–10.2); make "gaps" link only to on-site chapters or an on-site ranked list, with no handbook or roadmap mention at all, to avoid the current stale page's core error.
```

DECISION-VERDICT: rebuild crosswalk in place, because one audience and one already-linked URL should own the curriculum view, not two pages.

PAGE-ORDER-VERDICT: open with the module-to-page coverage mapping (student's "where am I" question) and move the full course table plus order explanation down or behind an expander.
