# Mano Atlas (मनो एट्लास) — project memory

Free, open, bilingual (English/नेपाली) mental-health education site. LIVE at https://pcs.pravashkarki.com — Vercel project `mano-atlas` (LastDoor team) auto-deploys from GitHub `pravashkarki/mano-atlas` main on every push (~30s). Born from the CTEVT Psychosocial Counselor (PSC) course; written for anyone learning. Owner: Pravo (the public site contact is the address split across email_user / email_domain in build.py; it is obfuscated in HTML and never written in plain text anywhere in the repo).

## Architecture (zero-framework, stdlib Python build)

```
content/     one HTML fragment per chapter = the teaching text (EDIT THESE)
quizzes/     one file per page: the three Quick-check questions
keypoints/   one file per page: the three "Key points" bullets shown before the Quick check
assets/      style.css, lang.js, search.js, search-index.js (generated)
build.py     SITE config + PAGES list + SHELL template → generates the root *.html
*.html       GENERATED — never edit by hand, always edit content/ and rebuild
review/      local working files, git-ignored, never pushed
```

After ANY edit: `python3 build.py` then commit. The build regenerates all pages, the sidebar accordion, home contents grid, pagers, reading times, care notes, res-type icons, the search index, the per-page "updated" stamp (from git) and the home "Recently added" strip.

Add a chapter: create `content/<name>.html` (with an EMPTY `<span class="secbadge neutral"></span>`), `keypoints/<name>.html`, `quizzes/<name>.html`, add one row to `PAGES` in build.py at the reading-order position, rebuild. Chapter numbers are NOT stored anywhere: the build numbers by position (since 2026-09-02, commit c2cf486). Slugs are the stable identity; numbers are reading-order positions.

Cross-references in prose are written by slug, never by number: `{{page:tools}}`, `{{section:foundation}}`, `{{पृष्ठ:tools}}`, `{{खण्ड:foundation}}`; `{{n:slug}}` / `{{न:slug}}` give a bare number; `{{n:last:practice}}` the last chapter of a group. The build resolves and links them. Build GATES fail on: a hand-written chapter number ("page 20", a digit in a secbadge), an unresolved token, a duplicate slug, a page without quiz or keypoints (allowlist NO_QUIZ / NO_KEYPOINTS), an em-dash in content/, quizzes/ or keypoints/.

Opt-in depth: `<details class="deeper"><summary><!--ICON:chev--><span class="en">Go deeper: …</span><span class="ne">…</span>[CTEVT pill]</summary><div class="deeper-body">…</div></details>`; closed by default, the summary carries the curriculum tag, print opens them.

Source intake: every instructor deck gets a row in `review/intake.md` (landing, dropped claims, conflicts) mirrored to `~/Obsidian/Mano/sources/intake.md`. A claim rejected once is not re-imported from a later deck. Growth rules: about 1800 English words and one reader question per chapter, then split; new chapters go where a first-time reader needs them; re-file shipped pages when a new intake changes where something belongs; when the practice group needs splitting, split by reader question (the curriculum view is the crosswalk page).

## Bilingual pattern (never break this)

Every user-visible string exists twice: `class="en"` and `class="ne"` (Nepali). CSS on `html[data-lang]` shows one. This includes text INSIDE SVG diagrams (`<text class="en">`/`<text class="ne">`). Nothing ships in one language. Nepali gets slightly larger sizes / taller line-height (Mukta renders smaller than Latin at equal nominal size).

## House style rules (Pravo-set, strict)

