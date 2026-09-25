# Plan: Markdown content contract, English-first phase, app bundle

Status: READY WITH FIXES (pair review, 2026-09-25). Founder's go pending. Nothing shipped beyond docs.

## TASK

Make the content a single contract both the site and the Mano app can consume, and ship the English-first phase the Founder approved.

1. New chapters are authored as Markdown + YAML frontmatter, not HTML fragments.
2. build.py learns to parse both: existing HTML fragments stay untouched; Markdown pages generate the page and an entry in a versioned `content-bundle.json` for the app (reading purpose only, no state tracking).
3. New pages are English-only in phase 1. The site hides the Nepali toggle until a page's Nepali is confirmed and the per-page flag flips (phase 2). Hidden at build, not by CSS.
4. The voice guide (`docs/VOICE-TONE.md`) becomes the standard the content checks pass against.

Pair review verdict (free reviewer, opencode nemotron-3-ultra, 2026-09-25): the `:::en/:::ne` body convention is rejected (not CommonMark, fights the gates). English-only Markdown is the PRIMARY phase-1 format, not a fallback. Full verdicts at the bottom.

## PREMISE CHECK

- Content lives as HTML fragments in `content/<slug>.html`, every string bilingual via `<span class="en">` / `<span class="ne">`. 29 pages, four sidebar groups.
- keypoints and quizzes live in per-page files: `keypoints/<slug>.html`, `quizzes/<slug>.html`. The build enforces "three keypoints, three questions" and scans all three directories for gates. These are SEPARATE FILES, not frontmatter, and stay that way.
- build.py is zero-framework stdlib Python. It builds chapter numbers from position (PAGES list order), resolves slug cross-refs (`{{page:slug}}` etc.), stamps badges, generates sidebar, home grid, pagers, search index (`assets/search-index.js`, 98 entries), reading times, and the per-page updated stamp.
- Gates (in build.py): no em-dashes in content/quizzes/keypoints, no hand-written chapter numbers, no unresolved tokens, no duplicate slugs, quiz + keypoints present per page (NO_QUIZ / NO_KEYPOINTS allowlists), no missing PDF placeholders.
- The gates operate on the FINAL rendered HTML fragment shape: the parser functions (`resolve_refs`, badge stamping) expect `class="en/ne"` spans, `secbadge` spans, and the block/paragraph structure the SHELL renders. Markdown input must be pre-rendered into that exact shape before the gates run, or the gates silently stop applying.
- Cross-references render by page name now (shipped to dev, commit 3427f54).
- The Mano app brief (APP-BRIEF.md, docs/) already plans its own structured bilingual source (states, responses, skills, help cards). Decision made 2026-09-25: the atlas content becomes a shared reading content source the app bundles, so the same facts are not written twice.
- Bilingual pattern, language phasing and voice are documented: `CLAUDE.md`, `docs/VOICE-TONE.md`. Chapters 19, 20, 22, 24 and the first-session scripts are the native-review candidates for phase 2.

## WHAT SHIPS

### 1. Markdown authoring format (English-only in phase 1)

New pages use `content/<slug>.md` with frontmatter:

- slug, group, catvar (order is implicit by position in PAGES).
- en_title (ne_title only when bilingual).
- language: `english-only` (phase 1) or `bilingual` (phase 2, Nepali confirmed).
- No keypoints and no quiz in frontmatter. They stay per-page files: `keypoints/<slug>.md`, `quizzes/<slug>.md` (same three-item rule, now Markdown).

Body: plain Markdown, English only in phase 1, NO pairing markers in prose. The old `:::en/:::ne` convention is dropped (pair review: not CommonMark, breaks the gates).

Phase 2 Nepali returns as a PARALLEL file `content/<slug>.ne.md` (English body + Nepali body kept apart, not interleaved), and the existing per-string `class="en/ne"` pattern is re-emitted by the build from the two files until the per-page flag flips. No interleaved bilingual authoring format is shipped.

### 2. build.py changes

- Detect `.md` fragments alongside `.html`. Frontmatter feeds the existing PAGES machinery; the Markdown BODY is pre-rendered by build.py into the exact HTML fragment shape the existing gates and SHELL expect (paragraphs, headings, `class="en/ne"` spans, resolves slug tokens), so `resolve_refs`, badge stamping and every gate run on Markdown pages unchanged.
- `gate_sources` expands to scan `content/*.md`, `keypoints/*.md` and `quizzes/*.md` with the same rules (em-dashes, numbers, tokens).
- Chapter-number check runs on the rendered HTML, not the Markdown source (a `{{n:slug}}` written in Markdown resolves only if its number is real).
- New output: `content-bundle.json`, versioned with a content hash over the SOURCE files (not the bundle JSON — a source edit must bump it). Per-slug reading content: slug, titles, group, keypoints, quiz, cross-references, glossary terms, and a `feeling_state_map` linking each atlas slug to the app's feeling-state keys, plus the app's own response copy as a `response_ref` (the app keeps its response paragraphs in its own source; the bundle points at them, it does not duplicate them), and helplines with `last_verified` dates from the live site.
- Search index: with a page English-only, its index entry carries English strings only. Nepali strings are excluded while the flag is off, so there are no orphan search hits on hidden text.

