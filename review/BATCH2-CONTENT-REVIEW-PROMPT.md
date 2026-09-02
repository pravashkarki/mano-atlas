# Content pair review: PDF batch 2 (2026-09-02)

Work only inside this repository; do not read files outside it. Review the SOURCES, not the generated root pages.

Files in scope (new or changed today):
- New chapters: `content/skills-listening.html`, `content/skills-moving.html`, `content/first-sessions.html`, `content/techniques.html`, with their `keypoints/*.html` and `quizzes/*.html`.
- Changed: `content/skills.html` (non-verbal card and the pointer line), `content/approaches.html` (exposure row, four `details.deeper` expanders, the iceberg SVG), `content/process.html` (room checklist, stages 3 to 6 card), `content/basics.html` (one clause), `content/ocd.html`, `content/depression.html`, `content/anxiety.html`, `content/tools.html` (one cross-link sentence each), `content/glossary.html` (seven new rows), `content/crosswalk.html` (sources and module note).
- Source decks the chapters were built from: `review/sources/*.txt` (Nepali may be garbled there; the English structure is reliable). Decisions already taken about what NOT to import are in `review/intake.md` and `review/plan-triage.md`; do not re-argue those unless you find them wrong.

Context: a free bilingual (English/Nepali) mental-health education site for CTEVT Psychosocial Counselor students, health workers and family members. Every string exists twice, `class="en"` and `class="ne"`. Cross-references are `{{page:slug}}` tokens resolved by the build. Quizzes reassure, never judge.

Your job: find real problems in what was written. Check, in priority order:

1. FACTUAL ACCURACY: attributions (Egan, Ivey, Rogers, Maslow, Beck, Ellis, Hayes, Pavlov, Watson, Skinner), the ACT six processes, behavioural activation steps, ERP framing (expectancy violation, response prevention), classical and operant conditioning definitions, reinforcement schedules, the cognitive triad and distortions, the Nepali legal claim on child-abuse reporting (Act Relating to Children 2018), the curriculum task numbering (tasks 1 to 24).
2. SAFETY: anything a distressed family reader could misuse (ERP or ACT read as self-treatment despite the framing; the emotion skill box; the psychosis and suicide rows on first-sessions; confidentiality limits stated too absolutely).
3. BILINGUAL PARITY AND NEPALI QUALITY: Nepali that says something different from the English, is missing, or reads as a literal translation rather than spoken counselling Nepali; wrong register (the site uses तपाईं to the client, सेवाग्राही/परामर्शकर्ता); terminology against the house rule (English term when no natural Nepali exists; Devanagari for everyday loans; Latin for codes and acronyms).
4. PEDAGOGY: claims that are right but misleading for a beginner; quiz answers that are arguable; the fictional-composite student framing; anything in the new chapters that duplicates or contradicts an existing chapter.
5. HOUSE STYLE: em-dashes (none allowed); crimson/crisis styling outside crisis content; treatment claims inside a skill box; a client case study presented as real.

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `FILE | short quoted text | VERDICT (WRONG / SAFETY / PARITY / NEPALI / QUESTIONABLE) | correction with source or the better Nepali wording`
- Most serious first. Maximum 30 findings. Do not restate what is fine. Do not praise.
- Then a final line: `CLEAN: <comma-separated list of in-scope files with no findings>`
If you cannot verify a claim either way, mark it QUESTIONABLE and say what source would settle it.