- NO em-dashes anywhere, ever (use colon, comma, semicolon, or parentheses).
- No client case studies on the public site.
- Resource links only when verified to exist; otherwise cite by title only. No TikTok links (unverifiable).
- Never invent Nepali prevalence figures.
- Nepali terminology (Pravo, 2026-08-27): when a clinical or technical term has no natural Nepali equivalent, use the English term in the Nepali text too; do not coin Sanskritised Nepali. Keep the site's existing convention: Devanagari transliteration for everyday spoken loans (ओसीडी, डिप्रेसन, थेरापी), Latin script for codes, acronyms and formulas (DSM-5, F42, U=U, PTSD when quoted as a code).
- Crimson/--crisis colors are reserved strictly for crisis content; the calm teal --accent for everything else.
- Quizzes reassure, never judge: no scores, warm explain-why feedback.
- Soft humanistic reader voice; care elements (reading time, rotating closing notes) are dismissible.
- Fixed page order on disorder pages: definition → DSM-5 criteria → international → Nepal → diagram → "A skill to try" box → Quick check → Learn more.
- Coping-skill boxes are skills, never treatment claims (no body-scan on eating page; family-routine advice, not meditation, on psychosis page).
- Font sizes come from the type-scale tokens on :root in style.css (`--fs-11` … `--fs-28`, named by px at the 16px root; half steps like `--fs-13h` are the Devanagari offset, one half step up for a Nepali override). Never write a literal rem font-size; body is `--fs-19`, UI chrome 11 to 15, nothing below `--fs-11`. Literata and Archivo have metric-matched local fallbacks (`Literata-fb`, `Archivo-fb`) in every stack; keep them when adding a stack.
- Social images: `assets/og/<slug>.png` are generated. After any PAGES or title change run `python3 build.py && sh tools/og-render.sh` (needs Chrome, online) and commit the PNGs; this is part of the intake checklist. Contrast must hold WCAG AA in BOTH themes (light + dark; three-state theming: bare :root light, media-query dark guarded :not([data-theme="light"]), explicit [data-theme="dark"]).
- Diagrams: real bilingual SVG text (never outline it); on mobile figures keep 600px width and scroll inside the card.
- Illustrations: flat line-art style, thick ink outlines (currentColor), solid dark hair, blank faces, single teal accent fill (var(--accent)), whites as var(--bg). Original compositions, don't copy references. Iterate by rendering screenshots, never ship blind-drawn SVG.
- Icons: Lucide inline SVGs from the ICON dict in build.py.
- Spot illustrations (home contents group headers) live in the SPOT dict in build.py; keypoints/ holds the per-page Key points bullets; diagrams are inline <figure> SVGs in content/.
- Diagnostic code chips (e.g. 296.2x · F32) get their hover title automatically at build.

## Content truth status

All 29 pages fact-checked (Aug 2026) against DSM-5, WHO, and Nepali sources by four independent review agents; confirmed errors fixed. Key facts that were verified and must not regress: NWC "Khabar Garaun" helpline = 1145 (there is no NWC 104); suicide helpline 1166 (Mental Hospital Lagankhel); TUTH 1660 012 1600; women's 1145; emergency 112/100; first National Mental Health Policy 1996; official CTEVT module numbering = 1 Psychosocial Intervention (contains Mental Health sub-module) · 2 Case Management · 3 Counseling Skill and Process · 4 Capacity Building; GBV medical care: 72h window is HIV PEP only, 120h emergency contraception, care helps at any time; child-abuse reporting: Act Relating to Children 2075 (2018) Section 68(1), anyone who learns of violence or sexual abuse against a child must inform the nearest police office, informant protected under 68(3) and (4) (verified from the Law Commission text, 2026-09-02). Batch 2 chapters (Sep 2026) were pair-reviewed as content by DeepSeek and GPT-5.6; ledger in `review/content-triage.md`.

## Pending / next work

- Session s02 closed 2026-09-02; vault mirror at `~/Obsidian/Mano/` (tasks, sprint log, session files, `sources/` with the intake ledger and triage files). Starter prompt for the next intake is at the top of `TASKS.md`. The Mano app lives in `~/Work/mano-app` (see its TASKS.md).
- Weekly deck intake until about March 2027: Pravo adds decks to the Drive folder; each deck gets a placement plan pair-reviewed before building, an intake-ledger row, bilingual chapters with keypoints and quiz, OG re-render, both-theme check, content pair review, one commit per chapter, same-day deploy. Batch 1 (Aug) and batch 2 (five Module 3 decks, Sep 2) are done; `review/intake.md` records what landed where and which claims were rejected, and those rejections hold for later decks.
- Open: native Nepali proofread by a human (chapters 19, 20, 22, 24 and the first-session scripts first). Parked: AAA contrast mode, only if readers ask. Approaches (1837 words inside closed expanders) is the one recorded ceiling exception.
- Pair-review tooling: DeepSeek v4 Pro and GPT-5.6 via opencode against a brief in `review/`; GPT-5.6 must be told not to spawn sub-agents or it stalls (memory: opencode-review-runs).

## Verification before every commit

`python3 build.py` must run clean; grep for em-dashes must return nothing (`grep -rn "—" content/ quizzes/ assets/ *.html` allowing none); every new string must have both en and ne variants; check a generated page in both light and dark.
