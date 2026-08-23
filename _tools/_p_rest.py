# -*- coding: utf-8 -*-
from _build import *
from _frag import *
K = KAKAO
P = "../"

# ══════════════ 작업물 ══════════════
allworks = WEB_WORKS + CLIP_WORKS + AI_WORKS
body = """
<section class="phead">
  <div class="wrap phead-in">
    __CRUMB__
    <p class="eyebrow rv">Work <span class="ko">만든 것들</span></p>
    <h1>지금 열리는<br>주소로 보여 드립니다.</h1>
    <p class="phead-lede">캡처가 아니라 <b>실제로 배포된 사이트</b>입니다. 스마트폰에서 직접 눌러 보셔도 됩니다.
      아래에는 업종별로 화면 구조를 어떻게 다르게 잡는지도 함께 정리해 두었습니다.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="filters" id="workFilters" role="group" aria-label="서비스별 보기">
      <button class="filter" type="button" data-f="all" aria-pressed="true">전체</button>
      <button class="filter" type="button" data-f="web" aria-pressed="false">온도 웹</button>
      <button class="filter" type="button" data-f="clip" aria-pressed="false">온도 클립</button>
      <button class="filter" type="button" data-f="ai" aria-pressed="false">온도 AI</button>
    </div>
    <p class="filter-count" id="workCount" aria-live="polite"></p>

    <h2 class="rv" style="margin-top:34px">배포된 사이트</h2>
    <p class="lede rv">누르면 새 창으로 열립니다.</p>
    <div class="pfs">__PFS__</div>
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Structure <span class="ko">업종별 구성</span></p>
    <h2 class="rv">업종마다 화면 구조가 다릅니다</h2>
    <p class="lede rv">손님이 확인하고 싶은 게 업종마다 다르기 때문입니다.
      시공은 전후 사진, 카페는 메뉴와 분위기, 학원·병원은 상담 예약.</p>
    <div class="works" style="margin-top:34px">__WORKS__</div>

    <div class="note-box rv" style="--sv:var(--web);--sv-t:#EDF2FF">
      <b>솔직하게 적습니다.</b> 바로 위 화면들은 실제 고객 사이트가 아니라 <b>구성 순서를 보여 주는 예시</b>입니다.
      실제로 배포된 것은 이 페이지 맨 위의 사이트들이고, 나머지 업종의 데모는 준비되는 대로 여기에 주소로 걸어 두겠습니다.
      없는 실적이나 리뷰를 지어내지 않겠습니다.
    </div>
  </div>
</section>
"""
body = (body
  .replace("__CRUMB__", crumb(P, [(None, "작업물")]))
  .replace("__PFS__", "".join(pf(P, *x) for x in PORTFOLIO))
  .replace("__WORKS__", "".join(work(*w) for w in allworks)))
body += band(P, "이런 걸 원하셨나요?", "비슷한 느낌으로 원하시는 게 있으면 그 이야기부터 하시면 됩니다. 상담과 견적은 무료입니다.")

page("work/index.html",
     "작업물 — 업종별 화면 구조 예시 | 온도컴퍼니",
     "세이프클린ENG, 개묘한여행, 커리어 랩 등 실제로 배포된 사이트와 업종별 화면 구성 예시를 모아 두었습니다. 눌러서 바로 열어 보실 수 있습니다.",
     body, P, "work/")
print("work/index.html")

# ══════════════ 요금 ══════════════
def panel(pid, tabid, plans_html, note, hidden=False):
    h = " hidden" if hidden else ""
    return ('<div class="ppanel" role="tabpanel" id="' + pid + '" aria-labelledby="' + tabid + '"' + h + '>'
            '<div class="plans">' + plans_html + '</div>'
            '<div class="plan-note">' + note + '</div></div>')

