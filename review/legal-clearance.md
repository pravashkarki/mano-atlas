# Pre-launch clearance: what has to be settled before Mano Atlas carries a licence and a disclaimer

Written 2026-09-26, on the Founder's instruction that all data be verified twice and cited properly, and that nothing on the site should leave him exposed to liability he did not choose.

**This is not legal advice.** Nothing here is a legal opinion. It is the list of questions a lawyer needs to answer, with the facts already gathered so the lawyer does not have to re-derive them. Every item says what we know, what the risk is, and what to do.

## What the site actually is, for the lawyer's framing

A free bilingual static site, 34 pages, no accounts, no payments, no user data collected, no diagnostic tool, no advice engine. Teaching text for a mental-health worker course, plus crisis contact numbers. No advertising. The strongest single fact for a defence is the second one: the site is educational content, it never assesses a user and never tells an individual what is wrong with them.

The most important protective boundary is one we already hold and must not lose: **no page ever diagnoses, triages or tells a reader what treatment to get.** The "A skill to try" boxes are skills, never treatment claims. Keep that boundary, and it is worth stating explicitly in the terms as a fact about the product rather than as a promise.

## Blocking: the rights in the teaching text are not established

**What we know.** `review/intake.md` records 8 teaching decks from named instructors landing in the chapters, 5 fully included and 3 mostly. Example entries: "Sub module 1 (Sunil Parajuli), 12 pp, Mostly (9 of 12 full)", "Counseling Approaches (Sunil Parajuli), 27 pp, Included (17 of 21 full)", "Applying Verbal Communication Skill (Sunil Parajuli), 21 pp, Included (9 of 9 skills)". The ledger also records softenings, for example a claim about speaking without proof being a crime changed to "say you do not know".

**The risk.** Adapting a named colleague's instructional prose is a derivative work. Until we know what those authors agreed to, we cannot know that the site can be licensed openly at all. A licence grant we have no right to make is a misrepresentation, and it is the kind of thing that becomes a problem when someone commercialises a translation from it.

**To clear.**
1. Ask each named author what licence they are willing to grant for the adapted material: open, or all rights reserved with our own writing layered on.
2. Record each answer per author per deck, with the date, in the intake ledger. Silence is not permission.
3. Until answered, the site carries no open licence on the derived teaching text.

A Nepali-language government training course with 8 decks from what appear to be the same small professional community makes this more likely to be resolvable by asking than by arguing. Ask.

## The licence itself: split it, because one licence cannot cover this site

A single footer statement of "CC BY-NC-SA" is legally imprecise here, because the site is a mixed collection. It mixes material with genuinely different terms:

| Element | Position |
|---|---|
| Original prose, diagrams, illustrations, quizzes, keypoints | Ours, licenceable |
| Build code, CSS, JavaScript | Ours, but a creative licence is the wrong tool for code |
| Instructor-derived teaching text | Third-party until cleared above |
| DSM-5 criteria and codes | APA holds copyright on its text; we paraphrase, codes are facts |
| NMHS, police, health-ministry figures | Government data, per-dataset licence terms |
| WHO and GBD figures | Licence terms on the source document |
| ACA Code of Ethics 2005 | Quoted in part on the ethics page |
| GAD-7 instrument | A published instrument, not a free text |
| Lally and Valentine-French 2021 | Already CC BY-NC-SA 3.0, cited only |
| Nepali consent form | Correctly summarised, not reproduced |

**Recommendation to put to the Founder, subject to the rights question above.**

- **Content:** CC BY-NC-SA 4.0. The existing intent was NC-SA, and NC is the right instinct for teaching material: it keeps paid course material built from it from undercutting a free resource. Say 4.0, never an unversioned reference.
- **Code:** MIT, separately stated. Creative licences on code create real friction for other people and buy nothing here.
- **Name and logo:** all rights reserved, stated explicitly. Without that, an open content licence would arguably let someone rebrand the site and call it the atlas.
- **Mixed collection:** a source register naming each third-party input and its terms, plus a statement that the collection is mixed and per-item terms apply. This is what makes a single site-wide licence claim honest.

