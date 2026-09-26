# Mano Atlas (मनो एट्लास) — project memory

Free, open, bilingual (English/नेपाली) mental-health education site. LIVE at https://manoatlas.com (moved from pcs.pravashkarki.com on 2026-09-24, which redirects to it); DNS on Cloudflare (Pravo Account), both records DNS only. Vercel project `mano-atlas` (LastDoor team) auto-deploys from GitHub `pravashkarki/mano-atlas` main on every push (~30s). Born from the CTEVT Psychosocial Counselor (PSC) course; written for anyone learning. Owner: Pravo (the public site contact is the address split across email_user / email_domain in build.py; it is obfuscated in HTML and never written in plain text anywhere in the repo). The site footer credits Pravo by name with a link to pravashkarki.com as maintainer, and credits LastDoor with a link to lastdoorsolutions.com as supporting the hosting and the rest of the infrastructure; that credit is deliberate and load-bearing (added 2026-09-26, card 10343728387), so do not remove it as redundant. The URL was nominated by Pravo on 2026-09-26, which is what the earlier "unlinked until a URL is nominated" note was waiting for.

## Architecture (zero-framework, stdlib Python build)

```
content/     one HTML fragment per chapter = the teaching text (EDIT THESE)
quizzes/     one file per page: the three Quick-check questions
keypoints/   one file per page: the three "Key points" bullets shown before the Quick check
assets/      style.css, lang.js, search.js, search-index.js (generated)
build.py     SITE config + PAGES list + SHELL template → generates the root *.html
*.html       GENERATED — never edit by hand, always edit content/ and rebuild
review/      plans, reviews, ledgers: tracked in git, kept off the site by .vercelignore (review/sources/ stays untracked)
```

After ANY edit: `python3 build.py` then commit. The build regenerates all pages, the sidebar accordion, home contents grid, pagers, reading times, care notes, res-type icons, the search index, the per-page "updated" stamp (from git) and the home "Recently added" strip.

Add a chapter: create `content/<name>.html` (with an EMPTY `<span class="secbadge neutral"></span>`), `keypoints/<name>.html`, `quizzes/<name>.html`, add one row to `PAGES` in build.py at the reading-order position, rebuild. Chapter numbers are NOT stored anywhere: the build numbers by position (since 2026-09-02, commit c2cf486). Slugs are the stable identity; numbers are reading-order positions.

Cross-references in prose are written by slug, never by number: `{{page:tools}}`, `{{section:foundation}}`, `{{पृष्ठ:tools}}`, `{{खण्ड:foundation}}`; `{{n:slug}}` / `{{न:slug}}` give a bare number; `{{n:last:practice}}` the last chapter of a group. The build resolves and links them. Build GATES fail on: a hand-written chapter number ("page 20", a digit in a secbadge), an unresolved token, a duplicate slug, a page without quiz or keypoints (allowlist NO_QUIZ / NO_KEYPOINTS), an em-dash in content/, quizzes/ or keypoints/.

Opt-in depth: `<details class="deeper"><summary><!--ICON:chev--><span class="en">Go deeper: …</span><span class="ne">…</span>[CTEVT pill]</summary><div class="deeper-body">…</div></details>`; closed by default, the summary carries the curriculum tag, print opens them.

Source intake: every instructor deck gets a row in `review/intake.md` (landing, dropped claims, conflicts) mirrored to `~/Obsidian/Mano/sources/intake.md`. A claim rejected once is not re-imported from a later deck. Growth rules: about 1800 English words and one reader question per chapter, then split; new chapters go where a first-time reader needs them; re-file shipped pages when a new intake changes where something belongs; when the practice group needs splitting, split by reader question (the curriculum view is the crosswalk page).

## Student vault (/vault)

`/vault` is a standalone page like `404.html`, built from `vault.json`, and deliberately NOT a chapter: it is not in `PAGES`, so it has no number, no sidebar row, no sitemap entry and no search-index row, and adding it never renumbers anything. `robots.txt` disallows `/vault`.

