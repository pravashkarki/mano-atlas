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
