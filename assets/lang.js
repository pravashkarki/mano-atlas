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

/* ---- theme: auto / light / dark ---- */
var THEME_LABELS = {
  auto:  '◐ <span class="en">Auto</span><span class="ne">स्वतः</span>',
  light: '○ <span class="en">Light</span><span class="ne">उज्यालो</span>',
  dark:  '● <span class="en">Dark</span><span class="ne">अँध्यारो</span>'
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
