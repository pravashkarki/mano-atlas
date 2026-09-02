#!/usr/bin/env python3
"""Build the Mano Atlas static pages.

Each page = shared shell (sidebar nav + lang switcher) + content/<slug>.html.
Add a page: drop a file in content/, add one entry to PAGES, run: python3 build.py
"""
import html as html_mod
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent

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
    "site_url": "https://pcs.pravashkarki.com",
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


SITE_DESC = "Mano Atlas (मनो एट्लास): a free, bilingual (English/नेपाली) atlas of mental disorders: DSM-5 criteria, teaching diagrams, and the Nepali context."
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
        num = NUM[slug]
        if word in ("पृष्ठ", "खण्ड", "न"):
            num = num.translate(NE_DIGITS)
        if word in ("n", "न"):
            return num
        return f'<a href="{slug}.html">{word} {num}</a>'
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
<script>(function(){{var d=document.documentElement;try{{var l=localStorage.getItem('psc-lang');d.setAttribute('data-lang',l==='ne'?'ne':'en');d.lang=l==='ne'?'ne':'en';var t=localStorage.getItem('psc-theme');if(t==='light'||t==='dark')d.setAttribute('data-theme',t);if(localStorage.getItem('psc-nav-collapsed'))d.classList.add('nav-collapsed-init');}}catch(e){{d.setAttribute('data-lang','en');}}}})();</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Mano Atlas (मनो एट्लास): a free, bilingual (English/नेपाली) atlas of mental disorders: DSM-5 criteria, teaching diagrams, and the Nepali context.">
<title>{title}</title>
<link rel="canonical" href="{page_url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Mano Atlas · मनो एट्लास">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{page_desc}">
<meta property="og:url" content="{page_url}">
<meta property="og:locale" content="en_GB">
<meta property="og:locale:alternate" content="ne_NP">
<meta name="twitter:card" content="summary">
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
        <div class="langsw" role="group" aria-label="Language">
          <button id="btn-en" class="btn-en" onclick="setLang('en')">EN</button>
          <button id="btn-ne" class="btn-ne" onclick="setLang('ne')">ने</button>
        </div>
        <button id="btn-theme" class="themesw btn-theme" onclick="cycleTheme()" title="Colour theme">◐ Auto</button>
      </div>
    </div>
    <div class="search" id="searchbox"><span class="s-ico">{icon_search}</span>
      <input id="q" type="search" autocomplete="off" spellcheck="false"
        placeholder="Search · खोज्नुहोस्" aria-label="Search the atlas">
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
        <div class="langsw" role="group" aria-label="Language">
          <button class="btn-en" onclick="setLang('en')">EN</button>
          <button class="btn-ne" onclick="setLang('ne')">ने</button>
        </div>
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
          <p class="en">A free, open atlas of mental health in English and नेपाली. Educational resource, not a diagnostic tool: criteria are paraphrased from DSM-5 (2013). Diagnosis belongs to qualified clinicians.</p>
          <p class="ne">अंग्रेजी र नेपालीमा मानसिक स्वास्थ्यको निःशुल्क, खुला एट्लास। शैक्षिक सामग्री हो, निदान-उपकरण होइन: मापदण्ड DSM-5 (2013) बाट सरलीकृत छन्। निदान योग्य चिकित्सकको काम हो।</p>
          <p class="en">Learning sticks best in small sittings. It is fine to close this tab and come back another day.</p>\n          <p class="ne">सिकाइ साना-साना बसाइमा राम्रो टिक्छ। ट्याब बन्द गरेर अर्को दिन फर्किए हुन्छ।</p>\n          <p><span class="en">Last reviewed: {reviewed_en} · This page updated {updated_en}</span><span class="ne">पछिल्लो समीक्षा: {reviewed_ne} · यो पृष्ठ अद्यावधिक {updated_ne}</span></p>
        </div>
        <div class="crisis-col">
          <h3 class="foot-h">{icon_phone} <span class="en">If you need help now · Nepal</span><span class="ne">अहिले नै सहयोग चाहिए · नेपाल</span></h3>
          <p><strong><a href="tel:1166">{helpline_suicide}</a></strong> <span class="en">National Suicide Prevention Helpline</span><span class="ne">राष्ट्रिय आत्महत्या रोकथाम हेल्पलाइन</span></p>
          <p><strong><a href="tel:16600121600">{helpline_tuth}</a></strong> <span class="en">TUTH mental-health hotline</span><span class="ne">टिचिङ अस्पताल हटलाइन</span></p>
          <p><strong><a href="tel:1145">{helpline_women}</a></strong> <span class="en">Women's helpline</span><span class="ne">महिला हेल्पलाइन</span> · <strong><a href="tel:112">112</a> / <a href="tel:100">100</a></strong> <span class="en">emergency</span><span class="ne">आपतकाल</span></p>
          <p class="outside"><span class="en">These numbers work inside Nepal. Elsewhere, <a href="https://findahelpline.com" target="_blank" rel="noopener">findahelpline.com</a> lists your country's lines.</span><span class="ne">यी नम्बर नेपालभित्र चल्छन्। अन्यत्र हुनुहुन्छ भने <a href="https://findahelpline.com" target="_blank" rel="noopener">findahelpline.com</a> मा आफ्नो देशका नम्बर भेटिन्छन्।</span></p>
        </div>
        <div>
          <h3 class="foot-h"><span class="en">Open &amp; improvable</span><span class="ne">खुला र सुधारयोग्य</span></h3>
          <p class="en">Content licensed <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license noopener" target="_blank">CC BY-NC-SA 4.0</a>: share and adapt with credit, non-commercially.</p>
          <p class="ne">सामग्री <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license noopener" target="_blank">CC BY-NC-SA 4.0</a> अन्तर्गत: श्रेयसहित, गैर-व्यावसायिक रूपमा बाँड्न र मिलाउन पाइन्छ।</p>
          <p>{icon_mail} <span class="en">Spotted an error?</span><span class="ne">त्रुटि भेट्नुभयो?</span> <span class="mailrev" data-u="{email_user}" data-d="{email_domain}" data-t="{email_tld}">{email_user} [at] {email_domain} [dot] {email_tld}</span></p>
        </div>
      </div>
      <p class="fine"><span class="en">Built from the CTEVT Psychosocial Counselor curriculum, class notes, and the sources named on each page.</span><span class="ne">सीटीईभीटी मनोसामाजिक परामर्शकर्ता पाठ्यक्रम, कक्षा-नोट र प्रत्येक पृष्ठमा उल्लिखित स्रोतबाट निर्मित।</span></p>
    </footer>
    </div>
  </main>
