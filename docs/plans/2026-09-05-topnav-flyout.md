# Plan: top nav with flyouts, contextual sidebar, Superhuman-style flow

Status: DRAFT, awaiting Pravo's approval (2026-09-05). Nothing built yet.

## TASK

Rebuild the Mano Atlas shell so it reads like superhuman.com in flow and
structure while keeping our own colours, fonts, content and build pipeline:

1. Navigation moves from the left sidebar to a sticky top bar.
2. Each chapter group (Overview, Disorder categories, Counselling practice,
   Reference) is a top-bar item that opens a flyout card listing its chapters.
3. On a chapter page the left sidebar shows only the current group's chapters
   (on Roots you see the five Overview chapters, on Anxiety the ten disorder
   chapters). The home page has no sidebar and flows top to bottom in bands.

## CONTEXT (what is there now)

- `build.py` SHELL: `.layout` flex with a 282px sticky `aside.sidebar` (brand,
  dhaka ribbon, accordion `nav.snav` of all four groups) and `main` holding a
  floating `.topctrl` pill (search, EN/ne, theme) plus a collapse/expand button.
- `nav_html(slug)` renders all groups as `<details>` with the active group open.
- Mobile (<=900px): sidebar becomes a top strip; "Chapters" button drops the
  full accordion under it.
- `lang.js`: language + theme, nav-open toggle, `psc-seen` ticks, reading
  progress, sidebar collapse with `psc-nav-collapsed` and `nav-collapsed-init`.
- Home: hero + `toc_html()` contents grid (group headers with SPOT art) +
  "Recently added" strip.
- Per-page one-line descriptions already exist at build time (`page_descs`).

What Superhuman actually does (checked 2026-09-05): plain sticky top bar,
brand left, five text items with a chevron, utilities right. A menu opens on
click (hover only underlines). The flyout is a calm white card, rounded, soft
shadow, a single vertical list with generous row height, no icons or blurbs in
the Products menu. The page below is full-width bands with one idea each.

## DONE WHEN

- Desktop (>900px): sticky top bar with brand, four group menus, search,
  EN/ne, theme. Click opens one flyout at a time; click outside or Escape
  closes; arrow keys move between rows; focus returns to the trigger;
  `aria-expanded` and `aria-controls` are correct. Each row: number, category
  mark, bilingual title, seen tick. Active chapter highlighted.
- Chapter pages: left sidebar (about 240px) shows the group name and only that
  group's chapters, active highlighted, seen ticks kept. Previous/next pager
  and reading progress unchanged.
- Home: no sidebar. Hero full width, then one band per group (SPOT art left,
  chapter cards right, using the existing `toc_html` data), then Recently
  added, then the footer with the crisis column. Bands alternate `--bg` and
  `--surface` for rhythm.
- Mobile (<=900px): top bar is brand + Menu + EN/ne + theme. Menu opens a
  sheet with the four groups as an accordion (today's `snav` markup). Chapter
  pages get a horizontal "In this section" scroller above the title instead
  of the sidebar.
- Sticky bar never covers anchor targets (`scroll-margin-top`), search results
  dropdown sits above the flyouts, print hides the bar and sidebar.
- Both themes, both languages, keyboard only, reduced motion: checked with
  screenshots at 1440, 1024 and 390 wide.
- `python3 build.py` clean, em-dash grep empty, every new string en + ne,
  OG images unaffected (no title changes).

## PLAN (one commit each, same-day deploy)

1. `build.py`: add `topbar_html(slug)` (brand, menus with `flyout_html(group,
   slug)`, utilities) and `sidenav_html(slug)` (current group only). Rework
   SHELL to `header.topbar` + `div.layout` (aside + main). Home renders with
   `layout no-side`. Remove the collapse/expand buttons from the template.
2. `style.css`: `.topbar` (sticky, `--surface`, 1px `--line` bottom, 56px),
   `.menu` trigger (Archivo 600, chevron rotates when open), `.flyout` card
   (`--surface`, `--line`, `--shadow`, radius 12, rows 44px, `--accent-wash`
   active). Sidebar to 240px with the group label in Plex Mono caps. Body
   `scroll-margin-top`. Retire `.topctrl`, collapse and `nav-collapsed` rules.
3. `lang.js`: flyout controller (open/close, outside click, Escape, arrows,
   focus return), mobile sheet toggle, search pill mounted in the top bar.
   Remove collapse code; `psc-nav-collapsed` is ignored from now on.
4. Home flow: `toc_html()` emits bands instead of the grid; hero goes full
   width; "Recently added" keeps its place.
5. Mobile: sheet menu + "In this section" scroller; test at 390 and 768.
6. QA pass: screenshot matrix (light/dark x en/ne x 3 widths), keyboard walk,
   print preview, build gates, then deploy and re-check live.

## RISKS

- Sticky bar costs 56px of height on laptops; mitigated by hiding the
  reading-time and care notes nowhere, just by keeping the bar thin.
- Anchor links and the on-page chips must offset for the bar or headings hide
  under it.
- Nepali group labels are longer (परामर्श अभ्यास); the bar must not wrap at
  1024px. Fallback: shorter Nepali labels in GROUPS for the bar only.
- Losing "all chapters visible" on desktop: the flyouts and the home bands
  carry that. Seen ticks live in both flyout and sidebar.
- Touch users cannot hover; click-to-open avoids the problem by design.
- Search dropdown z-index versus flyouts; one stacking scale for the bar.

## ASSUMPTIONS

- No change to colours, type scale, content, quizzes, OG images.
- No new dependencies; still stdlib Python + vanilla JS + one CSS file.
- The `.hero-art` and SPOT illustrations are reused as they are.

## NON-GOALS

Superhuman's gradients, photography, marketing copy, animations or sign-in
chrome. No dark-only hero. No framework.

## DECISIONS (proposed defaults, say if any should change)

1. Flyouts open on click, not hover (calmer, works on touch, matches Superhuman).
2. Home page has no sidebar; the bands are the map.
3. The sidebar collapse toggle is dropped (sidebar is now small and contextual).
4. "On this page" chips stay inside the article for now; moving them into the
   sidebar is a possible later step.

## VALIDATION

Build gates, em-dash grep, en/ne check, screenshot matrix, keyboard-only pass,
Lighthouse accessibility on one chapter page and home, live check after deploy.
