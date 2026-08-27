# Mano Atlas (मनो एट्लास)

A free, open, bilingual (English / नेपाली) atlas of mental disorders — DSM-5 criteria in plain language, teaching diagrams, international examples, and the Nepali context throughout. Born from a CTEVT Psychosocial Counselor study project; written for anyone learning. Curriculum topics carry a small "CTEVT PSC curriculum" tag for counselling students.

A multi-page static site with a sticky, grouped sidebar (Overview · Disorder categories · Reference) and an English/नेपाली switcher that persists across pages.

```
content/     one HTML fragment per section (edit these)
assets/      style.css, lang.js, search.js, search-index.js (generated)
build.py     assembles content/ + sidebar shell → the *.html pages
*.html       generated pages (index, anxiety, ocd, depression, …)
```

To add a chapter: create `content/<name>.html`, add one line to `PAGES` in `build.py`, run `python3 build.py` (this also regenerates the search index), commit.

## What's inside

- The DSM-5 category map with study status (studied / curriculum / beyond curriculum)
- Full DSM-5 diagnostic criteria (paraphrased for study) for the disorders covered in class and in the CTEVT curriculum: anxiety disorders, OCD & related, depression, trauma/PTSD, conversion & somatic, psychosis, child mental illness, eating disorders, sleep disorders, substance use
- International examples and Nepali context (idioms of distress, ethnopsychology, mass conversion, referral culture) for each
- Hand-drawn SVG teaching diagrams: fight-or-flight body map, the negative-reinforcement loop, the eating-disorder decision tree, a night hypnogram, the Nepali map of the person

## Sources

DSM-5 (APA, 2013) · CTEVT PSC Curriculum (2010) · Sub-module 1 & 2 class notes (Sunil Parajuli) · Mental Health-3 class notes · Introduction to Psychology · PSC Study Handbook Vol 1 & 2.

> Student study resource — not a diagnostic instrument. Criteria are paraphrased; verify wording against the DSM-5 before an exam.

## Development

Open `index.html` in a browser. To add content, edit the section markers (`<!-- ============ NN ... -->`). Every user-visible string appears twice: `class="en"` and `class="ne"`.

## Deployment

Hosted on Vercel (static). `vercel.json` sets clean URLs; the site is served from the repository root.
