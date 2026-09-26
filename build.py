#!/usr/bin/env python3
"""Build the Mano Atlas static pages.

Each page = shared shell (sidebar nav + lang switcher) + content/<slug>.html.
Add a page: drop a file in content/, add one entry to PAGES, run: python3 build.py
"""
import html as html_mod
import json
import pathlib
import re
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent

# English-first phase: site ships English only until the Nepali text of a page is
# reviewed (plan docs/plans/content-contract-english-first.md). The toggle is removed
# at build, class="ne" output is dropped, and the search index excludes Nepali strings.
# Existing Nepali in content/ stays untouched and returns when the flag flips back.
PHASE1_ENGLISH_ONLY = True

# ---- site-wide values: edit HERE, then run python3 build.py ----
SITE = {
    "reviewed_en": "August 2026",
    "reviewed_ne": "भदौ २०८३",
    "email_user": "kpravash",       # contact email, kept out of raw HTML for spam bots
    "email_domain": "gmail",
    "email_tld": "com",
    "helpline_suicide": "1166",
    "helpline_tuth": "1660 012 1600",
    "helpline_women": "1145",
    "helpline_emergency": "112 / 100",
    "site_url": "https://manoatlas.com",
    "recent_since": "2026-08-31",   # home "Recently added" lists chapters added after this date (and within 90 days)
}

# slug, content file, en title, ne title, catvar (sidebar colour mark), group.
# Chapter numbers are NOT stored here: the build numbers pages by position, so inserting
# a row anywhere renumbers everything (badges, sidebar, pagers, cross-references).
PAGES = [
    ("index",      "map",        "Home & the DSM-5 map",      "गृहपृष्ठ र DSM-5 नक्सा",        None,       "overview"),
    ("roots",      "roots",      "Roots: philosophy to psychology", "जरा: दर्शनदेखि मनोविज्ञान", None,     "overview"),
    ("foundation", "foundation", "Fear: the foundation",      "डर: आधारशिला",                  None,       "overview"),
    ("basics",     "basics",     "Mental health basics",      "मानसिक स्वास्थ्यका आधार",       None,       "overview"),
    ("development","development","Human development",         "मानव विकास",                    None,       "overview"),
    ("anxiety",    "anxiety",    "Anxiety disorders",         "चिन्ता विकारहरू",               "--c-anx",  "disorders"),
    ("ocd",        "ocd",        "OCD & related",             "ओसीडी र सम्बन्धित",             "--c-ocd",  "disorders"),
    ("depression", "depression", "Depressive disorders",      "उदासी (डिप्रेसन)",              "--c-dep",  "disorders"),
    ("trauma",     "trauma",     "Trauma & stressor",         "आघात र तनाव",                   "--c-tra",  "disorders"),
    ("somatic",    "somatic",    "Conversion & somatic",      "कन्भर्सन र शारीरिक",            "--c-som",  "disorders"),
    ("psychosis",  "psychosis",  "Psychosis",                 "मनोविकृति (साइकोसिस)",          "--c-psy",  "disorders"),
    ("child",      "child",      "Child mental illness",      "बाल मानसिक समस्या",             "--c-chi",  "disorders"),
    ("eating",     "eating",     "Eating disorders",          "खानपान विकार",                  "--c-eat",  "disorders"),
    ("sleep",      "sleep",      "Sleep-wake disorders",      "निद्रा विकार",                  "--c-slp",  "disorders"),
    ("substance",  "substance",  "Substance use",             "लागुपदार्थ प्रयोग",             "--c-sub",  "disorders"),
    ("wellbeing",  "wellbeing",  "Wellbeing & intervention",  "तन्दुरुस्ती र हस्तक्षेप",       None,       "practice"),
    ("approaches", "approaches", "Approaches & forms",        "विधि र रूपहरू",                 None,       "practice"),
    ("skills",     "skills",     "Communication skills",      "संवाद-सीप",                     None,       "practice"),
    ("skills-listening", "skills-listening", "Listening back: reflecting skills", "सुनेको फर्काउने: प्रतिबिम्बन-सीप", None, "practice"),
    ("skills-moving",    "skills-moving",    "Moving forward: change skills",   "अगाडि बढाउने: परिवर्तन-सीप",     None, "practice"),
    ("process",    "process",    "The counselling process",   "परामर्श-प्रक्रिया",             None,       "practice"),
    ("first-sessions", "first-sessions", "The first sessions",    "पहिला सत्रहरू",                 None,       "practice"),
    ("tools",      "tools",      "Tools & techniques",        "औजार र प्रविधि",                None,       "practice"),
    ("techniques", "techniques", "Techniques step by step",   "प्रविधि चरणैपिच्छे",            None,       "practice"),
    ("suicide",    "suicide",    "Suicide: assessment",       "आत्महत्या: मूल्याङ्कन",         None,       "practice"),
    ("pfa",        "pfa",        "PFA & emergencies",         "पीएफए र आपतकाल",                None,       "practice"),
    ("gbv",        "gbv",        "Gender & GBV",              "लैङ्गिकता र जीबीभी",            None,       "practice"),
    ("hiv",        "hiv",        "HIV & AIDS counselling",    "एचआईभी परामर्श",                None,       "practice"),
    ("casemgmt",   "casemgmt",   "Case management",           "केस व्यवस्थापन",                None,       "practice"),
    ("ethics",     "ethics",     "Ethics & self-care",        "नैतिकता र आत्म-हेरचाह",         None,       "practice"),
    ("more",       "rest",       "The rest of the map",       "बाँकी नक्सा",                   None,       "reference"),
    ("nepal",      "nepal",      "Culture & the Nepal panorama", "संस्कृति र नेपाली परिदृश्य", None,       "reference"),
    ("crosswalk",  "crosswalk",  "For PSC students",          "पीएससी विद्यार्थीलाई",          None,       "reference"),
    ("glossary",   "glossary",   "Glossary",                  "शब्दावली",                       None,       "reference"),
]

NUM = {slug: f"{i + 1:02d}" for i, (slug, *_rest) in enumerate(PAGES)}
if len(NUM) != len(PAGES):
    raise SystemExit("build: duplicate slug in PAGES")
NO_QUIZ = {"glossary"}          # reference pages that deliberately have no Quick check
NO_KEYPOINTS = {"map"}          # the home page has no Key points box

GROUPS = {
    "overview":  ("Overview", "सिंहावलोकन"),
    "disorders": ("Disorder categories", "विकार वर्गहरू"),
    "practice":  ("Counselling practice", "परामर्श अभ्यास"),
    "reference": ("Reference", "सन्दर्भ"),
}

