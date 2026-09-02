/* Mano Atlas: client-side search over the build-time index (assets/search-index.js). */
(function () {
  var loading = false;
  function loadIndex(cb) {
    if (window.MANO_INDEX) { cb(); return; }
    if (loading) return; loading = true;
    var sc = document.createElement('script'); sc.src = 'assets/search-index.js'; sc.onload = cb; document.head.appendChild(sc);
  }
  function boot() {
    var input = document.getElementById('q'); if (!input) return;
    var started = false;
    function start() { if (started) return; started = true; loadIndex(function () { init(); if (input.value) input.dispatchEvent(new Event('input')); }); }
    input.addEventListener('focus', start); input.addEventListener('input', start);
    if (document.activeElement === input) start();
  }
  function init() {
    var input = document.getElementById('q');
    var box = document.getElementById('qres');
    if (!input || !box || !window.MANO_INDEX) return;

    var IDX = window.MANO_INDEX.map(function (e) {
      return { e: e, lx: e.x.toLowerCase(), lte: e.te.toLowerCase() };
    });

    /* everyday-language routes: a worried family member does not know the chapter names */
    var ALIASES = [
      { k: ['school', 'won\'t go', 'wont go', 'refus', 'exam', 'homework', 'bidyalaya', 'skul', 'विद्यालय', 'स्कुल', 'परीक्षा', 'पढ्न मान्दैन', 'बदमास'], u: 'child.html', te: 'Child mental illness: school refusal, exams, behaviour', tn: 'बाल मानसिक समस्या: विद्यालय जान नमान्नु, परीक्षा, व्यवहार' },
      { k: ['cries', 'crying', 'cry', 'sad', 'no interest', 'hopeless', 'tired all', 'man dukh', 'udas', 'रुन्छ', 'रुने', 'रोइरह', 'मन दुख', 'उदास', 'निराश', 'जाँगर छैन'], u: 'depression.html', te: 'Depression: crying, low mood, no interest', tn: 'डिप्रेसन: रुनु, मन दुख्नु, जाँगर नहुनु' },
      { k: ['suicid', 'kill', 'die', 'end my life', 'self-harm', 'self harm', 'aatmahatya', 'marna', 'आत्महत्या', 'मर्न', 'मर्ने', 'आत्म-हानि', 'ज्यान'], u: 'suicide.html', te: 'Suicide: what to ask, what to do now (helplines 1166, 1660 012 1600)', tn: 'आत्महत्या: के सोध्ने, अहिले के गर्ने (हेल्पलाइन ११६६, १६६० ०१२ १६००)' },
      { k: ['worry', 'worried', 'nervous', 'tension', 'chinta', 'aatti', 'mutu dhukdhuk', 'चिन्ता', 'आत्ति', 'डर', 'ढुकढुक', 'टेन्सन'], u: 'anxiety.html', te: 'Anxiety: worry, fear, panic', tn: 'चिन्ता: फिक्री, डर, प्यानिक' },
      { k: ['panic', 'heart attack', 'chest', 'breath', 'mutu kamjor', 'छाती', 'सास', 'मुटु कमजोर'], u: 'anxiety.html#panic', te: 'Panic attacks: chest, breath, "mutu kamjor"', tn: 'प्यानिक एट्याक: छाती, सास, «मुटु कमजोर»' },
      { k: ['voices', 'hearing', 'talks alone', 'suspicious', 'paagal', 'pagal', 'baulayo', 'आवाज', 'एक्लै बोल्छ', 'शङ्का', 'पागल', 'बौलायो', 'बहुला'], u: 'psychosis.html', te: 'Psychosis: hearing voices, strange beliefs, "paagal"', tn: 'मनोविकृति: आवाज सुन्नु, अनौठा विश्वास, «पागल»' },
      { k: ['sleep', 'insomnia', 'nightmare', 'nidra', 'निद्रा', 'सुत्न', 'नराम्रो सपना'], u: 'sleep.html', te: 'Sleep: cannot sleep, nightmares', tn: 'निद्रा: सुत्न नसक्नु, नराम्रो सपना' },
      { k: ['alcohol', 'drink', 'drunk', 'drugs', 'raksi', 'jaand', 'ganja', 'nasha', 'रक्सी', 'जाँड', 'गाँजा', 'नशा', 'लागुपदार्थ', 'पिउ'], u: 'substance.html', te: 'Alcohol and drugs: when drinking is a problem', tn: 'रक्सी र लागुपदार्थ: पिउनु कहिले समस्या हो' },
      { k: ['beat', 'beats', 'hits', 'violence', 'husband', 'rape', 'abuse', 'kutne', 'हिंसा', 'कुट्छ', 'पिट्छ', 'श्रीमान', 'बलात्कार', 'दुर्व्यवहार'], u: 'gbv.html', te: 'Violence at home or sexual violence: safety, 1145, OCMC', tn: 'घरेलु वा यौन हिंसा: सुरक्षा, ११४५, ओसीएमसी' },
      { k: ['not eating', 'eating', 'vomit', 'thin', 'weight', 'khana', 'खाँदैन', 'बान्ता', 'दुब्ल', 'तौल'], u: 'eating.html', te: 'Eating problems: not eating, vomiting, weight', tn: 'खानपान समस्या: नखानु, बान्ता, तौल' },
      { k: ['fits', 'faint', 'seizure', 'unconscious', 'behos', 'jhatka', 'बेहोस', 'मुर्छा', 'दौरा', 'छोपेको', 'छोप्ने'], u: 'somatic.html', te: 'Fainting, fits, "chhopne": conversion and mass conversion', tn: 'बेहोस, दौरा, «छोप्ने»: कन्भर्सन' },
      { k: ['earthquake', 'flood', 'accident', 'nightmares', 'flashback', 'trauma', 'sato', 'भूकम्प', 'बाढी', 'दुर्घटना', 'सातो', 'आघात'], u: 'trauma.html', te: 'After a terrible event: trauma, PTSD, "sato gayo"', tn: 'भयानक घटनापछि: आघात, पीटीएसडी, «सातो गयो»' },
      { k: ['washing', 'checking', 'repeat', 'doubt', 'हात धुन', 'बारम्बार', 'जाँच्न', 'शङ्का'], u: 'ocd.html', te: 'OCD: washing, checking, repeating', tn: 'ओसीडी: धुनु, जाँच्नु, दोहोर्‍याउनु' },
      { k: ['help now', 'helpline', 'hotline', 'emergency', 'number', 'हेल्पलाइन', 'नम्बर', 'आपतकाल', 'सहयोग'], u: 'suicide.html', te: 'Help now: helplines inside Nepal', tn: 'अहिले नै सहयोग: नेपालभित्रका हेल्पलाइन' },
      { k: ['start', 'where to begin', 'new here', 'basics', 'सुरु', 'कहाँबाट'], u: 'basics.html', te: 'Start here: mental health basics', tn: 'यहाँबाट सुरु: मानसिक स्वास्थ्यका आधार' },
      { k: ['what to say', 'paraphras', 'reflect', 'summaris', 'summariz', 'phrases', 'role-play', 'role play', 'confront', 'brainstorm', 'के भन्ने', 'पुनर्कथन', 'प्रतिबिम्ब', 'सारांश', 'मन्थन', 'चुनौती'], u: 'skills-practice.html', te: 'Verbal skills in practice: what to say, what goes wrong', tn: 'शाब्दिक सीप अभ्यासमा: के भन्ने, के बिग्रन्छ' },
      { k: ['first session', 'introduce', 'confidential', 'consent', 'expectation', 'assessment', 'intake', 'what to ask', 'पहिलो सत्र', 'परिचय', 'गोपनीयता', 'सहमति', 'मूल्याङ्कन', 'के सोध्ने'], u: 'first-sessions.html', te: 'The first sessions: scripts and the assessment questions', tn: 'पहिला सत्रहरू: स्क्रिप्ट र मूल्याङ्कनका प्रश्न' },
      { k: ['act ', 'acceptance', 'activation', 'activity chart', 'erp', 'exposure', 'hierarchy', 'fear ladder', 'defusion', 'life skills', 'एक्सपोजर', 'गतिविधि', 'तालिका', 'भर्‍याङ', 'जीवन सीप'], u: 'techniques.html', te: 'Techniques step by step: ACT, behavioural activation, ERP', tn: 'प्रविधि चरणैपिच्छे: ACT, behavioural activation, ERP' }
    ];
    function norm(s) {
      s = s.toLowerCase();
      try { s = s.normalize('NFD').replace(/[\u0300-\u036f]/g, ''); } catch (e) {}
      return s.replace(/\u0901/g, '\u0902').replace(/[\u200c\u200d]/g, '').replace(/\s+/g, ' ');
    }
    function esc(s) {
      return s.replace(/[&<>"]/g, function (c) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
      });
    }

    function snippet(e, pos, qlen) {
      var s = Math.max(0, pos - 55);
      var t = Math.min(e.x.length, pos + qlen + 75);
      return (s > 0 ? '…' : '') + esc(e.x.slice(s, pos)) +
        '<mark>' + esc(e.x.substr(pos, qlen)) + '</mark>' +
        esc(e.x.slice(pos + qlen, t)) + (t < e.x.length ? '…' : '');
    }

    function search(q) {
      q = q.trim();
      if (q.length < 2) { box.hidden = true; box.innerHTML = ''; return; }
      var lq = q.toLowerCase();
      var nq = norm(q);
      var res = [];
      var hits = [];
      for (var a = 0; a < ALIASES.length; a++) {
        var al = ALIASES[a];
        for (var kk = 0; kk < al.k.length; kk++) {
          if (nq.indexOf(norm(al.k[kk])) >= 0) { hits.push(al); break; }
        }
      }
      for (var i = 0; i < IDX.length; i++) {
        var it = IDX[i];
        var score = 0;
        if (it.lte.indexOf(lq) >= 0 || it.e.tn.indexOf(q) >= 0) score += 10;
        var pos = it.lx.indexOf(lq);
        if (pos >= 0) score += (it.e.u.indexOf('#') < 0 ? 4 : 3);
        if (score > 0) res.push({ it: it, score: score, pos: pos });
      }
      res.sort(function (a, b) { return b.score - a.score; });
      res = res.slice(0, 8);
      var top = hits.slice(0, 3).map(function (al) {
        return '<a href="' + al.u + '" class="qroute"><span class="qt"><span class="en">' + esc(al.te) +
          '</span><span class="ne">' + esc(al.tn) + '</span></span></a>';
      }).join('');
      if (!res.length && !top) {
        box.innerHTML = '<div class="qempty"><span class="en">No results. Try an English or नेपाली term</span>' +
          '<span class="ne">केही भेटिएन। अर्को शब्द प्रयास गर्नुहोस्</span></div>';
        box.hidden = false;
        return;
      }
      box.innerHTML = top + res.map(function (r) {
        var e = r.it.e;
        var snip = r.pos >= 0 ? '<span class="qs">' + snippet(e, r.pos, q.length) + '</span>' : '';
        return '<a href="' + e.u + '"><span class="qt"><span class="en">' + esc(e.te) +
          '</span><span class="ne">' + esc(e.tn) + '</span></span>' + snip + '</a>';
      }).join('');
      box.hidden = false;
    }

    var timer;
    input.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () { search(input.value); }, 120);
    });
    input.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') { box.hidden = true; input.blur(); }
      if (ev.key === 'Enter') {
        var a = box.querySelector('a');
        if (a) location.href = a.getAttribute('href');
      }
    });
    input.addEventListener('focus', function () {
      if (box.innerHTML) box.hidden = false;
    });
    document.addEventListener('click', function (ev) {
      if (!ev.target.closest || !ev.target.closest('.search')) box.hidden = true;
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
