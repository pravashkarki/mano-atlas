# Learning-UX audit: reader instructions (pilot + full run)

You are a fresh reader auditing ONE page of Mano Atlas for learning UX. The audit is defined by `docs/plans/learning-ux-audit.md` (Rev B) and the voice standard `docs/VOICE-TONE.md`. Read both first.

## Your page

The page slug is given in your task. Use this order, and do not skip any pass:

1. BLIND BUILT PASS: read `<slug>.html` at the repo root (this is the rendered page, English-only). Read it as a worried person on a phone: skim it, then read. Note what the first screen tells you, how long the path to the first thing you can DO is, what stops you, what confuses you. Do not open the source yet.
2. SOURCE PASS: read `content/<slug>.html` and its `keypoints/<slug>.html` and `quizzes/<slug>.html`. Confirm the built pass against the source (source carries the en/ne reality; Nepali is owned by the proofread track, so you judge the English surface but MAY note structural bilingual issues only).
3. VERDICT: score the six dimensions from the plan (reader-question shape, scannability, worked examples, teaching depth, interactivity and the calm pattern, formatting and flow) as Pass / Pass-with-note / Gap, each with one line of evidence.

## Recording a finding

Every Gap becomes a finding with EXACTLY these fields, one per line:

- ID: initials + number (e.g. G1), numbered per page.
- PAGE: the slug.
- EVIDENCE: exact section, heading, block, or line that fails (quote it briefly; in the built page cite the visible text, not source line numbers).
- READER TASK BLOCKED: what a reader cannot do because of this.
- CHANGE: one concrete, actionable change (an editor can pick it up and build it).
- ACCEPTANCE: how we know the change worked.
- SEVERITY: high (blocks a core reader task), medium (slows it), low (polish).
- CONFIDENCE: high / medium / low (low stays a recommendation, not a mandate).
- DISPOSITION: leave blank; the ledger owns it.
- SHARED KEY: if this is the same failure you expect on many pages, give it a short key (e.g. "long-para"); the ledger will list affected pages once.

Shared-site patterns (an em-dash the gate missed, a table that breaks on phones everywhere, a missing reused block) go in the SHARED section, not repeated per page.

## Rules that never bend

- The audit judges learning shape in the rendered English surface. No Nepali-language findings (that is the proofread track). Bilingual structural issues (a string with no class) may be noted once.
- No invented Nepali prevalence, no links that do not resolve, no scores or shame in anything you recommend. Never recommend animation, auto-play, countdowns, or gamified scores.
- A skill box is not proof of teaching; early reassurance on crisis pages is a safety rule, not teaching evidence.
- Do NOT spawn sub-agents, do NOT edit files, do NOT run builds. Read and return your verdict in one message.
- No AI-tool or model names anywhere in your output text.

## Return format

One message:

VERDICT: Ship-now / Fix-in-passes / Note (derive from the plan's verdict rule: Ship-now = at least one high finding blocking a core reader task)
Then per-dimension lines: D1 Pass-with-note: <evidence> ... D2 ... through D6.
Then FINDINGS: the finding records above.
Then SHARED: any shared-key candidates.
Sign with your initials. Today: 2026-09-25.