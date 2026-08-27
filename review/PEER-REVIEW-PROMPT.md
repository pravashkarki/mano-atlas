# Peer review brief: Mano Atlas (pcs.pravashkarki.com)

You are reviewing a free, bilingual (English/Nepali) mental-health education site built as a static site in this repository. The teaching text lives in `content/*.html` (one fragment per chapter, ~30 files); every user-visible sentence appears twice, once in `<... class="en">` and once in `<... class="ne">`. Quizzes live in `quizzes/*.html`. Do not review the generated root `*.html` pages; review the sources.

Your job: find real problems, not restatements. Check, in priority order:

1. FACTUAL ACCURACY: DSM-5 criteria fidelity (symptom counts, durations, specifiers), epidemiology figures, named researchers/models/attributions, Nepali legal and health-system claims (helpline numbers, OCMC, laws), and history-of-psychology dates.
2. SAFETY: anything that could harm a distressed reader (wrong crisis numbers, advice that could discourage help-seeking, missing caveats on self-diagnosis, coping-skill boxes making treatment claims).
3. BILINGUAL PARITY: places where the Nepali text says something different from the English, is missing, or is machine-literal to the point of changing meaning.
4. PEDAGOGY: claims that are technically right but misleading for a beginner; quiz answers that are arguable.
5. LINKS AND CITATIONS: named books/papers/videos that do not exist or are misattributed.

House rules you must respect in any suggested wording: no em-dashes anywhere; never invent Nepali prevalence figures; crimson/crisis styling is reserved for crisis content; quizzes reassure, never judge; no client case studies.

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `FILE | short quoted claim | VERDICT (WRONG / QUESTIONABLE / SAFETY / PARITY) | correction with source`
- Most serious first. Maximum 25 findings.
- Then a final line: `CLEAN: <comma-separated list of files with no findings>`
Do not rewrite whole passages. Do not praise. If you cannot verify a claim either way, mark it QUESTIONABLE and say what source would settle it.
