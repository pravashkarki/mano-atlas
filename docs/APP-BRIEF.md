# Mano app: brief (v2, 2026-08-27, after pair review; ledger in review/app-review-ledger.md)

## One sentence
(Scope note, 2026-08-29: v1 is one core feature, done well, with two regions: Nepal (full, and growing with every release) and International (basic, English, generic crisis routing). The direction is a full mental-health guide for anyone, in any language; Nepal and Nepali come first. Architecture decisions in APP-TECH-RESEARCH.md sections 9 and 10 are made for that direction.)

A simple phone app for Nepal where a person logs how they feel, gets a warm, plain-language response drawn from Mano Atlas, and is encouraged, never pushed, toward help; everything stays on the phone.

## Why now
The 2026 floods. Remote districts have almost no mental-health workers; what people have is a phone, often offline, often shared, often in Nepali only.

## Non-negotiables
1. **One goal.** Log a feeling, understand it, know where help is. Nothing else in v1.
2. **Data never leaves the phone.** No account, no analytics, no crash reporting that carries content, no ads. Sharing or connecting with a counselor is a later, explicit, user-initiated act.
3. **Works offline.** All content (education, skills, helplines) ships inside the app. Nepali first, English available, switchable at any time from the main screen.
4. **Warm, not clinical.** Same voice and rules as the site: reassure, never judge, no scores that shame, crisis numbers always one tap away.
5. **Open.** Same CC BY-NC-SA content; source public.

## Core loop (v1)
1. Open → "How is your man (heart-mind) today?" Tap one or more states written in Nepali idioms (drawn from validated idiom research, tested with district users before copy freeze), including "I do not feel safe", "drinking more than I want", and "none of these". No free text in v1.
2. Response: one short, kind paragraph in second person written for the app (not the atlas's counselor voice), two skill options with a "stop if it gets worse" line, and one line about when it is worth telling someone safe.
3. Help is always one tap away, on every screen: the crisis card (helplines with hours and a last-verified date, tap-to-call; the ask-for-help line: "Right now, call, or go to someone you trust and tell them how you feel. Ask them to stay with you tonight and to keep pesticides and medicines somewhere you cannot reach. Help works better when you are not alone."; what to do if nobody answers; health post, FCHV, OCMC, police, ambulance). Means safety is always phrased as something a helper does with the person, never as a self-managed instruction (decided 2026-08-28)., plus an urgent-danger route for psychosis, intoxication, violence or medical danger that comes before any skill.
4. Learn: a small offline "understand this" per state, lay language only, no diagnostic criteria, no external links.
5. Settings (v1, kept tiny): language switch नेपाली / English, chosen on first open (default from the phone's locale, Nepali if unsure) and changeable any time from a visible control on the Today screen, not buried; text size (follows the phone, with a larger option); optional app lock; erase everything; the "nobody reads this" note and the privacy text in both languages. Every string ships in both languages, same rule as the site.
Deferred to v2: history calendar, pattern nudge (opt-in, dismissible, normalising), free text, audio versions of skills, regional directory of health posts and OCMCs.

## Safety rules
- The "I do not feel safe" state opens the crisis card first, calmly, with tap-to-call, "telling someone safe helps", and "if you are alone, call or go to the nearest person you trust". No lock-out, no alarm sounds. Keyword scanning (Devanagari, Romanized, idioms) is only a backup and never re-triggers from old entries.
- Shared phones: optional PIN or biometric lock, delete one entry, erase everything, blank recent-apps thumbnail, generic notifications, and a first-run line that entries are visible to anyone who opens the app and that nobody is reading them.
- Content reviewed against the same fact ledger as the site (review/triage.md); every state-to-skill pairing reviewed by a counselor; Nepali copy reviewed by a native speaker.

## Direction after v1 (noted 2026-08-29; roadmap, not commitments)
- **Partnerships**: government (MoHP, the National Mental Health Strategy's task-sharing programme, local governments after disasters), hospitals (Mental Hospital Lagankhel, TUTH, OCMCs), counselor associations and NGOs (TPO Nepal, CMC Nepal), so the help routes in the app are official and kept current by the people who run them.
- **Remote counselling**: a way for a person to reach a verified counselor or doctor from the app, by their own choice. This is the first feature that needs a backend, consent, identity of the professional, and a data-protection design; it must not weaken the v1 promise (the log stays on the phone unless the person shares it). Design as a separate, opt-in module with its own privacy text, ideally with a partner who already provides the service (helpline operators, TPO, hospital telepsychiatry) rather than building the clinical side ourselves.
- **Full guide**: the atlas chapters rewritten in lay voice, more languages, more regions.

## Later (v2+, not in v1)
- Connect with a counselor or doctor by the person's choice: a directory first (name, place, phone), then possibly a secure channel. Nothing automatic.
- Export or share a log summary as text, only when the person taps share.
- Reminders, opt-in only, local notifications.

## Technical direction (after review)
- Flutter (Dart), one codebase for Android and iOS; SQLite on device; Android encrypted with SQLCipher (sqflite_sqlcipher, key in Keystore), iOS protected with built-in Data Protection so no export-compliance filing is needed; optional app lock in v1 on both. Reasoning in APP-TECH-RESEARCH.md section 1.
- Android first; iOS only when there is a stated reason. Play: closed test (14 days, 12 testers) and publishing identity decided before the store account.
- Content: the app has its own structured bilingual source (states, responses, skills, crisis card, help routes) validated at build; helplines in one JSON with a last-verified date. Facts shared with the site; prose not.
- Privacy, proven not asserted: android:allowBackup=false and dataExtractionRules; iOS isExcludedFromBackup and NSFileProtectionComplete; no INTERNET permission (Flutter release default, kept); no analytics or crash SDKs; fonts bundled; signed release proxy-tested through every screen; store label "Data Not Collected"; privacy policy in both languages at a stable URL naming what the platforms themselves collect and Nepal's Individual Privacy Act 2075.
- Pre-build checks: real Android version spread on district phones; cold start and memory on a 2 GB Android Go device; Mukta rendering fixtures; size budget set from the first build (per-ABI AAB, Hermes, subset fonts).
- PWA + Trusted Web Activity is the fallback if native maintenance stalls; it cannot give the shared-phone protections above, which is why native is v1. Expo/React Native is the second choice if Dart proves a blocker.

## Open questions
- Feeling states: idioms first (recommended); the final list comes from idiom research plus the district test.
- Name in the store: "Mano" alone or "Mano Atlas"; supported age range (recommend 12+ rating wording, 18+ target audience on Play).
- Who reviews the Nepali copy and the state-to-skill pairings before launch.
- Publishing identity (person or LastDoor) and the Play/Apple accounts.

