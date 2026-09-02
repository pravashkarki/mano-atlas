AREA 4 | "ERP and ACT are counselor protocols done with a trained person; the chapter says so at the top" | DISAGREE | ERP's hierarchy + SUDS + response prevention + "no reassurance" + relapse plan is a treatment protocol, not a skill; publishing full steps for the site's "family members" audience invites unsupervised self-treatment and contradicts ocd.html's own "full ERP belongs with a professional". Keep only the existing urge-surfing skill public; put the full protocol under an explicit "for trainees, under supervision" framing or off the public page.

AREA 2 | "drop the column; the build numbers pages by position inside the list" | DISAGREE | Every content file hard-codes its own number in a secbadge span (e.g. process.html `<span class="secbadge neutral">19</span>`) that build.py never injects, so position-derived numbering leaves stale badges on every shifted page. Derive or drop secbadge too, else "inserting a row renumbers everything" is false on the first insert.

AREA 2 | "review/intake.md (git-ignored like the rest of review/)" | DISAGREE | The single audit trail for ~25 intakes would be unbacked-up and invisible to readers, defeating the "content truth status" durable-record purpose. Commit it (SOURCES.md/INTAKE.md in the repo) and echo a short "last changed" line on affected pages.

AREA 2 | "Chapter ceiling: about 1800 English words" | RISK | The two new chapters are never word-budgeted: ACT+BA+life-skills+ERP+charts+emotion box (ch. 22) and nine full skill cards (ch. 19) each plausibly exceed 1800 words, breaking your own ceiling the same day. Estimate both before writing and split techniques by reader question (ACT/ERP vs BA vs life-skills).

AREA 4 | "The running case is kept as the deck has it (village student in Kathmandu)" | AGREE-WITH-CHANGE | A sustained student with a GPA and family debt reads as a real client and brushes the "no case studies" rule; the site's existing vignettes are single-sentence hypotheticals. Keep it but open with an explicit "fictional student, a composite" line so it is unambiguously a teaching device.

AREA 1 | "One card per skill (nine)" | MISSING | skills.html teaches "the verbal seventeen" but the deck deep-dives nine; the plan never reconciles the eight left out (questioning, feedback, self-disclosure, suggest-and-fade, empathy, consoling/touch, non-verbals, active listening). Name the chapter honestly or add a line that the remaining eight stay in the table.

AREA 1 | "basics.html keeps its short version and links here" | RISK | basics.html teaches "two distortions, three questions" while the CBT expander will teach "five distortions, six steps", so one skill carries two conflicting counts. Reconcile: basics says "2 of the 5 named distortions" or align to five.

AREA 1 | "the avoidance loop shared by ACT and ERP ... or reuse the OCD-loop idea" | AGREE-WITH-CHANGE | A fourth near-identical loop (foundation 03, OCD, depression spiral already exist) duplicates and fights "one mind". Link the foundation negative-reinforcement loop and only annotate the ERP-specific "skip the ritual" step; no new figure.

AREA 3 | "applications list linked to chapter 22" | MISSING | The deck's aversion therapy (pairing alcohol with a nausea drug) is dated and ethically contested; the plan never flags it, so importing it teaches an unsafe technique as current. Drop it or mark it historical/discredited in the behavioural expander.

AREA 3 | "ACT founder Hayes ... all check out" | RISK | The deck's "Benefits of ACT" credits ACT for PTSD and substance use without nuance, and the plan passes it. Keep evidence-backed uses (anxiety, OCD, depression) and soften or cut PTSD/substance to "adjunct, under a trained provider".

AREA 5 | "The Verbal Skills deck's Nepali extracts garbled" | RISK | The same font-garbling afflicts the ACT/BA/life-skills/ERP Nepali (therapy-techniques.txt is visibly garbled too), but the plan only calls out the verbal deck. Apply "render from the PDF, never extract" to all five decks before any Nepali string ships.

AREA 5 | "the deck's bilingual therapist lines as quotes" | MISSING | Metaphors (quicksand, silly repetition, traffic light, on-one-hand) have no natural Nepali equivalent and the plan gives no strategy. Render each to a Nepali-familiar equivalent per the house rule, not a literal/transliterated coin.

AREA 2 | "the audit trail the CLAUDE.md 'content truth status' paragraph needs" | MISSING | Nothing reader-facing shows what a new intake changed beyond the static "Last reviewed: August 2026" footer, so returning students can't see updates. Add a per-page or site changelog keyed to the ledger.

AREA 5 | "add terms ... (kinesics, proxemics, paralanguage, cognitive defusion, response prevention, conditions of worth, therapeutic alliance)" | MISSING | These have no natural Nepali; the plan lists them for the glossary but not how they render in Nepali text. Per the house rule, keep the English term in the Nepali text and glossary rather than coining transliterations.

AREA 3 | "Beck/Ellis ... check out" | AGREE-WITH-CHANGE | The deck attributes "CBT" jointly to Beck and Ellis, but Ellis founded REBT; teaching "CBT = Beck & Ellis" is loose. Credit Beck for CBT and Ellis for REBT in the one-line note.

AREA 1 | "renumber 19 to 30 as 21 to 32" | RISK | The mapping is off by one at the head: process goes 19→20 and tools 20→21, not 19→21; the shorthand will mislead whoever edits PAGES. State the exact 19→20, 20→21, [22 new], 21→23 … 30→32 map.

AREA 2 | "position rule: a new chapter goes where a first-time reader needs it" | MISSING | No rule covers re-filing already-shipped pages when a new intake changes where something belongs, so content drifts out of order across 25 intakes. Add "re-file, not just insert" so placement is re-judged every intake, not only for new pages.

PLACEMENT-VERDICT: nonverbal = keep (skills.html) · verbal = keep as skills-practice 19, but split if it exceeds ~1800 words · approaches = keep (approaches.html) · therapy-techniques = keep as techniques 22, but move the full ERP/ACT protocol off the flat public path (trainee-supervision framing) and consider splitting life-skills out · process = keep (process.html).

STRATEGY-VERDICT: derive section numbers from position everywhere, including the hard-coded secbadge in each content file, so an insert truly touches only PAGES.
