# Peer-review triage ledger (2026-08-27)

Source reviews: `review/deepseek-review.md` (15 findings). `review/chatgpt-review.md` came back empty twice (opencode gpt-5.6 exits silently after globbing content/); see note at the bottom.

Verdict key: ACCEPT = changed in content/ both languages; REJECT = claim checked against a primary source and does not hold; PARTIAL = part accepted.

| # | File | Finding | Verdict | Primary source / reasoning |
|---|---|---|---|---|
| 1 | suicide.html, hero.html | TUTH hotline 1660 012 1600 may be dead | REJECT | TherapyRoute Nepal crisis-line directory lists TUTH Suicide Hotline 16600121600, 24/7; CLAUDE.md records it as verified in the Aug 2026 four-agent sweep. Reviewer offered no counter-source. Kept; 1166 remains listed first. |
| 2 | depression.html | "over 300 million" affected | ACCEPT | WHO depression fact sheet (updated 29 Aug 2025): "approximately 332 million people". Now "over 330 million" / "करिब ३३ करोड". |
| 3 | depression.html | postpartum "1 in 8 mothers globally" | ACCEPT (softened) | WHO depression fact sheet: "more than 10% of pregnant women and women who have just given birth experience depression"; WHO maternal MH page: 13% postpartum for any mental disorder. Now "more than 1 in 10". |
| 4 | depression.html | women "1.5 to 2 times" | ACCEPT | WHO fact sheet: "about 1.5 times more common among women". Now "about 1.5 times". |
| 5 | depression.html | "largest single contributor to disability" | ACCEPT | Current WHO wording is "a leading cause of disability"; GBD YLD rankings do not place depression first every year. Now "a leading cause of disability worldwide". |
| 6 | psychosis.html | lifetime prevalence 0.3–0.7% atypical | REJECT | DSM-5, Schizophrenia, Prevalence: "lifetime prevalence of schizophrenia appears to be approximately 0.3%–0.7%". Site matches DSM-5 exactly. |
| 7 | roots.html | Charaka dated ~400 BCE; four humours Galenic | PARTIAL | Charaka Samhita is conventionally dated c. 100 BCE to 200 CE; row now reads "Hippocrates, ~400 BCE; Charaka, ~100 BCE–200 CE". Four-humours part rejected: the Hippocratic corpus (On the Nature of Man) already sets out four humours; Galen systematised, did not originate. |
| 8 | roots.html | Abhidhamma misdated by "~800 BCE onward" | REJECT | "Onward" is an open bracket starting at the Upanishads; Abhidhamma (~3rd c. BCE) falls inside it. No change. |
| 9 | ocd.html | OCD chip "300.3 · F42.3" | ACCEPT | Site convention (chip hover text in build.py) is codes "as printed in the DSM-5" (2013): OCD = 300.3 (F42). F42.3 is the ICD-10-CM 2016 hoarding code (used by DSM-5-TR), not OCD. Now "300.3 · F42". |
| 10 | ocd.html | hoarding "300.3 · F42.3" | ACCEPT | DSM-5 (2013): hoarding = 300.3 (F42); the Nepali column already said F42. Now "300.3 · F42" in both. (If the site ever moves to DSM-5-TR codes: OCD F42.2, hoarding F42.3, excoriation F42.4.) |
| 11 | substance.html, ethics.html | Hari TED talk unhedged | ACCEPT | The "connection" thesis is a popular synthesis, not a research finding (Rat Park replications are mixed). Added a short caveat to both res-notes, both languages. Link kept: it exists and is verified. |
| 12 | suicide.html | "Most people who die communicated intent" | ACCEPT | Psychological-autopsy estimates vary widely by study and era; WHO myth/fact materials say people who talk about suicide "may be reaching out for help". Now "Many ... gave some warning; talking about it is often a reach for help". |
| 13 | ocd.html | Nepali code column drops DSM-5 codes | ACCEPT | Parity: Nepali rows now carry the same "300.3 · F42 / 312.39 · F63.3 / 698.4 · L98.1" pairs. |
| 14 | child.html | Nepali onset row adds "(before 18)" | ACCEPT | DSM-5 ID criterion C: "onset during the developmental period" with no age cut-off. Nepali now "विकासात्मक अवधिमा (बाल्यकाल वा किशोरावस्था)". |
| 15 | anxiety.html | Nepali drops "vasovagal" | ACCEPT | Parity: added "भासोभेगल" to the Nepali specifier note. |

Extra (not in the review, noticed during triage, not changed): psychosis.html line 72, the Nepali sentence omits the English parenthetical "(later re-analyses have contested how general this finding is)". Flagged for Pravo.

