# -*- coding: utf-8 -*-
"""페이지들이 공유하는 마크업 조각"""

PHONE_WEB = """<div class="svc-visual rv">
      <div class="phone" aria-hidden="true">
        <div class="ph-pad"></div>
        <div class="b b-sv b-hero"></div>
        <div class="b b-txt w9"></div>
        <div class="b b-txt w7"></div>
        <div class="b b-sv-d b-bar"></div>
        <div class="b-grid2"><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div></div>
        <div class="b b-txt w5"></div>
        <div class="b b-wide"></div>
        <div class="b b-sv b-dock"></div>
      </div>
      <p class="sr">반응형 홈페이지 화면 구조 예시 — 히어로, 소개 문구, 문의 버튼, 갤러리, 지도, 하단 고정 전화 버튼</p>
    </div>"""

CLIPS = """<div class="svc-visual rv">
      <div class="clips" aria-hidden="true">
        <div class="clip-f"><div class="clip-play"></div><div class="clip-cap"></div><div class="clip-cap s"></div></div>
        <div class="clip-f mid"><div class="clip-play"></div><div class="clip-cap"></div><div class="clip-cap s"></div></div>
        <div class="clip-f"><div class="clip-play"></div><div class="clip-cap"></div><div class="clip-cap s"></div></div>
      </div>
      <p class="sr">세로 숏폼 영상 3편 예시 — 자막이 들어간 30초 세로 규격</p>
    </div>"""

AICARD = """<div class="svc-visual rv">
      <div class="aicard" aria-hidden="true">
        <div class="ac-top">
          <div class="ac-av"></div>
          <div class="ac-line"><div class="b b-txt w7"></div><div class="b b-txt w4"></div></div>
        </div>
        <span class="ac-badge">배포 완료</span>
        <div class="ac-time">
          <div class="ac-ev hit"><div class="b b-sv b-txt w5"></div><div class="b b-txt w9"></div></div>
          <div class="ac-ev hit"><div class="b b-sv b-txt w4"></div><div class="b b-txt w7"></div></div>
          <div class="ac-ev"><div class="b b-txt w5"></div><div class="b b-txt w9"></div></div>
        </div>
        <div class="ac-metric">
          <i class="on" style="width:56px"></i><i style="width:40px"></i><i class="on" style="width:64px"></i><i style="width:44px"></i>
        </div>
      </div>
      <p class="sr">취업용 AI 결과물 화면 구조 예시 — 프로젝트 개요, 만든 과정 기록, 성과 지표</p>
    </div>"""

def work(mood, moodt, cat, h3, p, phone, tag):
    return ('<article class="work rv" data-svc-tag="' + tag + '" style="--mood:' + mood +
            ';--mood-t:' + moodt + '">\n'
            '  <div class="work-stage"><div class="phone" aria-hidden="true">' + phone + '</div></div>\n'
            '  <div class="work-body">\n'
            '    <p class="work-cat">' + cat + '</p>\n'
            '    <h3>' + h3 + '</h3>\n'
            '    <p>' + p + '</p>\n'
            '    <div class="work-foot"><span class="work-soon">데모 준비 중</span></div>\n'
            '  </div>\n</article>')

PH_CONST = ('<div class="ph-pad"></div><div class="b b-sv b-hero"></div><div class="b b-txt w9"></div>'
            '<div class="b-grid2"><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div></div>'
            '<div class="b b-sv-d b-bar"></div><div class="b b-txt w7"></div><div class="b b-sv b-dock"></div>')
PH_CAFE = ('<div class="ph-pad"></div><div class="b b-sv b-hero" style="height:62px"></div><div class="b b-txt w5"></div>'
           '<div class="b-stack"><div class="b b-txt w9"></div><div class="b b-txt w7"></div><div class="b b-txt w9"></div><div class="b b-txt w5"></div></div>'
           '<div class="b b-wide"></div><div class="b b-sv b-dock"></div>')
PH_CLINIC = ('<div class="ph-pad"></div><div class="b b-txt w7"></div><div class="b b-txt w9"></div>'
             '<div class="b b-sv b-bar"></div><div class="b b-wide"></div><div class="b b-txt w9"></div>'
             '<div class="b b-sv b-bar"></div><div class="b b-txt w5"></div><div class="b b-sv b-dock"></div>')
PH_BRAND = ('<div class="ph-pad"></div><div class="b b-sv b-txt w9" style="height:9px"></div>'
            '<div class="b b-sv b-txt w7" style="height:9px"></div><div class="b b-txt w5"></div>'
            '<div class="b-grid3"><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div></div>'
            '<div class="b b-txt w7"></div><div class="b b-sv-d b-dock"></div>')