WEB_PLANS = "".join([
 plan("베이직", "일단 주소부터 필요한 경우", "5", "~8만원",
      ["원페이지 3~4섹션", "모바일 반응형", "전화 바로걸기 버튼", "카톡 문의 버튼", "카톡 공유 미리보기", "배포 주소 + 소스", "무료 수정 1회"], "베이직 문의", K),
 plan("스탠다드", "손님을 실제로 받는 가게라면", "10", "~15만원",
      ["5~7섹션 · 베이직 전부 포함", "갤러리 · 메뉴 · 전후 비교", "네이버 지도 · 오시는 길", "사진 보정 · 웹 최적화", "검색 등록 기본 세팅", "무료 수정 1회"],
      "스탠다드 문의", K, best=True, tag="추천 구성"),
 plan("프리미엄", "페이지를 더 나눠야 하는 경우", "20", "만원~",
      ["스탠다드 전부 포함", "서브페이지 1~2개", "업종별 맞춤 기능 협의", "구성 상담 후 확정 견적", "무료 수정 2회"], "프리미엄 문의", K),
])
CLIP_PLANS = "".join([
 plan("숏폼 30초", "짧게 빠르게 알리고 싶을 때", "25", "만원 · 1편",
      ["AI 생성 세로 영상 1편 (30초 내외)", "시나리오 · 대사 작성", "연출 선택 (동물·아나운서·실사 등)",
       "자막 · 저작권 안전 배경음", "썸네일 1컷 · 업로드 문구 초안", "제작 전 이미지·대사 확인"],
      "30초 문의", K, was="30만원"),
 plan("숏폼 60초", "설명이 필요한 업종이라면", "60", "만원 · 1편",
      ["AI 생성 세로 영상 1편 (60초 내외)", "30초 구성 전부 포함", "장면 수 2배 · 구성 분기",
       "상세 시나리오 · 컷 구성표", "제작 전 이미지·대사 확인"],
      "60초 문의", K, best=True, tag="추천 구성", was="80만원"),
 plan("월 관리", "꾸준히 올려야 효과가 납니다", "90", "만원 · 월 4편",
      ["30초 세로 영상 4편 (편당 22만 5천원)", "30초 구성 전부 포함",
       "매달 주제 기획 · 대사 작성", "업로드 순서 · 문구 제안",
       "반응 보고 다음 편 방향 조정", "월 단위 해지 가능"],
      "월 관리 문의", K, was="100만원", note="월 단위 · 상담 후 확정"),
])
AI_PLANS = "".join([
 plan("결과물", "이력서에 넣을 결과물이 필요하다면", "8", "~12만원",
      ["주제 선정 상담", "작동하는 결과물 1개", "배포 주소 + 소스 전체", "구조 설명 문서", "무료 수정 2회"], "결과물 문의", K),
 plan("결과물 + 전략", "이력서·면접까지 정리하려면", "15", "~18만원",
      ["앞 구성 전부 포함", "이력서 문단 초안", "자기소개서 문단 초안", "면접 예상 질문 + 답변 뼈대", "공고 1건 맞춤 조정"],
      "결과물 + 전략 문의", K, best=True, tag="추천 구성"),
 plan("＋ 바이브코딩 강의", "다음 결과물은 직접 만들려면", "25", "만원~",
      ["앞 구성 전부 포함", "제작 강의 6강 (녹화 영상)", "실습용 예제 파일", "2주간 카톡 질문", "두 번째 결과물 점검 1회"], "강의 포함 문의", K),
])

_TAIL = (
 "<b>확정</b> · 표시 금액은 상담에서 구성을 확인한 뒤 확정합니다. 시작한 다음에 올리지 않습니다<br>"
 "<b>증빙</b> · 세금계산서·현금영수증이 필요하시면 문의 때 먼저 말씀해 주세요. 가능한 방법을 확인해서 알려 드립니다")
NOTE_COMMON = ("<b>수정</b> · 표기된 횟수 포함. 이후는 건당 1~2만원으로 안내드립니다<br>" + _TAIL)
NOTE_COMMON_CLIP = _TAIL

body = """
<section class="phead">
  <div class="wrap phead-in">
    __CRUMB__
    <p class="eyebrow rv">Price <span class="ko">상담 후 확정</span></p>
    <h1>가격은 처음에<br>다 말씀드립니다.</h1>
    <p class="phead-lede">작업 중에 늘어나는 비용이 없도록, 포함되는 것과 아닌 것을 미리 구분해 두었습니다.
      애매하면 상담에서 먼저 확정하고 시작합니다.</p>
    <div class="phead-btns">
      <a class="btn btn-kko btn-lg" href="__K__" target="_blank" rel="noopener">견적만 물어보기</a>
      <a class="btn btn-line btn-lg" href="../contact/">문의 남기기</a>
    </div>
  </div>
</section>

<section class="sec" id="s-price">
  <div class="wrap">
    <div class="ptabs" role="tablist" aria-label="서비스별 요금">
      <button class="ptab" role="tab" type="button" id="pt-web" aria-controls="pp-web" aria-selected="true" data-svc="web">온도 웹</button>
      <button class="ptab" role="tab" type="button" id="pt-clip" aria-controls="pp-clip" aria-selected="false" tabindex="-1" data-svc="clip">온도 클립</button>
      <button class="ptab" role="tab" type="button" id="pt-ai" aria-controls="pp-ai" aria-selected="false" tabindex="-1" data-svc="ai">온도 AI</button>
    </div>
    __PANELS__
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Compare <span class="ko">한눈에</span></p>
    <h2 class="rv">세 서비스 비교</h2>
    __CMP__
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">FAQ <span class="ko">요금 관련</span></p>
    <h2 class="rv">돈 이야기에서 자주 나오는 것</h2>
    __FAQ__
  </div>
</section>
"""

