# Mano app: tech-stack research (2026-08-27)

Companion to APP-BRIEF.md. Facts checked on the day against the linked sources; opinions marked as such.

## 1. Framework options (revised after review; Flutter now recommended)

| Option | For this app | Against | Verdict |
|---|---|---|---|
| **Flutter** (Dart) | Release builds carry no INTERNET permission by default (only debug/profile add it for hot reload), so "no network" is the starting state ([flutter #20789](https://github.com/flutter/flutter/issues/20789), [PR #22139](https://github.com/flutter/flutter/pull/22139)). No telemetry in shipped apps; analytics is a developer-tool setting. Encryption is a drop-in: `sqflite_sqlcipher`, same API as sqflite plus a password ([sqflite_sqlcipher](https://pub.dev/packages/sqflite_sqlcipher)). Bundles Mukta and shapes text itself, so Nepali conjuncts look the same on an Android 5 phone and an iPhone. Minimum Android 5 (API 21), two versions lower than Expo. Stable channel breaks less than Expo's yearly SDKs. Flutter apps ship with the App Store label "Data Not Collected". | Dart is new to the team. Base install is larger (~15 MB before content). Widgets are drawn, not native, so platform quirks (text scaling, screen readers) need explicit testing. | **Recommended.** |
| React Native + Expo (TypeScript) | Native text rendering, big talent pool, expo-sqlite local-first path documented ([Expo local-first](https://docs.expo.dev/guides/local-first/)). | Ships INTERNET permission and can carry analytics-capable modules unless stripped and audited ([Jellyfin on Expo privacy](https://jellyfin.org/posts/a-note-about-privacy-and-expo/)); no SQLCipher without a third-party module; minimum Android 7 ([Expo SDK 54](https://expo.dev/changelog/sdk-54)); annual SDK upgrades. | Good second choice; more privacy work to reach the same guarantees. |
| Capacitor (web in a shell) | Reuses the site's HTML/CSS. | Weak offline storage, WebView text on old phones, thin-wrapper store risk. | Fallback only. |
| PWA + Trusted Web Activity | Zero-install, one codebase. | Cannot guarantee app lock, blank thumbnail, backup control or no-network; iOS PWA storage is evictable. | Fallback if native maintenance stalls. |

Correction to the first draft: the Flutter text issue I cited ([#164974](https://github.com/flutter/flutter/issues/164974)) was an Android animation-shadow artifact, closed as fixed, and not about Devanagari; no open Devanagari shaping issue was found.

## 2. On-device data
- **sqflite_sqlcipher** for the log (date, state). Encrypted SQLite on the device with the key in Keychain/Keystore; nothing syncs unless we build it.
- Encryption at rest: SQLCipher from day one (see above) plus the optional app lock, which is what protects against household access on a shared phone.
- No cloud backup of the log: mark the database directory as excluded from iCloud/Google backup, and say so in the privacy text. Apple forbids storing personal health information in iCloud for health apps ([Apple guideline 5.1.3](https://developer.apple.com/app-store/review/guidelines/)).
- Share is an explicit action: export as plain text via the OS share sheet, nothing else.

## 3. "No tracking" has to be engineered, not just promised
- Start from Flutter's release manifest (no INTERNET permission) and keep it that way; tap-to-call uses `tel:` and needs no network. Do not add Firebase, Crashlytics or any analytics package. Verify the signed release with a proxy through every screen: zero requests.
- Android: `android:allowBackup="false"` and `dataExtractionRules` excluding the database; test with `adb backup`. iOS: `isExcludedFromBackup` on the database directory and `NSFileProtectionComplete`; Apple forbids personal health information in iCloud anyway (5.1.3).
- iOS privacy manifest: declare the reason codes for UserDefaults and file timestamps for the plugins used; goal is the App Store label **"Data Not Collected"**.
- Publish the source and the build settings; the promise is checkable.

## 4. Store compliance (both are stricter for health in 2026)
- **Google Play**: the Health apps declaration form is mandatory; a privacy policy is mandatory even when data never leaves the device; the app must state it "is not a medical device and does not diagnose, treat, cure, or prevent any medical condition" and remind users to consult healthcare professionals ([Play Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en)). Data safety section must match reality (all "not collected").
- **Apple**: health apps are reviewed with extra scrutiny; must disclose methodology behind any health claim and remind users to check with a doctor ([guideline 1.4](https://developer.apple.com/app-store/review/guidelines/)); collect only what the core function needs (5.1.1); no health data to third parties or iCloud (5.1.3). Neither store mandates crisis resources, but reviewers look for them in mental-health apps; ours are core to the product anyway.
- Write the privacy policy first, in both languages, in plain words: "your entries stay on your phone; we cannot see them; there is no account."

## 5. Nepali, fonts, low-end phones
- Bundle Mukta (Nepali) and the Latin faces inside the app; no web fonts. Test on a 2 GB-RAM Android with a small screen, the common phone in the districts.
- Keep the app under ~25 MB: content is text, the mark is SVG, diagrams from the site can be bundled as SVG only where they help (window of tolerance, panic curve).
- Nepali digits and dates as on the site; Bikram Sambat display is a later decision.

## 6. Content pipeline
- One source of truth: `content/`, `keypoints/` and the help-now boxes in this repo. A build step (`build.py` already parses every chapter) emits `app-content.json` with: states → response paragraph, skill box, crisis card, "understand this" text, helplines. The site and the app can never drift.
- Fact ledger and review rules apply unchanged (review/triage.md; no invented prevalence; crimson only for crisis).

## 7. Suggested v1 architecture
- Flutter stable, Dart; packages: sqflite_sqlcipher, flutter_secure_storage (key), local_auth (optional app lock), url_launcher (tel:), flutter_localizations; fonts bundled; no other plugins.
- Three screens: Today (log), History (calendar of states, gentle pattern line), Help (crisis card, helplines, what a counselor/health post/OCMC do). Learn content opens from Today's response.
- Local notifications only if the person turns them on.
- Tests: safety-state routing, backup exclusion, zero network calls, cold start and memory on a 2 GB Android Go device, Mukta fixtures at large accessibility font sizes, screen-reader pass (TalkBack, VoiceOver).

## 8. Decisions needed before build
1. Feeling states: idioms-first list (brief) or a scale; recommendation idioms-first.
2. Encryption: SQLCipher from the start (decided above); confirm key handling on Android 5 devices.
3. Store accounts and the developer names shown in the stores.
4. Nepali reviewer for the app copy and the store listing.
5. Name: "Mano".

## 9. Apple App Store: full criteria check (2026-08-29, against the live guidelines)

| Guideline | What it means for Mano | Action |
|---|---|---|
| **4.2 Minimum functionality** | The biggest rejection risk for a "simple" app: Apple rejects apps that feel like a web clip or a single-purpose gimmick. One tap → one paragraph could be read that way. | Ship the core loop with the pieces that make it an app: state chips, matched response and skills, the always-available crisis card, offline learn content, settings (language, lock, erase). Native UI, no web views. Describe it in review notes as an offline self-help and crisis-routing tool. |
| 4.2.2 / 4.2.3 | Not marketing, not a link collection; must work standalone. | No external links in v1; nothing downloaded after install. |
| 2.1 Completeness | No placeholders, all URLs live, tested on device. | Privacy policy and support pages live on pcs.pravashkarki.com before submission; provide reviewer notes describing the safety state and crisis card so they are not mistaken for incomplete flows. |
| 1.4.1 Medical | Extra scrutiny; no accuracy claims without methodology; "check with a doctor" reminder. | In-app "not a medical device, not treatment; talk to a doctor or counselor" in both languages; skills carry the site's "a coping skill, not a treatment" line; cite sources (DSM-5, WHO, mhGAP) in About. Category: Health & Fitness, not Medical. |
| 1.1 / self-harm content | Content about suicide must be supportive, not instructional. | Crisis card wording from the brief; no method detail anywhere; age-rating questionnaire answered honestly (see below). |
| 5.1.1 Privacy | Privacy policy link in App Store Connect and in-app; data minimisation; no consent prompts needed since nothing is collected. | Policy in EN and NE at a stable URL; App Privacy label "Data Not Collected". |
| 5.1.2 Data use | No sharing, no tracking, no ATT prompt needed. | Confirm no SDK reads IDFA; no analytics. |
| 5.1.3 Health | No health data in iCloud; no use for marketing. | Database excluded from iCloud backup; state it in the policy. |
| Privacy manifest | Required for the app and any SDK using "required reason" APIs (UserDefaults, file timestamps). | Flutter and plugins ship manifests; verify at archive time; fix any "missing reason" warnings before upload. |
| **Export compliance (encryption)** | SQLCipher (AES-256 for local data) is not an exempt use; answering "uses non-exempt encryption" means an annual self-classification report to the US BIS by 1 Feb, and a French declaration note. iOS Data Protection (built-in) is exempt. | Decision: on iOS use built-in Data Protection (NSFileProtectionComplete) for the database and the app lock for household access, so ITSAppUsesNonExemptEncryption = NO. Keep SQLCipher on Android only, where no such filing exists. Revisit if a single cross-platform encryption layer becomes worth the yearly filing. |
| Age rating (2025 questionnaire) | New bands 4+/9+/13+/16+/18+; mandatory modules include medical/health topics and mature themes. Suicide and self-harm content pushes the rating up. | Answer the health module truthfully; target 13+ or 16+; keep the listing text and screenshots 4+ (2.3.8). Do not use "18+" unless required, or teenagers cannot find it. |
| 2.3 Metadata | Screenshots must match the app; no misleading claims; metadata in both languages. | Localised App Store listing (EN, NE), screenshots from real builds in both languages. |
| 2.5.1 / current OS | Public APIs, runs on current iOS. | Flutter stable; test on the current iOS and one version back. |
| Accessibility | Not a rejection criterion by itself, but expected. | VoiceOver labels on every control, Dynamic Type, contrast per the site's AA rule. |
| 3.x Business | Free app, no purchases. | Nothing to declare; keep "free, open, CC BY-NC-SA" in About with attribution. |
| Sign in with Apple (4.8) | Only required if third-party login exists. | No accounts, so not applicable; keep it that way. |
| Developer account | Pravo's Apple developer account exists; App Store Connect needs the privacy questionnaire, age rating, export compliance, and the health questionnaire answered per version. | Decide the seller name shown publicly (individual vs organisation) before the first upload. |

## 10. Global scope (the app is a mental-health guide for everyone; Nepal first)
- **Localisation from day one**: all strings in ARB files; Nepali and English in v1; the structure lets any language be added without code changes. Never hard-code helpline numbers in UI code.
- **Two regions in v1 (decided 2026-08-29): Nepal and International.** Chosen on first open from the phone's region setting (no GPS, no location permission), changeable in settings. Nepal is the full experience and keeps growing release by release (idioms, helplines with hours, health post / FCHV / OCMC routes, Nepali copy). International is the basic loop in English: the same states and skills, a crisis card that points to findahelpline.com and the local emergency number, and no Nepal-specific routes. Helplines and crisis text live in one JSON keyed by region with a last-verified date, so adding a third region later is content, not code.
- **Content model built for growth**: states, responses, skills, learn topics and crisis cards as structured entries with language variants, so the future "full guide" (the atlas chapters, rewritten in lay voice) slots in without a rewrite.
- **Region rules**: no accounts means GDPR/UK/other data laws are largely satisfied by design, but each market's medical-app disclaimers and crisis-line etiquette differ; keep the disclaimer and crisis card as per-region content, not code.
- **What v1 still is**: one core feature (log how you feel → response and skill → help), Nepal helplines, two languages. Everything above is architecture so that v2+ can widen without a rewrite.

## Sources
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) · [Export compliance for encryption](https://developer.apple.com/help/app-store-connect/reference/app-information/export-compliance-documentation-for-encryption/) · [Updated age ratings](https://developer.apple.com/news/?id=ks775ehf)
- [flutter #20789 INTERNET permission](https://github.com/flutter/flutter/issues/20789) · [sqflite_sqlcipher](https://pub.dev/packages/sqflite_sqlcipher) · [Drift encryption](https://drift.simonbinder.eu/platforms/encryption/)
- [Expo local-first guide](https://docs.expo.dev/guides/local-first/) · [Expo SDK 54](https://expo.dev/changelog/sdk-54) · [Expo privacy manifests](https://docs.expo.dev/guides/apple-privacy/) · [Jellyfin: privacy and Expo](https://jellyfin.org/posts/a-note-about-privacy-and-expo/)
- [Flutter text artifacts issue #164974](https://github.com/flutter/flutter/issues/164974) · [Flutter vs React Native 2026 (Finite Field)](https://finitefield.org/en/whitepapers/flutter-vs-react-native-2026/)
- [Google Play: Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) · [Google Play policy announcement, April 2026](https://support.google.com/googleplay/android-developer/answer/16926792?hl=en)
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