</div>
<script src="assets/lang.js" defer></script>
<script src="assets/search.js" defer></script>
</body>
</html>
"""


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


def main() -> None:
    content_dir = ROOT / "content"
    hero = (content_dir / "hero.html").read_text().replace('<!--TOC-->', recent_html() + toc_html())
    gate_sources()
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
        head_text = plain_text(parts[0] if slug != "index" else hero + "\n" + parts[0])
        search_index.append({"u": f"{slug}.html", "te": en, "tn": ne, "x": head_text[:3000]})
        for pi, part in enumerate(parts[1:], 1):
            h3 = re.search(r"<h3>([\s\S]*?)</h3>", part)
            te, tn = dual_title(h3.group(1) if h3 else "", (en, ne))
            search_index.append({
                "u": f"{slug}.html#{slug}-c{pi}",
                "te": te, "tn": tn,
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
                          'not a diagnosis. If something here stays on your mind, a conversation with a '
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
        # on-page contents for chapters with three or more cards
        cards = re.findall(r'<article class="card" id="([^"]+)"[^>]*>\s*<div class="card-head">\s*<h3><span class="en">(.*?)</span><span class="ne">(.*?)</span>', body, re.S)
        if slug != "index" and len(cards) >= 3:
            items = "".join(f'<li><a href="#{cid}"><span class="en">{te}</span><span class="ne">{tn}</span></a></li>' for cid, te, tn in cards)
            onpage = (f'<nav class="onpage" aria-label="On this page"><span class="onpage-h"><span class="en">On this page</span>'
                      f'<span class="ne">यस पृष्ठमा</span></span><ol>{items}</ol></nav>\n')
            content = content.replace('<div class="pagetools"></div>', '<div class="pagetools">' + onpage + '</div>', 1)
        secsub = re.search(r'<p class="secsub en">(.*?)</p>', body, re.S)
        page_desc = html_mod.escape(plain_text(secsub.group(1))[:200] if secsub else SITE_DESC)
        page_url = f'{SITE["site_url"]}/' if slug == "index" else f'{SITE["site_url"]}/{slug}'
        group_en, group_ne = GROUPS[group]
        jsonld = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "WebSite", "@id": SITE["site_url"] + "/#site", "url": SITE["site_url"] + "/", "name": "Mano Atlas", "alternateName": "मनो एट्लास",
                 "description": SITE_DESC, "inLanguage": ["en", "ne"], "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
                 "publisher": {"@type": "Person", "name": "Pravash Karki"}},
                {"@type": ["Article", "LearningResource"], "@id": page_url + "#article", "url": page_url, "headline": title.replace(" · Mano Atlas", ""),
                 "alternativeHeadline": ne, "description": html_mod.unescape(page_desc), "inLanguage": ["en", "ne"], "isPartOf": {"@id": SITE["site_url"] + "/#site"},
                 "about": "Mental health education; DSM-5; psychosocial counselling; Nepal", "educationalLevel": "Diploma (CTEVT Psychosocial Counselor)",
                 "learningResourceType": "reading", "audience": {"@type": "EducationalAudience", "educationalRole": "student"},
                 "dateModified": updated, "license": "https://creativecommons.org/licenses/by-nc-sa/4.0/", "isAccessibleForFree": True,
                 "author": {"@type": "Person", "name": "Pravash Karki"}},
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Mano Atlas", "item": SITE["site_url"] + "/"},
                    {"@type": "ListItem", "position": 2, "name": group_en},
                    {"@type": "ListItem", "position": 3, "name": en, "item": page_url}]}
            ]}, ensure_ascii=False)
        page_descs.append((slug, en, ne, html_mod.unescape(page_desc), group_en))
        html = SHELL.format(title=title, nav=nav_html(slug), content=content, pager=pager_html(i), page_desc=page_desc, page_url=page_url, jsonld=jsonld,
                            updated_en=updated, updated_ne=updated.translate(NE_DIGITS), icon_search=ICON["search"], icon_menu=ICON["menu"], icon_panel=ICON["panel"], icon_phone=ICON["phone"], icon_mail=ICON["mail"], **SITE)
        (ROOT / f"{slug}.html").write_text(html)
        print("built", f"{slug}.html")

    idx_js = "window.MANO_INDEX=" + json.dumps(search_index, ensure_ascii=False, separators=(",", ":")) + ";"
    (ROOT / "assets" / "search-index.js").write_text(idx_js)
    # sitemap, robots, 404
    urls = "".join(f'  <url><loc>{SITE["site_url"]}/{"" if s == "index" else s}</loc></url>\n' for s, *_ in PAGES)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE["site_url"]}/sitemap.xml\n')
    nf = ('<div class="pagehead"><span class="bignum" aria-hidden="true">404</span><div class="kicker"><span class="en">Page not found</span><span class="ne">पृष्ठ भेटिएन</span></div></div>\n'
          '<h2><span class="en">That page is not here</span><span class="ne">त्यो पृष्ठ यहाँ छैन</span></h2>\n'
          '<p class="secsub en">The address may be old or mistyped. Use the search, pick a chapter from the list, or start from the home page.</p>\n'
          '<p class="secsub ne">ठेगाना पुरानो वा गलत टाइप भएको हुन सक्छ। खोज प्रयोग गर्नुहोस्, सूचीबाट अध्याय रोज्नुहोस्, वा गृहपृष्ठबाट सुरु गर्नुहोस्।</p>\n'
          '<p><a href="index.html"><span class="en">Go to the home page</span><span class="ne">गृहपृष्ठमा जानुहोस्</span></a></p>\n')
    # llms.txt: a plain-text map for language models and other crawlers that read it
    by_grp = {}
    for s, e, n_, d, g in page_descs:
        by_grp.setdefault(g, []).append(f"- [{e} · {n_}]({SITE['site_url']}/{'' if s == 'index' else s}): {d}")
    llms = ("# Mano Atlas (मनो एट्लास)\n\n> " + SITE_DESC + " Written for CTEVT Psychosocial Counselor students, community health workers and families in Nepal. "
            "Every page carries the same text in English and Nepali. Content is licensed CC BY-NC-SA 4.0. It is an educational resource, not a diagnostic tool; diagnosis belongs to qualified clinicians.\n\n"
            "Helplines inside Nepal: National Suicide Prevention Helpline 1166 (Mental Hospital, Lagankhel); TUTH mental-health hotline 1660 012 1600; women's helpline 1145 (NWC Khabar Garaun); emergency 112 / 100.\n\n"
            "Sources: DSM-5 (APA, 2013), CTEVT PSC Curriculum (2010), Sub-module 1 & 2 and Mental Health-3 class notes, WHO fact sheets and mhGAP, IASC MHPSS guidelines, Nepal MoHP policy documents.\n\n")
    for g, lines in by_grp.items():
        llms += f"## {g}\n\n" + "\n".join(lines) + "\n\n"
    llms += "## Optional\n\n- [Sitemap](" + SITE["site_url"] + "/sitemap.xml)\n- [Source repository](https://github.com/pravashkarki/mano-atlas)\n"
    (ROOT / "llms.txt").write_text(llms)
    html404 = SHELL.format(title="Page not found · Mano Atlas", nav=nav_html("index"), content=nf, pager="", page_desc=SITE_DESC, page_url=SITE["site_url"] + "/404", jsonld="{}",
                           updated_en=SITE["reviewed_en"], updated_ne=SITE["reviewed_ne"], icon_search=ICON["search"], icon_menu=ICON["menu"], icon_panel=ICON["panel"], icon_phone=ICON["phone"], icon_mail=ICON["mail"], **SITE)
    (ROOT / "404.html").write_text(html404)
    print(f"search index: {len(search_index)} entries, {len(idx_js)//1024} KB")


if __name__ == "__main__":
    main()