PH_CLIP = ('<div class="ph-pad"></div><div class="b b-sv b-hero" style="height:120px"></div>'
           '<div class="b b-sv-d b-txt w7"></div><div class="b b-txt w5"></div>'
           '<div class="b-grid3"><div class="b b-sq"></div><div class="b b-sq"></div><div class="b b-sq"></div></div>'
           '<div class="b b-sv b-dock"></div>')
PH_AI = ('<div class="ph-pad"></div><div class="b b-txt w7"></div><div class="b b-sv b-hero" style="height:40px"></div>'
         '<div class="b b-txt w9"></div><div class="b b-txt w7"></div><div class="b b-sv-d b-bar"></div>'
         '<div class="b-grid2"><div class="b b-sq"></div><div class="b b-sq"></div></div>'
         '<div class="b b-txt w5"></div><div class="b b-sv b-dock"></div>')

WEB_WORKS = [
    ("#1B5BFF", "#EDF2FF", "Construction", "시공 · 인테리어 · 청소",
     "시공 전후 2×2 그리드가 중심. 견적 문의 버튼을 스크롤 내내 노출합니다.", PH_CONST, "web"),
    ("#F2650F", "#FFF1E7", "Cafe &amp; Dining", "카페 · 식당",
     "사진이 주인공. 메뉴는 리스트로, 지도와 영업시간은 아래에 고정합니다.", PH_CAFE, "web"),
    ("#0E9AA7", "#E6F7F9", "Clinic &amp; Academy", "병원 · 학원",
     "여백을 넉넉히. 상담 예약 버튼을 섹션마다 반복 배치합니다.", PH_CLINIC, "web"),
    ("#7C3AED", "#F4EDFF", "Personal Brand", "개인 브랜딩 · 프리랜서",
     "타이포가 히어로. 작업물 3열 그리드로 스크롤 없이 훑게 합니다.", PH_BRAND, "web"),
]
CLIP_WORKS = [
    ("#7C3AED", "#F4EDFF", "Before &amp; After", "시공 전후 30초",
     "지저분한 화면에서 깨끗한 화면으로 한 번에 넘기는 구성. 첫 1초에 전후를 붙입니다.", PH_CLIP, "clip"),
    ("#9333EA", "#F6EDFF", "Menu Cut", "메뉴 소개 30초",
     "대표 메뉴 3개를 한 컷씩. 가격과 위치 자막을 마지막 3초에 고정합니다.", PH_CLIP, "clip"),
    ("#6D28D9", "#F1EBFF", "Owner Interview", "사장님 한마디 30초",
     "말이 길어도 자막으로 끊어 읽히게. 소리를 꺼도 내용이 전달되는 편집입니다.", PH_CLIP, "clip"),
]
AI_WORKS = [
    ("#F2650F", "#FFF1E7", "Job Portfolio", "취업용 결과물 웹앱",
     "지원 직무에 맞춘 작동하는 웹앱 한 개. 배포 주소·소스·설명 문서까지 한 세트입니다.", PH_AI, "ai"),
    ("#EA580C", "#FFF0E6", "Career Doc", "이력서 반영 문단",
     "만든 결과물을 이력서·자기소개서·면접 답변으로 옮겨 적을 수 있는 형태로 정리합니다.", PH_AI, "ai"),
]

def cmp_table():
    return """<div class="cmp rv">
      <table>
        <caption class="sr">온도 웹 · 온도 클립 · 온도 AI 세 서비스 비교표</caption>
        <thead>
          <tr>
            <th scope="col"><span class="sr">구분</span></th>
            <th scope="col">온도 웹<small>반응형 홈페이지</small></th>
            <th scope="col">온도 클립<small>홍보 숏폼</small></th>
            <th scope="col">온도 AI<small>취업용 AI 결과물</small></th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="row">이런 분께</th>
            <td>검색했을 때 나올 자리가 <b>아예 없는</b> 사장님</td>
            <td>홈페이지는 있는데 <b>새 손님이 안 오는</b> 사장님</td>
            <td>이력서에 쓸 <b>결과물이 없는</b> 취업·이직 준비생</td></tr>
          <tr><th scope="row">받으시는 것</th>
            <td>바로 쓸 수 있는 <b>웹 주소</b> + 소스 전체</td>
            <td>30초 세로 영상 + 썸네일</td>
            <td>작동하는 <b>웹앱 주소</b> + 소스 + 설명 자료</td></tr>
          <tr><th scope="row">기간</th><td>3~5일</td><td>2~3일</td><td>4~10일</td></tr>
          <tr><th scope="row">시작 가격</th><td><b>5만원~</b></td><td><b>20만원</b> <small>편당</small></td><td><b>8만원~</b></td></tr>
          <tr><th scope="row">가장 먼저</th>
            <td>여기부터. 나머지가 다 여기로 연결됩니다</td>
            <td>웹이 있는 다음</td>
            <td>가게가 아니라 <b>본인</b>이 목적이면 이것만</td></tr>
        </tbody>
      </table>
    </div>"""