PANELS = (
 panel("pp-web", "pt-web", WEB_PLANS,
       "<b>옵션</b> · 커스텀 도메인 연결 +2~3만원 / 섹션 추가 건당 1~2만원 / 이메일 문의폼 연결 +1~2만원<br>"
       "<b>연락 방법</b> · 기본은 전화 바로걸기 + 카톡 문의 버튼입니다. 이메일 문의폼은 외부 무료 서비스를 연결하는 옵션입니다<br>"
       "<b>도메인</b> · 도메인 값은 본인 명의로 직접 구입하시고, 연결 작업만 받으시면 됩니다<br>" + NOTE_COMMON) +
 panel("pp-clip", "pt-clip", CLIP_PLANS,
       "<b>길이</b> · 30초·60초는 내외 기준입니다. 그보다 길면 별도로 견적을 내 드립니다<br>"
       "<b>월 관리</b> · 30초 4편 기준입니다. 60초는 포함되지 않으며 필요하실 때 건별로 추가합니다<br>"
       "<b>수정</b> · AI 영상은 수정이 곧 재제작이라 무료 수정이 없습니다. 대신 제작 전에 이미지와 대사를 확인받고 진행합니다<br>"
       "<b>촬영</b> · 촬영이 필요 없습니다. 화면은 AI로 만듭니다<br>"
       "<b>해지</b> · 월 관리는 월 단위로 해지하실 수 있고 위약금이 없습니다<br>" + NOTE_COMMON_CLIP, hidden=True) +
 panel("pp-ai", "pt-ai", AI_PLANS,
       "<b>AI 사용료</b> · 결과물에 들어가는 기능에 따라 별도 발생할 수 있습니다. 무료 범위 안에서 만드는 방법을 우선 안내드립니다<br>"
       "<b>강의</b> · 녹화 영상과 실습 자료를 링크로 드리고 질문은 2주간 카톡으로 받습니다<br>" + NOTE_COMMON, hidden=True)
)

body = (body
  .replace("__CRUMB__", crumb(P, [(None, "요금")]))
  .replace("__K__", K)
  .replace("__PANELS__", PANELS)
  .replace("__CMP__", cmp_table())
  .replace("__FAQ__", faq([
    ("왜 가격이 범위로 적혀 있나요?",
     "섹션 수, 사진 정리 분량, 기능 범위에 따라 달라지기 때문입니다. 상담에서 구성을 확인한 뒤 <b>금액을 확정하고 시작</b>합니다. 시작한 다음에 올리지 않습니다."),
    ("추가 비용이 생기는 경우는 언제인가요?",
     "① 무료 수정 횟수를 넘긴 수정, ② 처음 정한 범위 밖의 기능·섹션 추가, ③ 커스텀 도메인 연결, ④ 이메일 문의폼 연결, ⑤ 온도 AI에서 유료 AI 서비스가 필요한 경우입니다. 모두 <b>발생 전에 먼저 말씀드리고</b> 동의하시면 진행합니다."),
    ("계약금이나 선입금이 있나요?",
     "소액 작업은 완성 후 결제, 규모가 있는 작업은 절반씩 나누는 방식으로 진행합니다. 상담에서 편하신 쪽으로 정하시면 됩니다."),
    ("결제는 어떻게 하나요? 증빙은 되나요?",
     "크몽으로 오시면 크몽 결제 절차를 그대로 따르고, 카톡으로 직접 오시면 계좌 이체로 진행합니다. <b>세금계산서나 현금영수증이 필요하시면 문의하실 때 먼저 말씀해 주세요.</b> 발행 가능한 방법을 확인해서 알려 드리겠습니다. 확실하지 않은 것을 된다고 말씀드리지 않겠습니다."),
    ("월 유지비가 정말 없나요?",
     "온도 웹은 무료 호스팅에 올려 드려 <b>월 이용료가 0원</b>입니다. 커스텀 도메인을 쓰실 경우에만 도메인 값(연 1~2만원 수준)이 들고, 그건 본인 명의로 직접 결제하시는 편이 안전해서 대금에 포함하지 않습니다."),
  ])))
body += band(P, "우리 경우엔 얼마쯤일까요?", "상황만 알려 주시면 예상 금액과 일정을 바로 알려 드립니다. 견적만 받아 보셔도 됩니다.")

page("pricing/index.html",
     "요금 — 온도 웹 · 온도 클립 · 온도 AI 가격표 | 온도컴퍼니",
     "반응형 홈페이지 5만원부터, AI 홍보 영상 30초 25만원·60초 60만원, 취업용 AI 결과물 8만원부터. 포함 사항과 추가 비용을 미리 구분해 적어 두었습니다.",
     body, P, "pricing/")
print("pricing/index.html")
