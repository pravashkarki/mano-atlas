#!/usr/bin/env python3
"""Build the Mano Atlas static pages.

Each page = shared shell (sidebar nav + lang switcher) + content/<slug>.html.
Add a page: drop a file in content/, add one entry to PAGES, run: python3 build.py
"""
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
}

# slug, content file, num, en title, ne title, catvar (sidebar colour mark), group
PAGES = [
    ("index",      "map",        "01", "Home & the DSM-5 map",      "गृहपृष्ठ र DSM-5 नक्सा",        None,       "overview"),
    ("roots",      "roots",      "02", "Roots: philosophy to psychology", "जरा: दर्शनदेखि मनोविज्ञान", None,     "overview"),
    ("foundation", "foundation", "03", "Fear: the foundation",      "डर: आधारशिला",                  None,       "overview"),
    ("basics",     "basics",     "04", "Mental health basics",      "मानसिक स्वास्थ्यका आधार",       None,       "overview"),
    ("development","development","05", "Human development",         "मानव विकास",                    None,       "overview"),
    ("anxiety",    "anxiety",    "06", "Anxiety disorders",         "चिन्ता विकारहरू",               "--c-anx",  "disorders"),
    ("ocd",        "ocd",        "07", "OCD & related",             "ओसीडी र सम्बन्धित",             "--c-ocd",  "disorders"),
    ("depression", "depression", "08", "Depressive disorders",      "उदासी (डिप्रेसन)",              "--c-dep",  "disorders"),
    ("trauma",     "trauma",     "09", "Trauma & stressor",         "आघात र तनाव",                   "--c-tra",  "disorders"),
    ("somatic",    "somatic",    "10", "Conversion & somatic",      "कन्भर्सन र शारीरिक",            "--c-som",  "disorders"),
    ("psychosis",  "psychosis",  "11", "Psychosis",                 "मनोविकृति (साइकोसिस)",          "--c-psy",  "disorders"),
    ("child",      "child",      "12", "Child mental illness",      "बाल मानसिक समस्या",             "--c-chi",  "disorders"),
    ("eating",     "eating",     "13", "Eating disorders",          "खानपान विकार",                  "--c-eat",  "disorders"),
    ("sleep",      "sleep",      "14", "Sleep-wake disorders",      "निद्रा विकार",                  "--c-slp",  "disorders"),
    ("substance",  "substance",  "15", "Substance use",             "लागुपदार्थ प्रयोग",             "--c-sub",  "disorders"),
    ("wellbeing",  "wellbeing",  "16", "Wellbeing & intervention",  "तन्दुरुस्ती र हस्तक्षेप",       None,       "practice"),
    ("approaches", "approaches", "17", "Approaches & forms",        "विधि र रूपहरू",                 None,       "practice"),
    ("skills",     "skills",     "18", "Communication skills",      "संवाद-सीप",                     None,       "practice"),
    ("process",    "process",    "19", "The counselling process",   "परामर्श-प्रक्रिया",             None,       "practice"),
    ("tools",      "tools",      "20", "Tools & techniques",        "औजार र प्रविधि",                None,       "practice"),
    ("suicide",    "suicide",    "21", "Suicide: assessment",       "आत्महत्या: मूल्याङ्कन",         None,       "practice"),
    ("pfa",        "pfa",        "22", "PFA & emergencies",         "पीएफए र आपतकाल",                None,       "practice"),
    ("gbv",        "gbv",        "23", "Gender & GBV",              "लैङ्गिकता र जीबीभी",            None,       "practice"),
    ("hiv",        "hiv",        "24", "HIV & AIDS counselling",    "एचआईभी परामर्श",                None,       "practice"),
    ("casemgmt",   "casemgmt",   "25", "Case management",           "केस व्यवस्थापन",                None,       "practice"),
    ("ethics",     "ethics",     "26", "Ethics & self-care",        "नैतिकता र आत्म-हेरचाह",         None,       "practice"),
    ("more",       "rest",       "27", "The rest of the map",       "बाँकी नक्सा",                   None,       "reference"),
    ("nepal",      "nepal",      "28", "Culture & the Nepal panorama", "संस्कृति र नेपाली परिदृश्य", None,       "reference"),
    ("crosswalk",  "crosswalk",  "29", "For PSC students",          "पीएससी विद्यार्थीलाई",          None,       "reference"),
]

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


