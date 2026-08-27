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


def nav_html(active_slug: str) -> str:
    out = []
    current_group = None
    for slug, _f, num, en, ne, cat, group in PAGES:
        if group != current_group:
            g_en, g_ne = GROUPS[group]
            out.append(f'<div class="snav-group"><span class="en">{g_en}</span><span class="ne">{g_ne}</span></div>')
            current_group = group
        href = f"{slug}.html" if slug != "index" else "index.html"
        cls = ' class="active" aria-current="page"' if slug == active_slug else ""
        mark = f'<span class="catmark" style="background:var({cat})"></span>' if cat else '<span class="catmark" style="background:transparent"></span>'
        out.append(
            f'<a href="{href}"{cls}><span class="secnum">{num}</span>{mark}'
            f'<span class="en">{en}</span><span class="ne">{ne}</span></a>'
        )
    return "\n      ".join(out)


def pager_html(i: int) -> str:
    parts = []
    if i > 0:
        s, _f, num, en, ne, *_ = PAGES[i - 1]
        href = "index.html" if s == "index" else f"{s}.html"
        parts.append(
            f'<a class="prev" href="{href}"><span class="lbl"><span class="en">Previous · {num}</span>'
            f'<span class="ne">अघिल्लो · {num}</span></span><span class="en">{en}</span><span class="ne">{ne}</span></a>'
        )
    if i < len(PAGES) - 1:
        s, _f, num, en, ne, *_ = PAGES[i + 1]
        parts.append(
            f'<a class="next" href="{s}.html"><span class="lbl"><span class="en">Next · {num}</span>'
            f'<span class="ne">अर्को · {num}</span></span><span class="en">{en}</span><span class="ne">{ne}</span></a>'
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Mukta:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Caveat:wght@600&display=swap">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main"><span class="en">Skip to content</span><span class="ne">सामग्रीमा जानुहोस्</span></a>
<div class="layout">
  <aside class="sidebar">
    <div class="top">
      <a class="brand" href="index.html"><span class="en">Mano Atlas</span><span class="ne">मनो एट्लास</span>
        <span class="sub"><span class="en">Mental health · two languages</span><span class="ne">मानसिक स्वास्थ्य · दुई भाषा</span></span></a>
      <div class="langsw" role="group" aria-label="Language">
        <button id="btn-en" onclick="setLang('en')">EN</button>
        <button id="btn-ne" onclick="setLang('ne')">ने</button>
      </div>
      <button id="btn-theme" class="themesw" onclick="cycleTheme()" aria-label="Colour theme">◐ Auto</button>
    </div>
    <div class="search">
      <input id="q" type="search" autocomplete="off" spellcheck="false"
        placeholder="Search · खोज्नुहोस्" aria-label="Search the atlas">
      <div id="qres" class="qres" hidden></div>
    </div>
    <nav class="snav" aria-label="Site">
      {nav}
    </nav>
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
          <p><span class="en">Last reviewed: {reviewed_en}</span><span class="ne">पछिल्लो समीक्षा: {reviewed_ne}</span></p>
        </div>
        <div class="crisis-col">
          <h4><span class="en">If you need help now</span><span class="ne">अहिले नै सहयोग चाहिए</span></h4>
          <p><strong>{helpline_suicide}</strong> <span class="en">National Suicide Prevention Helpline</span><span class="ne">राष्ट्रिय आत्महत्या रोकथाम हेल्पलाइन</span></p>
          <p><strong>{helpline_tuth}</strong> <span class="en">TUTH mental-health hotline</span><span class="ne">टिचिङ अस्पताल हटलाइन</span></p>
          <p><strong>{helpline_women}</strong> <span class="en">Women's helpline</span><span class="ne">महिला हेल्पलाइन</span> · <strong>{helpline_emergency}</strong> <span class="en">emergency</span><span class="ne">आपतकाल</span></p>
        </div>
        <div>
          <h4><span class="en">Open &amp; improvable</span><span class="ne">खुला र सुधारयोग्य</span></h4>
          <p class="en">Content licensed <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license noopener" target="_blank">CC BY-NC-SA 4.0</a>: share and adapt with credit, non-commercially.</p>
          <p class="ne">सामग्री <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" rel="license noopener" target="_blank">CC BY-NC-SA 4.0</a> अन्तर्गत: श्रेयसहित, गैर-व्यावसायिक रूपमा बाँड्न र मिलाउन पाइन्छ।</p>
          <p><span class="en">Spotted an error?</span><span class="ne">त्रुटि भेट्नुभयो?</span> <span class="mailrev" data-u="{email_user}" data-d="{email_domain}" data-t="{email_tld}">{email_user} [at] {email_domain} [dot] {email_tld}</span></p>
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

        if slug == "index":
            content = f'<header class="hero">\n{hero}\n</header>\n<section id="map">\n{body}\n</section>'
        else:
            gentle = ""
            if group == "disorders":
                gentle = ('<p class="gentle"><span class="en">A gentle note before you read: symptom lists make '
                          'almost everyone recognise themselves somewhere. That is a normal effect of reading, '
                          'not a diagnosis. If something here stays on your mind, a conversation with a '
                          'professional helps more than re-reading.</span>'
                          '<span class="ne">पढ्नुअघि एउटा कोमल कुरा: लक्षण-सूची पढ्दा झन्डै सबैलाई कतै न कतै आफ्नै झल्को मिल्छ। '
                          'त्यो पढाइको सामान्य असर हो, निदान होइन। कुनै कुरा मनमा अडिरह्यो भने फेरि-फेरि पढ्नुभन्दा '
                          'पेसागत व्यक्तिसँगको कुराकानीले बढी सघाउँछ।</span></p>\n')
            content = (
                f'<div class="pagehead"><div class="kicker"><span class="en">Section {num}</span>'
                f'<span class="ne">खण्ड {num}</span></div></div>\n{gentle}'
                f'<section id="{fname}" style="margin-top:12px">\n{body}\n</section>'
            )
        title = "Mano Atlas" if slug == "index" else f"{en} · Mano Atlas"
        html = SHELL.format(title=title, nav=nav_html(slug), content=content, pager=pager_html(i), **SITE)
        (ROOT / f"{slug}.html").write_text(html)
        print("built", f"{slug}.html")

    idx_js = "window.MANO_INDEX=" + json.dumps(search_index, ensure_ascii=False, separators=(",", ":")) + ";"
    (ROOT / "assets" / "search-index.js").write_text(idx_js)
    print(f"search index: {len(search_index)} entries, {len(idx_js)//1024} KB")


if __name__ == "__main__":
    main()