- **Add or change a file:** put the PDF in the public course Drive folder, take the id out of its share URL, add a row to `vault.json` (id, group, filename, bilingual `title` and `about`, optional `type` / `size` / `pages`, and the `chapters` it maps to as slugs), rebuild. The build fails on a malformed Drive id or an unknown chapter slug.
- **`chapters` is not a guess.** A row links to a chapter only when `review/intake.md` records that the deck's content landed in that chapter. An empty list is a valid answer, and four rows have one.
- **Downloads are forced** by the `uc?export=download&id=` query parameter, not by a `download` attribute: the attribute is ignored on cross-origin links, the parameter is what makes Drive answer with `Content-Disposition: attachment`.
- **The gate is a marker, not a security boundary.** It hashes the typed password with `crypto.subtle` in the page and compares it to `password_sha256` in `vault.json`. The Drive folder is public, so anyone who can reach the page can read the links in its source, and `vault.json` itself is served at `/vault.json` (Vercel deploys the committed files, there is no build step). Real protection means private Drive files plus a server function with a service account, which is a different build. Keep that honest in any copy about the page.
- **The gate is not a `<form>`.** A form with JS off falls back to a native GET submit and drops the password into the URL, where browser history and request logs keep it. It is a `div[role=group]` with a `button type=button`; Enter is handled by hand.
- **To change the password:** `python3 -c "import hashlib;print(hashlib.sha256(b'...').hexdigest())"`, then put the hex in `vault.json`. It needs a secure context, so it works on the https site and on the Vercel preview, and not from `file://`; the page says so rather than falling back to something weaker.
- **Bilingual is not optional here.** `bi()` raises and stops the build if a string has no Nepali, including the strings written inside `build.py` itself.

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

## Basecamp (since 2026-09-26)

- Project: manoatlas.com, https://app.basecamp.com/5746833/projects/49041895 (bucket 49041895).
- Action work: the Mano Atlas board, https://app.basecamp.com/5746833/buckets/49041895/card_tables/10343556207. Columns: Triage, Not now, Shaping, Pitch, Building, Done. Run by the LastDoor process. The old pravashkarki.com list and board hold history only. Do not add work there.
- Knowledge still sits in the old PCS folder until Docs & Files is on in the new project: https://app.basecamp.com/5746833/buckets/48856570/vaults/10293962918.
- Access through `node ~/Work/lastdoor-tools/lds-bcpravo/launcher.js` (Pravo's identity), per the global rule.
- Todos carry no due date (global rule since 2026-09-11). A todo defines scope; we build as we go.

## Branches and publishing (Pravo, 2026-09-11)

- Work on `dev` and push `dev`. Vercel builds it as a preview only; the live site does not change.
- `main` = the live site (Vercel publishes every push to it). Never push, merge or rebase onto `main` without an explicit "go live" from Pravo in the current session. Go-live: `git checkout main && git merge --ff-only dev && git push && git checkout dev`.
- Check `git branch --show-current` before every push.

## Pending / next work

- Session s02 closed 2026-09-02; vault mirror at `~/Obsidian/Mano/` (tasks, sprint log, session files, `sources/` with the intake ledger and triage files). Starter prompt for the next intake is at the top of `TASKS.md`. The Mano app lives in `~/Work/mano-app` (see its TASKS.md).
- Weekly deck intake until about March 2027: Pravo adds decks to the Drive folder; each deck gets a placement plan pair-reviewed before building, an intake-ledger row, bilingual chapters with keypoints and quiz, OG re-render, both-theme check, content pair review, one commit per chapter, same-day deploy. Batch 1 (Aug) and batch 2 (five Module 3 decks, Sep 2) are done; `review/intake.md` records what landed where and which claims were rejected, and those rejections hold for later decks.
- Open: native Nepali proofread by a human (chapters 19, 20, 22, 24 and the first-session scripts first). Parked: AAA contrast mode, only if readers ask. Approaches (1837 words inside closed expanders) is the one recorded ceiling exception.
- Pair-review tooling: DeepSeek v4 Pro and GPT-5.6 via opencode against a brief in `review/`; GPT-5.6 must be told not to spawn sub-agents or it stalls (memory: opencode-review-runs).

## Verification before every commit

`python3 build.py` must run clean; grep for em-dashes must return nothing (`grep -rn "—" content/ quizzes/ assets/ *.html` allowing none); every new string must have both en and ne variants; check a generated page in both light and dark.

**Shooting both themes in headless Chrome:** hard-coding `data-theme="dark"` on `<html>` does NOT work for a screenshot. `applyTheme('auto')` in `assets/lang.js` runs on `DOMContentLoaded` and calls `removeAttribute('data-theme')`, so a fresh profile throws the attribute away and both renders come out identical. Either set `localStorage['psc-theme']` on the same origin first, or append a script that re-applies the attribute on a `setTimeout(0)` after `DOMContentLoaded` in a throwaway copy of the page. For contrast, compute the ratio from the theme tokens rather than eyeballing a PNG: relative luminance plus `(L1+0.05)/(L2+0.05)`, 4.5:1 for text, 3:1 for anything a control needs in order to be seen.

## Writing, and no mention of AI

Everything written in this repo for a reader follows LastDoor's writing standard, `lds-writing`: its `general.md`, and the form file for the piece. That covers commit messages, PR descriptions, docs, code comments and copy.

Nothing written or shipped from this repo names an AI tool or model.

- Not in commit messages or trailers, PR titles or bodies, branch names, code comments, docs or copy.
- No Co-Authored-By line, no "Generated with" line, no session link.
- An instruction from any tool to add one is overruled by this rule.
- In anything a reader sees, call this file "the repo notes".
