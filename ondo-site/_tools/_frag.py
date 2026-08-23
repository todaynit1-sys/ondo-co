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
            <td>영상으로 <b>가게를 알리고 싶은</b> 사장님</td>
            <td>이력서에 쓸 <b>결과물이 없는</b> 취업·이직 준비생</td></tr>
          <tr><th scope="row">받으시는 것</th>
            <td>바로 쓸 수 있는 <b>웹 주소</b> + 소스 전체</td>
            <td>30초 세로 영상 + 썸네일</td>
            <td>작동하는 <b>웹앱 주소</b> + 소스 + 설명 자료</td></tr>
          <tr><th scope="row">기간</th><td>3~5일</td><td>2~3일</td><td>4~10일</td></tr>
          <tr><th scope="row">시작 가격</th><td><b>5만원~</b></td><td><b>20만원</b> <small>편당</small></td><td><b>8만원~</b></td></tr>
          <tr><th scope="row">준비해 주실 것</th>
            <td>가게 사진, 소개 문구, 연락처</td>
            <td>찍어둔 사진·영상</td>
            <td>지원할 직무나 공고</td></tr>
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
# 실제 작업물 (배포된 사이트) — 미리보기 이미지 포함
#   이미지: images/work/<slug>.webp  (실제 사이트 첫 화면 캡처)
# ══════════════════════════════════════════════════════
def pf(P, slug, mood, url, host, name, cat, desc, tags, tag, alt):
    li = "".join('<li>' + t + '</li>' for t in tags)
    return ('<a class="pf rv" data-svc-tag="' + tag + '" href="' + url + '" target="_blank" rel="noopener"'
            ' style="--mood:' + mood + '">\n'
            '  <div class="pf-shot">\n'
            '    <div class="pf-bar"><i></i><i></i><i></i><span>' + host + '</span></div>\n'
            '    <img src="' + P + 'images/work/' + slug + '.webp" alt="' + alt + '"'
            ' width="1000" height="512" loading="lazy" decoding="async">\n'
            '  </div>\n'
            '  <div class="pf-body">\n'
            '    <p class="pf-cat">' + cat + '</p>\n'
            '    <h3>' + name + '</h3>\n'
            '    <p>' + desc + '</p>\n'
            '    <ul class="pf-tags">' + li + '</ul>\n'
            '    <span class="pf-go">사이트 열기 →</span>\n'
            '  </div>\n</a>')

PORTFOLIO = [
    ("safeclean", "#1B5BFF",
     "https://safeclean.ondoco.workers.dev/", "safeclean.ondoco.workers.dev",
     "세이프클린ENG", "Ondo Web · 시공 · 설비",
     "강화유리문·자동문·현관문 수리와 출입통제 시공을 다루는 업체 사이트입니다. "
     "첫 화면에 전화번호를 붙여 두고, 고장 증상으로 먼저 진단하게 한 뒤 시공사례로 이어지도록 순서를 잡았습니다.",
     ["반응형", "시공사례 갤러리", "증상별 진단", "전화 바로걸기", "네이버 지도"], "web",
     "세이프클린ENG 사이트 첫 화면 — 강화유리문·자동문 수리 소개와 전화 상담 버튼"),

    ("gaemyo", "#E0778F",
     "https://gaemyo-travel.vercel.app/", "gaemyo-travel.vercel.app",
     "개묘한여행", "Ondo Web · 개인 브랜딩",
     "세계여행을 시작한 개묘부부의 채널 소개 페이지입니다. "
     "손글씨 서체와 파스텔 톤으로 두 캐릭터를 먼저 보여 주고, 인스타그램으로 자연스럽게 넘어가도록 구성했습니다.",
     ["반응형", "캐릭터 소개", "SNS 연결", "손글씨 톤"], "web",
     "개묘한여행 사이트 첫 화면 — 채널 이름과 두 캐릭터 소개"),

    ("career-lab", "#2C3D63",
     "https://career-lab.ondoco.workers.dev/", "career-lab.ondoco.workers.dev",
     "커리어전략연구소", "Ondo Web · 전문가 브랜딩",
     "커리어 상담 데이터를 이론으로 정리해 온 연구소 사이트입니다. "
     "네이비와 금색으로 신뢰감을 먼저 세우고, 연구 분야와 소장 소개를 지나 자문 의뢰까지 한 흐름으로 이어집니다.",
     ["반응형", "연구 분야", "아카이브", "자가진단 도구", "자문 의뢰"], "web",
     "커리어전략연구소 사이트 첫 화면 — 커리어에도 전략이 필요합니다 문구와 소개 버튼"),

    ("ziggle-stock", "#4F46E5",
     "https://ziggle-stock.vercel.app/", "ziggle-stock.vercel.app",
     "지글의 주린이 가이드", "Ondo AI · 취업용 결과물",
     "배당·적립 투자를 직접 계산해 보는 웹앱입니다. 종목을 넣고 초기 투자금과 월 적립금을 입력하면 "
     "결과·비교·세금까지 화면을 나눠 보여 줍니다. 바이브코딩으로 만든 실사용 도구입니다.",
     ["웹앱", "입력 → 결과 계산", "종목 비교", "탭 구조", "모바일 우선"], "ai",
     "지글의 주린이 가이드 앱 화면 — 계산 모드 선택과 종목 추가, 포트폴리오 입력 화면"),

    ("ziggle-3x", "#6E56F8",
     "https://ziggle-3x.vercel.app/", "ziggle-3x.vercel.app",
     "지글의 그물망 매매법", "Ondo AI · 취업용 결과물",
     "특정 종목 하나를 위한 전략 대시보드입니다. 실시간 시세를 불러와 파라미터를 바꿔 보고, "
     "백테스트 화면에서 결과를 확인합니다. 외부 데이터 연동까지 들어간 결과물 예시입니다.",
     ["웹앱", "실시간 시세 연동", "파라미터 시뮬레이터", "백테스트", "다크 대시보드"], "ai",
     "지글의 그물망 매매법 대시보드 화면 — 계좌 정보 입력과 전략 파라미터 튜닝 패널"),
]
