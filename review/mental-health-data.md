# Mental health data: Nepal and global (source-audited)

**Why.** The site needs a small, traceable set of Nepal-specific and global numbers, each carrying its source, year, sample, method, and a measured-or-modelled label, so no figure a reader sees is invented or unsourced.

This is a research reference for shaping a possible future data layer. It is not a public page, and no figure here is authorized for the live site yet.

## Premise check

- The repo already has 29 pages fact-checked against DSM-5, WHO, and Nepali sources (see the repo notes, "Content truth status"). That work checked the claims inside chapters. It did not build one source-audited data reference.
- `review/intake.md` and `review/curriculum-coverage.md` already record which claims landed where and which were rejected. This document is the source-side counterpart and does not reopen those decisions.
- No public data page exists in the repo, and none is authorized. This document is the input to shaping one, not the page.
- Every figure below was either opened by the main session from a primary source, or is explicitly marked as reported by a research subagent and not yet opened. The two tiers are never mixed.

## What ships

1. Source layer: which portals hold Nepal and world mental-health data, and what each one actually contains.
2. Nepal prevalence block, per disorder, measured (National Mental Health Survey 2020).
3. Care-pathways block, measured (National Mental Health Survey 2020).
4. Suicide block, measured (Nepal Police, FY 2080/81 factsheet).
5. Financing and workforce block, measured (Rai et al. 2021, Table 1).
6. Global and service-coverage block (WHO Mental Health Atlas 2024, with modelled sub-indicators labelled).
7. Pending-verification list (subagent-reported, not yet opened).
8. Open-decision list (global anchor, whether lifetime-only conditions ship, suicide trend, public use).

## 1. The source layer

### opendatanepal.com (primary target for Nepal)

A CKAN data portal run by Open Knowledge Nepal. The site advertises 630 datasets, 24 categories and 48 publishers; the API returns 418. Licence is CC BY 4.0 site-wide, and individual datasets carry their own, so check the dataset licence before republishing. It exposes a public CKAN API at `https://api.opendatanepal.com/api/3/action/`, so datasets can be fetched as CSV without scraping a page.

Mental-health-relevant datasets, verified by opening them:

| Dataset | Publisher | What it holds |
|---|---|---|
| National Mental Health Survey, Nepal (2020) | Nepal Health Research Council | 18 CSVs: per-disorder adult prevalence, adolescent prevalence and suicidality, care pathways, disability impact, alcohol and substance use |
| Suicide and Cyber Crime Data 2024 | Nepal Police HQ, Crime Investigation Department | Deaths by suicide, suicide deaths by year, methods by year (plus cybercrime) |
| Mental Health Service Indicators and Targets, National Strategy Framework 2077 to 2085 | Ministry of Health and Population | Baselines and policy targets for mental-health service access and coverage |
| Nepal Health Facility Survey 2077/78 (2021) | Ministry of Health and Population | Facility counts and service availability |
| Nepal Burden of Disease 2017 | Nepal Health Research Council | YLL, YLD and DALY data |
| Non-Communicable Disease Risk Factors and Prevalence 2013 to 2019 | Nepal Health Research Council | Risk-factor and prevalence series |
| Nepal Drug Users | Central Bureau of Statistics | Drug-use survey data |
| Status of health professionals permanently registered | Department of Health Services | Workforce registers |
| Health service statistics, major health indicators, health service coverage | Department of Health Services | Service and coverage series |
| Nepal Demographic and Health Survey 2022 | Ministry of Health and Population | 31 resources, all maternal, child and nutrition. No mental-health resource. Do not cite it for prevalence. |

The 2019 Burden of Disease entry on the portal is column definitions and a codebook only. The 2017 edition is the one with data.

### Other Nepal official portals

