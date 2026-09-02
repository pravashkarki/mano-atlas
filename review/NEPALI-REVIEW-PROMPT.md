# Nepali language review brief: Mano Atlas (pcs.pravashkarki.com)

Work only inside this repository; do not read any file outside it and do not read any CLAUDE.md or agent files. Begin by reading content/*.html and quizzes/*.html directly.

You are reviewing the NEPALI text of a free bilingual mental-health education site. The English was written by hand; the Nepali was machine-translated and then lightly checked. Every user-visible sentence appears twice: once in `<... class="en">` and once in `<... class="ne">`, including `<text>` inside SVG diagrams and the quiz files in quizzes/. Do not review the generated root *.html pages; review the sources in content/ and quizzes/.

Readers: Nepali counselling students (CTEVT Psychosocial Counselor course), community health workers, and family members of people who are unwell. Register wanted: clear, warm, standard written Nepali as used in good Nepali health-education material (MoHP, TPO Nepal, CMC Nepal leaflets); not Sanskritised, not Hinglish, not word-for-word English.

Check, in priority order:

1. MEANING DRIFT: places where the Nepali says something different from, less than, or more than the English. Clinical numbers, durations, negations ("never", "only", "not"), and helpline instructions matter most.
2. CLINICAL TERMS: wrong or unusual Nepali for a disorder, symptom or technique. Prefer the terms used in Nepal's mental-health services and the CTEVT curriculum (for example उदासी/डिप्रेसन, चिन्ता, मनोविकृति, आत्महत्या, मनोसामाजिक परामर्श, सेवाग्राही). Flag transliterations where a good Nepali word exists, and Nepali coinages where the field actually uses the English term.
3. MACHINE-LITERAL NEPALI: sentences that are grammatical but read as translated English (unnatural word order, English idioms carried over, wrong postpositions, over-long sentences, gender or honorific mismatch, तपाईं/तिमी inconsistency).
4. TONE FOR A DISTRESSED READER: anything that sounds judging, alarming or cold in Nepali where the English is warm. Quiz feedback must reassure.
5. SCRIPT AND TYPOGRAPHY: wrong Devanagari conjuncts, chandrabindu/anusvara errors, wrong halant, mixed Nepali/Hindi spellings (e.g. Hindi है, हूँ, में), Devanagari digits vs Latin digits used inconsistently within a sentence, spacing around «» and punctuation.

House rules for any suggested wording: no em-dashes anywhere; never invent Nepali prevalence figures; keep the same meaning as the English; keep it short.

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `FILE | quoted Nepali (short) | VERDICT (DRIFT / TERM / LITERAL / TONE / SCRIPT) | suggested Nepali replacement, then a five-word English gloss`
- Most serious first. Maximum 40 findings. Group repeated errors (same wrong term across files) into one line listing the files.
- Then a final line: `CLEAN: <comma-separated list of files with no findings>`
Do not rewrite whole passages. Do not praise. Do not comment on the English.
