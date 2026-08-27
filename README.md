# Mano Atlas (मनो एट्लास)

A free, open, bilingual (English / नेपाली) atlas of mental disorders: DSM-5 criteria in plain language, teaching diagrams, international examples, and the Nepali context throughout. Born from a CTEVT Psychosocial Counselor study project; written for anyone learning. Curriculum topics carry a small "CTEVT PSC curriculum" tag for counselling students.

A multi-page static site with a centred sidebar-plus-content layout, grouped navigation (Overview · Disorder categories · Counselling practice · Reference), client-side search, an English/नेपाली switcher, an Auto/Light/Dark theme switch, interactive "Quick check" questions on every page, and a site-wide footer with crisis helplines, a CC BY-NC-SA licence, and an error-report contact.

```
content/     one HTML fragment per section (the teaching text)
quizzes/     one small file per page: the three Quick-check questions
assets/      style.css, lang.js, search.js, search-index.js (generated)
build.py     SITE config + PAGES list; assembles everything → the *.html pages
*.html       generated pages (never edit these by hand)
```

## Where to change what

| You want to change… | Edit… |
|---|---|
| Teaching text of a page | `content/<name>.html` |
| A quiz question | `quizzes/<name>.html` |
| Helpline numbers, contact email, review date | the `SITE` dict at the top of `build.py` |
| Page list, titles, nav order and groups | the `PAGES` list in `build.py` |
| Colours, fonts, layout | `assets/style.css` |
| Language/theme/search/quiz behaviour | `assets/lang.js`, `assets/search.js` |

After any edit: `python3 build.py`, then commit and push. The pages, sidebar, home contents grid, pagers, gentle notes and the search index all regenerate themselves.

To add a chapter: create `content/<name>.html`, add one line to `PAGES` in `build.py`, run `python3 build.py` (this also regenerates the search index), commit.

## What's inside

- The DSM-5 category map with study status (studied / curriculum / beyond curriculum)
- Full DSM-5 diagnostic criteria (paraphrased for study) for the disorders covered in class and in the CTEVT curriculum: anxiety disorders, OCD & related, depression, trauma/PTSD, conversion & somatic, psychosis, child mental illness, eating disorders, sleep disorders, substance use
- International examples and Nepali context (idioms of distress, ethnopsychology, mass conversion, referral culture) for each
- Hand-drawn SVG teaching diagrams: fight-or-flight body map, the negative-reinforcement loop, the eating-disorder decision tree, a night hypnogram, the Nepali map of the person

## Sources

DSM-5 (APA, 2013) · CTEVT PSC Curriculum (2010) · Sub-module 1 & 2 class notes (Sunil Parajuli) · Mental Health-3 class notes · Introduction to Psychology · PSC Study Handbook Vol 1 & 2.

> Student study resource, not a diagnostic instrument. Criteria are paraphrased; verify wording against the DSM-5 before an exam.

## Development

Open `index.html` in a browser. To add content, edit the section markers (`<!-- ============ NN ... -->`). Every user-visible string appears twice: `class="en"` and `class="ne"`.

**House style rules:** no em-dashes anywhere (use a colon, comma, semicolon, or parentheses instead); no client case studies on the public site; resource links only when verified, otherwise cite by title; never invent Nepali prevalence figures.

## Deployment

Hosted on Vercel (static). `vercel.json` sets clean URLs; the site is served from the repository root.