- `https://data.nsonepal.gov.np` (National Statistics Office). The NSO data portal, with the Nepal Living Standards Survey 2022/23, national accounts, population, poverty and social series. This is the source for social and economic context, not mental-health prevalence.
- `https://microdata.nsonepal.gov.np` (National Data Archive, NADA). Survey and census microdata with metadata public and data released by application. Holds Department of Health Services, Civil Registration, MICS 2024/25 and DHS collections. Use for original analysis, not for quoting a number on the site, because access is controlled.

### World sources for comparison

- WHO Global Health Observatory, `https://www.who.int/data/gho`. Country and regional health indicators, downloadable.
- `https://data.who.int`. WHO's current data platform.
- WHO Mental Health Atlas, `https://www.who.int/teams/mental-health-and-substance-use/data-research/mental-health-atlas`. The normative survey on policy, financing, workforce and service coverage. Already used for the global block.
- WHO Global Health Estimates. Causes of death and disability by country, with a consistent modelling method.
- Our World in Data mental health, `https://ourworldindata.org/mental-health`. The best fit for a general reader. CC BY, country comparison charts, embeddable, and it includes South-East Asia. It also publishes a chart counting how many countries have primary prevalence data at all, which is the caveat that matters: most countries have no survey, so modelled figures dominate global comparisons and Nepal is comparatively well measured.
- IHME Global Burden of Disease and the GHDx health data catalogue. The modelled alternative, and the source of the Global Burden of Disease figures.

## 2. Nepal prevalence, per disorder (measured)

Source: National Mental Health Survey 2020, Ministry of Health and Population with Nepal Health Research Council, fieldwork January 2019 to January 2020, instrument MINI and DSM-5, nationally representative household survey. Peer-reviewed as Dhimal et al., DOI `10.33314/jnhrc.v19i04.4017`. The tables below are the survey's own CSVs, republished on opendatanepal.com.

| Disorder | Timeframe | Percent | 95% CI |
|---|---|---|---|
| Any mental disorder | Lifetime | 10.0 | 8.5 to 11.8 |
| Any mental disorder | Current | 4.3 | 3.5 to 5.2 |
| Mood disorders | Lifetime | 3.0 | 2.5 to 3.7 |
| Major depressive disorder | Lifetime | 2.9 | 2.3 to 3.7 |
| Major depressive disorder | Current | 1.0 | 0.8 to 1.4 |
| Bipolar affective disorder | Lifetime | 0.2 | 0.1 to 0.5 |
| Neurotic and stress-related disorders | Current | 3.0 | 2.5 to 3.6 |
| Dissociative disorder | Current | 1.0 | 0.7 to 1.4 |
| Generalized anxiety disorder | Current | 0.8 | 0.6 to 1.1 |
| Panic disorder | Lifetime | 0.7 | 0.6 to 0.9 |
| Somatic symptom disorder | Current | 0.5 | 0.3 to 0.8 |
| Panic disorder | Current | 0.4 | 0.3 to 0.5 |
| Alcohol use disorder | Past 12 months | 4.2 | 3.6 to 4.8 |
| Obsessive compulsive disorder | Current | 0.2 | 0.1 to 0.4 |
| Phobic anxiety disorder | Current | 0.2 | 0.1 to 0.4 |
| Agoraphobia | Current | 0.2 | 0.1 to 0.4 |
| Other substance use disorder | Past 12 months | 0.2 | 0.1 to 0.3 |
| Schizophrenia, schizotypal and delusional disorders | Lifetime | 0.2 | 0.1 to 0.3 |
| Bipolar affective disorder | Current | 0.1 | 0.1 to 0.3 |
| Social anxiety disorder | Current | 0.1 | 0.0 to 0.3 |
| Schizophrenia, schizotypal and delusional disorders | Current | 0.1 | 0.1 to 0.3 |
| Post-traumatic stress disorder | Current | 0.0 | 0.0 to 0.2 |

Adolescents, lifetime any disorder: 5.2% (95% CI 4.2 to 6.4). Sampled 9,200 adults and 5,888 adolescents; 99% of those contacted agreed to take part.

