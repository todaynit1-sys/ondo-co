# -*- coding: utf-8 -*-
from _build import *
from _frag import *
K = KAKAO
P = "../"

body = """
<section class="phead">
  <div class="wrap phead-in">
    __CRUMB__
    <p class="eyebrow rv">Service 01 <span class="ko">검색에 보이게</span></p>
    <h1><span class="en">Ondo Web</span>가게 이름을 쳤을 때<br>나올 자리를 만듭니다.</h1>
    <p class="phead-lede">네이버·구글에서 찾았을 때 <b>뭘 얼마에 어떻게 해주는지</b> 한 화면에 보이는 홈페이지.
      전부 스마트폰 기준으로 먼저 만들고, 완성되면 바로 열리는 주소로 올려 드립니다.</p>
    <dl class="phead-facts">
      <div class="phead-fact"><dt>시작 가격</dt><dd>5<small>만원~</small></dd></div>
      <div class="phead-fact"><dt>제작 기간</dt><dd>3~5<small>일</small></dd></div>
      <div class="phead-fact"><dt>무료 수정</dt><dd>2<small>회</small></dd></div>
      <div class="phead-fact"><dt>월 유지비</dt><dd>0<small>원</small></dd></div>
    </dl>
    <div class="phead-btns">
      <a class="btn btn-kko btn-lg" href="__K__" target="_blank" rel="noopener">카카오톡으로 상담하기</a>
      <a class="btn btn-line btn-lg" href="#price">요금 보기</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Problem <span class="ko">이런 상태라면</span></p>
    <h2 class="rv">홈페이지가 없으면<br>손님은 판단할 근거가 없습니다.</h2>
    <p class="lede rv">가격도, 시공 사례도, 영업시간도 물어봐야 알 수 있으면 대부분은 안 물어보고 다른 곳으로 갑니다.</p>
    <div class="spots">
      <div class="spot rv"><span class="spot-k">검색</span>
        <h3>플레이스에 리뷰 몇 줄이 전부다</h3>
        <p>지도 등록만으로는 우리가 어떤 일을 어떻게 하는지 보여줄 자리가 없습니다.</p></div>
      <div class="spot rv"><span class="spot-k">공유</span>
        <h3>보낼 링크가 없어서 말로 설명한다</h3>
        <p>카톡으로 주소 하나 보내면 끝날 설명을, 매번 사진 여러 장과 문장으로 반복합니다.</p></div>
      <div class="spot rv"><span class="spot-k">신뢰</span>
        <h3>블로그·인스타만 있으면 규모가 작아 보인다</h3>
        <p>특히 견적이 큰 업종일수록, 자기 주소가 있는 곳과 없는 곳의 첫인상이 갈립니다.</p></div>
    </div>
  </div>
</section>

<section class="sec sec-mist svc" id="what">
  <div class="wrap svc-grid">
    <div>
      <p class="eyebrow rv">What you get <span class="ko">받으시는 것</span></p>
      <h2 class="rv">파일이 아니라<br>열리는 주소를 드립니다.</h2>
      <p class="svc-desc rv">싸게 만들어 주는 곳은 많습니다. 그런데 받고 나면 “이걸 이제 어디에 올리죠?”가 남습니다.
        온도 웹은 인터넷에 올리는 것까지 끝내고 주소를 드립니다. 명함·전단지·인스타 프로필에 그대로 붙이시면 됩니다.</p>
      <ul class="svc-list rv">
        <li><span><b>모바일 우선 반응형</b> — 375px 기준으로 만들고 태블릿·PC까지 대응</span></li>
        <li><span><b>전화 바로걸기</b> — 모바일 화면 아래에 고정. 누르면 바로 통화</span></li>
        <li><span><b>카톡 채널 · 네이버 지도</b> — 문의와 길찾기를 한 번에</span></li>
        <li><span><b>문의폼</b> — 사장님 이메일로 바로 수신. 서버 관리 필요 없음</span></li>
        <li><span><b>카톡 공유 미리보기</b> — 링크 보냈을 때 제목·설명·이미지가 뜨게</span></li>
        <li><span><b>소스 파일 전체</b> — 나중에 다른 곳으로 옮기셔도 됩니다</span></li>
      </ul>
      <div class="svc-cta rv">
        <span class="svc-price">5만원~<small>3~5일</small></span>
        <a class="btn btn-sv" href="__K__" target="_blank" rel="noopener">카톡으로 상담하기</a>
      </div>
    </div>
    __PHONE__
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Work <span class="ko">실제로 만든 것</span></p>
    <h2 class="rv">지금 열리는 주소로 보여 드립니다</h2>
    <p class="lede rv">캡처가 아니라 실제로 배포된 사이트입니다. 눌러서 스마트폰으로도 확인해 보세요.</p>
    <div class="pfs">__PFS_WEB__</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Structure <span class="ko">업종별 구성</span></p>
    <h2 class="rv">같은 템플릿을 색만 바꿔 돌리지 않습니다</h2>
    <p class="lede rv">업종마다 손님이 먼저 확인하는 것이 다릅니다. 그래서 첫 화면부터 순서를 다르게 잡습니다.</p>
    <div class="works">__WORKS__</div>
    <p class="cmp-note rv" style="margin-top:26px">
      위 화면은 실제 고객 사이트가 아니라 구성 순서를 보여주는 예시입니다.
      <a href="../work/" style="color:var(--sv);font-weight:700">작업물 페이지에서 더 보기 →</a>
    </p>
  </div>
</section>

<section class="sec sec-mist" id="price">
  <div class="wrap">
    <p class="eyebrow rv">Price <span class="ko">부가세 별도</span></p>
    <h2 class="rv">가격은 처음에 다 말씀드립니다</h2>
    <p class="lede rv">작업 중에 늘어나는 비용이 없도록, 포함되는 것과 아닌 것을 미리 구분해 두었습니다.</p>
    <div class="plans" style="margin-top:38px">__PLANS__</div>
    <div class="plan-note rv">
      <b>옵션</b> · 커스텀 도메인 연결 +2~3만원 / 섹션 추가 건당 1~2만원 / 유지보수는 월 단위 별도 협의<br>
      <b>수정</b> · 표기된 횟수 포함. 이후는 건당 1~2만원으로 안내드립니다<br>
      <b>도메인</b> · 구입비는 별도이며 소유는 본인 명의로 등록해 드립니다<br>
      <b>묶음</b> · 온도 웹 + 온도 클립을 함께 하시면 클립 금액에서 10% 할인해 드립니다
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Process <span class="ko">문의부터 납품까지</span></p>
    <h2 class="rv">하실 일은 두 가지입니다</h2>
    <p class="lede rv">자료 보내주시고, 완성본 확인해 주시면 됩니다.</p>
    __STEPS__
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">FAQ <span class="ko">온도 웹</span></p>
    <h2 class="rv">홈페이지 관련해 자주 묻는 것</h2>
    __FAQ__
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Next <span class="ko">다른 서비스</span></p>
    <h2 class="rv">홈페이지가 아니라 다른 게 필요하시면</h2>
    <p class="lede rv">세 서비스는 각각 다른 일입니다. 홈페이지 없이 아래만 하셔도 됩니다.</p>
    __NEXTS__
  </div>
</section>
"""

