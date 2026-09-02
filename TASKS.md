# Mano Atlas — task list

Working list for development sessions. Check items off (`[x]`) as they land; add new ones at the bottom of the right section. House rules for any task: see CLAUDE.md.

## Starter prompt (paste this to resume with new decks)

> Read `CLAUDE.md`, `TASKS.md` and `review/intake.md` in ~/Work/PCS, then the latest session file in `~/Obsidian/Mano/sprints/sessions/`. Pull the new decks from the Drive folder `13wT9HZxAF4a8McSyR30mZxavghwzz3uu` (they are also in ~/Downloads); extract text into `review/sources/` and render pages with the scratch venv (pymupdf) so Nepali is read from images, never from extracted text. Map each deck against the site (grep for overlap, read the neighbouring chapters), write a short placement plan in `review/`, pair-review the plan (DeepSeek v4 Pro and GPT-5.6 via opencode; GPT needs "do NOT spawn sub-agents"), get my approval, then build: place by reader question, one row per deck in `review/intake.md`, bilingual text with keypoints and quiz, cross-references as `{{page:slug}}`, `python3 build.py && sh tools/og-render.sh`, both themes in the browser, content pair review with the same two models, triage against primary sources, one commit per chapter, push, mirror `review/intake.md` and triage files to `~/Obsidian/Mano/sources/`. Decks over about 60 pages split across two weeks. Do not touch the Nepali proofread item; that is a human pass.

## Where things stand (2026-09-02, end of s02)

- Site: 33 chapters live; practice group at 15 (sub-group by reader question at about 16). Build numbers chapters by position; prose refers to chapters by slug; gates fail on hand-written numbers, unresolved references, missing quiz or keypoints, em-dashes.
- Batch 2 done and pair-reviewed (plan and content); ledger `review/intake.md`; triage `review/plan-triage.md`, `review/content-triage.md`.
- Housekeeping done: type-scale tokens, OG images, Lighthouse pass. Parked: AAA contrast mode (only if readers ask).
- Open: native Nepali proofread (chapters 19, 20, 22, 24 and the first-session scripts first); next decks from Pravo.

## Now

- [x] PDF batch 2 (2026-09-02): five Module 3 decks landed. Build refactor c2cf486 (numbers by position, slug cross-refs, gates, update stamp, Recently added); skills.html non-verbal; NEW skills-listening (19) and skills-moving (20), split from one 2042-word chapter; approaches expanders + exposure row fix; process stages 3 to 6; NEW first-sessions (22); NEW techniques (24); crosswalk, glossary, search aliases. Plan `review/pdf-batch-2-plan.md` (v2 after GPT-5.6 + DeepSeek pair review, `review/plan-triage.md`); ledger `review/intake.md` (mirrored to the vault). Checked light and dark in the browser. Content pair review done (DeepSeek 6 findings, GPT-5.6 30; ledger `review/content-triage.md`; 35 accepted, 1 rejected; Section 68 of the Act Relating to Children verified from the Law Commission text). Open from this batch: native Nepali pass on the new scripts and phrase banks; approaches (1837 words, inside closed expanders) recorded as the one ceiling exception.
- [ ] Weekly intake cadence (about 25 decks to March 2027): one deck per week, one ledger row, one commit per chapter, live the same day; decks over about 60 pages split across two weeks by stage.
- [x] Readability Tier 1 (2026-08-27): linked cross-refs, tap-to-call helplines, 19px on phones, Devanagari section numbers, help-now boxes on 6 pages, trauma reassurance first, suicide/ADHD/panic/GAD-7 splits, steadying care line + gentle note on heavy chapters
- [x] Nepali language review by DeepSeek + GPT-5.6 (brief: review/NEPALI-REVIEW-PROMPT.md); 43 accepted fixes, terminology rule added to CLAUDE.md (2026-08-27)
- [x] Triage external peer reviews: `review/deepseek-review.md` (done 2026-08-27, ledger in `review/triage.md`) and `review/chatgpt-review.md` (done 2026-08-27, same ledger) (brief: `review/PEER-REVIEW-PROMPT.md`). Verify every finding against a primary source (DSM-5, WHO, Nepali law/MoHP) before changing content; reject findings that don't hold. Keep a short accepted/rejected ledger in review/.
- [x] Mine Sub module 1, SUB module 2 New and Mental Health-3 PDFs against the site (done 2026-08-27, commit ce2cf9d: goals table, Bronfenbrenner + wellbeing elements, CB-MHPSS roadmap, APA principles + decision ladder, cognitive restructuring + ten habits, ID "before 18"). Open conflict, not changed: class notes date the first National Mental Health Policy 1997, site says 1996 (verified); notes use the old term "somatoform".

## Next