Three cautions on this table.

- The PTSD figure is 0.0% with a confidence interval up to 0.2%. That is a floor, not an absence. Never print it as zero.
- Alcohol use disorder at 4.2% over the past year is higher than major depressive disorder at 2.9% lifetime. Any framing that leads with depression as the commonest condition misleads.
- The paper's own narrative mixes timeframes. In a passage about current prevalence it gives panic disorder as 0.7%, which is the lifetime figure; the current figure is 0.4%. Always take the number from Table 2, not from the running text.

### The "current" window, resolved

The CSVs use three labels, "Lifetime", "Current" and "Past 12 Months", without defining "Current". The prevalence paper reports current beside lifetime and does not define the window either. The window is nonetheless established from the survey's own design:

- The survey administered the Barriers to Accessing Care Evaluation and a help-seeking questionnaire to participants "diagnosed with any mental disorders in the past 12 months" (pilot report, PMC7819577).
- MINI 7.0.2, the instrument used, asks about the past 12 months for the modules in this table.

So "current" means past 12 months. The evidence is the survey's own instrument frame plus the standard MINI frame, not a sentence in the prevalence paper. One line from the full NMHS report would confirm it outright, and that confirmation is still outstanding. Until then, label the figure "current, meaning the past 12 months" and cite the survey, which is honest about the basis.

Consequence for comparison: any-disorder current is 4.3% (3.5 to 5.2) and any-disorder lifetime is 10.0% (8.5 to 11.8). Compare a current figure only with 4.3%, and a lifetime figure only with 10.0%. Setting a current figure against the 10.0% lifetime figure misleads, because 10.0% is 2.3 times the current figure. For generalized anxiety and obsessive compulsive disorder there is no lifetime figure in the survey, so no such correction can be computed for them at all, which is a reason not to set any per-disorder figure beside an any-disorder reference.

Two timeframes in one sentence is the error to design against. Five of the seven conditions covered by the depression, anxiety and OCD chapters are current-only (generalized anxiety 0.8, phobic anxiety 0.2, agoraphobia 0.2, social anxiety 0.1, obsessive compulsive 0.2), and only major depressive disorder and panic disorder carry both timeframes. The survey publishes no per-disorder reference figure, only the any-disorder 4.3% and 10.0% pair, so there is nothing reliable for a per-disorder figure to be measured against.

### The comparison the survey itself makes

The paper compares Nepal with the Indian mental health survey at 13.7% lifetime, using the same MINI tool, and describes its own headline as "one out of every ten adults in Nepal has one or more mental morbidities". For a chapter, this is a better comparison than any Global Burden of Disease figure: same instrument, same method, no modelling, and it is the comparison the authors chose. Use the India figure for context and leave the modelled global releases out of the chapter blocks.

## 3. Care pathways (measured)

Source: National Mental Health Survey 2020, percentages among adults who have a mental disorder. The treatment gap is the first row of this block.

| Item | Percent | 95% CI |
|---|---|---|
| Talked to anyone about symptoms | 40.1 | 36.8 to 43.5 |
| Sought treatment for symptoms | 22.7 | 19.3 to 26.5 |
| Did not seek treatment (the treatment gap) | 77.3 | |
| Adhered to treatment prescribed | 21.1 | 17.6 to 25.2 |
| Admitted to hospital | 3.7 | 2.5 to 5.5 |
| Talked to a health service provider | 3.5 | 2.2 to 5.5 |
| Consulted a faith healer | 6.7 | 4.9 to 9.0 |
| Consulted a traditional healer | 1.9 | 1.1 to 3.4 |

Who people went to, among adults with a disorder: a non-specialist doctor 8.8%, a psychiatrist 6.5%, a faith healer 6.7%, a counsellor 0.3%, a psychologist 0.2%, a paramedic 0.3%, a female community health volunteer 0.0%.