def faq(items):
    out = '<div class="faq rv">'
    for q, a in items:
        out += ('<details><summary>' + q + '</summary>'
                '<div class="faq-a">' + a + '</div></details>')
    return out + '</div>'

def steps(rows):
    out = '<div class="steps">'
    for day, h, p in rows:
        out += ('<div class="step rv"><p class="step-day">' + day + '</p>'
                '<h3>' + h + '</h3><p>' + p + '</p></div>')
    return out + '</div>'

def plan(name, forwho, price, unit, items, cta, href, best=False, tag=None):
    li = "".join('<li><span>' + x + '</span></li>' for x in items)
    t = '<span class="plan-tag">' + tag + '</span>' if tag else ''
    cls = 'plan rv plan-best' if best else 'plan rv'
    btn = 'btn btn-sv' if best else 'btn btn-line'
    return ('<div class="' + cls + '">' + t +
            '<h3>' + name + '</h3><p class="plan-for">' + forwho + '</p>'
            '<p class="plan-price">' + price + '<small>' + unit + '</small></p>'
            '<p class="plan-unit">부가세 별도</p>'
            '<ul>' + li + '</ul>'
            '<a class="' + btn + '" href="' + href + '" target="_blank" rel="noopener">' + cta + '</a></div>')


# ══════════════════════════════════════════════════════
# 실제 작업물 (배포된 사이트)
# ══════════════════════════════════════════════════════
def pf(mood, mood2, url, host, name, sub, cat, h3, desc, tags, tag):
    li = "".join('<li>' + t + '</li>' for t in tags)
    return ('<a class="pf rv" data-svc-tag="' + tag + '" href="' + url + '" target="_blank" rel="noopener"'
            ' style="--mood:' + mood + ';--mood-2:' + mood2 + '">\n'
            '  <div class="pf-top">\n'
            '    <span class="pf-url">' + host + '</span>\n'
            '    <span class="pf-name">' + name + '<small>' + sub + '</small></span>\n'
            '  </div>\n'
            '  <div class="pf-body">\n'
            '    <p class="pf-cat">' + cat + '</p>\n'
            '    <h3>' + h3 + '</h3>\n'
            '    <p>' + desc + '</p>\n'
            '    <ul class="pf-tags">' + li + '</ul>\n'
            '    <span class="pf-go">사이트 열기 →</span>\n'
            '  </div>\n</a>')

PORTFOLIO = [
    ("#0E5FD8", "#4E90FF",
     "https://safeclean.ondoco.workers.dev/", "safeclean.ondoco.workers.dev",
     "SAFECLEAN", "세이프클린ENG",
     "Ondo Web · 시공 · 설비", "강화유리문 수리 전문 업체 사이트",
     "강화유리문·자동문·현관문 수리와 출입통제 시공을 다루는 업체 사이트입니다. "
     "고장 증상으로 먼저 진단하게 하고, 시공사례를 모아 보여 준 뒤 문의로 이어지도록 순서를 잡았습니다.",
     ["반응형", "시공사례 갤러리", "증상별 진단", "서비스 지역", "전화·문의"], "web"),

    ("#0E9AA7", "#3FD0DC",
     "https://gaemyo-travel.vercel.app/", "gaemyo-travel.vercel.app",
     "GAEMYO", "개묘한여행",
     "Ondo Web · 개인 브랜딩", "여행 채널 소개 사이트",
     "세계여행을 준비하는 유튜브 채널의 소개 페이지입니다. "
     "채널의 캐릭터 설정을 먼저 보여 주고, 영상과 SNS로 자연스럽게 넘어가도록 구성했습니다.",
     ["반응형", "유튜브 임베드", "캐릭터 소개", "SNS 연결"], "web"),

    ("#D9540C", "#FF9040",
     "https://career-lab.ondo-co.workers.dev/", "career-lab.ondo-co.workers.dev",
     "CAREER LAB", "커리어 랩",
     "Ondo AI · 취업용 결과물", "커리어 준비용 웹앱",
     "온도컴퍼니가 만든 커리어 준비용 웹앱입니다. "
     "온도 AI로 어떤 결과물이 나오는지 직접 눌러 보실 수 있는 예시입니다.",
     ["웹앱", "배포 완료", "온도 AI 결과물"], "ai"),
]
