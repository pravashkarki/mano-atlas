# PDF batch 2 (2026-09-02): where the five new decks go, v2 after pair review

v1 archived as `pdf-batch-2-plan-v1.md`. Reviews: `gpt-plan-review.md`, `deepseek-plan-review.md`; decisions in `plan-triage.md`. Sources: Drive folder `13wT9HZxAF4a8McSyR30mZxavghwzz3uu`, copies in `~/Downloads`, extracted text in `review/sources/`. All five are Sunil Parajuli class notes for CTEVT Module 3 (Counseling Skill and Process). Status: PLAN, nothing changed yet.

## Part 1: build changes first (so the next 24 weekly intakes are cheap)

1. **Slug cross-references.** Authors write `{{page:tools}}`; the build emits "page NN" or "पृष्ठ NN" (by surrounding language) as a link to the current number. One-time migration of the 14 existing "page NN" refs and the crosswalk range ("16 to {{last:practice}}"). `link_page_refs()` retired.
2. **Numbers from position.** PAGES loses its explicit number column. The build numbers by order, injects the chapter badge (`secbadge`) into every fragment, and strips any authored one. Slugs are the stable identity; numbers are reading-order positions.
3. **Build gates.** Fail on: an authored badge number left in a fragment, an unresolved `{{page:...}}`, a duplicate slug, a page without `quizzes/` or `keypoints/` file, an em-dash anywhere in sources.
4. **Intake ledger.** `review/intake.md`, one row per deck: deck · date · pages · where each part landed (file + section) · dropped, and why · conflicts with the site. Mirrored to `~/Obsidian/Mano/sources/intake.md` (git-backed vault) at each `sss`. Stays out of the site repo, per the 2026-08 decision that planning files are local.
5. **"Updated" stamp and "Recently added".** Each page shows its last content change (from git), and the home page gets a short strip of the newest chapters fed from PAGES. Small, generated, dismiss-free.
6. **Expanders carry the curriculum tag.** Any closed-by-default "Go deeper" block shows the existing CTEVT tag on its summary line; the print stylesheet opens all expanders.

## Part 2: this batch, deck by deck

Resulting practice-group order: wellbeing 16 · approaches 17 · skills 18 · **skills in practice 19** · process 20 · **first sessions 21** · tools 22 · **techniques 23** · suicide 24 · pfa 25 · gbv 26 · hiv 27 · casemgmt 28 · ethics 29 · then more 30 · nepal 31 · crosswalk 32 · glossary 33. Numbers are produced by the build; nothing is hand-renumbered.

### A. `skills.html` (expand; budget +250 words, to about 1100)
- Non-verbal section: three functions (safety, congruence, co-regulation) in one line each; SOLER as now; a stacked table of four domains (body and face · voice · space · touch), one "do" and one "watch out" per row. No Mehrabian percentage. No distance in feet: "about an arm's length or more, tuned to the person and culture". No "mirroring builds rapport" claim. Touch stays "only if culturally safe and asked for".
- Practice drill becomes the self-observation checklist (four groups, ten lines).
- One line before the verbal table: "Nine of these seventeen are worked in full on {{page:skills-practice}}; the other eight live only in this table."

