/* Mano Atlas: client-side search over the build-time index (assets/search-index.js). */
(function () {
  function init() {
    var input = document.getElementById('q');
    var box = document.getElementById('qres');
    if (!input || !box || !window.MANO_INDEX) return;

    var IDX = window.MANO_INDEX.map(function (e) {
      return { e: e, lx: e.x.toLowerCase(), lte: e.te.toLowerCase() };
    });

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
      var res = [];
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
      if (!res.length) {
        box.innerHTML = '<div class="qempty"><span class="en">No results. Try an English or नेपाली term</span>' +
          '<span class="ne">केही भेटिएन। अर्को शब्द प्रयास गर्नुहोस्</span></div>';
        box.hidden = false;
        return;
      }
      box.innerHTML = res.map(function (r) {
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
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
