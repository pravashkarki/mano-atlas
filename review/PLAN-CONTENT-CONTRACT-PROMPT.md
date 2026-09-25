# Plan review brief: Markdown content contract, English-first phase, app bundle

Work only inside this repository; do not read files outside it. You are reviewing a PLAN, not content. Nothing has been built yet.

Read, in this order:
1. `docs/plans/content-contract-english-first.md` (the plan under review).
2. `docs/VOICE-TONE.md` (the voice and tone standard the plan adopts).
3. `README.md`, `CLAUDE.md`, `build.py` (PAGES, SHELL, resolve_refs, the gates), and skim `content/anxiety.html` and `content/techniques.html` to see the current authoring format and bilingual pattern.
4. `docs/APP-BRIEF.md` (the Mano app, which will consume the proposed content bundle, reading purpose only).

Context: a free bilingual (English/Nepali) mental-health education site for CTEVT Psychosocial Counselor students. Today content is HTML fragments in content/ with every string paired as class="en" / class="ne". The site is a zero-framework stdlib Python build. The Founder has decided: (a) the content becomes a single contract both the site and the Mano app consume; (b) English is phase 1, Nepali returns per page only after a native review (chapters 19, 20, 22, 24, first-session scripts first); (c) the build stays build.py, no CMS, no framework port, no new runtime; (d) the voice guide is adopted as the standard.

Your job: find the real problems with the plan. Judge, in priority order:

1. MARKDOWN CONTRACT: is the proposed `content/<slug>.md` + YAML frontmatter format sound for this site? Is the `:::en / :::ne` paired-block convention workable in CommonMark and for authors, or will it fight the build's existing gates (no em-dashes, resolved slug cross-refs, quiz + keypoints present, chapter numbers from position)? Does the fallback (English-only Markdown for phase 1, HTML fragments stay for bilingual pages) interact correctly with the content-bundle goal?
2. BILINGUAL PHASE ORDER: the plan hides the Nepali toggle site-wide at build time until a page's frontmatter flag flips. Is hiding by build (no class="ne" in the DOM, no orphan search hits) the right call versus a CSS toggle? What breaks with the existing bilingual pattern, search index, and lang.js?
3. APP BUNDLE: the plan emits a versioned content-bundle.json (slug, titles, quiz, keypoints, glossary, cross-refs, summaries; full prose deferred). For the Mano app's stated needs, is this scope right? What is missing or over-built?
4. GATES AND BUILD: which build.py gates survive the Markdown path, which silently stop applying, and which new checks are needed? Anything in the plan that will produce inconsistent pages between the .html path and the .md path?
5. VOICE ADOPTION: does adopting docs/VOICE-TONE.md as the standard change anything the plan does not account for (authoring, review prompts, the readability plan in review/readability-plan.md)?

House rules the plan must respect: no em-dashes; never invent Nepali prevalence; quizzes reassure never judge; no client case studies; coping-skill boxes are skills never treatment claims; complexity is opt-in; keep the bilingual pattern's spirit even when English-first.

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `AREA (1 to 5) | what the plan says (short quote) | VERDICT (DISAGREE / RISK / MISSING / AGREE-WITH-CHANGE) | your recommendation, concrete, one or two sentences`
- Most important first. Maximum 25 findings. No praise, no restating the plan.
- Then one line: `CONTRACT-VERDICT: <the one change to the Markdown format you would insist on before building>`
- Then one line: `BUNDLE-VERDICT: <the one change to the app bundle scope you would insist on>`
- Then one line: `PHASE-VERDICT: <is English-first with a build-time toggle hide sound, yes or no, and why in one clause>`