This block is the strongest argument the site has for its care notes and helplines. Most people tell a family member, and only a small minority reach a health worker.

One third-party paper restates this block as 52.6% spoke to someone, 21.2% sought treatment and 17.8% completed treatment, where the survey's own CSVs give 40.1%, 22.7% and 21.1%. The CSVs are the primary tables, so the site uses them. The discrepancy is recorded because it exists in the literature and a reader may meet it.

## 4. Suicide (measured)

Source: Annual Factsheet on Suicide and Cyber Crime, fiscal year 2080/81, Police Headquarters, Crime Investigation Department, Naxal, Kathmandu, republished on opendatanepal.com.

| Fiscal year | Suicide deaths |
|---|---|
| 2020 to 21 | 7,117 |
| 2021 to 22 | 6,792 |
| 2022 to 23 | 6,993 |
| 2023 to 24 | 7,223 |

By category in FY 2080/81: men 4,011, women 2,364, girls 574, boys 272.

Two things to record honestly. The source's own year table says 7,223 for FY 2080/81 while its own category table sums to 7,221, so the two figures differ by two cases inside one factsheet. And this four-year series shows a dip then a recovery, not a steep rise, so it does not support a claim of an 82% increase. Any trend claim needs a longer police series, cited as such.

## 5. Nepal financing and workforce (measured, 2020)

Source: Rai et al., BJPsych International, DOI `10.1192/bji.2020.58`, Table 1. Administrative and survey counts for 2020, with 2008 comparators where given.

| Indicator | 2020 | 2008 |
|---|---|---|
| Mental health share of the health budget | 0.2% | 0.8% |
| Psychiatrists | 200 | 39 |
| Psychiatric beds | 500 | 385 |

Also: 25 inpatient psychiatric facilities; 3 child psychiatrists; 30 clinical psychologists at MPhil and 200 at MA level; 50 psychiatric nurses; 700 psychosocial counsellors trained to a 780-hour NGO curriculum; MD Psychiatry at 16 institutions. The health budget itself was 6.15% of the national budget in 2020.

## 6. Global and service coverage (WHO Mental Health Atlas 2024)

Source: WHO Mental Health Atlas 2024, ISBN 9789240114487, published 2 September 2025, data from 144 countries, read from the WHO IRIS primary text.

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

## 7. Reported by subagents, not yet opened by the main session

- Legal: no separate Mental Health Act. Supreme Court order 11433, case 077-WO-0035, 2 December 2024, full text 31 May 2025 at `https://nkp.gov.np/full_detail/10528`, states a separate specialised law remains a precondition and a 2006 writ went unimplemented for 18 years.
- First National Mental Health Policy 1996.
- Treatment caseload 281,570 on treatment in FY 2081/82. People on treatment, not annual unique cases.
- Community care: a four-municipality model exists.
- Stigma prevalence figures, source not confirmed.
- The longer police suicide series behind the 82% claim.
- Global anchors: GBD 2019 gives 654.8 million (2019); GBD 2023 gives 1.17 billion (2023, published 2026); WHO 2025 gives 1.095 billion (2021, 13.6%). None opened by the main session.

## Cases and decisions