PLANS = "".join([
 plan("베이직", "일단 주소부터 필요한 경우", "5", "~8만원",
      ["원페이지 3~4섹션 (히어로·소개·연락처)", "모바일 반응형", "전화 바로걸기 버튼",
       "카톡 공유 미리보기", "배포 주소 + 소스 파일", "무료 수정 2회"],
      "베이직 문의", K),
 plan("스탠다드", "손님을 실제로 받는 가게라면", "10", "~15만원",
      ["5~7섹션 · 베이직 전부 포함", "갤러리 · 메뉴 · 시공 전후 비교", "문의폼 (이메일 수신)",
       "네이버 지도 · 오시는 길", "사진 보정 · 웹 최적화", "무료 수정 2회"],
      "스탠다드 문의", K, best=True, tag="가장 많이 선택"),
 plan("프리미엄", "페이지를 더 나눠야 하는 경우", "20", "만원~",
      ["스탠다드 전부 포함", "서브페이지 1~2개", "커스텀 도메인 연결",
       "업종별 맞춤 기능 협의", "무료 수정 2회"],
      "프리미엄 문의", K),
])

body = (body
  .replace("__CRUMB__", crumb(P, [(None, "온도 웹")]))
  .replace("__K__", K)
  .replace("__PHONE__", PHONE_WEB)
  .replace("__PFS_WEB__", "".join(pf(P, *x) for x in PORTFOLIO if x[-2] == "web"))
  .replace("__WORKS__", "".join(work(*w) for w in WEB_WORKS))
  .replace("__PLANS__", PLANS)
  .replace("__NEXTS__", nexts(P, "web"))
  .replace("__STEPS__", steps([
     ("DAY 0", "문의 · 접수", "카톡으로 업종과 원하시는 느낌을 알려 주세요. 필요한 정보를 정리한 질문지를 보내 드립니다."),
     ("DAY 1–2", "시안 확인", "실제로 작동하는 주소로 시안을 보내 드립니다. 스마트폰에서 직접 눌러보실 수 있습니다."),
     ("DAY 3–4", "수정", "고칠 곳을 모아서 말씀해 주세요. 문구·사진·순서 모두 바꿀 수 있고 2회가 포함됩니다."),
     ("DAY 5", "배포 · 납품", "바로 열리는 주소와 소스 파일을 드립니다. 나중에 수정 맡기는 방법도 안내해 드립니다."),
  ]))
  .replace("__FAQ__", faq([
     ("정말 매달 내는 돈이 없나요?",
      "네. 사이트를 띄워 두는 비용은 <b>0원</b>입니다. 무료로 제공되는 공간에 올려 드리기 때문입니다. 다만 ‘우리가게이름.com’ 같은 개인 주소를 쓰고 싶으시면 그 주소 값(연 1~2만원 수준)만 사장님이 직접 결제하시면 됩니다."),
     ("온라인 결제나 예약 기능도 되나요?",
      "결제·회원가입·실시간 예약처럼 계속 서버 관리가 필요한 기능은 <b>이 서비스 범위 밖</b>입니다. 대신 카톡 문의 버튼, 문의폼, 구글폼 예약 링크를 연결해 드리는 방식으로 대부분 해결하고 계십니다. 필요하신 흐름을 말씀해 주시면 가능한 방법을 알려 드리겠습니다."),
     ("사진이 없는데 만들 수 있나요?",
      "가능합니다. 상업적으로 쓸 수 있는 무료 사진으로 먼저 채워 드리고, 나중에 가게 사진이 생기면 교체해 드립니다. 휴대폰으로 찍은 사진도 보정해서 씁니다."),
     ("참고하고 싶은 사이트가 있는데 그대로 만들어 주시나요?",
      "그대로 복사하지는 않습니다. 저작권 문제도 있고, 업종이 다르면 그 구성이 안 맞는 경우가 많습니다. 대신 색·구성·여백 감각을 분석해서 <b>사장님 업종에 맞게 새로 짭니다</b>. 어떤 점이 마음에 드셨는지만 말씀해 주세요."),
     ("만든 사이트는 제 것이 되나요?",
      "네. 완성된 소스 파일을 함께 드립니다. 나중에 다른 곳으로 옮기시거나 직접 고치셔도 됩니다."),
     ("수정은 몇 번까지 되나요?",
      "무료 수정 2회가 포함됩니다. 문구 교체, 사진 교체, 순서 변경 모두 가능합니다. 3회차부터는 건당 1~2만원 선으로 안내드립니다. <b>고칠 곳을 한 번에 모아서</b> 주시면 더 빠르게 끝납니다."),
  ])))

