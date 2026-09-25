# Content review brief: rebuilt crosswalk page

You are a content reviewer for Mano Atlas (manoatlas.com), a free bilingual English/Nepali mental-health education site built for CTEVT PSC students. You have never seen this page before. Review it independently and cold.

## What to review

The page `content/crosswalk.html` and its companion `keypoints/crosswalk.html` and `quizzes/crosswalk.html` were just rebuilt (dev commit b6f0876) to turn the old crosswalk into a real PSC curriculum map, per `review/curriculum-page-plan.md` (the approved plan, read it first).

## Your job

1. Read `review/curriculum-page-plan.md` and check the built page against the approved structure: lead, "You are here" module map, course-at-a-glance, course table with hours/marks, why the order differs, sources footer.
2. Fact-check every number and status in the page against `review/curriculum-coverage.md` (the read-only audit of the real curriculum PDF).
3. Check the page's house rules:
   - No em-dashes anywhere.
   - Every user-visible string exists in both English (`class="en"`) and Nepali (`class="ne"`). Tables use the site convention: one `.data en` table and one `.data ne` table.
   - No invented figures (especially no invented Nepali prevalence numbers).
   - Statuses are teaching words ("covered here" / "partly" / "not yet on the site"), never percentages, never audit jargon.
   - Module hours/marks are the official values only; never present derived sums as official.
   - No links to a private handbook, a roadmap, or internal docs. Links go only to on-site pages.
   - No coverage percentages, ever.
   - The OJT/course numbers match the audit (780 h = 620 in-house + 160 OJT; 600 marks Th 100 / Pr 500; pass 60%, attendance 90%, OJT 100 marks).
   - Quiz questions are warm and reassuring, never judging; each has one clearly correct option and a `data-a` matching it.
4. Write your findings to a NEW file `review/<your-name>-crosswalk-content-review.md` in this repo. Lead with a verdict sentence (AGREE / AGREE-WITH-CHANGE / DISAGREE), then a numbered list: each line = finding, severity (must-fix / should-fix / nit), the file and line, and the suggested fix. Quote the exact text you mean.

## Rules for you

- Do NOT spawn sub-agents; work directly.
- Do NOT edit any build/HTML/source file. Write only your review file.
- Do NOT use em-dashes anywhere in your review file (house rule).
- Be specific and concrete. If you cannot verify a number, say so and mark it unverified rather than guessing.
- Run `python3 build.py` once if useful to confirm the page builds; never commit anything.

Return a one-paragraph summary of your verdict and the count of must-fix / should-fix / nit findings.