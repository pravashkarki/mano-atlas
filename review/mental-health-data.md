# Mental health data: Nepal and global (source-audited)

**Why.** The site needs a small, traceable set of Nepal-specific and global numbers, each carrying its source, year, sample, method, and a measured-or-modelled label, so no figure a reader sees is invented or unsourced.

This is a research reference for shaping a possible future data page. It is not a public page, and no figure here is authorized for the live site yet.

## Premise check

- The repo already has 29 pages fact-checked against DSM-5, WHO, and Nepali sources (see `CLAUDE.md`, "Content truth status"). That work checked the claims inside chapters. It did not build one source-audited data reference.
- `review/intake.md` and `review/curriculum-coverage.md` already record which claims landed where and which were rejected. This document is the source-side counterpart and does not reopen those decisions.
- No public data page exists in the repo, and none is authorized. This document is the input to shaping one, not the page.
- Every figure below was either opened by the main session from a primary or peer-reviewed source, or is explicitly marked as reported by a research subagent and not yet opened. The two tiers are never mixed.

## What ships

1. Nepal prevalence block (measured, National Mental Health Survey 2020).
2. Nepal financing and workforce block (measured, 2020 counts).
3. Global and service-coverage block (WHO Mental Health Atlas 2024, with modelled sub-indicators labelled).
4. Pending-verification list (subagent-reported, not yet opened by the main session).
5. Open-decision list (global anchor, the "current" prevalence window, public-page and bilingual timing).

## The data

### 1. Nepal prevalence (measured)

Source: National Mental Health Survey 2020, Ministry of Health and Population with Nepal Health Research Council. Peer-reviewed as Dhimal et al., Journal of Nepal Health Research Council, DOI `10.33314/jnhrc.v19i04.4017`; report on the NHRC eLibrary, handle `20.500.14356/3085`. Fieldwork 2019 to 2020. Instrument: MINI, DSM-5. Sampled 9,200 adults and 5,888 adolescents, 15,088 total.

| Figure | Value |
|---|---|
| Adults, lifetime any mental disorder | 10.0% (95% CI 8.5 to 11.8) |
| Adults, current any mental disorder | 4.3% (95% CI 3.5 to 5.2) |
| Adolescents, lifetime any mental disorder | 5.2% |
| Suicidality, adults | 7.2% |
| Suicidality, adolescents | 4.1% |

Also reported: current suicidal ideation 6.5%, lifetime suicide attempt 1.1%. Confirm which subgroup each belongs to before publishing.

### 2. Nepal financing and workforce (measured, 2020)

Source: Rai et al., BJPsych International, DOI `10.1192/bji.2020.58`, Table 1. These are administrative and survey counts for 2020, with 2008 comparators where given.

| Indicator | 2020 | 2008 |
|---|---|---|
| Mental health share of the health budget | 0.2% | 0.8% |
| Psychiatrists | 200 | 39 |
| Psychiatric beds | 500 | 385 |

Also: 25 inpatient psychiatric facilities; 3 child psychiatrists; 30 clinical psychologists at MPhil and 200 at MA level; 50 psychiatric nurses; 700 psychosocial counsellors trained to a 780-hour NGO curriculum; MD Psychiatry at 16 institutions. The health budget itself was 6.15% of the national budget in 2020.

### 3. Global and service coverage (WHO Mental Health Atlas 2024)

Source: WHO Mental Health Atlas 2024, ISBN 9789240114487, published 2 September 2025, data from 144 countries. Read from the WHO IRIS primary text.

| Indicator | Global median | Range |
|---|---|---|
| Mental health share of government health spending | 2.1% (same as 2017 and 2020) | 1.5% or less in LMIC to 4.3% in HIC |
| Mental health spending per capita | US$2.69 | US$0.04 low-income to US$65.89 high-income |
| Specialized mental health workers per 100,000 | 13.5 | 1.1 to 2.4 in LIC and LMIC, 67.2 in HIC |
| Children and adolescents, workers per 100,000 | 1.5 | |
| Depression treatment coverage | 9.1% (modelled, 2021) | not an Atlas measurement |
| Psychosis treatment coverage | 40% (22 countries, 2024) | 29% in 2020 |

