# Readability plan (2026-08-27), synthesised from DeepSeek + GPT-5.6 reviews + own phone-width pass

Verified against the code: mobile body drops to 17.5px (style.css:146); zero tel: links; "खण्ड 06" mixed digits; 12 unlinked "page NN" cross-refs; no @media print; sticky mobile header = 213px of a 797px viewport.

## Tier 1: small effort, high impact (one session)
1. Link every "page NN" cross-reference (12 places) to the chapter. build.py can do it at build time.
2. Helplines tap-to-call: tel: links, one row per number with purpose, footer + crisis boxes.
3. Keep 19px body on phones (drop the 640px shrink rule); Nepali too.
4. Devanagari digits for section/pager numbers when Nepali is active.
5. "Help now" line at the top of depression, eating, psychosis, substance, GBV, PFA (crisis colour, both languages), and move the substance withdrawal warning and the PFA "not responding" line up.
6. Move "most people exposed to trauma do not develop PTSD" above the criteria on the trauma page.
7. Split the two densest paragraphs: suicide "respond by level" into three tiers; child ADHD criterion into two checklists; panic 13 symptoms into 3 groups; GAD-7 into blocks.
8. Care line chosen by page group (heavy pages get a calm line), and the gentle note extended to GBV/suicide/ethics.

## Tier 2: medium effort, high impact
9. Mobile navigation: replace the 29-item horizontal strip with a compact drawer button; shrink the sticky header (nameplate + search only).
10. Plain-language search aliases: bilingual map of everyday phrases ("son won't go to school", "wife cries every day", "man dukhcha", "hearing voices", "can't sleep") to chapters, plus diacritic normalisation.
11. "Key points" box (3 bullets, bilingual) before every quick check, generated from a small per-page list.
12. "Start here" routes on the home page: family member / community worker / student.
13. Wide tables to stacked cards on phones: somatic seizure comparison, nepal idioms table, process 6-stage table, development Erikson table, approaches table, ethics principles, roots eras. Can be one CSS pattern (data-label on cells) applied to all tables under 640px.
14. Plain-words gloss line under each disorder definition, before the criteria; first-use glosses for Latin-script terms in Nepali text.
15. Expandable "what are these labels?" (codes + curriculum tags) on every chapter, not only the home page.

## Tier 3: larger
16. Bilingual glossary page (~25 recurring clinical terms) with inline links.
17. Print stylesheet (already on TASKS).
18. "Review later" marker for quick-check questions (localStorage).
19. In-page "On this page" list for chapters with 3+ cards.
20. Replace Latin symbols (≥, ≈, →) with words in Nepali text.

Rejected: nothing outright; GPT's "starting routes" and DeepSeek's "start here" merged (12). Both reviewers independently flagged: mobile nav strip, symptom-led search, help-now lines, suicide/ADHD/panic density, somatic table, key-points box, label explanation.
