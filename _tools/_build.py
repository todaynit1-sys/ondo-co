# -*- coding: utf-8 -*-
"""ONDO 멀티페이지 정적 사이트 생성기 (결과물은 순수 HTML)"""
import json, os, io

# 어디에서 실행하든 사이트 루트(= _tools 의 상위 폴더)에 파일을 쓴다
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = "https://REPLACE-ME.github.io/ondo/"     # 배포 후 실제 주소로 일괄 치환
KAKAO = "https://open.kakao.com/o/suzwcdKi"
FORM_ACTION = "https://formspree.io/f/REPLACE_FORMSPREE"
BRAND = "온도컴퍼니"

NAV = [
    ("web/",     "온도 웹",   "web"),
    ("clip/",    "온도 클립", "clip"),
    ("ai/",      "온도 AI",   "ai"),
    ("work/",    "작업물",    None),
    ("pricing/", "요금",      None),
]

MARK = ('<svg class="mark" viewBox="0 0 44 44" aria-hidden="true">'
        '<circle class="ring" cx="19" cy="25" r="14"/>'
        '<circle class="dot" cx="34.5" cy="12" r="6.4"/></svg>')

def brand(P, cls="nav-brand", tag=True):
    t = '<span class="tag">' + BRAND + '</span>' if tag else ''
    return ('<a class="' + cls + '" href="' + (P or './') + '" aria-label="온도컴퍼니 홈">'
            + MARK + '<span class="wordmark">ONDO<b>°</b></span>' + t + '</a>')

def nav(P, here):
    links = ""
    for href, label, svc in NAV:
        cls = ' class="is-here"' if here == href else ''
        links += '<a href="' + P + href + '"' + cls + '>' + label + '</a>'
    menu = ""
    for href, label, svc in NAV:
        sub = {"web/": "반응형 홈페이지", "clip/": "홍보 숏폼", "ai/": "취업용 AI 결과물",
               "work/": "만든 것들", "pricing/": "세 서비스 요금표"}[href]
        d = ' data-svc="' + svc + '"' if svc else ''
        menu += ('<a href="' + P + href + '"' + d + '><span>' + label
                 + '</span><small>' + sub + '</small></a>')
    return (
'<div class="prog" aria-hidden="true"><i id="progFill"></i></div>\n'
'<header class="nav" id="nav">\n'
'  <div class="wrap nav-in">\n'
'    ' + brand(P) + '\n'
'    <nav class="nav-links" aria-label="주요 메뉴">' + links + '</nav>\n'
'    <div class="nav-right">\n'
'      <a class="btn btn-kko btn-sm" href="' + KAKAO + '" target="_blank" rel="noopener">카톡 상담</a>\n'
'      <button class="nav-burger" id="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="메뉴 열기"><span></span></button>\n'
'    </div>\n'
'  </div>\n'
'</header>\n'
'<div class="menu" id="menu" hidden>\n'
'  <div class="menu-head">' + brand(P, "nav-brand", False) +
'    <button class="menu-x" id="menuX" type="button" aria-label="메뉴 닫기">×</button>\n'
'  </div>\n'
'  <nav class="menu-list" aria-label="전체 메뉴">' + menu +
'    <a href="' + P + 'contact/"><span>문의</span><small>카톡으로 바로</small></a>\n'
'  </nav>\n'
'  <div class="menu-cta">\n'
'    <a class="btn btn-kko btn-lg" href="' + KAKAO + '" target="_blank" rel="noopener">카카오톡으로 상담하기</a>\n'
'  </div>\n'
'</div>\n')

def footer(P):
    return (
'<footer class="ftr">\n'
'  <div class="wrap">\n'
'    <div class="ftr-top">\n'
'      <div style="display:flex;align-items:center;gap:11px">' + MARK +
'<span class="wordmark">ONDO<b>°</b></span>'
'<span class="ftr-slogan" style="margin-left:6px;color:var(--ink-3)">온라인에 온도를 더합니다</span></div>\n'
'      <nav class="ftr-links" aria-label="푸터 메뉴">'
'<a href="' + P + 'web/">온도 웹</a>'
'<a href="' + P + 'clip/">온도 클립</a>'
'<a href="' + P + 'ai/">온도 AI</a>'
'<a href="' + P + 'work/">작업물</a>'
'<a href="' + P + 'pricing/">요금</a>'
'<a href="' + P + 'contact/">문의</a>'
'<a href="' + KAKAO + '" target="_blank" rel="noopener">카톡 상담</a>'
'</nav>\n'
'    </div>\n'
'    <!-- 사업자 등록 후 아래 주석을 풀고 값을 채우세요\n'
'    <div class="biz">\n'
'      <span><b>상호</b> 온도컴퍼니 (ONDO Co.)</span>\n'
'      <span><b>대표</b> 000</span>\n'
'      <span><b>사업자등록번호</b> 000-00-00000</span>\n'
'      <span><b>주소</b> 000</span>\n'
'      <span><b>문의</b> 000-0000-0000</span>\n'
'    </div>\n'
'    -->\n'
'    <p class="copy">© <span data-year>2026</span> ONDO COMPANY. ALL RIGHTS RESERVED.</p>\n'
'  </div>\n'
'</footer>\n'
'<div class="dock"><a class="btn btn-kko" href="' + KAKAO + '" target="_blank" rel="noopener">'
'카카오톡으로 상담하기</a></div>\n'
'<button class="totop" id="toTop" type="button" aria-label="맨 위로">'
'<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
'stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>\n')