- Attribution. The survey is Ministry of Health and Population with Nepal Health Research Council, not the National Human Rights Commission. Two earlier attributions in this repo's history were wrong; correct them if they resurface.
- The 0.2% framing. Mental health received 0.2% of the health budget in 2020, and the health budget was 6.15% of the national budget. Some secondary write-ups say "0.2% of the national health budget", which reads as 0.2% of national. State both shares whenever the 0.2% appears.
- Per-chapter prevalence is the highest-value use. The survey ships one CSV per disorder, so each disorder section that teaches a condition can carry that condition's Nepal figure with its year. The mapping is mechanical and checkable, it needs no new page, and it puts the number where the reader meets the condition.
- Key the data per disorder section, not per chapter. The anxiety chapter is six separate disorder cards and the OCD chapter is two, the second being body dysmorphic disorder, which the survey does not cover. A single figure per chapter would misrepresent every section it did not describe.
- Show the figure as a number, not a bar. The values run from 0.1% to 2.9% across the conditions these chapters teach, so a bar on a ten-percent scale renders most of them as a stub inside their own confidence interval, and any minimum width would overstate the value. A large figure with its timeframe and interval is readable at any value and cannot lie about scale. The number takes the calm teal, not the chapter colour: the chapter colours clear 4.5:1 on the Nepal wash in both themes for depression and obsessive compulsive but not for anxiety, and the house rule reserves teal for non-crisis content anyway. An "about one in N adults" line is available if wanted, but it must not claim a denominator, because 9,200 is the sample size and not a population.
- The three "no national prevalence figure exists" statements, not two. The OCD chapter, the specific phobia card in the anxiety chapter, and the site-wide standing rule on the Nepal chapter all claim it. The eating disorders sentence is true, because the survey carries no eating-disorder row, and the sleeping half of the standing rule is true for the same reason. Six strings counting the bilingual twins. Fixing the chapter prose without the standing rule leaves the site contradicting itself.
- Global anchor conflict. GBD 2019, GBD 2023 and WHO 2025 differ because they are different releases and methods. Inside a chapter, do not use them at all: the survey's own India comparison at 13.7% lifetime uses the same MINI instrument, so it is the honest context. If a global anchor is ever needed, pick one release, label it, and never mix two in one sentence.
- Measured versus modelled. The Atlas depression-treatment 9.1% is modelled. Every figure in this document carries that label.
- The "current" window, resolved. "Current" means the past 12 months, established from the survey's own help-seeking frame and the MINI frame rather than from a sentence in the prevalence paper. Publish it as "current, meaning the past 12 months" and keep the one outstanding confirmation from the full report noted in the table section. Remaining open decision: whether the two lifetime-only conditions ship at all.
- The PTSD floor. 0.0% is a rounding floor with a confidence interval reaching 0.2%. Publishing it as zero would be wrong.
- Suicide figures. Cite 7,223 or 7,221 with the table it came from, because the source disagrees with itself by two. Do not claim a rising trend from a four-year series that dips in the middle.
- Public use. Whether any of this becomes public content is a separate shaped piece. When it does, every string needs both `en` and `ne`, the survey year must be shown, and Nepali needs a native proofread (still open for chapters 19, 20, 22, 24).

## Security

This document holds data, not code. The risks are publishing a number that is mislabelled, misattributed, wrong, or stale. The gate: every figure carries source, year, sample or countries, method, and a measured-or-modelled label. No chart or dashboard, no untraceable subnational figure, no invented Nepali prevalence. The survey fieldwork ended in January 2020, so any figure published now is at least six years old and must say so. Nothing here reaches the live site without the Founder's go and the bilingual rule.

## Validation

A reviewer re-opens each source and finds the figure:

- Prevalence, care pathways: the NMHS 2020 CSVs on opendatanepal.com, or DOI `10.33314/jnhrc.v19i04.4017`, or the eLibrary report.
- Suicide: the Police Headquarters FY 2080/81 factsheet CSVs on opendatanepal.com.
- Financing and workforce: DOI `10.1192/bji.2020.58`, Table 1.
- Global: ISBN 9789240114487, WHO IRIS full text.

Done means: every figure on the site traces to a source in this document, every modelled figure is labelled modelled, every timeframe is defined, and every item in section 7 is either verified into the sections above or dropped.

## Rollout

Internal first. This document is mirrored to `~/Obsidian/Mano/sources/mental-health-data.md`. Findings and the open decisions are posted as a signed comment on Basecamp card 10343685092 (Shaping). Any public data layer is a new shaped card, not part of this work.

Card: https://app.basecamp.com/5746833/buckets/49041895/card_tables/cards/10343685092
