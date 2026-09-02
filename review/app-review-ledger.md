# App plan: pair-review ledger (2026-08-27)

Reviewers: DeepSeek v4 (24 findings), GPT-5.6 (24), a second Claude session (23). All three verdicts: proceed with changes. Files: review/deepseek-app.md, review/chatgpt-app.md, review/claude-app.md.

## Raised by all three (accepted, now in the brief)
1. Crisis path must be always reachable from every screen, never gated on a keyword match. Add a first-class safety state ("I do not feel safe"); keep keyword scanning only as a backup, covering Devanagari, Romanized Nepali and idioms.
2. Crisis card content is thin: add means safety (pesticides and medicines out of reach tonight), "tell someone safe" (not "family"), what to do when nobody answers, offline routes (health post, FCHV, OCMC, police, ambulance), helpline hours, a visible last-verified date.
3. Shared phones are the norm: optional PIN/biometric lock, delete one entry and erase all, blank the recent-apps thumbnail, generic notifications, first-run note that entries are visible to anyone who opens the app.
4. "Data never leaves the phone" has to be engineered and proven: disable Android auto-backup and device-transfer, exclude the database from iCloud, strip the INTERNET permission, ship no OTA/telemetry modules, bundle fonts, proxy-test the signed release. Free text is exposed to third-party keyboards: cut it from v1.
5. The atlas is written in counselor voice with DSM-5 criteria; it cannot be piped into the app. The app gets its own second-person lay copy (same fact ledger); only helplines and facts are shared. No diagnostic criteria, no external links in-app.
6. The pattern nudge can read as diagnosis or surveillance: opt-in, dismissible for good, normalise first, minimum count and window, never after a heavy log. Deferred out of v1.
7. Test with district users before copy freeze; name the Nepali reviewer; draw states from validated idiom research (Kohrt, TPO Nepal); allow "none of these" and multiple selection.

## Raised by two
- Android first; iOS only when there is a stated reason (Claude, GPT). Accepted.
- Encryption is vague: either SQLCipher via op-sqlite with a Keychain/Keystore key, or say plainly it relies on the phone lock; the app lock is what matters against household access (all three touched it). Accepted: app lock in v1, SQLCipher decision at build start.
- Age rating and children (GPT, Claude). Accepted: word the crisis card to keep 12+, decide supported age.
- Nepal Individual Privacy Act 2075, in-app "not a medical device" line in both languages (GPT, Claude). Accepted.
- Verify real device Android versions; Android 5/6 may still be common (DeepSeek, GPT). Accepted as a pre-build check.

## Raised by one, accepted
- Urgent-danger route for psychosis, intoxication, violence, medical danger before any coping skill (GPT).
- Two skill options with a "stop if it gets worse" line; "trusted person" wording must not push a GBV survivor toward family (GPT).
- Alcohol state after disasters (Claude).
- Say plainly that nobody is reading the entries (GPT).
- Play closed-test requirement (14 days, 12 testers) and publishing identity (Claude, DeepSeek).
- Drop expo-router (DeepSeek). Attribution for CC BY-NC-SA in About (DeepSeek).

## Raised, not accepted as stated
- Build v1 as a PWA + Trusted Web Activity first (Claude). Rejected for v1: the shared-phone protections everyone asked for (app lock, blank thumbnail, backup control, no-network guarantee) are exactly what a PWA cannot guarantee. Kept as the fallback if native maintenance stalls; the content pipeline stays reusable either way.
- Voice-over for skills (DeepSeek, GPT). Deferred; good v2 candidate.
- Static offline list of health posts and OCMCs by region (DeepSeek). Deferred: no verified dataset yet; would ship stale. v1 shows the route types and how to find them.