### 3. English-first, toggle hidden at build

- A single build constant, e.g. `PHASE1_ENGLISH_ONLY = True`. When on:
  - the EN/NE switch is REMOVED from the rendered pages (not hidden by CSS; lang.js gets the flag and drops the button, so the language switcher stays honest);
  - all `class="ne"` output is suppressed in the built HTML;
  - the search index generator skips `class="ne"` strings.
- Existing Nepali stays in the source files, untouched; it returns per page when its frontmatter flag flips (phase 2).
- Decision needed from the Founder (one question): the existing 29 pages carry live bilingual output today. Under a site-wide `PHASE1_ENGLISH_ONLY`, those pages also render English-only in phase 1 (the toggle disappears site-wide, which is what "hide the toggle" implies), even though their Nepali ships today. The alternative is to exempt the existing 29 and hide the toggle only on new pages. Recommended: site-wide, because it matches "live Nepali keeps improving through the native review" and the wrong-case cost of showing unvouched Nepali is higher than a temporary English-only site.

### 4. Voice guide adoption

- `docs/VOICE-TONE.md` is the copy standard for all content checks.
- Phase-1 English-only pages are written directly against it, including its "what the voice refuses" checklist in the content pair-review prompts.
- "Translation readiness" note: English-first risks baking in English idioms that do not carry to Nepali. Each chapter's frontmatter records translation-readiness issues as they surface, so phase 2 does not re-translate prose word-for-word (the reviewer's point: carry the voice across, not the words).

## CASES AND DECISIONS

- Markdown pages and HTML pages coexist; the sidebar and numbering do not care which format a page is.
- The app bundle is reading content only: no state tracking, no user data, no external links beyond helplines.
- A page without confirmed Nepali is `english-only`; nothing ships half-confirmed.
- A chapter number written by hand is caught by the gate either way; authors never write numbers (PAGES position owns them).

## SECURITY

- Static output only; the bundle contains curated reading content, no executable payload.
- Bundle hash committed, so a tampered or stale bundle is detectable; helplines carry `last_verified` dates.
- No new runtime, no new dependencies (stdlib Python).

## VALIDATION

- A phase-1 English-only chapter (candidate: the Sub module 5 intake, crosswalk page "communication skills") is authored in Markdown, builds through every existing gate, renders correct in light and dark, and appears in `content-bundle.json` with quiz, keypoints, cross-refs and feeling-state map.
- `grep -rn "\u2014" content/ quizzes/ keypoints/` returns nothing (gate already does this; Markdown files must be covered).
- Search index: no `class="ne"` strings present for English-only pages; no orphan Nepali hits.
- All verified on the dev preview; nothing moves to main without the Founder's go.

## ROLLOUT

- Commits on `dev`, preview only. Founder verifies the preview, then yes to main.
- Docs (CLAUDE.md one line, review prompts, README authoring section) in the same PR as the build change.

## DONE WHEN

- Markdown authoring works end to end through the gates; content-bundle.json emits; site ships English-only with no toggle and no Nepali search hits; voice guide is the named standard; the Sub module 5 intake is the proof chapter.
- Everything verified on the dev preview before any move to main.

## NON-GOALS

- No CMS, no framework port, no new runtime. Build stays stdlib Python, site stays static.
- No state tracking or sensitive content in the bundle.
- No new chapters beyond the phase-1 proof until the Founder approves this plan.
- No interleaved bilingual authoring (English and Nepali bodies stay in separate files).

## OPEN DECISIONS (for the Founder)

1. Site-wide English-only for phase 1 (recommended) vs exempt the existing 29 bilingual pages.
2. The migration proof page (candidate: Sub module 5 "Applying Communication Skills").
3. Whether the app bundle carries full bilingual prose in v1 (recommended: no, summaries and structured sections only; the app's own response copy stays in its source via `response_ref`).

---

## PAIR REVIEW VERDICTS (reproduced for the record)

Reviewer: opencode, model nemotron-3-ultra-free, 2026-09-25.

Key via verdicts:
- CONTRACT-VERDICT: Markdown pages are English-only in phase 1 with no bilingual markers; Nepali in a parallel `content/<slug>.ne.md` only when the phase-2 flag flips; render both through a single HTML-fragment emitter so all existing gates apply unchanged.
- BUNDLE-VERDICT: add a `feeling_state_map` linking atlas slugs to app feeling-state keys, include the app's response copy as a `response_ref` (its own source, not a duplicate), and helplines with `last_verified` dates.
- PHASE-VERDICT: yes, build-time toggle hide is sound; the flag must also remove the lang.js button and filter the search index by language.

Disagreements actioned: dropped the `:::en/:::ne` convention (no CommonMark support); keypoints/quiz stay separate files, not frontmatter; bundle hash covers source files; gates (em-dash scan, chapter-number check) extended to Markdown inputs; existing 29 pages' phase-1 treatment made an explicit Founder decision.