NE_DIGITS = str.maketrans("0123456789", "०१२३४५६७८९")

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
    active_group = next((g for s, _f, _n, _e, _ne, _c, g in PAGES if s == active_slug), None)
    by_group = {}
    for slug, _f, num, en, ne, cat, group in PAGES:
        by_group.setdefault(group, []).append((slug, num, en, ne, cat))
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
        s, _f, num, en, ne, *_ = PAGES[i - 1]
        href = "index.html" if s == "index" else f"{s}.html"
        parts.append(
            f'<a class="prev" href="{href}"><span class="lbl">{ICON["left"]}<span class="en">Previous · {num}</span>'
            f'<span class="ne">अघिल्लो · {num}</span></span><span class="en">{en}</span><span class="ne">{ne}</span></a>'
        )
    if i < len(PAGES) - 1:
        s, _f, num, en, ne, *_ = PAGES[i + 1]
        parts.append(
            f'<a class="next" href="{s}.html"><span class="lbl"><span class="en">Next · {num}</span>'
            f'<span class="ne">अर्को · {num}</span>{ICON["right"]}</span><span class="en">{en}</span><span class="ne">{ne}</span></a>'
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


def toc_html() -> str:
    out = []
    for slug, _f, num, en, ne, cat, group in PAGES:
        if slug == "index":
            continue
        mark = f'<span class="catmark" style="background:var({cat})"></span>' if cat else ""
        out.append(f'<a href="{slug}.html">{mark}<span class="secnum">{num}</span>'
                   f'<span class="en">{en}</span><span class="ne">{ne}</span></a>')
    return '<nav class="toc" aria-label="Contents">\n    ' + "\n    ".join(out) + '\n  </nav>'


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Mano Atlas (मनो एट्लास): a free, bilingual (English/नेपाली) atlas of mental disorders: DSM-5 criteria, teaching diagrams, and the Nepali context.">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;1,7..72,400&family=Mukta:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Caveat:wght@600&display=swap">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main"><span class="en">Skip to content</span><span class="ne">सामग्रीमा जानुहोस्</span></a>
<div class="layout">
  <aside class="sidebar">
    <div class="top">
      <a class="brand" href="index.html"><span class="en">Mano Atlas</span><span class="ne">मनो एट्लास</span>
        <span class="sub"><span class="en">Mental health · two languages</span><span class="ne">मानसिक स्वास्थ्य · दुई भाषा</span></span></a>
      <div class="ctrls">
        <div class="langsw" role="group" aria-label="Language">
          <button id="btn-en" onclick="setLang('en')">EN</button>
          <button id="btn-ne" onclick="setLang('ne')">ने</button>
        </div>
        <button id="btn-theme" class="themesw" onclick="cycleTheme()" aria-label="Colour theme">◐ Auto</button>
      </div>
    </div>
    <div class="search"><span class="s-ico">{icon_search}</span>
      <input id="q" type="search" autocomplete="off" spellcheck="false"
        placeholder="Search · खोज्नुहोस्" aria-label="Search the atlas">
      <div id="qres" class="qres" hidden></div>
    </div>
    <nav class="snav" aria-label="Site">
      {nav}
    </nav>
    <div class="side-foot"><span id="progress"></span></div>
  </aside>
  <main id="main">
    <div class="wrap">
{content}
    <nav class="pager" aria-label="Chapter">
    {pager}
    </nav>
    <footer class="sitefoot">
      <div class="cols">
        <div>
          <h4><span class="en">Mano Atlas</span><span class="ne">मनो एट्लास</span></h4>
          <p class="en">A free, open atlas of mental health in English and नेपाली. Educational resource, not a diagnostic tool: criteria are paraphrased from DSM-5 (2013). Diagnosis belongs to qualified clinicians.</p>
          <p class="ne">अंग्रेजी र नेपालीमा मानसिक स्वास्थ्यको निःशुल्क, खुला एट्लास। शैक्षिक सामग्री हो, निदान-उपकरण होइन: मापदण्ड DSM-5 (2013) बाट सरलीकृत छन्। निदान योग्य चिकित्सकको काम हो।</p>
          <p class="en">Learning sticks best in small sittings. It is fine to close this tab and come back another day.</p>\n          <p class="ne">सिकाइ साना-साना बसाइमा राम्रो टिक्छ। ट्याब बन्द गरेर अर्को दिन फर्किए हुन्छ।</p>\n          <p><span class="en">Last reviewed: {reviewed_en}</span><span class="ne">पछिल्लो समीक्षा: {reviewed_ne}</span></p>
        </div>
        <div class="crisis-col">
          <h4>{icon_phone} <span class="en">If you need help now · Nepal</span><span class="ne">अहिले नै सहयोग चाहिए · नेपाल</span></h4>
          <p><strong>{helpline_suicide}</strong> <span class="en">National Suicide Prevention Helpline</span><span class="ne">राष्ट्रिय आत्महत्या रोकथाम हेल्पलाइन</span></p>
          <p><strong>{helpline_tuth}</strong> <span class="en">TUTH mental-health hotline</span><span class="ne">टिचिङ अस्पताल हटलाइन</span></p>
          <p><strong>{helpline_women}</strong> <span class="en">Women's helpline</span><span class="ne">महिला हेल्पलाइन</span> · <strong>{helpline_emergency}</strong> <span class="en">emergency</span><span class="ne">आपतकाल</span></p>
          <p class="outside"><span class="en">These numbers work inside Nepal. Elsewhere, <a href="https://findahelpline.com" target="_blank" rel="noopener">findahelpline.com</a> lists your country's lines.</span><span class="ne">यी नम्बर नेपालभित्र चल्छन्। अन्यत्र हुनुहुन्छ भने <a href="https://findahelpline.com" target="_blank" rel="noopener">findahelpline.com</a> मा आफ्नो देशका नम्बर भेटिन्छन्।</span></p>
        </div>
        <div>
          <h4><span class="en">Open &amp; improvable</span><span class="ne">खुला र सुधारयोग्य</span></h4>
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
<script src="assets/lang.js"></script>
<script src="assets/search-index.js" defer></script>
<script src="assets/search.js" defer></script>
</body>
</html>
"""


def main() -> None:
    content_dir = ROOT / "content"
    hero = (content_dir / "hero.html").read_text().replace('<!--TOC-->', toc_html())
    search_index = []
    quiz_dir = ROOT / "quizzes"
    for i, (slug, fname, num, en, ne, cat, group) in enumerate(PAGES):
        body = (content_dir / f"{fname}.html").read_text()
        quiz_file = quiz_dir / f"{fname}.html"
        if quiz_file.exists():
            quiz = quiz_file.read_text().rstrip() + "\n"
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

        # inline icon placeholders: <!--ICON:name--> anywhere in a fragment
        body = re.sub(r'<!--ICON:(\w+)-->', lambda m: ICON[m.group(1)], body)
        # resource-type icons (Lucide), picked from the label text
        body = re.sub(
            r'<span class="res-type">(?!<svg)(.*?)</span>',
            lambda m: f'<span class="res-type">{res_type_icon(m.group(1))}{m.group(1)}</span>',
            body,
        )

        if slug == "index":
            content = f'<header class="hero">\n{hero}\n</header>\n<section id="map">\n{body}\n</section>'
        else:
            gentle = ""
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
            ce, cn = CARELINES[i % len(CARELINES)]
            careline = (f'<p class="careline">{ICON["heart"]}<span class="care-tx">'
                        f'<span class="en">{ce}</span><span class="ne">{cn}</span></span>'
                        '<button class="care-x" aria-label="Hide these notes for this visit" title="Hide">&times;</button></p>')
            content = (
                f'<div class="pagehead"><div class="kicker"><span class="en">Section {num}</span>'
                f'<span class="ne">खण्ड {num}</span>{readtime}</div></div>\n'
                f'<nav class="pager pager-top" aria-label="Chapter (top)">\n{pager_html(i)}\n</nav>\n{gentle}'
                f'<section id="{fname}" style="margin-top:12px">\n{body}\n</section>\n{careline}'
            )
        title = "Mano Atlas" if slug == "index" else f"{en} · Mano Atlas"
        html = SHELL.format(title=title, nav=nav_html(slug), content=content, pager=pager_html(i),
                            icon_search=ICON["search"], icon_phone=ICON["phone"], icon_mail=ICON["mail"], **SITE)
        (ROOT / f"{slug}.html").write_text(html)
        print("built", f"{slug}.html")

    idx_js = "window.MANO_INDEX=" + json.dumps(search_index, ensure_ascii=False, separators=(",", ":")) + ";"
    (ROOT / "assets" / "search-index.js").write_text(idx_js)
    print(f"search index: {len(search_index)} entries, {len(idx_js)//1024} KB")


if __name__ == "__main__":
    main()