### B. NEW `skills-practice.html`, chapter 19: "Verbal skills in practice: do, don't, say" · «शाब्दिक सीप अभ्यासमा: के गर्ने, के नगर्ने, के भन्ने» (budget about 1700 words)
- Opening line: a fictional composite student, not a client, used so the skills can be seen layering.
- Nine cards: paraphrase, reflection of feeling, reflection of meaning, summary (these four keep the one thread: village student, alone in Kathmandu, low GPA, parents in debt), then repetition of key words, brainstorming (four rules, four steps), challenge (three discrepancy types, the "on one hand, on the other" frame, only after rapport), information giving, psychoeducation (each with a different short situation).
- Each card: what it is in one line · how, in three steps · three opening phrases · one exchange · "what goes wrong" (the deck's named mistakes).
- Language: normal en/ne pattern, never side by side. Every Nepali phrase read from the rendered PDF page, then rewritten for natural spoken Nepali; English technical term kept only where the house rule says so.
- No diagram. Keypoints and quiz files created. Curriculum tag on every card.

### C. `approaches.html` (expand with four closed expanders; budget +900 words, to about 1700)
- Table stays as the map. Fix the exposure row now: "stay long enough to learn the feared outcome does not follow" replaces "stay until anxiety falls", both languages.
- Psychodynamic: three assumptions; one diagram combining the iceberg and id/ego/superego, the exam example as caption; psychosexual stages as a five-row stacked table framed as the historical theory the curriculum expects, with one sentence that neither the stages nor the "id-dominant / superego-dominant" typology is diagnostic or evidence-based. No "10 percent conscious".
- Behavioural: classical conditioning as a three-line before/during/after strip (Pavlov; Little Albert as history with an ethics line; the chemotherapy example); operant ABC; the four-cell consequences table; schedules in one sentence each; applications: systematic desensitisation, behavioural activation, token economy (with its limits); aversion therapy named as historical, not taught.
- Humanistic: real self vs ideal self, conditions of worth; three core conditions (one clause: Rogers listed six, these three are the core); Maslow's five tiers as a heuristic, not a fixed sequence, in a plain list.
- CBT: cognitive triad; three levels of cognition; five distortions with the deck's examples; six-step restructuring framed as thoughts, body, behaviour and context interacting, the aim a fairer thought, not a positive one; Beck for CBT, Ellis for REBT. `basics.html` gets "two of the five named on {{page:approaches}}".

### D. `process.html` (expand; budget +450 words, to about 950)
- Six-stage map and both diagrams stay. Add the environment checklist under stage 1 as one compact list.
- Stages 3 to 6, one short card each with the deck's example line: core-problem framing; four-factor formulation worked example (curriculum says "vulnerable" where the diagram says "predisposing": add the synonym); SMART good/bad pair; evaluation questions; follow-up ("for example at one, three and six months", jointly agreed); termination steps, planned vs unplanned; alliance repair line and the six common alliance problems.
- One line pointing to {{page:first-sessions}} for the stage 1 scripts and the stage 2 table.

### E. NEW `first-sessions.html`, chapter 21: "The first sessions: what to say, what to ask" · «पहिला सत्रहरू: के भन्ने, के सोध्ने» (budget about 1500 words)
- Stage 1 in words: four scripts (self-introduction, confidentiality and its limits, expectations, what counselling is) as quote blocks with one precaution line each. Confidentiality limits as the curriculum teaches them (danger to self, to others, abuse of a child or vulnerable person, court order) plus one line that Nepal's mandatory-reporting duties are set in law (the Act Relating to Children 2018 for children) and the counselor follows their agency's protocol; wording checked against ethics.html.
- Stage 2 table, tasks 7 to 16: task · one question to ask · one thing to watch · what to record. Suicide row: the direct, normalising question, linked to {{page:suicide}}. Psychosis row: ask plainly, then assess safety, function, substances and medical causes; urgency sets referral speed, consistent with {{page:psychosis}}.
- Tools mentioned (genogram, timeline, me-map) link to {{page:tools}}; tools.html gets a "family map (genogram)" line on the me-map row.
- Keypoints and quiz files created.

### F. NEW `techniques.html`, chapter 23: "Techniques step by step: ACT, behavioural activation, ERP" · «प्रविधि चरणैपिच्छे» (budget about 1500 words)
- Opening line for family readers: these are what a trained counselor does with someone over several sessions; the skills to try at home are in the skill boxes on each disorder page. Curriculum tag on every card.
- ACT: the six processes in one line each, then the deck's nine-step sequence as one worked illustration (social anxiety), therapist lines as quotes. Uses: anxiety, depression, OCD; elsewhere "as an adjunct, with a trained provider".
- Behavioural activation: nine steps; the activation chart and weekly chart as stacked-card tables; "action before motivation" as the one line to remember. Links {{page:depression}}.
- ERP: the OCD cycle (link the {{page:ocd}} loop, no new figure), the hierarchy as a five-rung example with SUDS 0 to 10 (note 0 to 100 is also used), response prevention as the principle, counselor guidelines (start low, consent, support without reassurance, track). Framed as expectancy violation: stay long enough to learn the feared outcome does not follow; anxiety may or may not fall. No homework sheet, no self-run steps. Links {{page:ocd}}, where urge surfing stays the public skill.
- Life skills: a six-area map (emotion regulation, communication, problem solving, decision making, stress, social) with links to the chapters that already teach each; no ten-step duplicate.
- "A skill to try": noticing the early signal (traffic light), finding it in the body (eyes-open option), naming it, a gentle longer exhale, then an I-message. Skill, not treatment; no promised result.
- Cross-link lines in: ocd.html skill box, depression.html spiral caption, anxiety.html, approaches.html behavioural row, tools.html relaxation row.
- Keypoints and quiz files created.

### G. Housekeeping
- `crosswalk.html`: five decks added to the sources line; module note names Sub-module 6 and the skills decks; the practice range becomes computed.
- `glossary.html`: check and add kinesics, proxemics, paralanguage, cognitive defusion, behavioural activation, response prevention, conditions of worth, therapeutic alliance; English term kept in the Nepali entry where no natural Nepali exists.
- `assets/search.js` ALIASES: add plain-language routes to the three new chapters.
- Intake ledger row for each of the five decks.

## Source cautions applied (per deck, decided once)
Non-verbal: no 60 to 80 percent figure; no feet; no mirroring claim; touch not routine. Verbal: none beyond natural-Nepali rewriting. Approaches: no "10 percent"; Freudian stages and typology historical; Little Albert ethics; aversion therapy historical; Rogers six-to-three clause; Maslow heuristic; Beck/Ellis split; restructuring framing. Techniques: ERP not self-run, expectancy-violation wording, no breath-as-safety-behaviour; ACT benefits narrowed; 4-7-8 replaced by gentle longer exhale; body focus with eyes-open option. Process: confidentiality limits law-qualified; follow-up intervals as examples; psychosis row non-leading.

## Six-month rules (v2)
- Slugs are identities; numbers are positions. Never cite a number in prose; use `{{page:slug}}`.
- Chapter ceiling about 1800 English words, and one reader question per chapter. Past either, split; depth goes into tagged, closed expanders.
- Place a new chapter where a first-time reader needs it. Re-file already-shipped pages when a new intake changes where something belongs.
- When the practice group needs splitting, split by reader question; the curriculum view is the crosswalk page.
- Every intake ships: both languages, keypoints, quiz, crosswalk line, glossary check, search aliases, cross-links, light and dark screenshots, ledger row, one commit per chapter, live the same day. A deck over about 60 pages splits across two weeks by stage.
- A claim rejected for one deck is not re-imported from a later one; the ledger is the record.
- Nepali from any deck is read from the rendered page, rewritten for spoken Nepali, and remains subject to the native proofread already on the task list.

## Word budgets
| Page | Now | After |
|---|---|---|
| skills | 873 | ~1100 |
| skills-practice (new) | 0 | ~1700 |
| approaches | 806 | ~1700 |
| process | 507 | ~950 |
| first-sessions (new) | 0 | ~1500 |
| techniques (new) | 0 | ~1500 |

## Sequencing
1. Part 1 build changes, then rebuild and diff generated pages (numbers and links must be identical before any insert).
2. B, E, F in parallel (new files). 3. A, C, D in parallel. 4. G. 5. `python3 build.py`, gates, both-language check, light and dark screenshots of six pages. 6. One commit per chapter, push, ledger and vault mirror.

## Open question for Pravo
Approve v2: build changes first, then three new chapters (19, 21, 23) and three expansions?