body += band(P, "우리 가게는 얼마쯤 나올까요?", "업종과 원하시는 구성만 알려 주시면 예상 금액과 일정을 바로 알려 드립니다.", "web")

LD = {"@context": "https://schema.org", "@type": "Service", "name": "온도 웹",
      "serviceType": "반응형 홈페이지 제작", "url": SITE + "web/",
      "provider": {"@type": "ProfessionalService", "name": "온도컴퍼니", "@id": SITE + "#org"},
      "areaServed": {"@type": "Country", "name": "대한민국"},
      "description": "소상공인을 위한 모바일 우선 반응형 홈페이지 제작. 전화 바로걸기·카톡 채널·네이버 지도·문의폼 포함, 배포된 주소까지 납품하고 월 호스팅비는 0원.",
      "offers": {"@type": "AggregateOffer", "priceCurrency": "KRW", "lowPrice": "50000", "highPrice": "200000"}}

page("web/index.html",
     "온도 웹 — 소상공인 반응형 홈페이지 제작 | 온도컴퍼니",
     "가게 이름을 검색했을 때 나올 자리를 만듭니다. 모바일 우선 반응형, 전화·카톡·지도·문의폼 기본 포함. 5만원부터, 3~5일, 배포 주소까지 납품하고 월 유지비 0원.",
     body, P, "web/", ld=LD, theme="t-web")
print("web/index.html")