def page(path, title, desc, body, P, here, ld=None, theme=None, canon=None):
    cls = ' class="' + theme + '"' if theme else ''
    url = SITE + (canon if canon is not None else path.replace("index.html", ""))
    ldjson = ''
    if ld:
        ldjson = ('<script type="application/ld+json">'
                  + json.dumps(ld, ensure_ascii=False, separators=(",", ":"))
                  + '</script>\n')
    html = (
'<!DOCTYPE html>\n<html lang="ko">\n<head>\n'
'<meta charset="UTF-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
'<title>' + title + '</title>\n'
'<meta name="description" content="' + desc + '">\n'
'<link rel="canonical" href="' + url + '">\n'
'<meta name="theme-color" content="#FFFFFF">\n'
'<meta property="og:type" content="website">\n'
'<meta property="og:site_name" content="온도컴퍼니">\n'
'<meta property="og:locale" content="ko_KR">\n'
'<meta property="og:title" content="' + title + '">\n'
'<meta property="og:description" content="' + desc + '">\n'
'<meta property="og:url" content="' + url + '">\n'
'<meta property="og:image" content="' + SITE + 'images/og.png">\n'
'<meta name="twitter:card" content="summary_large_image">\n'
'<link rel="icon" href="' + P + 'images/favicon.png" sizes="any">\n'
'<link rel="apple-touch-icon" href="' + P + 'images/apple-touch-icon.png">\n'
'<link rel="preconnect" href="https://fonts.googleapis.com">\n'
'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
'<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>\n'
'<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">\n'
'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&display=swap">\n'
'<link rel="stylesheet" href="' + P + 'assets/css/ondo.css">\n'
+ ldjson +
'<script src="' + P + 'assets/js/ondo.js" defer></script>\n'
'</head>\n<body' + cls + '>\n'
'<a class="skip" href="#main">본문으로 바로가기</a>\n'
+ nav(P, here) +
'<main id="main">\n' + body + '</main>\n'
+ footer(P) +
'</body>\n</html>\n')
    out = os.path.join(ROOT, path)
    d = os.path.dirname(out)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    io.open(out, "w", encoding="utf-8").write(html)
    return len(html)

def crumb(P, trail):
    out = '<nav class="crumb" aria-label="현재 위치"><a href="' + (P or './') + '">홈</a>'
    for i, (href, label) in enumerate(trail):
        out += '<i>›</i>'
        if href:
            out += '<a href="' + P + href + '">' + label + '</a>'
        else:
            out += '<b aria-current="page">' + label + '</b>'
    return out + '</nav>'

def band(P, h2, p, svc=None):
    q = ('?svc=' + svc) if svc else ''
    return (
'<section class="band">\n<div class="wrap band-in">\n'
'  <h2 class="rv">' + h2 + '</h2>\n'
'  <p class="rv">' + p + '</p>\n'
'  <div class="band-btns rv">\n'
'    <a class="btn btn-kko btn-lg" href="' + KAKAO + '" target="_blank" rel="noopener">카카오톡으로 상담하기</a>\n'
'    <a class="btn btn-ghost btn-lg" href="' + P + 'contact/' + q + '">문의 남기기</a>\n'
'  </div>\n</div>\n</section>\n')

def nexts(P, cur):
    data = {
      "web":  ("web",  "Ondo Web",  "온도 웹", "검색했을 때 나올 자리를 만듭니다. 전화 바로걸기·카톡 문의·네이버 지도를 한 화면에 정리한 반응형 홈페이지.", "web/"),
      "clip": ("clip", "Ondo Clip", "온도 클립", "검색하지 않은 사람에게 닿는 통로. 찍어둔 사진·영상으로 30초 세로 영상을 만듭니다.", "clip/"),
      "ai":   ("ai",   "Ondo AI",   "온도 AI", "이력서에 쓸 결과물이 없다면 만들면 됩니다. 취업용 AI 결과물부터 제작 강의까지.", "ai/"),
    }
    out = '<div class="nexts">'
    for k in ["web", "clip", "ai"]:
        if k == cur:
            continue
        svc, en, ko, p, href = data[k]
        out += ('<a class="next rv" data-svc="' + svc + '" href="' + P + href + '">'
                '<span class="next-k">' + en + '</span>'
                '<h3>' + ko + '</h3><p>' + p + '</p>'
                '<span class="next-go">자세히 보기 →</span></a>')
    return out + '</div>'