Workforce composition: mental health nurses 43%, psychologists 22%, psychiatrists 16%.

The 9.1% depression figure is a modelled estimate of minimally adequate treatment coverage for major depressive disorder from a 2021 global analysis, carried into the Atlas. The report states it could not be computed from Atlas data. Label it modelled wherever it is used.

### 4. Reported by subagents, not yet opened by the main session

Verify each against the primary source before any use. Each is currently shaping input only.

- Treatment gap 77.3%: the share of people with a disorder who received no treatment. Source not yet confirmed.
- Suicide, police-recorded: 7,221 deaths in FY 2080/81, up 82% from 3,977 in FY 2068/69. A separate EDCD figure of 7,223 conflicts. WHO modelled estimate 9.77 per 100,000 (2019) is a different quantity.
- Legal: no separate Mental Health Act. Supreme Court order 11433, case 077-WO-0035, 2 December 2024, full text 31 May 2025 at `https://nkp.gov.np/full_detail/10528`, states a separate specialised law remains a precondition and a 2006 writ went unimplemented for 18 years, still unimplemented as of 31 December 2025.
- First National Mental Health Policy 1996.
- Treatment caseload 281,570 on treatment in FY 2081/82. This is people on treatment, not annual unique cases.
- Community care: a four-municipality model exists.
- Stigma prevalence figures, source not yet confirmed.
- Global anchors: GBD 2019 gives 654.8 million (2019); GBD 2023 gives 1.17 billion (2023, published 2026); WHO 2025 gives 1.095 billion (2021, 13.6%). None of these has been opened by the main session.

## Cases and decisions

- Attribution. The survey is Ministry of Health and Population with Nepal Health Research Council, not the National Human Rights Commission. Two earlier attributions in this repo's history were wrong; correct them if they resurface.
- The 0.2% framing. Mental health received 0.2% of the health budget in 2020, and the health budget was 6.15% of the national budget. Some secondary write-ups say "0.2% of the national health budget", which reads as 0.2% of national. State both shares whenever the 0.2% appears.
- Global anchor conflict. GBD 2019 (654.8 million), GBD 2023 (1.17 billion) and WHO 2025 (1.095 billion) differ because they are different releases and methods. Pick one anchor, label its release, and never mix two in the same sentence. Open decision: which one the site uses.
- Measured versus modelled. The Atlas depression-treatment 9.1% is modelled, not measured. Every figure in this document carries that label.
- The "current" window. The survey reports a "current" adult prevalence of 4.3%. The reporting window (12-month or past-month) must be read from the report before "current" is published. Do not publish it until resolved.
- Sample N. The peer paper reports 9,200 adults sampled; a subagent read 8,940 completed adult interviews. Reconcile the two before publishing any rate.
- Public page. Whether any of these figures becomes a public, bilingual data page is a separate shaped piece. It is not authorized. When it happens, every string needs both `en` and `ne`, and Nepali needs a native proofread (still open for chapters 19, 20, 22, 24).

## Security

This document holds data, not code. The risk is publishing a number that is mislabelled, misattributed, or wrong. The gate: every figure carries source, year, sample or countries, method, and a measured-or-modelled label. No chart, no dashboard, no untraceable subnational figure, no invented Nepali prevalence. Nothing here reaches the live site without the Founder's go and the bilingual rule.

## Validation

A reviewer re-opens each Tier 1 source by DOI or handle and finds the figure in the text:

- Prevalence: DOI `10.33314/jnhrc.v19i04.4017`, or the eLibrary report.
- Financing and workforce: DOI `10.1192/bji.2020.58`, Table 1.
- Global: ISBN 9789240114487, WHO IRIS full text.

Done means: every figure on the site traces to a Tier 1 source in this document, every modelled figure is labelled modelled, and every item in section 4 is either verified into section 1 to 3 or dropped.

## Rollout

Internal first. This document is mirrored to `~/Obsidian/Mano/sources/mental-health-data.md`. Findings and the open decisions are posted as a signed comment on Basecamp card 10343685092 (Shaping). A public bilingual data page is a new shaped card, not part of this work.

Card: https://app.basecamp.com/5746833/buckets/49041895/card_tables/cards/10343685092