**One tension to decide, not to paper over.** NC stops a private college charging for a course built from this material, and stops a translation being sold. That may be the intent, or it may cost more reach than it protects. SA is also hard to enforce in Nepal, so it is the part of the licence most likely to be ignored. If maximum spread matters more than preventing commercial reuse, CC BY 4.0 without NC is the alternative, and it is a one-word change with real consequences either way. **This is a mission decision and it is the Founder's, not mine.**

### Decided 2026-09-26: NC, no charge to anyone

The Founder's answer: "nobody can charge using this content." So the content licence is **CC BY-NC-SA 4.0**, and the tension above is closed in favour of protecting the free resource over maximum spread.

**What NC does and does not do, stated plainly.** Nobody being able to charge is already the default position: copyright applies automatically, and without a licence nobody may copy commercially at all. A licence is a permission, not a prohibition. So the Founder has chosen how generous that permission is for non-commercial reuse, and NC is the clause that carves commercial use out. The intent is served, with one honest limit: **NC is not self-enforcing.** It is routinely ignored, and it carries no takedown mechanism of its own. The practical protection is the copyright notice, the licence statement, and willingness to ask someone to take something down. Do not describe the clause as preventing anything on its own.

**NC-SA rather than NC-ND.** ND would forbid derivatives outright, which would block translation and adaptation entirely. Not wanted. SA instead keeps the no-charging intent attached to any derivative, so a free translation or a free course must also stay non-commercial, which is what makes the clause propagate instead of evaporating.

**What shipped on this decision, 2026-09-26.**

- `LICENSE` at the repo root: content CC BY-NC-SA 4.0 with BY/NC/SA terms spelled out in plain language, code MIT with the full text, a not-covered list, and an explicit scope note.
- `/terms` page, built by `terms_html()` in `build.py` and linked from the footer on every page. Standalone like `/vault`, so it is not in `PAGES` and renumbers nothing.
- Footer licence line reworded from an unscoped "Content licensed CC BY-NC-SA 4.0" to "Our own content is CC BY-NC-SA 4.0: share and adapt with credit, never for charge", with a link to the terms page.
- The safeguarding notice added to the footer, because the error-report address was already live on every page and the notice was not.
- `README.md` licence claim replaced with the scoped version and a pointer to `LICENSE`.

**Still open, and the licence does not fix it.** The derived teaching text is still not ours to license. The terms page and the LICENSE both say so in the open rather than papering over it, and the per-author permission request is the item that actually closes the gap.

## Liability: what a disclaimer can and cannot do

The Founder's stated wish is not to take ownership of errors. That is legitimate and a disclaimer is the normal tool. Two hard limits on it.

**A disclaimer cannot make a wrong crisis number safe.** If the site tells someone in a crisis to call a number that is wrong, or to a service that cannot help, no footer wording helps. The helpline numbers are the highest-liability content on the site and the only content where a user's harm follows directly from our error. The data ledger lists four. This is the first thing to verify twice, and the one place where the effort spent is proportionate to the exposure.

**A disclaimer cannot cure a fabricated or uncited figure.** Hence the two-source rule, and hence `review/data-ledger.md`. Its nine unsourced epidemiology figures are not a licensing problem but they are a misrepresentation problem, and they are the ones most likely to be wrong.

**What the disclaimer should say, and not say.** It should say the site is educational, is not medical or legal advice, is not a substitute for assessment, and that the reader is responsible for decisions. It should not say the content is provided "as is" with no responsibility, because a court may read a total disclaimer as an attempt to disclaim negligence, and courts do not always honour that.

**What it must not do:** promise that nothing on the site is ever wrong, or imply a clinical guarantee.

## The error-report channel has a legal edge that is easy to miss

