# Pair review: Mano app plan

Work only inside this repository. Read docs/APP-BRIEF.md and docs/APP-TECH-RESEARCH.md (the plan), then CLAUDE.md and README.md for context on the existing site, and skim content/pfa.html, content/suicide.html and content/trauma.html.

Context: Mano Atlas is a free bilingual (English/Nepali) mental-health education site built for Nepal. After the 2026 floods the owner wants a small companion app: a person logs how they feel, gets a warm plain-language response, one two-minute skill, and is encouraged toward help. Data stays on the phone; no account, no analytics; connecting with counselors is a later, user-initiated feature. Target users are in remote districts, often offline, often on cheap Android phones, Nepali-first.

Review the plan critically. In priority order:
1. SAFETY: anything that could harm a distressed person (crisis handling, wording, the self-harm keyword trigger, what a "pattern" nudge might do to someone, shared phones).
2. PRIVACY CLAIMS: is "data never leaves the phone" actually deliverable with the proposed stack; what would break it (OS backups, crash reporters, fonts loaded from the web, app store requirements). Name concrete checks.
3. TECH STACK: is Expo/React Native the right call versus Flutter, Kotlin Multiplatform, a PWA, or native; Nepali text rendering; low-end Android; app size; long-term maintainability by a small team.
4. PRODUCT: is the core loop right for the stated users; what is missing for v1; what should be cut; what would make people delete it.
5. STORE AND LEGAL: Google Play health declaration, Apple health guidelines, privacy policy, disclaimers, anything specific to Nepal.

OUTPUT FORMAT, exactly this, nothing else:
- One line per finding: `AREA | the concern in one sentence | the concrete change | SEVERITY (HIGH / MEDIUM / LOW)`
- Highest severity first. Maximum 25 findings. Do not praise. Do not restate the plan.
- Then one final line: `VERDICT: <one sentence: proceed / proceed with changes / rethink, and why>`
