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
    ("#7C3AED", "#F4EDFF", "Animal Cast", "동물 캐릭터 광고 30초",
     "말하는 동물 캐릭터가 가게를 소개하는 구성. 사람이 나오지 않아 부담이 없고 시선이 잘 멈춥니다.", PH_CLIP, "clip"),
    ("#9333EA", "#F6EDFF", "AI Anchor", "AI 아나운서 소개 30초",
     "뉴스 형식으로 또박또박 전달하는 구성. 정보량이 많은 업종(학원·병원·수리)에 맞습니다.", PH_CLIP, "clip"),
    ("#6D28D9", "#F1EBFF", "Story 60s", "메뉴 · 서비스 소개 60초",
     "장면을 여러 개로 나눠 설명하는 구성. 왜 좋은지 근거를 붙여야 하는 경우에 씁니다.", PH_CLIP, "clip"),
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
            <th scope="col">온도 클립<small>AI 홍보 영상</small></th>
            <th scope="col">온도 AI<small>취업용 AI 결과물</small></th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="row">이런 분께</th>
            <td>검색했을 때 나올 자리가 <b>아예 없는</b> 사장님</td>
            <td><b>촬영할 시간도 소재도 없는</b> 사장님</td>
            <td>이력서에 쓸 <b>결과물이 없는</b> 취업·이직 준비생</td></tr>
          <tr><th scope="row">받으시는 것</th>
            <td>바로 쓸 수 있는 <b>웹 주소</b> + 소스 전체</td>
            <td>AI로 만든 세로 영상 + 썸네일</td>
            <td>작동하는 <b>웹앱 주소</b> + 소스 + 설명 자료</td></tr>
          <tr><th scope="row">매달 나가는 돈</th>
            <td><b>0원</b> <small>호스팅비 없음</small></td>
            <td>0원 <small>영상 파일 소유</small></td>
            <td><b>0원</b> <small>호스팅비 없음</small></td></tr>
          <tr><th scope="row">기간</th><td>3~5일</td><td>2~5일</td><td>3~7일</td></tr>
          <tr><th scope="row">시작 가격</th><td><b>5만원~</b></td><td><b>20만원</b> <small>30초 1편</small></td><td><b>8만원~</b></td></tr>
          <tr><th scope="row">준비해 주실 것</th>
            <td>가게 사진, 소개 문구, 연락처</td>
            <td>알리고 싶은 내용 한두 줄</td>
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

def plan(name, forwho, price, unit, items, cta, href, best=False, tag=None, was=None, note=None):
    li = "".join('<li><span>' + x + '</span></li>' for x in items)
    t = '<span class="plan-tag">' + tag + '</span>' if tag else ''
    cls = 'plan rv plan-best' if best else 'plan rv'
    btn = 'btn btn-sv' if best else 'btn btn-line'
    w = '<p class="plan-was">정가 <s>' + was + '</s> <em>오픈 기념 할인</em></p>' if was else ''
    n = note or '상담에서 구성 확인 후 확정'
    return ('<div class="' + cls + '">' + t +
            '<h3>' + name + '</h3><p class="plan-for">' + forwho + '</p>' + w +
            '<p class="plan-price">' + price + '<small>' + unit + '</small></p>'
            '<p class="plan-unit">' + n + '</p>'
            '<ul>' + li + '</ul>'
            '<a class="' + btn + '" href="' + href + '" target="_blank" rel="noopener">' + cta + '</a></div>')