The Founder wants readers to be able to email corrections. Good practice, and worth doing. But note the interaction with a rule already on the site: the Act Relating to Children 2075, section 68(1), which states that anyone who learns of violence or sexual abuse against a child must inform the nearest police, with informant protection under 68(3) and 68(4).

The exposure is specific. A site about counselling will receive disclosures. If a reader uses a "report an error" address to describe abuse of a child, then whoever reads that email may have acquired a reporting duty, and a duty the site never intended to create. Nothing in a footer prevents that.

**Before the address goes out:**
1. Publish a safeguarding notice beside it, saying that disclosures of abuse against a child will be handled by the statutory route and not kept confidential, and that emergency services should be used when someone is at risk now.
2. Decide who reads that inbox, and make sure a single named person or the team does, with the duty written down.
3. Route the address to something that is read and answered, not an unattended alias, or state honestly that it is not monitored. An unmonitored "report an error" box is worse than none.

This is the item most likely to put the Founder somewhere he did not intend to be, and it is created by the good instinct rather than by anything careless.

## Dataset and source licence terms to confirm

- **Open Data Nepal** is CC BY 4.0 site-wide, but each dataset carries its own licence. Confirm the terms on the two we use, the National Mental Health Survey 2020 and the Nepal Police suicide CSVs, before quoting figures.
- **WHO IRIS** publications commonly carry CC BY-NC-SA 3.0 IGO, which is non-commercial and share-alike. Quoting WHO *figures* is fine. Quoting WHO *text* into a collection we then license differently is not, so keep WHO to numbers and attribution.
- **IHME and GBD** results are free to use with citation, but confirm the current terms for the release we cite.
- **CTEVT curriculum 2010** is a government document. Quoting structure and marking totals is a low risk; reproducing text at length is not needed and is not proposed.
- **Nepal statute text** is official and quotable, but a mental-health chapter that names the governing law must name the right one. Flagged for verification: the research document currently says there is no separate Mental Health Act, which is very likely wrong, since the Mental Health Act 2052 exists. Correct before the site states anything about the legal framework.

## What is not a risk here, so nobody spends time on it

- **No personal data is collected.** No accounts, no forms that post, no analytics on the reading tracker, which is localStorage in the reader's own browser. This removes the largest category of modern site liability and is worth protecting by not adding analytics casually.
- **No payments, no medical device, no clinical decision support.** Nothing that could be argued to touch medical device rules.
- **Naming works in Learn more is fine.** Title-level citation of a book, film or guideline is nominative use. The one exception already handled: The 5 Love Languages is excluded entirely, which is correct.
- **DSM-5 is paraphrased.** Our own intake records the longest verbatim run as 16 words, and the site uses codes and criterion structure rather than the manual's prose. That is a reasonable position. It is worth a lawyer's eye, but it is not an obvious problem.
- **The vault gate is disclosed honestly**, and the page already tells the reader it is not a real security boundary. That candour is a liability mitigant, not a liability.

## The list, in the order to work it

1. **Deck authors.** Ask each what they will license. Blocks any open licence on teaching text. Nothing else on this list matters as much.
2. **The four crisis numbers.** Verify each twice, from two independent routes. The highest-liability content on the site.
3. **Safeguarding notice and inbox ownership**, before the error-report address goes out. Cheap to do now, awkward later.
4. **The licence decision itself**: NC-SA as the existing intent, or plain BY for reach, plus MIT for code and reserved name and logo, plus a per-source register.
5. **Fix the README**, which currently claims a licence that does not exist, and add the real licence files and the terms page.
6. **Confirm dataset terms** for the two we use, and the Mental Health Act point before the site says anything about legal framework.
7. **Work the data ledger's unsourced figures**, which is the misrepresentation exposure.

## One question for the Founder, held to one

NC or not NC. Everything else on this list can proceed in parallel and most of it is blocking for a reason that is not a choice. This one is a choice about what the atlas is for: if the aim is that no one can sell a course built on it, say NC. If the aim is that it reaches as many students and teachers as possible, say plain CC BY. Both are defensible and the licence text differs by one clause.
