function setLang(l){
    document.documentElement.setAttribute('data-lang', l);
    document.documentElement.lang = (l==='ne') ? 'ne' : 'en';
    document.getElementById('btn-en').classList.toggle('active', l==='en');
    document.getElementById('btn-ne').classList.toggle('active', l==='ne');
    try{ localStorage.setItem('psc-lang', l); }catch(e){}
  }
  (function(){
    var l='en';
    try{ l = localStorage.getItem('psc-lang') || 'en'; }catch(e){}
    setLang(l==='ne'?'ne':'en');
  })();

/* ---- theme: auto / light / dark (Lucide sun-moon / sun / moon) ---- */
function _lu(p){return '<svg class="lucide" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+p+'</svg>';}
var THEME_LABELS = {
  auto:  _lu('<path d="M12 8a2.83 2.83 0 0 0 4 4 4 4 0 1 1-4-4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.9 4.9 1.4 1.4"/><path d="m17.7 17.7 1.4 1.4"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.3 17.7-1.4 1.4"/><path d="m19.1 4.9-1.4 1.4"/>')+' <span class="en">Auto</span><span class="ne">स्वतः</span>',
  light: _lu('<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>')+' <span class="en">Light</span><span class="ne">उज्यालो</span>',
  dark:  _lu('<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>')+' <span class="en">Dark</span><span class="ne">अँध्यारो</span>'
};
var THEME_ORDER = ['auto', 'light', 'dark'];
function applyTheme(m) {
  if (m === 'auto') { document.documentElement.removeAttribute('data-theme'); }
  else { document.documentElement.setAttribute('data-theme', m); }
  var b = document.getElementById('btn-theme');
  if (b) { b.dataset.mode = m; b.innerHTML = THEME_LABELS[m]; }
  try { localStorage.setItem('psc-theme', m); } catch (e) {}
}
function cycleTheme() {
  var b = document.getElementById('btn-theme');
  var cur = (b && b.dataset.mode) || 'auto';
  applyTheme(THEME_ORDER[(THEME_ORDER.indexOf(cur) + 1) % 3]);
}
(function () {
  var m = 'auto';
  try { m = localStorage.getItem('psc-theme') || 'auto'; } catch (e) {}
  if (THEME_ORDER.indexOf(m) < 0) m = 'auto';
  function go() { applyTheme(m); }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', go); } else { go(); }
})();

/* ---- sidebar accordion: remember open groups; current group always open; all open on mobile ---- */
(function () {
  function go() {
    var secs = document.querySelectorAll('details.snav-sec');
    if (!secs.length) return;
    var saved = {};
    try { saved = JSON.parse(localStorage.getItem('psc-nav') || '{}'); } catch (e) {}
    var mobile = window.matchMedia('(max-width: 900px)').matches;
    secs.forEach(function (d) {
      var g = d.dataset.g;
      if (mobile) { d.open = true; return; }
      if (d.querySelector('a.active')) { d.open = true; }        /* never hide where you are */
      else if (g in saved) { d.open = !!saved[g]; }
      d.addEventListener('toggle', function () {
        var state = {};
        try { state = JSON.parse(localStorage.getItem('psc-nav') || '{}'); } catch (e) {}
        state[g] = d.open;
        try { localStorage.setItem('psc-nav', JSON.stringify(state)); } catch (e) {}
      });
    });
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', go); } else { go(); }
})();

/* ---- quick check: friendly, no scores ---- */
document.addEventListener('click', function (e) {
  var b = e.target.closest ? e.target.closest('.qz-opt') : null;
  if (!b || b.disabled) return;
  var qz = b.closest('.qz');
  var fb = qz.querySelector('.qz-fb');
  var hint = qz.querySelector('.qz-hint');
  if (b.dataset.i === qz.dataset.a) {
    b.classList.add('good');
    qz.querySelectorAll('.qz-opt').forEach(function (o) { o.disabled = true; });
    if (fb) fb.hidden = false;
    if (hint) hint.hidden = true;
  } else {
    b.classList.add('nope');
    b.disabled = true;
    if (hint) hint.hidden = false;
  }
});

/* ---- assemble the contact email in the browser (keeps it out of raw HTML for spam bots) ---- */
(function () {
  function go() {
    document.querySelectorAll('.mailrev').forEach(function (el) {
      var addr = el.dataset.u + '@' + el.dataset.d + '.' + el.dataset.t;
      var a = document.createElement('a');
      a.href = 'mailto:' + addr;
      a.textContent = addr;
      el.replaceWith(a);
    });
  }
  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', go); } else { go(); }
})();