- [ ] Mano app (iOS + Android): brainstorm first. Trigger: the 2026 Nepal floods; goal is to help people affected by them. Open questions to settle before any build: who exactly (survivors, family members, relief volunteers, PSC counselors in the field), offline-first content from this atlas (PFA, help-now numbers, grounding skills, trauma page) vs. new features (helpline dialer, nearby OCMC/health post, check-in prompts), Nepali-first UI, distribution (app stores vs. PWA installed from the site), and who maintains it. Uses the logo mark in assets/mark.svg. Brief: docs/APP-BRIEF.md · stack research: docs/APP-TECH-RESEARCH.md (recommendation: Expo + expo-sqlite, no tracking modules, content JSON generated from content/).

- [x] Readability Tier 2 (2026-08-27, commits 1f1362d + 3ec2f2d): mobile drawer + 94px header, stacked card tables, symptom-led search aliases, labels expander, start-here routes, Key points on 28 pages, plain-words lines. Plan: review/readability-plan.md: mobile nav drawer + smaller sticky header; symptom-led bilingual search aliases; "Key points" box before each quick check; "start here" routes on home; tables to stacked cards under 640px; plain-words line under each definition; "what are these labels?" expander on every chapter.
- [x] Readability Tier 3 (2026-08-27): glossary chapter (30), missed quiz questions flagged next visit, on-page contents on 3+ card chapters, ≥/≈ spelled out in Nepali, print stylesheet.

- [x] Spot illustrations (2026-08-27): two people talking, a diyo, an open book with a sprig, as group headers on the home contents grid (SPOT dict in build.py). Original: Spot illustrations, one per section group, in the established flat line-art style in the established flat line-art style (thick currentColor outlines, solid hair, blank face, single teal fill; original compositions; iterate via rendered screenshots — see CLAUDE.md illustration rules). Candidates: two people talking (Counselling practice), a lantern or diyo in the dark (Disorder categories), an open book with a sprig (Reference).
- [x] Type scale as tokens (2026-09-02): --fs-11 … --fs-28 plus half steps for the Devanagari offset; 140 declarations migrated with zero computed-size change (browser-verified); metric-matched fallbacks for Literata and Archivo to cut font-swap layout shift.
- [ ] Nepali proofread by a native speaker end to end (two model passes done 2026-08-27, DeepSeek + GPT-5.6, 43 fixes, ledger in review/triage.md; a human pass is still the gate for idioms of distress).
- [x] Print stylesheet (@media print): hide sidebar/quizzes, keep helplines and sources — students will print chapters.

## Later / ideas

- [ ] More source PDFs coming from Pravo's Drive ("we will keep adding"); integrate each new one and update the crosswalk page.
- [x] Per-page OG meta, canonical, JSON-LD (WebSite, Article/LearningResource, BreadcrumbList), llms.txt. Social images done 2026-09-02: assets/og/<slug>.png generated by tools/og-render.sh (headless Chrome) from build-written sources; re-render after every intake.
- [ ] Optional AAA contrast mode (7:1) if readers ask; would darken muted text.
- [x] Sitemap.xml + robots.txt + bilingual 404 page, generated by build.py.
- [x] Lighthouse pass (2026-09-02, mobile, Lighthouse 12): accessibility, best practices and SEO 100 on home, anxiety, skills-listening, techniques. Performance: chapter pages 68 to 99; home 52 to 71 live with FCP 4.6 s under simulated mobile against a cold edge, but 100 with FCP 1.2 s served locally, so the page is not the cause. Home CLS 0.30 was font swap; metric-matched fallbacks brought it to 0.009. Not done: inlining style.css (one fewer blocking round trip) because it costs cross-page caching. Open: none blocking.

## Done (recent)

- [x] v4 reading redesign: Literata, Lucide icons, sidebar accordion, care elements (reading time, rotating dismissible closing notes)
- [x] v5 identity pass: lokta-paper grain, dhaka ribbons, bilingual nameplate, ghost numerals, category card tops
- [x] Diagrams round 2 (2026-08-27): IASC pyramid redrawn full-width with text inside the bands; OCD loop; suicide risk ladder with response tiers; conversion vs epilepsy attack timelines; stages-of-change wheel with relapse chord. Round 3 same day: counselling six-stage track, PFA Look·Listen·Link panels, GBV response timeline, Bronfenbrenner rings, psychosis positive/negative panels, child-disorder quadrant. Round 4: micro-skills ladder (skills), VCT flow (hiv). 26 diagrams on 24 chapters; remaining text-only pages are reference pages by design.
- [x] 13 SVG teaching diagrams incl. panic curve, depression spiral, window of tolerance, Yerkes-Dodson, addiction cycle
- [x] Original hero illustration (tending the mind), iterated visually
- [x] Four-agent fact-check sweep; all confirmed errors fixed (helpline 1145 correction, 1996 policy, module numbering, GBV medical windows, etc.)
- [x] Soft reading tracker; coping-skill boxes on all 10 disorder pages
- [x] Accessibility: WCAG AA contrast audit passed both themes, rem sizes with 11px floor, reduced-motion
- [x] Magazine reading scale (19px body); mobile diagrams scroll instead of shrinking
- [x] Diagnostic-code chips explained (hover + map-page note)