# ══════════════════════════════════════════════════════
# 실제 작업물 (배포된 사이트) — 미리보기 이미지 포함
#   이미지: images/work/<slug>.webp  (실제 사이트 첫 화면 캡처)
# ══════════════════════════════════════════════════════
def pf(P, slug, mood, url, host, name, cat, desc, tags, tag, alt, mood_t=None):
    li = "".join('<li>' + t + '</li>' for t in tags)
    mt = (';--mood-t:' + mood_t) if mood_t else ''
    return ('<a class="pf rv" data-svc-tag="' + tag + '" href="' + url + '" target="_blank" rel="noopener"'
            ' style="--mood:' + mood + mt + '">\n'
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
    ("cheongdam", "#1A1714",
     "https://cheongdam.ondoco.workers.dev/", "cheongdam.ondoco.workers.dev",
     "헤어청담", "Ondo Web · 미용실",
     "안산 고잔동 미용실의 원페이지 사이트입니다. "
     "매장 로고와 실제 시술 사진을 앞에 두고, 스타일을 본 다음 가격표를 지나 인스타 DM 예약으로 이어지도록 순서를 잡았습니다.",
     ["반응형", "룩북 9장", "가격표 76항목", "인스타 DM 예약", "전화 바로걸기"], "web",
     "헤어청담 사이트 첫 화면 — CHEONG DAM 로고와 안산 고잔동 미용실 한 줄 소개, 인스타 DM 예약 버튼"),

    ("feet-lab", "#1D4E86",
     "https://feet-inha.ondoco.workers.dev/", "feet-inha.ondoco.workers.dev",
     "FEET Lab", "Ondo Web · 대학 연구실",
     "인하대학교 환경공학과 FEET 연구실 사이트입니다. "
     "무엇을 연구하는 곳인지 먼저 보여 주고, 논문과 구성원 소개를 지나 연구실 지원 문의로 이어지도록 5개 페이지로 나눠 구성했습니다.",
     ["반응형", "5개 페이지", "논문 아카이브", "구성원 소개", "원문 링크 연결"], "web",
     "FEET Lab 사이트 첫 화면 — 안 보이는 것을 끝까지 측정합니다 문구와 연구 소개 버튼"),

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
     "개묘한여행 사이트 첫 화면 — 채널 이름과 두 캐릭터 소개", "#A32F49"),

    ("career-lab", "#2C3D63",
     "https://career-lab.ondoco.workers.dev/", "career-lab.ondoco.workers.dev",
     "커리어전략연구소", "Ondo Web · 전문가 브랜딩",
     "커리어 상담 데이터를 이론으로 정리해 온 연구소 사이트입니다. "
     "네이비와 금색으로 신뢰감을 먼저 세우고, 연구 분야와 소장 소개를 지나 자문 의뢰까지 한 흐름으로 이어집니다.",
     ["반응형", "연구 분야", "아카이브", "자가진단 도구", "자문 의뢰"], "web",
     "커리어전략연구소 사이트 첫 화면 — 커리어에도 전략이 필요합니다 문구와 소개 버튼"),

    ("cleansheet", "#245FA8",
     "https://cleansheet-omega.vercel.app/", "cleansheet-omega.vercel.app",
     "CLEANSHEET", "Ondo AI · 취업용 결과물",
     "표를 붙여넣으면 중복 입력·거래처명 표기 불일치·날짜 형식 혼재를 먼저 찾아내고, "
     "우리 장부와 거래처 명세서를 맞춰 차액까지 뽑는 도구입니다. 영업관리·회계·정산 직무에 맞춰 만들었습니다.",
     ["웹앱", "표 붙여넣기 점검", "두 표 대조", "표기 차이 흡수", "결과 CSV 내려받기"], "ai",
     "CLEANSHEET 대조 결과 화면 — 표 A·B 합계와 차액, 금액 다름·A에만·B에만 항목 목록"),

    ("ziggle-stock", "#4F46E5",
     "https://ziggle-stock.vercel.app/", "ziggle-stock.vercel.app",
     "지글의 주린이 가이드", "Ondo AI · 취업용 결과물",
     "배당·적립 투자를 직접 계산해 보는 웹앱입니다. 종목과 초기 투자금·월 적립금을 넣으면 최대 30년까지 "
     "자산과 월 배당금을 계산하고, 계좌 종류에 따라 달라지는 세율과 배당 재투자까지 반영해 보여 줍니다.",
     ["웹앱", "종목별 계산", "계좌별 세율 반영", "배당 재투자", "CSV 내보내기"], "ai",
     "지글의 주린이 가이드 앱 화면 — 계산 모드 선택과 종목 추가, 포트폴리오 입력 화면"),

]
