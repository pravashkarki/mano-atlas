# Agent notes (Mano Atlas)

The full working notes for this repository are in `CLAUDE.md`. Read that first; it is the source of truth and this file only adds the rules that matter most before you touch anything.

## Read-only site source

The root `*.html` files are generated. Never edit one by hand. Every teaching page comes from `content/<slug>.html`, its three Quick-check questions from `quizzes/<slug>.html`, its three Key points from `keypoints/<slug>.html`, and the page shell, navigation, numbering, reading time, search index, sitemap and social images from `build.py`. Edit the source, then run `python3 build.py` and commit the result.

`review/` holds planning, review and source ledgers. It is tracked in git and kept off the deployment by `.vercelignore`. `content/`, `quizzes/`, `keypoints/` and `build.py` are also never deployed: Vercel serves the generated HTML.

## Nepali is on hold

The site ships **English only**. `PHASE1_ENGLISH_ONLY = True` in `build.py` is what does that.

Do not do Nepali work while the hold is in force: do not write, translate, rewrite, expand or improve it, do not proofread, transliterate or language-check it, do not schedule it, and do not open work for it. The Nepali already in the repository is unreviewed, which is exactly why it is hidden rather than deleted.

Two things that look like exceptions and are not:

- **Keep the bilingual markup.** Every user-visible string still needs its `class="en"` / `class="ne"` pair, including text inside SVG diagrams, and `bi()` still fails the build without it. Never delete a Nepali half to get a build to pass. If `bi()` raises on a new English string, fill the slot, do not weaken the gate.
- **If you notice an error in the existing Nepali, leave it.** Note it in `review/` and move on. Fixing it is the work that is on hold.

The hold lifts only when Pravo says so. Do not reinstate the old "native Nepali proofread" task on your own initiative.

## Verify before you claim anything works

`python3 build.py` must run clean, and `grep -rn "—" content/ quizzes/ assets/ *.html` must return nothing. Em dashes are banned site-wide. Check the changed page in both light and dark themes; for contrast, compute the ratio from the theme tokens rather than judging a screenshot.

For anything factual, the rule is two independent sources, and articles repeating one study count as one source. If you cannot find the second source, say so in `review/` and keep the ledger honest. Do not invent a figure to fill a gap, and do not claim a number is verified when it is not.
