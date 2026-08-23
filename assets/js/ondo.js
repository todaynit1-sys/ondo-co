/* ═══════════════════════════════════════════════════════════
   ONDO° 온도컴퍼니 — 공통 스크립트
   모든 페이지에서 <script src="…/assets/js/ondo.js" defer> 로 불러온다.
   각 블록은 해당 요소가 있을 때만 동작하므로 페이지마다 따로 손댈 필요가 없다.
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  var KAKAO = 'https://open.kakao.com/o/suzwcdKi'; /* 카카오톡 오픈채팅 */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (id) { return document.getElementById(id); };
  var $$ = function (sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  };

  /* ══ 공지 배너 ══ */
  (function () {
    var el = $('notice'), x = $('noticeX');
    if (!el || !x) return;
    var KEY = 'ondo_notice_off';
    try {
      var until = parseInt(localStorage.getItem(KEY) || '0', 10);
      if (until && until > new Date().getTime()) { el.hidden = true; return; }
    } catch (e) {}
    x.addEventListener('click', function () {
      el.hidden = true;
      try { localStorage.setItem(KEY, String(new Date().getTime() + 30 * 864e5)); } catch (e) {}
    });
  })();

  /* ══ 모바일 메뉴 ══ */
  (function () {
    var burger = $('burger'), menu = $('menu'), close = $('menuX');
    if (!burger || !menu) return;
    var lastY = 0;
    function open() {
      lastY = window.pageYOffset;
      menu.hidden = false;
      burger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      var first = menu.querySelector('a, button');
      if (first) first.focus();
    }
    function shut() {
      menu.hidden = true;
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      burger.focus();
      window.scrollTo(0, lastY);
    }
    burger.addEventListener('click', function () {
      if (menu.hidden) open(); else shut();
    });
    if (close) close.addEventListener('click', shut);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) shut();
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 900 && !menu.hidden) shut();
    });
  })();

  /* ══ 스크롤 등장 ══ */
  (function () {
    var els = $$('.rv');
    if (!els.length) return;
    if (reduce || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (list) {
      list.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -9% 0px', threshold: 0.05 });
    var seen = {};
    els.forEach(function (el) {
      var p = el.parentNode;
      var key = p && p.className ? p.className : 'x';
      seen[key] = (seen[key] || 0) + 1;
      if (seen[key] > 1 && seen[key] <= 4) el.style.transitionDelay = ((seen[key] - 1) * 0.08) + 's';
      io.observe(el);
    });
  })();

  /* ══ 탭 공통 ══ */
  function bindTabs(tabs, onSelect) {
    if (!tabs.length) return null;
    function select(i) {
      tabs.forEach(function (t, k) {
        var on = k === i;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        var p = document.getElementById(t.getAttribute('aria-controls'));
        if (p) p.hidden = !on;
      });
      if (onSelect) onSelect(tabs[i].dataset.svc, i);
    }
    tabs.forEach(function (tab, idx) {
      tab.addEventListener('click', function () { select(idx); });
      tab.addEventListener('keydown', function (ev) {
        var k = ev.key, n = -1;
        if (k === 'ArrowRight' || k === 'ArrowDown') n = (idx + 1) % tabs.length;
        else if (k === 'ArrowLeft' || k === 'ArrowUp') n = (idx - 1 + tabs.length) % tabs.length;
        else if (k === 'Home') n = 0;
        else if (k === 'End') n = tabs.length - 1;
        if (n < 0) return;
        ev.preventDefault();
        select(n);
        tabs[n].focus();
      });
    });
    return select;
  }

  function paint(el, svc) {
    var k = ({ web: 'web', clip: 'clip', ai: 'ai' })[svc] || 'web';
    el.style.setProperty('--sv', 'var(--' + k + ')');
    el.style.setProperty('--sv-d', 'var(--' + k + '-d)');
    el.style.setProperty('--sv-t', 'var(--' + k + '-t)');
  }

  /* ══ 메인 콘솔 탭 ══ */
  (function () {
    var con = $('console');
    if (!con) return;
    var gauge = $('conGauge');
    var bars = gauge ? Array.prototype.slice.call(gauge.children) : [];
    bindTabs($$('.tab', con), function (svc, i) {
      bars.forEach(function (b, k) { b.classList.toggle('on', k === i); });
    });
  })();

  /* ══ 요금 탭 ══ */
  (function () {
    var sec = $('s-price');
    if (!sec) return;
    var tabs = $$('.ptab', sec);
    var select = bindTabs(tabs, function (svc) { paint(sec, svc); });
    if (!select) return;
    /* 주소 뒤에 #price-clip 처럼 붙여 오면 그 탭을 연다 */
    var want = (location.hash || '').replace('#price-', '');
    var idx = 0;
    tabs.forEach(function (t, i) { if (t.dataset.svc === want) idx = i; });
    select(idx);
  })();

  /* ══ 작업물 필터 ══ */
  (function () {
    var box = $('workFilters');
    if (!box) return;
    var btns = $$('.filter', box);
    var items = $$('[data-svc-tag]');
    var count = $('workCount');
    function apply(f) {
      var n = 0;
      items.forEach(function (el) {
        var on = f === 'all' || el.dataset.svcTag === f;
        el.hidden = !on;
        if (on) n++;
      });
      btns.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.f === f ? 'true' : 'false'); });
      if (count) count.textContent = n + '개 항목을 보고 계십니다.';
    }
    btns.forEach(function (b) {
      b.addEventListener('click', function () { apply(b.dataset.f); });
    });
    apply('all');
  })();

  /* ══ 클립보드 ══ */
  $$('.copybtn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var text = btn.dataset.copy || '';
      var label = btn.dataset.label || btn.textContent;
      btn.dataset.label = label;
      function done(ok) {
        btn.textContent = ok ? '복사됨' : '복사 실패';
        btn.classList.toggle('ok', ok);
        window.setTimeout(function () { btn.textContent = label; btn.classList.remove('ok'); }, 1700);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(false); });
        return;
      }
      var ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) {}
      document.body.removeChild(ta);
      done(ok);
    });
  });

  /* ══ 문의폼 ══ */
  (function () {
    var form = $('cForm');
    if (!form) return;
    var fields = [
      { i: 'f-name', e: 'e-name' },
      { i: 'f-contact', e: 'e-contact' },
      { i: 'f-msg', e: 'e-msg' }
    ];
    /* 서비스 페이지에서 넘어오면 관심 서비스를 미리 채운다 (?svc=clip) */
    (function () {
      var m = /[?&]svc=(web|clip|ai)/.exec(location.search);
      var sel = $('f-svc');
      if (m && sel) sel.value = m[1];
    })();

    form.addEventListener('submit', function (ev) {
      var bad = null;
      fields.forEach(function (f) {
        var el = $(f.i), err = $(f.e);
        if (!el || !err) return;
        var empty = !el.value.trim();
        err.hidden = !empty;
        el.setAttribute('aria-invalid', empty ? 'true' : 'false');
        if (empty && !bad) bad = el;
      });
      if (bad) { ev.preventDefault(); bad.focus(); return; }

      /* 폼 주소가 아직 자리표시자면 전송하지 않고 카톡으로 안내 */
      if ((form.getAttribute('action') || '').indexOf('REPLACE_') > -1) {
        ev.preventDefault();
        form.hidden = true;
        var done = $('cDone');
        if (!done) return;
        done.hidden = false;
        done.querySelector('h3').textContent = '카카오톡으로 부탁드립니다';
        $('cDoneMsg').innerHTML =
          '아직 문의폼 수신 주소가 연결되지 않았습니다.<br>' +
          '<a href="' + KAKAO + '" target="_blank" rel="noopener" style="color:#1B5BFF;font-weight:700;text-decoration:underline">카카오톡 오픈채팅</a>으로 연락 주시면 바로 확인합니다.';
        done.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
      }
    });
    fields.forEach(function (f) {
      var el = $(f.i);
      if (!el) return;
      el.addEventListener('input', function () {
        if (this.value.trim()) {
          var err = $(f.e);
          if (err) err.hidden = true;
          this.setAttribute('aria-invalid', 'false');
        }
      });
    });
  })();

  /* ══ 진행바 · 네비 · 맨위로 ══ */
  (function () {
    var bar = $('progFill'), nav = $('nav'), up = $('toTop');
    var ticking = false;
    function update() {
      ticking = false;
      var s = document.documentElement.scrollHeight - window.innerHeight;
      var y = window.pageYOffset;
      var p = s > 0 ? Math.min(1, Math.max(0, y / s)) : 0;
      if (bar) bar.style.width = (p * 100).toFixed(2) + '%';
      if (nav) nav.classList.toggle('is-stuck', y > 8);
      if (up) up.classList.toggle('on', y > window.innerHeight * 0.9);
    }
    function onScroll() {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(update);
    }
    if (up) up.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
    });
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);
    update();
  })();

  /* ══ 연도 자동 ══ */
  $$('[data-year]').forEach(function (el) { el.textContent = String(new Date().getFullYear()); });
})();