# ---- inline Lucide icons (lucide.dev, ISC licence). stroke = currentColor ----
def _lucide(paths: str) -> str:
    return ('<svg class="lucide" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            f'{paths}</svg>')

ICON = {
    "search":  _lucide('<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>'),
    "clock":   _lucide('<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>'),
    "heart":   _lucide('<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>'),
    "phone":   _lucide('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>'),
    "mail":    _lucide('<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>'),
    "left":    _lucide('<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>'),
    "right":   _lucide('<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>'),
    "chev":    _lucide('<path d="m6 9 6 6 6-6"/>'),
    "book":    _lucide('<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'),
    "play":    _lucide('<polygon points="6 3 20 12 6 21 6 3"/>'),
    "film":    _lucide('<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18"/><path d="M3 7.5h4"/><path d="M3 12h18"/><path d="M3 16.5h4"/><path d="M17 3v18"/><path d="M17 7.5h4"/><path d="M17 16.5h4"/>'),
    "file":    _lucide('<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>'),
    "audio":   _lucide('<path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/>'),
    "pencil":  _lucide('<path d="M17 3a2.85 2.83 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5Z"/><path d="m15 5 4 4"/>'),
    "menu":    _lucide('<line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/>'),
    "info":    _lucide('<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>'),
    "panel":   _lucide('<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M9 3v18"/>'),
    "sprout":  _lucide('<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>'),
}

RES_ICON_RULES = [
    (("video", "talk", "ted"), "play"),
    (("film", "documentary", "movie"), "film"),
    (("podcast", "audio"), "audio"),
    (("book", "guide", "manual"), "book"),
    (("practice", "drill", "exercise", "role-play"), "pencil"),
]


def res_type_icon(label: str) -> str:
    l = label.lower()
    for keys, name in RES_ICON_RULES:
        if any(k in l for k in keys):
            return ICON[name]
    return ICON["file"]


SITE_DESC_BI = "Mano Atlas (मनो एट्लास): a free, bilingual (English/नेपाली) atlas of mental disorders: DSM-5 criteria, teaching diagrams, and the Nepali context."
SITE_DESC_EN = "Mano Atlas: a free, open atlas of mental disorders: DSM-5 criteria, teaching diagrams, and the Nepali context. English-first while the Nepali text is under review."
SITE_DESC = SITE_DESC_EN if PHASE1_ENGLISH_ONLY else SITE_DESC_BI
NE_DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")
HEAVY_PAGES = {"suicide", "gbv", "pfa", "trauma", "psychosis", "ethics"}


def card_tables(body: str) -> str:
    """Give every data table with 3+ columns per-cell data-labels so CSS can stack rows into cards on phones."""
    def one(m):
        cls, inner = m.group(1), m.group(2)
        rows = re.findall(r"<tr>(.*?)</tr>", inner, re.S)
        if not rows:
            return m.group(0)
        heads = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<th>(.*?)</th>", rows[0], re.S)]
        if len(heads) < 3:
            return m.group(0)
        out = []
        for r_i, row in enumerate(rows):
            if r_i == 0:
                out.append(f"<tr>{row}</tr>")
                continue
            k = [0]
            def td(mm):
                lab = heads[k[0]] if k[0] < len(heads) else ""
                k[0] += 1
                return f'<td data-label="{lab}">'
            out.append("<tr>" + re.sub(r"<td>", td, row) + "</tr>")
        return f'<table class="data cardy{cls}">' + "\n".join(out) + "</table>"
    return re.sub(r'<table class="data([^"]*)">(.*?)</table>', one, body, flags=re.S)


LABELS_HELP = (
    '<details class="labels-help"><summary>' + ICON["info"] +
    '<span class="en">What do the tags and codes on this page mean?</span>'
    '<span class="ne">यस पृष्ठका ट्याग र कोडको अर्थ के हो?</span></summary>'
    '<p class="en"><strong>CTEVT PSC curriculum</strong> marks content on the official Psychosocial Counselor syllabus, which can appear in the exam. '
    '<strong>Beyond curriculum</strong> is added for completeness: worth knowing, not examinable. '
    'A chip like <span class="code mono">296.2x · F32</span> is the diagnosis code: the DSM-5\'s older ICD-9-CM number first, then the ICD-10 "F-code" used in hospital records. '
    'Letters like <em>A.2</em> or <em>C.5</em> on the ethics page are section numbers of the ACA Code of Ethics. Readers who are not students can ignore all of these.</p>'
    '<p class="ne"><strong>सीटीईभीटी पाठ्यक्रम</strong> ले आधिकारिक मनोसामाजिक परामर्शकर्ता पाठ्यक्रमभित्रको, परीक्षामा आउन सक्ने सामग्री जनाउँछ। '
    '<strong>पाठ्यक्रमभन्दा बाहिर</strong> पूर्णताका लागि थपिएको हो: जान्न लायक, परीक्षामा नआउने। '
    '<span class="code mono">296.2x · F32</span> जस्तो चिप निदान-कोड हो: पहिले DSM-5 को पुरानो ICD-9-CM नम्बर, अनि अस्पतालको रेकर्डमा प्रयोग हुने ICD-10 «एफ-कोड»। '
    'नैतिकता-पृष्ठका <em>A.2</em> वा <em>C.5</em> जस्ता अक्षर एसीए नैतिक संहिताका खण्ड-नम्बर हुन्। विद्यार्थी नभएका पाठकले यी सबै बेवास्ता गरे हुन्छ।</p></details>\n'
)


INFO_POP = (
    '<span class="info"><button class="info-btn" type="button" aria-expanded="false" aria-label="What do these tags and codes mean?">' + ICON["info"] + '</button>'
    '<div class="info-pop" role="tooltip">'
    '<p class="en"><strong>CTEVT PSC curriculum</strong>: on the official Psychosocial Counselor syllabus, can appear in the exam. <strong>Beyond curriculum</strong>: added for completeness, not examinable. '
    'A chip like <span class="code mono">296.2x · F32</span> is the diagnosis code: the DSM-5\'s older ICD-9-CM number, then the ICD-10 "F-code" used in hospital records. Non-students can ignore all of these.</p>'
    '<p class="ne"><strong>सीटीईभीटी पाठ्यक्रम</strong>: आधिकारिक मनोसामाजिक परामर्शकर्ता पाठ्यक्रमभित्र, परीक्षामा आउन सक्ने। <strong>पाठ्यक्रमभन्दा बाहिर</strong>: पूर्णताका लागि थपिएको, परीक्षामा नआउने। '
    '<span class="code mono">296.2x · F32</span> जस्तो चिप निदान-कोड हो: DSM-5 को पुरानो ICD-9-CM नम्बर, अनि अस्पतालको रेकर्डमा प्रयोग हुने ICD-10 «एफ-कोड»। विद्यार्थी नभएकाले यी बेवास्ता गरे हुन्छ।</p>'
    '</div></span>'
)


def info_popovers(body: str) -> str:
    """Card head: title + curriculum tag on the left; code chip + info popover on the right."""
    pat = re.compile(r'(<h3>.*?</h3>)\s*(<span class="code mono"[^>]*>[^<]*</span>)?\s*(<span class="pill (?:todo|beyond)">.*?</span></span>)(\s*</div>\s*<div class="card-body">)', re.S)
    def one(m):
        code = m.group(2) or ""
        return m.group(1) + m.group(3) + '<span class="head-right">' + code + INFO_POP + '</span>' + m.group(4)
    return pat.sub(one, body)


REF_RE = re.compile(r"\{\{(page|section|n|पृष्ठ|खण्ड|न):(?:last:([a-z]+)|([a-z-]+))\}\}")
STALE_RE = re.compile(r"\b(?:page|section) \d{2}\b|पृष्ठ [०-९]{2}|खण्ड [०-९]{2}")


def resolve_refs(body: str, fname: str) -> str:
    """Cross-references are written by slug, never by number: {{page:tools}}, {{section:foundation}},
    {{पृष्ठ:tools}}, {{खण्ड:foundation}}; {{n:slug}} / {{न:slug}} give the bare number; {{n:last:practice}}
    the number of a group's last chapter. The build emits the current number, so inserting a chapter
    never leaves a stale reference behind."""
    def one(m):
        word, group, slug = m.group(1), m.group(2), m.group(3)
        if group:
            slug = [p[0] for p in PAGES if p[5] == group][-1]
        if slug not in NUM:
            raise SystemExit(f"build: {fname}: unknown page in cross-reference {m.group(0)}")
        if word in ("n", "न"):
            num = NUM[slug]
            if word == "न":
                num = num.translate(NE_DIGITS)
            return num
        row = next(p for p in PAGES if p[0] == slug)
        title = row[2] if word in ("page", "section") else row[3]
        return f'<a href="{slug}.html">{title}</a>'
    parts = re.split(r"(<[^>]+>)", body)
    for k in range(0, len(parts), 2):
        m = STALE_RE.search(parts[k])
        if m:
            raise SystemExit(f"build: {fname}: hard-coded chapter number '{m.group(0)}'; write {{{{page:slug}}}} instead")
    body = REF_RE.sub(one, body)
    if REF_RE.search(body) or re.search(r"\{\{[a-zA-Zपृष्ठखण्डन]+:", body):
        raise SystemExit(f"build: {fname}: unresolved reference token remains")
    return body


def stamp_badge(body: str, num: str, fname: str) -> str:
    """The chapter badge in each fragment is left empty by authors; the build fills it."""
    if re.search(r'<span class="secbadge[^>]*>\s*[0-9०-९]', body):
        raise SystemExit(f"build: {fname}: chapter number written by hand in the secbadge; leave it empty")
    return re.sub(r'(<span class="secbadge[^>]*>)\s*(</span>)', lambda m: m.group(1) + num + m.group(2), body, count=1)


def git_date(*paths: pathlib.Path, added: bool = False) -> str:
    """Last commit date (YYYY-MM-DD) touching any of the paths; the date the first was added if added=True.
    Untracked or uncommitted files count as changed today."""
    import datetime
    import subprocess
    today = datetime.date.today().isoformat()
    existing = [str(p) for p in paths if p.exists()]
    if not existing:
        return today
    try:
        if added:
            out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%cs", "--", *existing], capture_output=True, text=True, cwd=ROOT).stdout.split()
            return out[-1] if out else today
        dirty = subprocess.run(["git", "status", "--porcelain", "--", *existing], capture_output=True, text=True, cwd=ROOT).stdout.strip()
        if dirty:
            return today
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", *existing], capture_output=True, text=True, cwd=ROOT).stdout.strip()
        return out or today
    except OSError:
        return today


# closing care notes: varied per page (picked by page index), dismissible for the session
CARELINES = [
    ("That is plenty for one sitting. Whatever brought you here, reading about the mind with care is itself an act of care.",
     "एक बसाइका लागि यति नै प्रशस्त छ। जुनसुकै कारणले आइपुग्नुभयो, मनका कुरा ध्यानले पढ्नु आफैंमा हेरचाहको काम हो।"),
    ("In the flow? The next chapter is one click below. Tired? Stopping here is also progress.",
     "पढ्ने जोश छ? अर्को खण्ड एक क्लिक तल छ। थाक्नुभयो? यहीँ रोकिनु पनि प्रगति हो।"),
    ("One idea from this page will stay with you longer than the whole page read twice. Which one is yours?",
     "पूरै पृष्ठ दुई पटक पढ्नुभन्दा यसको एउटा विचार तपाईंसँग लामो समय रहनेछ। तपाईंको चाहिँ कुन हो?"),
    ("Learning about the mind can stir the mind. If something here sat heavily, saying it aloud to someone you trust helps.",
     "मनका कुरा पढ्दा मन नै हल्लिन सक्छ। कुनै कुरा गह्रौं लाग्यो भने भरपर्दो मान्छेलाई भन्दा हलुका हुन्छ।"),
    ("This page will still be here tomorrow, and it reads differently once you have met its ideas in real life.",
     "यो पृष्ठ भोलि पनि यहीँ हुनेछ, र वास्तविक जीवनमा यी कुरा भेटेपछि यसैलाई पढ्दा अर्कै अर्थ खुल्छ।"),
    ("Slow is fine. This curriculum took years to write; nobody expects it in one evening.",
     "बिस्तारै पढे हुन्छ। यो पाठ्यक्रम लेख्न वर्षौं लाग्यो; एकै साँझमा सक्नुपर्छ भन्ने छैन।"),
]


def nav_html(active_slug: str) -> str:
    active_group = next((g for s, _f, _e, _ne, _c, g in PAGES if s == active_slug), None)
    by_group = {}
    for slug, _f, en, ne, cat, group in PAGES:
        by_group.setdefault(group, []).append((slug, NUM[slug], en, ne, cat))
    out = []
    for group, items in by_group.items():
        g_en, g_ne = GROUPS[group]
        is_open = " open" if group == active_group else ""
        links = []
        for slug, num, en, ne, cat in items:
            href = f"{slug}.html" if slug != "index" else "index.html"
            cls = ' class="active" aria-current="page"' if slug == active_slug else ""
            mark = f'<span class="catmark" style="background:var({cat})"></span>' if cat else '<span class="catmark" style="background:transparent"></span>'
            links.append(
                f'<a href="{href}"{cls}><span class="secnum">{num}</span>{mark}'
                f'<span class="en">{en}</span><span class="ne">{ne}</span></a>'
            )
        links_html = "\n        ".join(links)
        out.append(
            f'<details class="snav-sec" data-g="{group}"{is_open}>\n'
            f'      <summary><span class="en">{g_en}</span><span class="ne">{g_ne}</span>'
            f'<span class="count">{len(items)}</span>{ICON["chev"]}</summary>\n'
            f'      <div class="snav-links">\n        {links_html}\n      </div>\n    </details>'
        )
    return "\n    ".join(out)


def pager_html(i: int) -> str:
    parts = []
    if i > 0:
        s, _f, en, ne, *_ = PAGES[i - 1]
        num = NUM[s]
        href = "index.html" if s == "index" else f"{s}.html"
        parts.append(
            f'<a class="prev" href="{href}"><span class="lbl">{ICON["left"]}<span class="en">Previous · {num}</span>'
            f'<span class="ne">अघिल्लो · {num.translate(NE_DIGITS)}</span></span><span class="en">{en}</span><span class="ne">{ne}</span></a>'
        )
    if i < len(PAGES) - 1:
        s, _f, en, ne, *_ = PAGES[i + 1]
        num = NUM[s]
        parts.append(
            f'<a class="next" href="{s}.html"><span class="lbl"><span class="en">Next · {num}</span>'
            f'<span class="ne">अर्को · {num.translate(NE_DIGITS)}</span>{ICON["right"]}</span><span class="en">{en}</span><span class="ne">{ne}</span></a>'
        )
    return "\n    ".join(parts)



TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
BLOCK_RE = re.compile(r"<(script|style|svg)[\s\S]*?</\1>")
DUAL_RE = re.compile(r'<span class="en">(.*?)</span>\s*<span class="ne">(.*?)</span>', re.S)


VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class _NeStripper(HTMLParser):
    """Rebuild HTML without any element whose class token list contains 'ne'."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.parts = []
        self.skip = 0  # open-tag depth inside a dropped '.ne' subtree

    def _cls(self, attrs):
        return dict(attrs).get("class", "").split() if attrs else []

    def handle_starttag(self, tag, attrs):
        if self.skip:
            if tag not in VOID_TAGS:
                self.skip += 1
            return
        if "ne" in self._cls(attrs):
            if tag not in VOID_TAGS:
                self.skip = 1
            return
        self.parts.append(self.get_starttag_text())

    def handle_startendtag(self, tag, attrs):
        if not self.skip and "ne" not in self._cls(attrs):
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if self.skip:
            if tag not in VOID_TAGS:
                self.skip -= 1
            return
        self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def handle_entityref(self, name):
        if not self.skip:
            self.parts.append(f"&{name};")

    def handle_charref(self, name):
        if not self.skip:
            self.parts.append(f"&#{name};")

    def handle_comment(self, data):
        if not self.skip:
            self.parts.append(f"<!--{data}-->")

    def handle_decl(self, decl):
        if not self.skip:
            self.parts.append(f"<!{decl}>")

    def handle_pi(self, data):
        if not self.skip:
            self.parts.append(f"<?{data}>")


def strip_ne(html: str) -> str:
    """Drop every element with a 'ne' class token (and its whole subtree)."""
    p = _NeStripper()
    p.feed(html)
    p.close()
    return "".join(p.parts)


# ---- SHELL fragments that swap with the language phase (build.py PHASE1_ENGLISH_ONLY) ----
LANG_BOOT_FULL = "(function(){var d=document.documentElement;try{if(localStorage.getItem('psc-lang')==='ne'){d.setAttribute('data-lang','ne');d.lang='ne';}else{d.setAttribute('data-lang','en');}var t=localStorage.getItem('psc-theme');if(t==='light'||t==='dark')d.setAttribute('data-theme',t);if(localStorage.getItem('psc-nav-collapsed'))d.classList.add('nav-collapsed-init');}catch(e){d.setAttribute('data-lang','en');}})();"
LANG_BOOT_PHASE1 = "(function(){var d=document.documentElement;d.setAttribute('data-lang','en');d.lang='en';try{var t=localStorage.getItem('psc-theme');if(t==='light'||t==='dark')d.setAttribute('data-theme',t);if(localStorage.getItem('psc-nav-collapsed'))d.classList.add('nav-collapsed-init');}catch(e){}})();"
LANGSW_SIDE = ('<div class="langsw" role="group" aria-label="Language">\n'
               '          <button class="btn-en" data-lang-btn="en" onclick="setLang(\'en\')">EN</button>\n'
               '          <button class="btn-ne" data-lang-btn="ne" onclick="setLang(\'ne\')">ने</button>\n'
               '        </div>\n        ')
LANGSW_PILL = ('<div class="langsw" role="group" aria-label="Language">\n'
               '          <button class="btn-en" data-lang-btn="en" onclick="setLang(\'en\')">EN</button>\n'
               '          <button class="btn-ne" data-lang-btn="ne" onclick="setLang(\'ne\')">ने</button>\n'
               '        </div>\n        ')
OG_LOCALE_BILINGUAL = '<meta property="og:locale:alternate" content="ne_NP">'
OG_LOCALE_ENGLISH_ONLY = ''
SEARCH_PH_BI = "Search · खोज्नुहोस्"
SEARCH_PH_EN = "Search the atlas"
FOOT_BLURB_BI = "A free, open atlas of mental health in English and नेपाली. Educational resource, not a diagnostic tool: criteria are paraphrased from DSM-5 (2013). Diagnosis belongs to qualified clinicians."
FOOT_BLURB_EN = "A free, open atlas of mental health in English, built for the Nepali context. Educational resource, not a diagnostic tool: criteria are paraphrased from DSM-5 (2013). Diagnosis belongs to qualified clinicians."


def plain_text(html: str) -> str:
    html = BLOCK_RE.sub(" ", html)
    txt = TAG_RE.sub(" ", html)
    for a, b in (("&amp;", "&"), ("&nbsp;", " "), ("&lt;", "<"), ("&gt;", ">"), ("&#8201;", " ")):
        txt = txt.replace(a, b)
    return WS_RE.sub(" ", txt).strip()


def dual_title(html: str, fallback):
    m = DUAL_RE.search(html or "")
    if not m:
        return fallback
    return (plain_text(m.group(1)), plain_text(m.group(2)))


SPOT = {'overview': '<svg class="spot" viewBox="0 0 170 120" role="img" aria-label="A compass with its needle pointing north-east.">\n  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">\n    <circle cx="85" cy="62" r="40" style="fill:var(--bg)"/>\n    <circle cx="85" cy="62" r="46" fill="none" opacity=".35"/>\n    <line x1="85" y1="14" x2="85" y2="20"/><line x1="85" y1="104" x2="85" y2="110"/>\n    <line x1="37" y1="62" x2="43" y2="62"/><line x1="127" y1="62" x2="133" y2="62"/>\n  </g>\n  <path d="M85,62 L104,36 L92,62 Z" style="fill:var(--accent)"/>\n  <path d="M85,62 L66,88 L78,62 Z" fill="currentColor"/>\n  <path d="M85,62 L104,36 L92,62 L85,62 L66,88 L78,62 Z" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>\n  <circle cx="85" cy="62" r="4" style="fill:var(--bg)" stroke="currentColor" stroke-width="2.4"/>\n</svg>', 'practice': '<svg class="spot" viewBox="0 0 170 120" role="img" aria-label="Two people sitting and talking, one leaning in to listen.">\n  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">\n    <line x1="18" y1="104" x2="152" y2="104"/>\n    <!-- left person -->\n    <path d="M40,104 L40,82 C40,70 48,62 60,62 L66,62 C74,62 80,68 80,76 L80,104" style="fill:var(--bg)"/>\n    <path d="M80,84 C90,82 96,84 100,90" fill="none"/>\n    <circle cx="61" cy="46" r="13" style="fill:var(--bg)"/>\n    <path d="M48,44 C48,32 60,28 66,32 C72,30 76,38 74,45 C68,40 56,40 48,44 Z" fill="currentColor"/>\n    <!-- right person, leaning in -->\n    <path d="M132,104 L132,84 C132,72 124,64 112,64 L106,64 C98,64 92,70 92,78 L92,104" style="fill:var(--accent)"/>\n    <path d="M92,86 C86,88 82,92 80,96" fill="none"/>\n    <circle cx="110" cy="48" r="13" style="fill:var(--bg)"/>\n    <path d="M97,46 C97,34 108,29 116,33 C122,34 124,42 122,48 C114,42 104,42 97,46 Z" fill="currentColor"/>\n  </g>\n  <path d="M74,22 C80,14 92,14 98,22" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="3 5"/>\n</svg>', 'disorders': '<svg class="spot" viewBox="0 0 170 120" role="img" aria-label="A small clay lamp, a diyo, burning in the dark.">\n  <circle cx="85" cy="56" r="46" fill="currentColor" opacity=".07"/>\n  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">\n    <path d="M42,76 C42,72 48,70 60,70 L110,70 C122,70 128,72 128,76 C128,92 112,102 85,102 C58,102 42,92 42,76 Z" style="fill:var(--bg)"/>\n    <path d="M42,76 C50,80 70,82 85,82 C100,82 120,80 128,76" fill="none"/>\n    <path d="M66,102 C66,108 72,112 85,112 C98,112 104,108 104,102" fill="none"/>\n    <path d="M85,70 C85,66 86,62 88,58" fill="none"/>\n  </g>\n  <path d="M85,66 C74,52 78,40 85,28 C92,40 96,52 85,66 Z" style="fill:var(--accent)"/>\n  <path d="M85,60 C80,52 82,46 85,40 C88,46 90,52 85,60 Z" style="fill:var(--bg)"/>\n  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" opacity=".7">\n    <line x1="56" y1="36" x2="62" y2="42"/><line x1="114" y1="36" x2="108" y2="42"/>\n    <line x1="85" y1="12" x2="85" y2="18"/>\n  </g>\n</svg>', 'reference': '<svg class="spot" viewBox="0 0 170 120" role="img" aria-label="An open book with a small sprig of leaves resting on it.">\n  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">\n    <path d="M24,34 C44,26 66,28 85,40 L85,98 C66,86 44,84 24,92 Z" style="fill:var(--bg)"/>\n    <path d="M146,34 C126,26 104,28 85,40 L85,98 C104,86 126,84 146,92 Z" style="fill:var(--bg)"/>\n    <line x1="85" y1="40" x2="85" y2="98"/>\n    <path d="M36,50 C50,46 62,48 74,54" fill="none" opacity=".5"/><path d="M36,64 C50,60 62,62 74,68" fill="none" opacity=".5"/>\n    <path d="M96,54 C108,48 120,46 134,50" fill="none" opacity=".5"/><path d="M96,68 C108,62 120,60 134,64" fill="none" opacity=".5"/>\n    <line x1="20" y1="98" x2="150" y2="98"/>\n  </g>\n  <g stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">\n    <path d="M100,92 C110,78 120,66 134,52" fill="none"/>\n    <path d="M112,76 C104,74 100,66 102,58 C110,60 114,68 112,76 Z" style="fill:var(--accent)"/>\n    <path d="M118,68 C126,66 134,58 134,50 C126,52 118,58 118,68 Z" style="fill:var(--accent)"/>\n    <path d="M106,84 C100,82 96,76 98,70 C104,72 108,78 106,84 Z" style="fill:var(--accent)"/>\n  </g>\n</svg>'}


def toc_html() -> str:
    out = []
    last_group = None
    for slug, _f, en, ne, cat, group in PAGES:
        num = NUM[slug]
        if slug == "index":
            continue
        if group != last_group:
            g_en, g_ne = GROUPS[group]
            art = SPOT.get(group, "")
            n = sum(1 for p in PAGES if p[5] == group)
            out.append(f'<div class="toc-grp{" has-art" if art else ""}">{art}<div><h2><span class="en">{g_en}</span><span class="ne">{g_ne}</span></h2>'
                       f'<span class="toc-count"><span class="en">{n} chapters</span><span class="ne">{str(n).translate(NE_DIGITS)} अध्याय</span></span></div></div>')
            last_group = group
        mark = f'<span class="catmark" style="background:var({cat})"></span>' if cat else ""
        out.append(f'<a href="{slug}.html">{mark}<span class="secnum">{num}</span>'
                   f'<span class="en">{en}</span><span class="ne">{ne}</span></a>')
    return '<nav class="toc" aria-label="Contents">\n    ' + "\n    ".join(out) + '\n  </nav>'


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<script>{lang_boot}</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{page_desc}">
{og_locale}
<title>{title}</title>
<link rel="canonical" href="{page_url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Mano Atlas · मनो एट्लास">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{page_desc}">
<meta property="og:url" content="{page_url}">
<meta property="og:locale" content="en_GB">
<meta property="og:locale:alternate" content="ne_NP">
<meta property="og:image" content="{site_url}/assets/og/{og_slug}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{site_url}/assets/og/{og_slug}.png">
<link rel="alternate" type="text/plain" href="{site_url}/llms.txt" title="llms.txt">
<script type="application/ld+json">{jsonld}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 48 48%22%3E%3Crect width=%2248%22 height=%2248%22 rx=%2211%22 fill=%22#1D6A73%22/%3E%3Cg stroke=%22#fff%22 stroke-width=%222.8%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 fill=%22none%22%3E%3Cpath d=%22M24 37 C24 30 23.5 25 24 19%22/%3E%3Cpath d=%22M24 27 C18 27 14.5 22.5 14 17 C20 17.5 23.5 21.5 24 27 Z%22 fill=%22#8ACBD2%22/%3E%3Cpath d=%22M24 23 C30 23 33.5 18.5 34 13 C28 13.5 24.5 17.5 24 23 Z%22 fill=%22#8ACBD2%22/%3E%3C/g%3E%3Ccircle cx=%2224%22 cy=%2238.5%22 r=%222.6%22 fill=%22#fff%22/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=Mukta:wght@400;600;700&family=IBM+Plex+Mono:wght@400&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=Mukta:wght@400;600;700&family=IBM+Plex+Mono:wght@400&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=Mukta:wght@400;600;700&family=IBM+Plex+Mono:wght@400&display=swap"></noscript>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main"><span class="en">Skip to content</span><span class="ne">सामग्रीमा जानुहोस्</span></a>
<div class="layout">
  <aside class="sidebar">
    <div class="top">
      <button class="collapse-btn" id="btn-collapse" type="button" aria-label="Hide chapters" title="Hide chapters">{icon_panel}</button>
      <a class="brand" href="index.html"><svg class="mark" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="20" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M24 35 C24 29 23.5 24 24 19" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M24 26 C18.5 26 15 22 14.5 17 C20 17.5 23.5 21 24 26 Z" style="fill:var(--accent)" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M24 22 C29.5 22 33 18 33.5 13 C28 13.5 24.5 17 24 22 Z" style="fill:var(--accent)" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="24" cy="36.5" r="2.4" fill="currentColor"/></svg><span class="en">Mano Atlas</span><span class="ne">मनो एट्लास</span></a>
      <div class="ctrls">
        {langsw_side}
        <button id="btn-theme" class="themesw btn-theme" onclick="cycleTheme()" title="Colour theme">◐ Auto</button>
      </div>
    </div>
    <div class="search" id="searchbox"><span class="s-ico">{icon_search}</span>
      <input id="q" type="search" autocomplete="off" spellcheck="false"
        placeholder="{search_ph}" aria-label="Search the atlas">
      <div id="qres" class="qres" hidden></div>
      <button id="btn-nav" class="navbtn" type="button" aria-expanded="false" aria-controls="snav">{icon_menu}<span class="en">Chapters</span><span class="ne">अध्याय</span></button>
    </div>
    <nav class="snav" id="snav" aria-label="Site">
      {nav}
    </nav>
  </aside>
  <main id="main">
    <div class="topctrl" id="topctrl" aria-label="Language and theme">
      <button class="expand-btn" id="btn-expand" type="button" aria-label="Show chapters">{icon_panel}<span class="en">Chapters</span><span class="ne">अध्याय</span></button>
      <div class="topctrl-pill" id="pill">
        <span class="pill-search" id="pill-search"></span>
        {langsw_pill}
        <button class="themesw btn-theme" onclick="cycleTheme()" title="Colour theme">◐ Auto</button>
      </div>
    </div>
    <div class="wrap">
{content}
    <p class="progress"><span id="progress"></span></p>
    <nav class="pager" aria-label="Chapter">
    {pager}
    </nav>
    <footer class="sitefoot">
      <div class="cols">
        <div>
          <h3 class="foot-h"><span class="en">Mano Atlas</span><span class="ne">मनो एट्लास</span></h3>
          <p class="en">{foot_blurb}</p>
          <p class="ne">अंग्रेजी र नेपालीमा मानसिक स्वास्थ्यको निःशुल्क, खुला एट्लास। शैक्षिक सामग्री हो, निदान-उपकरण होइन: मापदण्ड DSM-5 (2013) बाट सरलीकृत छन्। निदान योग्य चिकित्सकको काम हो।</p>
          <p class="en">Learning sticks best in small sittings. It is fine to close this tab and come back another day.</p>\n          <p class="ne">सिकाइ साना-साना बसाइमा राम्रो टिक्छ। ट्याब बन्द गरेर अर्को दिन फर्किए हुन्छ।</p>\n          <p><span class="en">Last reviewed: {reviewed_en} · This page updated {updated_en}</span><span class="ne">पछिल्लो समीक्षा: {reviewed_ne} · यो पृष्ठ अद्यावधिक {updated_ne}</span></p>
        </div>
        <div class="crisis-col">
          <h3 class="foot-h">{icon_phone} <span class="en">If you need help now · Nepal</span><span class="ne">अहिले नै सहयोग चाहिए · नेपाल</span></h3>
          <p><strong><a href="tel:1166">{helpline_suicide}</a></strong> <span class="en">National Suicide Prevention Helpline</span><span class="ne">राष्ट्रिय आत्महत्या रोकथाम हेल्पलाइन</span></p>
          <p><strong><a href="tel:16600121600">{helpline_tuth}</a></strong> <span class="en">TUTH mental-health hotline</span><span class="ne">टिचिङ अस्पताल हटलाइन</span></p>
          <p><strong><a href="tel:1145">{helpline_women}</a></strong> <span class="en">Women's helpline</span><span class="ne">महिला हेल्पलाइन</span> · <strong><a href="tel:112">112</a> / <a href="tel:100">100</a></strong> <span class="en">emergency</span><span class="ne">आपतकाल</span></p>
          <p class="outside"><span class="en">These numbers work inside Nepal. Elsewhere, <a href="https://findahelpline.com" target="_blank" rel="noopener noreferrer">findahelpline.com</a> lists your country's lines.</span><span class="ne">यी नम्बर नेपालभित्र चल्छन्। अन्यत्र हुनुहुन्छ भने <a href="https://findahelpline.com" target="_blank" rel="noopener noreferrer">findahelpline.com</a> मा आफ्नो देशका नम्बर भेटिन्छन्।</span></p>
        </div>
        <div>
          <h3 class="foot-h"><span class="en">Open &amp; improvable</span><span class="ne">खुला र सुधारयोग्य</span></h3>
          <p class="en">Our own content is <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license noopener noreferrer" target="_blank">CC BY-NC-SA 4.0</a>: share and adapt with credit, never for charge. <a href="terms.html">Terms, licence and sources</a></p>
          <p class="ne">हाम्रो आफ्नै सामग्री <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license noopener noreferrer" target="_blank">CC BY-NC-SA 4.0</a> अन्तर्गत: श्रेयसहित बाँड्न र मिलाउन पाइन्छ, तर कुनै शुल्क लिन पाइँदैन। <a href="terms.html">सर्त, इजाजतपत्र र स्रोतहरू</a></p>
          <p>{icon_mail} <span class="en">Spotted an error?</span><span class="ne">त्रुटि भेट्नुभयो?</span> <span class="mailrev" data-u="{email_user}" data-d="{email_domain}" data-t="{email_tld}">{email_user} [at] {email_domain} [dot] {email_tld}</span></p>
          <p class="fine"><span class="en">If a message says a child is being harmed, we have to tell the police.</span><span class="ne">सन्देशमा बालबालिकामाथि कुटुने कुरा भनिएको छ भने, हामीले प्रहरीलाई खबर गर्नुपर्छ।</span></p>
        </div>
      </div>
      <p class="fine"><span class="en">Built from the CTEVT Psychosocial Counselor curriculum, class notes, and the sources named on each page.</span><span class="ne">सीटीईभीटी मनोसामाजिक परामर्शकर्ता पाठ्यक्रम, कक्षा-नोट र प्रत्येक पृष्ठमा उल्लिखित स्रोतबाट निर्मित।</span></p>
      <p class="fine"><span class="en">Maintained and updated by <a href="https://pravashkarki.com" target="_blank" rel="noopener noreferrer">Pravash Karki</a>. Hosting and other infrastructure supported by <a href="https://lastdoorsolutions.com" target="_blank" rel="noopener noreferrer">LastDoor</a>.</span><span class="ne">सञ्चालन र अद्यावधिकारण <a href="https://pravashkarki.com" target="_blank" rel="noopener noreferrer">पृवाश कार्की</a>द्वारा गरिएको। होस्टिङ र अन्य पूर्वाधार सहयोग <a href="https://lastdoorsolutions.com" target="_blank" rel="noopener noreferrer">लास्टडोर</a>ले गरेको छ।</span></p>
    </footer>
    </div>
  </main>
</div>
<script src="assets/lang.js" defer></script>
<script src="assets/search.js" defer></script>
</body>
</html>
"""



OG_MARK = ('<svg viewBox="0 0 48 48" width="44" height="44" aria-hidden="true"><circle cx="24" cy="24" r="20" fill="none" stroke="#24272C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
           '<path d="M24 35 C24 29 23.5 24 24 19" fill="none" stroke="#24272C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
           '<path d="M24 26 C18.5 26 15 22 14.5 17 C20 17.5 23.5 21 24 26 Z" fill="#1D6A73" stroke="#24272C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
           '<path d="M24 22 C29.5 22 33 18 33.5 13 C28 13.5 24.5 17 24 22 Z" fill="#1D6A73" stroke="#24272C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
           '<circle cx="24" cy="36.5" r="2.4" fill="#24272C"/></svg>')

OG_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Mukta:wght@400;600;700&family=Literata:ital,opsz,wght@0,7..72,400&display=block">
<style>
html,body{{margin:0;padding:0}}
body{{width:1200px;height:630px;overflow:hidden;background:#F5F4F0;color:#24272C;font-family:'Archivo','Mukta',system-ui,sans-serif;position:relative}}
.dhaka{{position:absolute;left:0;top:0;width:1200px;height:12px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='56' height='12'%3E%3Cpath d='M0 12L14 0l14 12z' fill='%231D6A73'/%3E%3Cpath d='M28 12l14-12 14 12z' fill='%23C98A1B' fill-opacity='.75'/%3E%3C/svg%3E");background-repeat:repeat-x}}
.brand{{position:absolute;left:64px;top:52px;display:flex;align-items:center;gap:14px;font-weight:700;font-size:26px;letter-spacing:.01em}}
.brand .ne{{font-family:'Mukta',sans-serif;font-weight:600;font-size:29px;color:#6C6F76}}
.brand .dot{{color:#6C6F76;font-weight:400}}
.kicker{{position:absolute;left:64px;top:146px;font-size:19px;letter-spacing:.14em;text-transform:uppercase;color:#155A62;font-weight:700}}
.kicker .ne{{font-family:'Mukta',sans-serif;text-transform:none;letter-spacing:0;font-size:22px;font-weight:600;color:#6C6F76;margin-left:14px}}
.rule{{position:absolute;left:64px;top:186px;width:72px;height:4px;background:#1D6A73;border-radius:2px}}
.title{{position:absolute;left:64px;top:214px;width:880px}}
.title .en{{display:block;font-weight:800;font-size:{en_size}px;line-height:1.08;letter-spacing:-.015em;text-wrap:balance}}
.title .ne{{display:block;font-family:'Mukta',sans-serif;font-weight:600;font-size:{ne_size}px;line-height:1.3;margin-top:14px;color:#3A3E45;text-wrap:balance}}
.tag{{position:absolute;left:64px;top:{tag_top}px;width:880px;font-family:'Literata',Georgia,serif;font-size:24px;line-height:1.45;color:#6C6F76}}
.num{{position:absolute;right:56px;bottom:22px;font-weight:800;font-size:300px;line-height:1;letter-spacing:-.04em;color:#1D6A73;opacity:.13}}
.foot{{position:absolute;left:64px;bottom:44px;font-size:19px;color:#6C6F76;letter-spacing:.02em}}
.foot .ne{{font-family:'Mukta',sans-serif;font-size:21px}}
</style></head><body>
<div class="dhaka"></div>
<div class="brand">{mark}<span>Mano Atlas</span><span class="dot">·</span><span class="ne">मनो एट्लास</span></div>
{kicker}
<div class="rule"></div>
<div class="title"><span class="en">{en}</span><span class="ne">{ne}</span></div>
{tag}
{num}
<div class="foot">manoatlas.com &nbsp;·&nbsp; free &nbsp;·&nbsp; English / <span class="ne">नेपाली</span></div>
</body></html>
"""


def write_og_sources() -> None:
    """One self-contained HTML per page under assets/og/src/; tools/og-render.sh turns them into PNGs."""
    out = ROOT / "assets" / "og" / "src"
    out.mkdir(parents=True, exist_ok=True)
    for slug, _f, en, ne, _cat, group in PAGES:
        g_en, g_ne = GROUPS[group]
        if slug == "index":
            en_t, ne_t = "Mano Atlas", "मनो एट्लास"
            kicker = '<div class="kicker">An open atlas of mental health<span class="ne">मानसिक स्वास्थ्यको खुला एट्लास</span></div>'
            tag = ('<div class="tag">A free, bilingual atlas of mental disorders: DSM-5 criteria, teaching diagrams, and the Nepali context.<br>'
                   '<span style="font-family:Mukta,sans-serif;font-size:26px">मानसिक विकारहरूको निःशुल्क, द्विभाषी एट्लास: DSM-5 मापदण्ड, चित्र र नेपाली सन्दर्भ।</span></div>')
            num = ""
            en_size, ne_size, tag_top = 92, 60, 400
        else:
            en_t, ne_t = html_mod.escape(en), html_mod.escape(ne)
            kicker = f'<div class="kicker">Chapter {NUM[slug]} · {g_en}<span class="ne">{g_ne}</span></div>'
            tag = ""
            num = f'<div class="num" aria-hidden="true">{NUM[slug]}</div>'
            longest = max(len(en), len(ne) * 1.15)
            en_size = 72 if longest <= 26 else 62 if longest <= 34 else 54
            ne_size = round(en_size * 0.78)
            tag_top = 0
        (out / f"{slug}.html").write_text(OG_TEMPLATE.format(mark=OG_MARK, kicker=kicker, en=en_t, ne=ne_t, tag=tag, num=num,
                                                              en_size=en_size, ne_size=ne_size, tag_top=tag_top))


def gate_sources() -> None:
    """House rules that must hold before anything is generated."""
    for d in ("content", "quizzes", "keypoints"):
        for f in sorted((ROOT / d).glob("*.html")):
            txt = f.read_text()
            if "\u2014" in txt:
                raise SystemExit(f"build: {d}/{f.name}: em-dash found; use a colon, comma, semicolon or parentheses")


def recent_html() -> str:
    """Home page strip: chapters added in the last 90 days (from git), newest first, at most four."""
    import datetime
    today = datetime.date.today()
    rows = []
    for slug, fname, en, ne, _cat, _group in PAGES:
        if slug == "index":
            continue
        d = git_date(ROOT / "content" / f"{fname}.html", added=True)
        age = (today - datetime.date.fromisoformat(d)).days
        if age <= 90 and d > SITE["recent_since"]:
            rows.append((d, slug, en, ne))
    if not rows:
        return ""
    rows.sort(reverse=True)
    links = "".join(f'<a href="{s}.html"><span class="secnum">{NUM[s]}</span><span class="en">{e}</span><span class="ne">{n}</span></a>' for _d, s, e, n in rows[:4])
    return ('<div class="recent"><span class="recent-h">' + ICON["sprout"] + '<span class="en">Recently added</span><span class="ne">भर्खरै थपिएका</span></span>'
            + links + '</div>\n')


# ---- student vault (/vault): the Drive folder, tagged, behind a password ----
# A standalone page like 404.html, not a chapter: no number, no sidebar row, no
# sitemap entry, no search index row, and nothing in PAGES changes, so inserting
# it never renumbers a chapter.
#
# The gate is a browser-side password check against a stored SHA-256. It is a
# convenience marker, not a security boundary: the Drive folder is public and the
# links are in this page's source either way. Real protection means private Drive
# files plus a server function with a service account, which is a different build.
# export=download makes Drive answer with Content-Disposition: attachment, which is
# what forces a download rather than opening its viewer. The download attribute is
# ignored cross-origin, so the query parameter is what does the work here.
DRIVE_DL = "https://drive.google.com/uc?export=download&id={id}"
DRIVE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{25,60}$")   # a pasted web link or a filename here means a broken row


def bi(obj: dict) -> str:
    """Every user-visible string ships twice, en and ne (repo rule, never break it). The
    English-only phase is a display switch, not a source policy: strip_ne drops the ne
    span at build and PHASE1_ENGLISH_ONLY hides the switch, so the Nepali is still here
    and returns with the flag."""
    if not obj.get("ne"):
        raise SystemExit("build: vault: string has no Nepali; the bilingual pattern is not optional")
    return f'<span class="en">{obj["en"]}</span><span class="ne">{obj["ne"]}</span>'


def chapter_pill(slug: str) -> str:
    row = next(p for p in PAGES if p[0] == slug)
    return (f'<a class="vpill" href="{slug}.html"><span class="vnum">{NUM[slug]}</span>'
            f'<span class="en">{row[2]}</span><span class="ne">{row[3]}</span></a>')


def vault_html() -> str:
    data = json.loads((ROOT / "vault.json").read_text())
    groups = {g["key"]: g for g in data["groups"]}
    order = [g["key"] for g in data["groups"]]
    files = data["files"]
    known = set(NUM)
    sections = []
    for key in order:
        g = groups[key]
        rows = []
        for f in [x for x in files if x["group"] == key]:
            if not DRIVE_ID_RE.match(f["id"]):
                raise SystemExit(f"build: vault: {f['file']}: Drive id looks wrong ({f['id']})")
            for slug in f.get("chapters", []):
                if slug not in known:
                    raise SystemExit(f"build: vault: {f['file']}: unknown chapter slug {slug}")
            meta = " · ".join(x for x in (f.get("type"), f.get("size"), f.get("pages")) if x)
            chaps = f.get("chapters") or []
            if chaps:
                pills = "".join(chapter_pill(s) for s in chaps)
                chapline = ('<p class="vchap"><span class="vchap-h">'
                            + bi({"en": "Easier on the site:", "ne": "साइटमा सजिलो:"}) + "</span>" + pills + "</p>\n")
            else:
                chapline = ('<p class="vchap vchap-none">'
                            + bi({"en": "No chapter covers this one. It stands on its own, away from the atlas chapters.",
                                  "ne": "यसको कुनै खण्ड छैन। यो एटलासका खण्डबाट छुट्टै आफ्नै स्थानमा छ।"})
                            + "</p>\n")
            about = '<p class="vabout">' + bi(f["about"]) + "</p>"
            title = bi(f["title"])
            orig = f'<span class="vorig mono">{f["file"]}</span>\n' if f.get("file") else ""
            author = f'<span class="vauthor">{f["author"]}</span>' if f.get("author") else ""
            # the author is a separate field, so the separator belongs to the join, not to
            # whichever metadata value happens to come last (a row with no page count used
            # to run the name straight on from the file size)
            vmeta = " · ".join(x for x in (meta, author) if x)
            rows.append(
                f'<li class="vfile">\n<div class="vhead">'
                f'<a class="vname" href="{DRIVE_DL.format(id=f["id"])}">{title}</a>'
                f'<span class="vtag">{bi(g["title"])}</span></div>\n'
                f'<p class="vmeta mono">{vmeta}</p>\n{orig}{about}{chapline}</li>\n')
        sections.append(
            f'<section class="vgroup" id="v-{key}">\n'
            f'<h2>{bi(g["title"])}</h2>\n'
            f'<p class="secsub">{bi(g["note"])}</p>\n'
            f'<ul class="vfiles">\n' + "".join(rows) + '</ul>\n</section>\n')

    n = len(files)
    gate = (
        f'<section class="vaultgate" id="vgate" data-pw="{data["password_sha256"]}">\n'
        f'<h2>{bi({"en": "The class files, in one place", "ne": "कक्षाका फाइल, एउटै ठाउँमा"})}</h2>\n'
        f'<p class="secsub">{bi({
            "en": f"{n} files from the course folder, each one tagged so you know what to read first. Enter the password your instructor gave you.",
            "ne": f"पाठ्यक्रमको फोल्डरका {str(n).translate(NE_DIGITS)} फाइल, हरेकलाई ट्याग लगाइएको छ जसले अघि के पढ्ने भन्ने थाहा पाउनुहोस्। शिक्षकले दिनुभएको पासवर्ड लेख्नुहोस्।"})}</p>\n'
        # Not a <form>: a form with JS off falls back to a native GET submit and puts
        # the password in the URL, where browser history and request logs keep it.
        # There is no server to post to anyway, so it is a group with a button, and
        # Enter is handled by hand.
        f'<div class="vform" id="vform" role="group" autocomplete="off">\n'
        f'<label for="vpw">{bi({"en": "Course password", "ne": "पाठ्यक्रमको पासवर्ड"})}</label>\n'
        f'<input id="vpw" type="password" name="pw" spellcheck="false" autocapitalize="off">\n'
        f'<button type="button" id="vbtn" class="vbtn">{bi({"en": "Unlock", "ne": "खोल्नुहोस्"})}</button>\n'
        f'</div>\n'
        f'<p class="verr" id="verr" hidden>{bi({
            "en": "That password did not match. Try again, or ask your instructor.",
            "ne": "पासवर्ड मिलेन। फेरि प्रयास गर्नुहोस्, वा शिक्षकलाई सोध्नुहोस्।"})}</p>\n'
        f'<p class="verr" id="verrtech" hidden>{bi({
            "en": "The password check needs a secure connection. Open this page at manoatlas.com rather than from a file on disk.",
            "ne": "पासवर्ड जाँच्न सुरक्षित जडान चाहिन्छ। यो पृष्ठ डिस्कको फाइलबाट होइन, manoatlas.com मा खोल्नुहोस्।"})}</p>\n'
        f'<p class="vhint">{bi({
            "en": "No password? Ask your instructor. Do not share this page publicly: anyone with the link can reach the files.",
            "ne": "पासवर्ड छैन? शिक्षकलाई सोध्नुहोस्। यो पृष्ठ सार्वजनिक नगर्नुहोस्: लिंक भएकाले जो कोही फाइलमा पुग्न सक्छन्।"})}</p>\n'
        f'</section>\n')

    head = ('<div class="pagehead vault-head"><h1 class="kicker">'
            + bi({"en": "Student vault", "ne": "विद्यार्थी ताला"}) + '</h1></div>\n')
    # The gate runs in the page: SHA-256 of what was typed against the stored hash.
    # crypto.subtle needs a secure context, so the live https site and the Vercel
    # preview both work; opening the file straight off disk does not, and we say so
    # rather than falling back to something weaker.
    script = (
        '<script>\n(function(){\n'
        '  var gate=document.getElementById("vgate"),list=document.getElementById("vlist"),\n'
        '      btn=document.getElementById("vbtn"),input=document.getElementById("vpw"),\n'
        '      err=document.getElementById("verr"),tech=document.getElementById("verrtech");\n'
        '  if(!gate||!list||!btn||!input)return;\n'
        '  function show(ok){\n'
        '    gate.hidden=ok; list.hidden=!ok;\n'
        '    if(ok){try{sessionStorage.setItem("psc-vault","1");}catch(e){}}\n'
        '    else{err.hidden=false; input.select();}\n'
        '  }\n'
        '  try{if(sessionStorage.getItem("psc-vault")==="1")show(true);}catch(e){}\n'
        '  function check(){\n'
        '    err.hidden=true; tech.hidden=true;\n'
        '    if(!window.crypto||!crypto.subtle){tech.hidden=false;return;}\n'
        '    crypto.subtle.digest("SHA-256",new TextEncoder().encode(input.value))\n'
        '      .then(function(buf){\n'
        '        var hex=Array.prototype.map.call(new Uint8Array(buf),function(b){\n'
        '          return ("0"+b.toString(16)).slice(-2);}).join("");\n'
        '        show(hex===gate.getAttribute("data-pw"));\n'
        '      })\n'
        '      .catch(function(){err.hidden=false;});\n'
        '  }\n'
        '  btn.addEventListener("click",check);\n'
        '  input.addEventListener("keydown",function(e){if(e.key==="Enter"){e.preventDefault();check();}});\n'
        '})();\n</script>\n')
    return head + gate + '<div id="vlist" hidden>\n' + "".join(sections) + '</div>\n' + script


def _tcard(head_en: str, head_ne: str, body: list) -> str:
    # h2, not h3: these pages' title is the pagehead h1, so the card heads sit
    # directly beneath it. The size is pinned in style.css (.termscard h2) because
    # the browser default for h2 is larger than the h3 this replaced.
    return ('<div class="card termscard"><div class="card-body">\n'
            '        <h2><span class="en">' + head_en + '</span><span class="ne">' + head_ne + '</span></h2>\n'
            '        ' + "\n        ".join(body) + '\n      </div></div>\n')


def terms_html() -> str:
    """The terms, licence and safeguarding page.

    Standalone like /vault: not in PAGES, so it has no chapter number, no sidebar
    row and no sitemap entry, and adding it never renumbers anything. It is linked
    from the site footer on every page, because a licence nobody can reach is not a
    licence. Bilingual, and every string carries both languages.
    """
    cards = []
    cards.append(_tcard(
        "What this site is",
        "यो साइट के हो",
        ['<p>' + bi({"en": "Free open teaching material about mental health, in English and Nepali. "
                            "It was written for people training to counsel and for anyone who wants to understand the subject. "
                            "There is no account, no fee, and nothing here tracks who reads it.",
                     "ne": "मानसिक स्वास्थ्यबारे निःशुल्क, खुला सिकाउने सामग्री, अङ्ग्रेजी र नेपाली दुवै भाषामा। "
                           "यो परामर्शकर्ता बन्ने प्रशिक्षणार्थी र विषय बुझ्न चाहने जो कोहीका लागि लेखिएको हो। "
                           "यहाँ न खाता छ, न शुल्क, र कसले पढ्छ भन्ने कुरा यहाँ अनुगमन हुँदैन।"}) + '</p>']))
    cards.append(_tcard(
        "What it is not",
        "यो के होइन",
        ['<p>' + bi({"en": "It is not medical advice, not legal advice, and not a diagnostic tool. "
                            "Nothing here tells you what condition you have or what treatment you need. "
                            "Only a qualified person can do that, and seeing one is the right step if you are struggling.",
                     "ne": "यो चिकित्सकीय सल्लाह होइन, कानुनी सल्लाह होइन, र निदान गर्ने औजार होइन। "
                           "यहाँ के कसैलाई कुन रोग लागेको वा कुन उपचार चाहिन्छ भन्ने बताइँदैन। "
                           "त्यो काम योग्य व्यक्तिले मात्र गर्न सक्छ, र तपाईंलाई गाह्रो भइरहेको छ भने त्यसै व्यक्तिसँग जानु उचित हुन्छ।"}) + '</p>',
         '<p>' + bi({"en": "Every figure on these pages carries the source and the year it comes from. "
                            "Where a number is modelled by an international body rather than counted in Nepal, the page says so. "
                            "Where a Nepal figure does not exist, the page says that too, rather than estimating one.",
                     "ne": "यी पृष्ठका हरेक तथ्याङ्कसँग स्रोत र त्यसको वर्ष दिइएको छ। "
                           "कुनै अङ्क नेपालमा गनिएको नभई अन्तर्राष्ट्रिय निकायले अनुमान गरेको हो भने, पृष्ठले त्यो भन्छ। "
                           "नेपालको तथ्याङ्क नभएमा पनि पृष्ठले त्यही भन्छ, अनुमान गरेर दिँदैन।"}) + '</p>']))
    cards.append(_tcard(
        "If you are in crisis",
        "तपाईं संकटमा हुनुहुन्छ भने",
        ['<p>' + bi({"en": "Call 1166, the National Suicide Prevention Helpline at the Mental Hospital in Lagankhel, "
                            "or 1660 012 1600 at Tuth Hospital. In an emergency call 112 or 100. "
                            "If a number does not answer, try another, and if someone is in danger now do not wait on a helpline: "
                            "call 112 or 100. These four numbers are the highest-liability text on the whole site, which is why we "
                            "verify them against more than one source and why we ask you to tell us if one stops working.",
                     "ne": "११६६, लगनखेल मानसिक अस्पतालको राष्ट्रिय आत्महत्या रोकथाम हेल्पलाइन, वा टिचिंग अस्पतालको १६६० ०१२ १६०० मा फोन गर्नुहोस्। "
                           "आपतकालमा ११२ वा १०० मा फोन गर्नुहोस्। "
                           "कुनै नम्बरले उत्तर नदिए अर्को प्रयास गर्नुहोस्, र अहिले कसैलाई खतरा छ भने हेल्पलाइनमा पर्खनुहोस्: ११२ वा १०० मा फोन गर्नुहोस्। "
                           "यी चार नम्बर यो साइटका सबैभन्दा जोखिमपूर्ण अक्षर हुन्, त्यसैले हामी एकभन्दा बढी स्रोतबाट जाँच गर्छौं, "
                           "र कुनै नम्बर बिग्रिए तपाईंले हामीलाई जानकारी दिनु हुन्छ।"}) + '</p>']))
    cards.append(_tcard(
        "Reporting an error",
        "त्रुटि जानकारी दिनुहोस्",
        ['<p>' + bi({"en": "The address in the footer goes to the people who write these pages. "
                            "Tell us what is wrong and we will read it. We may correct it, we may leave it, "
                            "and we are not promising to change anything because you asked.",
                     "ne": "फुटरमा रहेको ठेगाना यी पृष्ठ लेख्नेहरूकहाँ पुग्छ। "
                           "के गलत छ भनी जानकारी दिनुहोस्, हामी पढ्छौं। हामी सुधार्न पनि सक्छौं, नसुधार्न पनि सक्छौं, "
                           "तर तपाईंले भन्नुभयो भनेर हामी केही बदल्ने प्रतिबद्धता दिँदैनौं।"}) + '</p>',
         '<p class="callout"><strong>' + bi({"en": "If your message says a child is being harmed, we have to tell the police.",
                                             "ne": "तपाईंको सन्देशमा बालबालिकामाथि कुटुने कुरा भनिएको छ भने, हामीले प्रहरीलाई खबर गर्नुपर्छ।"}) +
         '</strong> ' + bi({"en": "The law says anyone who learns of violence or sexual abuse against a child must inform the nearest police, "
                                 "and the law protects the person who does. So a message like that cannot be kept private, "
                                 "even if you ask us to. If someone is in danger now, do not email anyone: call 112 or 100, "
                                 "or 1166.",
                                 "ne": "कानुनअनुसार बालबालिकामाथि हिंसा वा यौन दुर्व्यवहारबारे थाहा पाउने जो कोहीले नजिकको प्रहरी कार्यालयमा जानकारी दिनुपर्छ, "
                                       "र त्यसो गर्ने व्यक्तिलाई कानुनले सुरक्षा दिन्छ। त्यसैले यस्तो सन्देश गोप्य राख्न सकिँदैन, तपाईंले भन्नुभए पनि। "
                                       "अहिले कसैलाई खतरा छ भने कसैलाई इमेल नगर्नुहोस्: ११२ वा १००, वा ११६६ मा फोन गर्नुहोस्।"}) + '</p>']))
    cards.append(_tcard(
        "Reusing the content",
        "सामग्री पुनः प्रयोग",
        ['<p>' + bi({"en": "Our own original material, which means the writing on these pages, the diagrams, the illustrations, "
                            "the Quick check questions and the Key points, is shared under a Creative Commons "
                            "Attribution, Non-Commercial, Share-Alike 4.0 licence.",
                     "ne": "हाम्रो आफ्नै मौलिक सामग्री, अर्थात् यी पृष्ठका लेख, चित्र, चित्रकारी, "
                           "Quick check प्रश्न र Key points, Creative Commons Attribution, Non-Commercial, Share-Alike 4.0 "
                           "इजाजतपत्रअन्तर्गत दिइएको छ।"}) + '</p>',
         '<p>' + bi({"en": "In practice: you may copy it, print it, translate it, and adapt it, including for a classroom, "
                            "a college, or a translation into another language. You cannot sell it, charge for it, or use it "
                            "as part of something you sell, and if you adapt it you must pass on the same licence. "
                            "Credit is required: name Mano Atlas, link to manoatlas.com, and say whether you changed anything.",
                     "ne": "व्यवहारमा: तपाईंले यसलाई प्रतिलिपि गर्न, छाप्न, अनुवाद गर्न वा रूपान्तरण गर्न सक्नुहुन्छ, कक्षा वा कलेजका लागि पनि, "
                           "अर्को भाषामा अनुवादका लागि पनि। तपाईंले यसलाई बेच्न, यसको शुल्क लिन, वा बिक्ने कुनै कुराको हिस्सा बनाउन सक्नुहुन्छन्, "
                           "र रूपान्तरण गर्दा यही इजाजतपत्र पनि अगाडि बढाउनुपर्छ। "
                           "श्रेय दिनुपर्छ: मानो एट्लासको नाम लिनुहोस्, manoatlas.com मा लिंक गर्नुहोस्, र केही परिवर्तन गरेको हो कि होइन भनी जनाउनुहोस्।"}) + '</p>',
         '<p class="fine">' + bi({"en": "Some sections adapt teaching material written by other people. That material belongs to "
                                        "its authors, and their terms are the ones that apply to it, not ours. Every contributor, "
                                        "what they gave us, and what terms apply are listed in the credits file, which is linked "
                                        "below and kept with the site source. We have not yet asked the authors what licence they "
                                        "will grant, and until we do, those sections carry no open licence from us. "
                                        "The licence above covers our own writing only.",
                                        "ne": "केही खण्डले अरू मानिसले लेखेको सिकाउने सामग्रीको रूपान्तरण गर्दै छन्। त्यो सामग्री तिनीहरूकै हो, "
                                              "र त्यसमा तिनीहरूकै सर्त लागू हुन्छ, हाम्रो होइन। कसले के दिए र कुन सर्त लागू हुन्छ, "
                                              "यो सबै तलको क्रेडिट फाइलमा उल्लेख छ, र त्यही फाइल साइटको स्रोतसँगै राखिएको छ। "
                                              "लेखकहरूलाई कस्तो इजाजत दिन्छन् भनी हामीले अझै सोधेका छैनौं, र सोधिएसम्म ती खण्डहरूमा "
                                              "हाम्रोतर्फबाट खुला इजाजत छैन। माथिको इजाजतपत्र हाम्रो आफ्नै लेखमा मात्र लागू हुन्छ।"}) + '</p>']))

    cards.append(_tcard(
        "The build code",
        "बिल्ड कोड",
        ['<p>' + bi({"en": "The scripts, styles and small pieces of JavaScript that assemble this site are under the MIT licence, "
                            "which is separate from the content licence above and lets anyone reuse the tooling freely.",
                     "ne": "यो साइट बनाउने स्क्रिप्ट, स्टाइल र साना जाभास्क्रिप्टहरू MIT इजाजतपत्रअन्तर्गत छन्, "
                           "जुन माथिको सामग्रीको इजाजतपत्रभन्दा छुट्टै हो र जसले कसैलाई पनि औजार निःशुल्क पुनः प्रयोग गर्न दिन्छ।"}) + '</p>',
         '<p class="fine">' + bi({"en": "The atlas name, the logo and the site's own visual identity are not covered by either "
                                        "licence. Please do not republish it as your own.",
                                        "ne": "एट्लासको नाम, लोगो र साइटको आफ्नै दृश्य पहिचान यी कुनै इजाजतपत्रअन्तर्गत छैन। "
                                              "कृपया यसलाई आफ्नै नाममा पुनः प्रकाशित नगर्नुहोस्।"}) + '</p>']))
    cards.append(_tcard(
        "What belongs to other people",
        "अरूका मालिकी सामग्री",
        ['<p>' + bi({"en": "Some things on these pages stay with their authors. Diagnostic criteria and codes are summarised "
                            "from DSM-5, which is published by the American Psychiatric Association, and the manual's own wording "
                            "belongs to them. Books, films and guidelines are named in the reading lists by title. "
                            "Figures from the national survey, the police and the health ministry, and from the World Health "
                            "Organization and the Global Burden of Disease, belong to whoever published them, and are reproduced "
                            "as numbers with attribution rather than as copied text.",
                     "ne": "यी पृष्ठका केही कुरा आफ्नै मालिकका छन्। निदानका मापदण्ड र कोड DSM-5 बाट सारांश गरिएका हुन्, "
                           "जुन अमेरिकन साइकियाट्रिक एसोसिएसनले प्रकाशन गर्छ, र पुस्तकको आफ्नै भाषा तिनीहरूकै हो। "
                           "पुस्तक, चलचित्र र दिशानिर्देश सन्दर्भ सूचीमा नाममात्र उल्लेख गरिएका छन्। "
                           "राष्ट्रिय सर्वेक्षण, प्रहरी र स्वास्थ्य मन्त्रालय, तथा विश्व स्वास्थ्य संगठन र विश्व भार बोझ अध्ययनबाट आएका अङ्क "
                           "जसले प्रकाशन गरे तिनीहरूका हुन्, र तिनीहरू प्रतिलिपि गरिएका अक्षरमा होइनन्, स्रोत देखाएर अङ्कका रूपमा दिइएका छन्।"}) + '</p>']))
    cards.append(_tcard(
        "How a claim on this site is checked",
        "यस साइटको दावी कसरी जाँचिन्छ",
        ['<p>' + bi({"en": "Our rule is that any figure we publish is checked against two independent sources, and that both are "
                            "named. Two articles repeating the same study count as one source, not two.",
                     "ne": "हाम्रो नियम हो: हामीले प्रकाशन गर्ने हरेक अङ्क दुई स्वतन्त्र स्रोतबाट जाँचिन्छ, र दुवै स्रोतको नाम उल्लेख हुन्छ। "
                           "एउटै अध्ययन दोहोर्‍याउने दुई लेखलाई दुई स्रोत होइनन्, एउटा मात्र हुन्।"}) + '</p>',
         '<p>' + bi({"en": "We are part-way through applying that rule to material published earlier, so we will not claim it is finished. "
                            "Where a page rests on a single source, the page says so instead of implying a second one. "
                            "The working ledger that tracks which figure stands where is in the site source, at "
                            "review/data-ledger.md.",
                     "ne": "हामी पहिले प्रकाशित सामग्रीमा यो नियम लागू गर्ने काम भइरहेको छ, त्यसैले यो पूरा भइसकेको दाबी गर्दैनौं। "
                           "जहाँ पृष्ठ एउटै स्रोतमा आधारित छ, त्यहाँ दोस्रो स्रोत छ जस्तो देखाउनुका साथै पृष्ठले त्यही भन्छ। "
                           "कुन अङ्क कहाँसम्म पुगेको छ भनी टाइ गरिएको कार्यपुस्तिका साइटको स्रोतभित्र, review/data-ledger.md मा छ।"}) + '</p>']))
    cards.append(_tcard(
        "The full credits",
        "पूरा क्रेडिट",
        ['<p>' + bi({"en": "Every contributor, what each of them gave us, and what terms apply to their material is written "
                            "down in one file, with thanks. It travels with the site source, so it can be read and checked "
                            "rather than taken on trust.",
                     "ne": "हरेक योगदानकर्ता, उनले हामीलाई के दिए, र तिनीहरूको सामग्रीमा कुन सर्त लागू हुन्छ, "
                           "यो सबै एउटै फाइलमा लेखिएको छ, धन्यवादसहित। त्यो फाइल साइटको स्रोतसँगै छ, "
                           "त्यसैले यसलाई पढेर जाँच्न सकिन्छ।"}) + '</p>',
         '<p><a href="https://github.com/pravashkarki/mano-atlas/blob/main/CREDITS.md" target="_blank" rel="noopener noreferrer">'
         + bi({"en": "Read the credits and sources", "ne": "क्रेडिट र स्रोतहरू पढ्नुहोस्"})
         + '</a></p>',
         '<p class="fine">' + bi({"en": "Four of the teaching decks carry no author name, so we cannot yet thank those writers by "
                                        "name or ask them what licence they want. We would like to fix that.",
                                        "ne": "चार सिकाउने डेकमा लेखकको नाम छैन, त्यसैले हामीले ती लेखकहरूलाई नामले धन्यवाद दिन अथवा "
                                              "कस्तो इजाजत चाहन्छन् भनी सोध्न असमर्थ छौं। त्यो ठीक गर्न हामी चाहन्छौं।"}) + '</p>']))
    return ('<div class="pagehead"><h1 class="kicker">'
            + bi({"en": "Terms, licence and sources", "ne": "सर्त, इजाजतपत्र र स्रोतहरू"}) + '</h1></div>\n'
            + "".join(cards))


def main() -> None:
    content_dir = ROOT / "content"
    hero = (content_dir / "hero.html").read_text().replace('<!--TOC-->', recent_html() + toc_html())
    if PHASE1_ENGLISH_ONLY:
        hero = hero.replace('<span class="en">English / नेपाली</span>', '<span class="en">English</span>')
    gate_sources()
    write_og_sources()
    # phase fragments: full bilingual shell vs English-first (no switch, no alternate locale)
    lang_boot = LANG_BOOT_PHASE1 if PHASE1_ENGLISH_ONLY else LANG_BOOT_FULL
    langsw_side = "" if PHASE1_ENGLISH_ONLY else LANGSW_SIDE
    langsw_pill = "" if PHASE1_ENGLISH_ONLY else LANGSW_PILL
    og_locale = OG_LOCALE_ENGLISH_ONLY if PHASE1_ENGLISH_ONLY else OG_LOCALE_BILINGUAL
    search_ph = SEARCH_PH_EN if PHASE1_ENGLISH_ONLY else SEARCH_PH_BI
    foot_blurb = FOOT_BLURB_EN if PHASE1_ENGLISH_ONLY else FOOT_BLURB_BI
    idx_langs = ["en"] if PHASE1_ENGLISH_ONLY else ["en", "ne"]
    search_index = []
    page_descs = []
    quiz_dir = ROOT / "quizzes"
    for i, (slug, fname, en, ne, cat, group) in enumerate(PAGES):
        num = NUM[slug]
        body = (content_dir / f"{fname}.html").read_text()
        quiz_file = quiz_dir / f"{fname}.html"
        kp_file = ROOT / "keypoints" / f"{fname}.html"
        if slug != "index" and fname not in NO_QUIZ and not quiz_file.exists():
            raise SystemExit(f"build: {slug}: quizzes/{fname}.html is missing")
        if fname not in NO_KEYPOINTS and not kp_file.exists():
            raise SystemExit(f"build: {slug}: keypoints/{fname}.html is missing")
        updated = git_date(content_dir / f"{fname}.html", quiz_file, kp_file)
        keypoints = kp_file.read_text() if kp_file.exists() else ""
        if quiz_file.exists():
            quiz = keypoints + quiz_file.read_text().rstrip() + "\n"
            if '<div class="resources">' in body:
                k = body.index('<div class="resources">')
                body = body[:k] + quiz + body[k:]
            elif '<div class="footer">' in body:
                k = body.index('<div class="footer">')
                body = body[:k] + quiz + body[k:]
            else:
                body = body.rstrip() + "\n" + quiz
        # give each article card a stable anchor id and index it for search
        counter = {"n": 0}

        def _add_id(m):
            counter["n"] += 1
            return f'<article class="card" id="{slug}-c{counter["n"]}"'

        body = re.sub(r'<article class="card"', _add_id, body)

        parts = re.split(r'(?=<article class="card")', body)
        if PHASE1_ENGLISH_ONLY:
            # English-only pages: Nepali text stays out of the search index
            parts = [strip_ne(p) for p in parts]
            head_html = (strip_ne(hero) if slug == "index" else "") + "\n" + parts[0]
            head_text = plain_text(head_html)
        else:
            head_text = plain_text(parts[0] if slug != "index" else hero + "\n" + parts[0])
        search_index.append({"u": f"{slug}.html", "te": en, "tn": "" if PHASE1_ENGLISH_ONLY else ne, "x": head_text[:3000]})
        for pi, part in enumerate(parts[1:], 1):
            h3 = re.search(r"<h3>([\s\S]*?)</h3>", part)
            te, tn = dual_title(h3.group(1) if h3 else "", (en, ne))
            search_index.append({
                "u": f"{slug}.html#{slug}-c{pi}",
                "te": te, "tn": "" if PHASE1_ENGLISH_ONLY else tn,
                "x": plain_text(part)[:3000],
            })

        # diagnostic code chips: explain themselves on hover/tap-hold
        body = body.replace(
            '<span class="code mono">',
            '<span class="code mono" title="Diagnostic codes: DSM-5 (ICD-9-CM) · ICD-10-CM, as printed in the DSM-5">',
        )
        # inline icon placeholders: <!--ICON:name--> anywhere in a fragment
        body = re.sub(r'<!--ICON:(\w+)-->', lambda m: ICON[m.group(1)], body)
        # resource-type icons (Lucide), picked from the label text
        body = re.sub(
            r'<span class="res-type">(?!<svg)(.*?)</span>',
            lambda m: f'<span class="res-type">{res_type_icon(m.group(1))}{m.group(1)}</span>',
            body,
        )

        body = info_popovers(card_tables(resolve_refs(stamp_badge(body, num, fname), fname)))
        # give each h2/h3 content heading a stable anchor id for the onpage nav
        _hcount = {"n": 0}
        # Each page ships exactly one h1, and the outline is never skipped.
        #
        # The content sources are written as title h2, card heads h3, sub-heads h4,
        # which nests correctly but leaves the whole site without a top-level
        # heading: only the homepage had an h1 (its hero). Rather than edit 33
        # content files and orphan every CSS rule keyed to those tags, shift the
        # whole body up one level at build time: h2->h1, h3->h2, h4->h3. The
        # result is h1 -> h2 -> h3 everywhere, with the relative nesting the
        # sources already had.
        #
        # This runs before _add_hid, so the anchors keep their existing
        # slug-h1, slug-h2, ... numbering and the on-page nav is unchanged.
        # The site's own index is excluded: its hero h1 is injected below, and
        # promoting its toc-group h2s would give the homepage two h1s.
        if slug not in ("index", "hero"):
            def _shift(m):
                return f"<h{int(m.group(1)) - 1}{m.group(2)}>{m.group(3)}</h{int(m.group(1)) - 1}>"
            body = re.sub(r"<h([234])((?:[^>]|\n)*?)>(.*?)</h\1>", _shift, body, flags=re.S)

        def _add_hid(m):
            tag = m.group(1)
            attrs = m.group(2)
            inner = m.group(3)
            if "foot-h" in attrs:
                return m.group(0)
            _hcount["n"] += 1
            return f'<{tag}{attrs} id="{slug}-h{_hcount["n"]}">{inner}</{tag}>'
        body = re.sub(r'<(h[123])((?:[^>]|\n)*?)>(.*?)</\1>', _add_hid, body, flags=re.S)
        if slug == "index":
            content = f'<header class="hero">\n{hero}\n</header>\n<section id="map">\n{body}\n</section>'
        else:
            gentle = ""
            if slug in HEAVY_PAGES and group != "disorders":
                gentle = (f'<p class="gentle">{ICON["sprout"]}<span class="gentle-tx"><span class="en">A gentle note before you read: this chapter carries heavy material. '
                          'Read at your own pace; stopping partway and coming back is allowed.</span>'
                          '<span class="ne">पढ्नुअघि एउटा कोमल कुरा: यो खण्डमा गह्रौं विषय छन्। '
                          'आफ्नै गतिमा पढ्नुहोस्; बीचमै रोकेर पछि फर्कन पाइन्छ।</span></span></p>\n')
            if group == "disorders":
                gentle = (f'<p class="gentle">{ICON["sprout"]}<span class="gentle-tx"><span class="en">A gentle note before you read: symptom lists make '
                          'almost everyone recognise themselves somewhere. That is a normal effect of reading, '
                          'not a diagnosis. If something here sits on your mind, a conversation with a '
                          'professional helps more than re-reading.</span>'
                          '<span class="ne">पढ्नुअघि एउटा कोमल कुरा: लक्षण-सूची पढ्दा झन्डै सबैलाई कतै न कतै आफ्नै झल्को मिल्छ। '
                          'त्यो पढाइको सामान्य असर हो, निदान होइन। कुनै कुरा मनमा अडिरह्यो भने फेरि-फेरि पढ्नुभन्दा '
                          'पेसागत व्यक्तिसँगको कुराकानीले बढी सघाउँछ।</span></span></p>\n')
            # gentle reading-time estimate: English words only (Devanagari mirrors them)
            words = len(re.findall(r"[A-Za-z][A-Za-z'-]+", plain_text(body)))
            mins = max(2, round(words / 170))
            readtime = (f'<span class="readtime">{ICON["clock"]}<span class="en">about {mins} min · no rush</span>'
                        f'<span class="ne">करिब {str(mins).translate(NE_DIGITS)} मिनेट · हतार छैन</span></span>')
            # heavy chapters always get the steadying line; others rotate
            ce, cn = CARELINES[3] if slug in HEAVY_PAGES else CARELINES[i % len(CARELINES)]
            careline = (f'<p class="careline">{ICON["heart"]}<span class="care-tx">'
                        f'<span class="en">{ce}</span><span class="ne">{cn}</span></span>'
                        '<button class="care-x" aria-label="Hide these notes for this visit" title="Hide">&times;</button></p>')
            content = (
                f'<div class="pagehead"><span class="bignum" aria-hidden="true">{num}</span>'
                f'<div class="kicker"><span class="en">Section {num}</span>'
                f'<span class="ne">खण्ड {num.translate(NE_DIGITS)}</span>{readtime}</div></div>\n'
                f'{gentle}<div class="pagetools"></div>\n'
                f'<section id="{fname}" style="margin-top:12px">\n{body}\n</section>\n{careline}'
            )
        title = "Mano Atlas" if slug == "index" else f"{en} · Mano Atlas"
        # on-page contents for chapters with three or more headings
        headings = re.findall(r'<(h[123]) id="([^"]+)"[^>]*>\s*<span class="en">(.*?)</span>', body, re.S)
        if slug != "index" and len(headings) >= 3:
            items = "".join(f'<li><a href="#{hid}"><span class="en">{htext}</span></a></li>' for _tag, hid, htext in headings)
            onpage = (f'<nav class="onpage" aria-label="On this page"><span class="onpage-h"><span class="en">On this page</span>'
                      f'<span class="ne">यस पृष्ठमा</span></span><ol>{items}</ol></nav>\n')
            content = content.replace('<div class="pagetools"></div>', '<div class="pagetools">' + onpage + '</div>', 1)
        secsub = re.search(r'<p class="secsub en">(.*?)</p>', body, re.S)
        page_desc = html_mod.escape(plain_text(secsub.group(1))[:200] if secsub else SITE_DESC)
        page_url = f'{SITE["site_url"]}/' if slug == "index" else f'{SITE["site_url"]}/{slug}'
        group_en, group_ne = GROUPS[group]
        article = {
            "@type": ["Article", "LearningResource"], "@id": page_url + "#article", "url": page_url,
            "headline": title.replace(" · Mano Atlas", ""),
            "description": html_mod.unescape(page_desc), "inLanguage": idx_langs, "isPartOf": {"@id": SITE["site_url"] + "/#site"},
            "about": "Mental health education; DSM-5; psychosocial counselling; Nepal", "educationalLevel": "Diploma (CTEVT Psychosocial Counselor)",
            "learningResourceType": "reading", "audience": {"@type": "EducationalAudience", "educationalRole": "student"},
            "dateModified": updated, "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/", "isAccessibleForFree": True,
            "author": {"@type": "Person", "name": "Pravash Karki"},
        }
        if not PHASE1_ENGLISH_ONLY:
            article["alternativeHeadline"] = ne
        jsonld = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "WebSite", "@id": SITE["site_url"] + "/#site", "url": SITE["site_url"] + "/", "name": "Mano Atlas", "alternateName": "मनो एट्लास",
                 "description": SITE_DESC, "inLanguage": idx_langs, "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
                 "publisher": {"@type": "Person", "name": "Pravash Karki"}},
                article,
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Mano Atlas", "item": SITE["site_url"] + "/"},
                    {"@type": "ListItem", "position": 2, "name": group_en},
                    {"@type": "ListItem", "position": 3, "name": en, "item": page_url}]}
            ]}, ensure_ascii=False)
        page_descs.append((slug, en, ne, html_mod.unescape(page_desc), group_en))
        html = SHELL.format(title=title, nav=nav_html(slug), content=content, pager=pager_html(i), page_desc=page_desc, page_url=page_url, jsonld=jsonld,
                            updated_en=updated, updated_ne=updated.translate(NE_DIGITS), og_slug=slug, og_alt=html_mod.escape(f"{en}" if PHASE1_ENGLISH_ONLY else (f"{en} · {ne}" if slug != "index" else "Mano Atlas · मनो एट्लास")), icon_search=ICON["search"], icon_menu=ICON["menu"], icon_panel=ICON["panel"], icon_phone=ICON["phone"], icon_mail=ICON["mail"],
                            lang_boot=lang_boot, og_locale=og_locale, langsw_side=langsw_side, langsw_pill=langsw_pill, search_ph=search_ph, foot_blurb=foot_blurb, **SITE)
        if PHASE1_ENGLISH_ONLY:
            html = strip_ne(html)
        (ROOT / f"{slug}.html").write_text(html)
        print("built", f"{slug}.html")

    idx_js = "window.MANO_INDEX=" + json.dumps(search_index, ensure_ascii=False, separators=(",", ":")) + ";"
    (ROOT / "assets" / "search-index.js").write_text(idx_js)
    # sitemap, robots, 404
    urls = "".join(f'  <url><loc>{SITE["site_url"]}/{"" if s == "index" else s}</loc></url>\n' for s, *_ in PAGES)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f'User-agent: *\nAllow: /\nDisallow: /vault\nSitemap: {SITE["site_url"]}/sitemap.xml\n')
    nf = ('<div class="pagehead"><span class="bignum" aria-hidden="true">404</span><div class="kicker"><span class="en">Page not found</span><span class="ne">पृष्ठ भेटिएन</span></div></div>\n'
          '<h1><span class="en">That page is not here</span><span class="ne">त्यो पृष्ठ यहाँ छैन</span></h1>\n'
          '<p class="secsub en">The address may be old or mistyped. Use the search, pick a chapter from the list, or start from the home page.</p>\n'
          '<p class="secsub ne">ठेगाना पुरानो वा गलत टाइप भएको हुन सक्छ। खोज प्रयोग गर्नुहोस्, सूचीबाट अध्याय रोज्नुहोस्, वा गृहपृष्ठबाट सुरु गर्नुहोस्।</p>\n'
          '<p><a href="index.html"><span class="en">Go to the home page</span><span class="ne">गृहपृष्ठमा जानुहोस्</span></a></p>\n')
    # llms.txt: a plain-text map for language models and other crawlers that read it
    by_grp = {}
    for s, e, n_, d, g in page_descs:
        title = e if PHASE1_ENGLISH_ONLY else f"{e} · {n_}"
        by_grp.setdefault(g, []).append(f"- [{title}]({SITE['site_url']}/{'' if s == 'index' else s}): {d}")
    lang_line = ("The site is currently English-only while the Nepali text is under review." if PHASE1_ENGLISH_ONLY
                 else "Every page carries the same text in English and Nepali.")
    llms = ("# Mano Atlas (मनो एट्लास)\n\n> " + SITE_DESC + " Written for CTEVT Psychosocial Counselor students, community health workers and families in Nepal. "
            + lang_line + " Content is licensed CC BY-NC-SA 4.0. It is an educational resource, not a diagnostic tool; diagnosis belongs to qualified clinicians.\n\n"
            "Helplines inside Nepal: National Suicide Prevention Helpline 1166 (Mental Hospital, Lagankhel); TUTH mental-health hotline 1660 012 1600; women's helpline 1145 (NWC Khabar Garaun); emergency 112 / 100.\n\n"
            "Sources: DSM-5 (APA, 2013), CTEVT PSC Curriculum (2010), Sub-module 1 & 2 and Mental Health-3 class notes, WHO fact sheets and mhGAP, IASC MHPSS guidelines, Nepal MoHP policy documents.\n\n")
    for g, lines in by_grp.items():
        llms += f"## {g}\n\n" + "\n".join(lines) + "\n\n"
    llms += "## Optional\n\n- [Sitemap](" + SITE["site_url"] + "/sitemap.xml)\n- [Source repository](https://github.com/pravashkarki/mano-atlas)\n"
    (ROOT / "llms.txt").write_text(llms)
    html404 = SHELL.format(title="Page not found · Mano Atlas", nav=nav_html("index"), content=nf, pager="", page_desc=SITE_DESC, page_url=SITE["site_url"] + "/404", jsonld="{}",
                           updated_en=SITE["reviewed_en"], updated_ne=SITE["reviewed_ne"], og_slug="index", og_alt="Mano Atlas" if PHASE1_ENGLISH_ONLY else "Mano Atlas · मनो एट्लास", icon_search=ICON["search"], icon_menu=ICON["menu"], icon_panel=ICON["panel"], icon_phone=ICON["phone"], icon_mail=ICON["mail"],
                           lang_boot=lang_boot, og_locale=og_locale, langsw_side=langsw_side, langsw_pill=langsw_pill, search_ph=search_ph, foot_blurb=foot_blurb, **SITE)
    if PHASE1_ENGLISH_ONLY:
        html404 = strip_ne(html404)
    (ROOT / "404.html").write_text(html404)

    # student vault: student-only, so it stays out of the sitemap (built above) and
    # out of robots indexing, and it is not in PAGES so it has no number or nav row
    vtitle = "Student vault" if PHASE1_ENGLISH_ONLY else "Student vault · विद्यार्थी ताला"
    vdesc = ("Class files for PCS students, each one tagged: curriculum decks, practice sheets, reference, extra. "
             "Enter the course password to open the list.")
    vjsonld = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": SITE["site_url"] + "/vault#webpage", "url": SITE["site_url"] + "/vault",
             "name": vtitle, "description": vdesc, "inLanguage": idx_langs,
             "isPartOf": {"@id": SITE["site_url"] + "/#site"},
             "audience": {"@type": "EducationalAudience", "educationalRole": "student"},
             "author": {"@type": "Person", "name": "Pravash Karki"}},
        ]}, ensure_ascii=False)
    # no active chapter: the vault is not in the sidebar, so nothing should read as "you are here"
    htmlv = SHELL.format(title=f"{vtitle} · Mano Atlas", nav=nav_html(""), content=vault_html(), pager="",
                         page_desc=vdesc, page_url=SITE["site_url"] + "/vault", jsonld=vjsonld,
                         updated_en=SITE["reviewed_en"], updated_ne=SITE["reviewed_ne"], og_slug="index",
                         og_alt="Mano Atlas", icon_search=ICON["search"], icon_menu=ICON["menu"], icon_panel=ICON["panel"], icon_phone=ICON["phone"], icon_mail=ICON["mail"],
                         lang_boot=lang_boot, og_locale=og_locale, langsw_side=langsw_side, langsw_pill=langsw_pill, search_ph=search_ph, foot_blurb=foot_blurb, **SITE)
    if PHASE1_ENGLISH_ONLY:
        htmlv = strip_ne(htmlv)
    (ROOT / "vault.html").write_text(htmlv)
    print("built vault.html")

    # terms, licence and safeguarding: linked from the footer on every page, because a
    # licence the reader cannot reach is not a licence. Standalone like /vault, so it is
    # not in PAGES: no chapter number, no sidebar row, no sitemap entry.
    ttitle = "Terms, licence and sources" if PHASE1_ENGLISH_ONLY else "सर्त, इजाजतपत्र र स्रोतहरू"
    tdesc = ("What Mano Atlas is and is not, how to report an error, the content and code licences, "
             "and what belongs to other people.")
    tjsonld = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": SITE["site_url"] + "/terms#webpage", "url": SITE["site_url"] + "/terms",
             "name": ttitle, "description": tdesc, "inLanguage": idx_langs,
             "isPartOf": {"@id": SITE["site_url"] + "/#site"},
             "about": {"@type": "Thing", "name": "Terms, licence and sources"},
             "author": {"@type": "Person", "name": "Pravash Karki"}},
        ]}, ensure_ascii=False)
    # not in the sidebar, so nothing should read as "you are here"
    htmlt = SHELL.format(title=f"{ttitle} · Mano Atlas", nav=nav_html(""), content=terms_html(), pager="",
                         page_desc=tdesc, page_url=SITE["site_url"] + "/terms", jsonld=tjsonld,
                         updated_en=SITE["reviewed_en"], updated_ne=SITE["reviewed_ne"], og_slug="index",
                         og_alt="Mano Atlas", icon_search=ICON["search"], icon_menu=ICON["menu"], icon_panel=ICON["panel"], icon_phone=ICON["phone"], icon_mail=ICON["mail"],
                         lang_boot=lang_boot, og_locale=og_locale, langsw_side=langsw_side, langsw_pill=langsw_pill, search_ph=search_ph, foot_blurb=foot_blurb, **SITE)
    if PHASE1_ENGLISH_ONLY:
        htmlt = strip_ne(htmlt)
    (ROOT / "terms.html").write_text(htmlt)
    print("built terms.html")
    print(f"search index: {len(search_index)} entries, {len(idx_js)//1024} KB")


if __name__ == "__main__":
    main()