## chatgpt-review.md
`opencode run -m openai/gpt-5.6` produced 0 bytes on Pravo's run and on two reruns from this session (second rerun with an explicit "stay inside the repo" prefix). stderr shows it globbing content/ and quizzes/ and then exiting with code 0 and no text. Not an opencode permission issue on the repo files; looks like the model returns nothing. Needs a run in an interactive opencode session to see what it does after the glob.

## chatgpt-review.md (gpt-5.6, third run succeeded: 25 findings)

| # | File | Finding | Verdict | Primary source / reasoning |
|---|---|---|---|---|
| G1 | somatic.html | normal EEG "during a seizure" as proof | ACCEPT | DSM-5 conversion disorder text gives this very example but adds "this alone does not exclude all forms of epilepsy or syncope". Caveat added, both languages. |
| G2 | somatic.html | injury/incontinence row over-discriminates | ACCEPT (softened) | ILAE/LaFrance 2013: injury and incontinence occur in both; lateral tongue bite is fairly specific for epilepsy; video-EEG is the standard. Row rewritten. |
| G3 | substance.html | craving "usually within 20 to 30 minutes"; withdrawal not distinguished | PARTIAL | Duration kept as "often" (standard urge-surfing psychoeducation); added one line: withdrawal from heavy alcohol or sedatives (tremor, sweating, confusion, fits) needs a doctor (mhGAP alcohol withdrawal). |
| G4 | suicide.html | "involve family now" | ACCEPT | Now "a safe trusted person (family, when family is safe)". Consistent with the site's own GBV chapter. |
| G5 | suicide.html | risk levels used to determine care | PARTIAL | Ladder kept (it is what the CTEVT curriculum teaches); added "levels guide urgency, they do not predict; every plan is individual" (NICE NG225 direction). |
| G6 | pfa.html | "entirely unresponsive" listed only as a referral trigger | ACCEPT | WHO PFA guide: people with serious injuries or who are unresponsive need urgent medical care first. Added. |
| G7 | anxiety.html | panic symptoms "harmless" | ACCEPT | Now "once a doctor has ruled out a heart or lung cause, harmless". The paragraph already assumes ER first. |
| G8 | gbv.html | confidentiality "only with consent" without exceptions | ACCEPT | WHO IPV clinical handbook lists mandatory-reporting and imminent-danger limits; Act Relating to Children 2018 (s.66) creates a reporting duty. Added exceptions with "minimum needed". |
| G9 | ethics.html | minors guardian consent unqualified | ACCEPT | Added evolving capacity and "never when the guardian is the source of harm" (ACA A.2.d). |
| G10 | hiv.html | U=U stated as universal | ACCEPT | WHO 2023 policy brief: undetectable viral load = zero risk of sexual transmission. Now "sustained undetectable viral load ... sexually untransmittable". |
| G11 | trauma.html | ASD "the same picture" | ACCEPT | DSM-5 ASD criterion B: 9 or more of 14 symptoms in 5 categories. Now "closely related picture (9 or more of 14 symptoms)". |
| G12 | eating.html | "Low weight always takes priority" | PARTIAL | DSM-5 AN needs criteria B and C too; caption now conditions priority on the anorexia criteria being met. |
| G13 | rest.html | bipolar "alternating with depression" | ACCEPT | DSM-5: Bipolar I requires a manic episode only; Bipolar II requires hypomania plus MDE and no mania. Rewritten. |
| G14 | quizzes/anxiety.html | GAD "three" without "adults" | ACCEPT | DSM-5 GAD criterion C: three of six in adults, one in children. Question now says "In adults". |
| G15 | sleep.html | OSA needs the ≥15 prong | ACCEPT | DSM-5 OSA hypopnea criterion A2: ≥15 events/hour regardless of symptoms. Added. |
| G16 | child.html | Conduct Disorder missing "one in the last 6 months" | ACCEPT | DSM-5 CD criterion A. Added. |
| G17 | child.html | disability cards "red/blue" only | ACCEPT | Disability ID Card Distribution Directive 2075 under the Rights of Persons with Disabilities Act 2017: four classes (red ka, blue kha, yellow ga, white gha). Both languages fixed. |
| G18 | casemgmt.html | "Module 3 in one page" | ACCEPT | CLAUDE.md verified numbering: 2 Case Management, 3 Counseling Skill and Process. Now Module 2. |
| G19 | hiv.html | रक्तदान for transfusion | ACCEPT | Now रक्तसञ्चार. |
| G20 | eating.html | Nepali omits QTc | ACCEPT | Added "ईसीजीमा QTc लम्बिनु". |
| G21 | tools.html | NET as retelling until charge fades | PARTIAL | Schauer, Neuner, Elbert: chronological lifeline plus detailed narration of hotspots with habituation. Row rewritten; the habituation aim kept in softer words. |
| G22 | roots.html | Abhidhamma dating (second reviewer, see #8) | ACCEPT | Two independent reviewers flagged it; now "Upanishads from ~800 BCE; Abhidhamma from ~300 BCE". Supersedes verdict #8 above. |
| G23 | trauma.html | biological transmission claim | REJECT | The text says stress "changes the body's alarm systems, and those settings shape how children react"; it does not claim inherited epigenetic transmission. No change. |
| G24 | wellbeing.html | "Most distress is prevented or healed at the bottom two layers" | ACCEPT (softened) | IASC 2007 pyramid: lower layers serve the majority of the population; it makes no healing claim. Now "Most people are served by the bottom two layers alone". |
| G25 | map.html | ICD-10-CM as the code used in Nepal | ACCEPT | Nepal reports in WHO ICD-10; ICD-10-CM is the US modification printed in the DSM-5. Sentence now says so. |

## Nepali language review, DeepSeek (review/deepseek-nepali.md, 10 findings)

Rule applied (Pravo, 2026-08-27, now in CLAUDE.md): where no natural Nepali term exists, use the English term; Devanagari for spoken loans, Latin for codes and acronyms.

| # | File | Finding | Verdict | Reasoning |
|---|---|---|---|---|
| N1 | trauma.html | आत्मघाती for "self-destructive" | ACCEPT | आत्मघाती means suicidal; now आत्म-विनाशकारी. |
| N2 | rest.html | असहमति for "non-consent" | ACCEPT | Now सहमतिविनाको व्यक्ति जोडिए. |
| N3 | gbv.html | «खबर गराऔं» misspelt | ACCEPT (corrected form) | Reviewer proposed गराऊँ (causative, wrong). The NWC 1145 service is "Khabar Garaun" = खबर गरौं. Fixed to that. |
| N4 | ocd.html, map.html | coined मनोग्रस्ति-बाध्यता | ACCEPT | Field says ओसीडी. Now ओसीडी र सम्बन्धित; page h3 ओसीडी (Obsessive-Compulsive Disorder). |
| N5 | somatic.html | तिम्रो in a तपाईं site | ACCEPT | तपाईंको कुरा सुनियो. |
| N6 | anxiety.html | stranded को after a list | ACCEPT | List bracketed, को attached. |
| N7 | 6 files | पेसा should be पेशा | REJECT | पेसा is the standard spelling in the Nepal Academy Brihat Shabdakosh and MoE materials; site is consistent. |
| N8 | substance.html | word order "सबै" | ACCEPT | सबै अवैध लागुपदार्थलाई उछिन्छन्. |
| N9 | ethics.html | "...भए होइन" unclear | ACCEPT | Now "भए अभिभावक-सहमति लिइँदैन". |
| N10 | anxiety.html | प्यानिक (आतंक) | ACCEPT | आतंक = terror; now प्यानिक विकार. |

## Nepali language review, GPT-5.6 (review/chatgpt-nepali.md, 40 findings)

Accepted 34, rejected 1, already fixed via DeepSeek 4 (rest असहमति, ocd/map मनोग्रस्ति, ethics guardian clause, somatic तिम्रो). All accepted fixes applied in content/ and quizzes/.

Notable decisions:
- DRIFT accepted: gbv "alcohol as accelerant" had been rendered as the opposite (मत्थर पार्ने, calming); now हिंसा भड्काउने. GAD-7 scale anchors now match the validated Nepali GAD-7 wording (केही दिन / आधाभन्दा बढी दिन / झन्डै हरेक दिन). Substance-use definition now carries the impairment-or-distress clause. "Men who have sex with men" spelled out. Suicide exposure question restored. Anorexia "one of the highest" restored. Peripartum label now covers pregnancy. Callous-unemotional CD sentence, "recall variable", GAD later-onset comparison, supplements example, and the crosswalk sources sentence (Kohrt and Harper) restored in Nepali. Hypoarousal "अति कम" not "शून्य".
- TERM accepted under the new house rule: बर्नआउट, जेन्डर डिस्फोरिया, विथड्रअल, कन्डिसनिङ, ट्रान्स (nepal.html and quizzes/psychosis; समाधि means meditative absorption), प्रवासी (not आप्रवासी) site-wide, पुनर्बलन for reinforcement, सन्दर्भ भ्रम for delusion of reference, उपलब्धि-बोध for mastery, आवेग for OCD urge, जोडाइ for linkage, मापक for SUDS "anchor".
- LITERAL/TONE accepted: quiz intro (29 files), hero banner "गाह्रो भइरहेको छ" instead of "संकटमा", suicide page subtitle, wind-down hour, bodies in alarm, pyramid top, 4-P arrows, Maslow floors metaphor.
- SCRIPT accepted: लड वा भाग (7 places incl. SVG), सञ्चार.
- REJECT: pfa "हेर · सुन · जोड" as a heading; short imperative labels mirror WHO PFA's Look · Listen · Link and are used as action words, not instructions to the reader. Body text already uses तपाईं forms.
