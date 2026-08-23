# -*- coding: utf-8 -*-
from _build import *
from _frag import *

K = KAKAO

# ══════════════════════════════════════════════════════════════
# 메인
# ══════════════════════════════════════════════════════════════
P = ""
body = """
<div class="notice" id="notice">
  <span>온도컴퍼니가 문을 열었습니다 · <b>상담과 견적은 무료입니다</b></span>
  <button class="notice-x" id="noticeX" type="button" aria-label="공지 닫기">×</button>
</div>

<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-grid">
      <div>
    <h1 class="ld ld1">보여야,<br><span class="grad">연락이 옵니다.</span></h1>
    <p class="hero-lede ld ld2">
      손님이든 인사담당자든, 찾아봤을 때 안 나오면 없는 겁니다.
      가게와 사람이 온라인에서 <b>보이게 만드는 일</b>, 온도컴퍼니가 하는 건 그거 하나입니다.
    </p>
    <div class="hero-btns ld ld3">
      <a class="btn btn-kko btn-lg" href="__K__" target="_blank" rel="noopener">카카오톡으로 3분 상담</a>
      <a class="btn btn-line btn-lg" href="pricing/">요금 먼저 보기</a>
    </div>
    <p class="hero-trust ld ld4">
      <span>5만원부터</span><span>영업일 2~7일</span><span>수정 포함</span><span>배포 주소까지 납품</span>
    </p>
      </div>

      <aside class="bp ld ld5" aria-label="브랜드 소개">
        <p class="bp-kicker">Brand · 이름의 뜻</p>
        <p class="bp-eq"><span class="on">ON</span><i>+</i><span class="do">DO</span></p>
        <p class="bp-mean"><b>온라인</b>에서 <b>되게</b> 만든다.<br>그래서 이름이 <b>온도(ONDO)</b>입니다.</p>
        <hr class="bp-hr">
        <p class="bp-title">온도컴퍼니는 <b>세 가지</b>를 합니다</p>
        <ul class="bp-list">
          <li data-svc="web"><span class="bp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M20.5 20.5l-5-5"/></svg></span><span><b>검색에 보이게</b><i>온도 웹 · 반응형 홈페이지</i></span></li>
          <li data-svc="clip"><span class="bp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2.5" width="12" height="19" rx="3.2"/><path d="M10.6 9.1l4.3 2.9-4.3 2.9z" fill="currentColor" stroke="none"/></svg></span><span><b>피드에 보이게</b><i>온도 클립 · AI 홍보 영상</i></span></li>
          <li data-svc="ai"><span class="bp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13.5 2.5H6.5a1.5 1.5 0 00-1.5 1.5v16a1.5 1.5 0 001.5 1.5h11a1.5 1.5 0 001.5-1.5V8z"/><path d="M13.5 2.5V8H19"/><path d="M8.8 15.1l2 2 4.4-4.4"/></svg></span><span><b>이력서에 보이게</b><i>온도 AI · 취업용 AI 결과물</i></span></li>
        </ul>
      </aside>
    </div>

    <div class="svcs-wrap ld ld6">
      <div class="svcs-rail" aria-hidden="true"></div>
      <p class="svcs-cap"><b>세 가지는 서로 다른 일입니다</b><span>필요한 것만 고르시면 됩니다</span></p>

      <div class="svcs">
        <a class="sc" data-svc="web" href="web/">
          <span class="sc-en">Ondo Web <i>Search</i></span>
          <h2>온도 웹</h2>
          <p class="sc-role">검색에 보이게 · 반응형 홈페이지</p>
          <p class="sc-desc">가게 이름이나 “동네+업종”으로 검색했을 때 나올 자리를 만듭니다. 스마트폰 기준으로 먼저 만듭니다.</p>
          <ul class="sc-chips"><li>반응형 5~7섹션</li><li>전화 바로걸기</li><li>카톡 문의</li><li>네이버 지도</li><li>갤러리</li></ul>
          <dl class="sc-meta">
            <div><dt>시작 가격</dt><dd>5<small>만원~</small></dd></div>
            <div><dt>제작 기간</dt><dd>3~5<small>일</small></dd></div>
          </dl>
          <span class="sc-go">온도 웹 자세히 보기 →</span>
        </a>

        <a class="sc" data-svc="clip" href="clip/">
          <span class="sc-en">Ondo Clip <i>Feed</i></span>
          <h2>온도 클립</h2>
          <p class="sc-role">피드에 보이게 · AI 홍보 영상</p>
          <p class="sc-desc">촬영이 필요 없습니다. 알리고 싶은 내용만 주시면 AI로 화면과 목소리를 만들어 세로 영상으로 완성합니다.</p>
          <ul class="sc-chips"><li>촬영 없음</li><li>동물·아나운서 연출</li><li>시나리오·대사</li><li>자막·배경음</li><li>썸네일</li></ul>
          <dl class="sc-meta">
            <div><dt>30초 1편</dt><dd>25<small>만원~</small></dd></div>
            <div><dt>제작 기간</dt><dd>2~5<small>일</small></dd></div>
          </dl>
          <span class="sc-go">온도 클립 자세히 보기 →</span>
        </a>

        <a class="sc" data-svc="ai" href="ai/">
          <span class="sc-en">Ondo AI <i>Career</i></span>
          <h2>온도 AI</h2>
          <p class="sc-role">이력서에 보이게 · 취업용 AI 결과물</p>
          <p class="sc-desc">지원 직무에 맞는 AI 결과물을 함께 만들고, 이력서·면접에 어떻게 넣을지까지 정리해 드립니다.</p>
          <ul class="sc-chips"><li>작동하는 결과물</li><li>배포 주소·소스</li><li>이력서 반영 전략</li><li>면접 예상 질문</li><li>바이브코딩 강의</li></ul>
          <dl class="sc-meta">
            <div><dt>시작 가격</dt><dd>8<small>만원~</small></dd></div>
            <div><dt>제작 기간</dt><dd>3~7<small>일</small></dd></div>
          </dl>
          <span class="sc-go">온도 AI 자세히 보기 →</span>
        </a>
      </div>

      <p class="svcs-note">홈페이지만, 영상만, 결과물만 하셔도 됩니다. 어느 쪽인지 모르겠으면 상황만 <a href="__K__" target="_blank" rel="noopener" style="color:var(--web);font-weight:700">카톡으로 알려 주세요</a>. 필요 없으면 필요 없다고 말씀드립니다.</p>
    </div>
  </div>
</section>

<section class="sec sec-mist" id="why">
  <div class="wrap">
    <p class="eyebrow rv">Why <span class="ko">지금 이런 상태라면</span></p>
    <h2 class="rv">사람들이 나를 만나는 자리는<br>세 군데뿐입니다.</h2>
    <p class="lede rv">그 세 자리 중에 비어 있는 곳이 있다면, 그만큼의 기회를 놓치고 있는 겁니다.</p>
    <div class="spots">
      <div class="spot rv"><span class="spot-k">검색</span>
        <h3>“동네 이름 + 업종”으로 검색해도 우리 가게가 안 나온다</h3>
        <p>플레이스 등록만으로는 리뷰 몇 줄이 전부입니다. 뭘 얼마에 어떻게 해주는지 보여줄 자리가 없습니다.</p></div>
      <div class="spot rv"><span class="spot-k">피드</span>
        <h3>스크롤하는 사람에게 우리 가게가 스쳐 지나간 적이 없다</h3>
        <p>검색은 이미 우리를 아는 사람만 합니다. 모르는 사람에게 닿는 통로는 짧은 영상인데, 찍을 여건이 안 됩니다.</p></div>
      <div class="spot rv"><span class="spot-k">이력서</span>
        <h3>지원할 회사는 정했는데, 보여줄 결과물이 없다</h3>
        <p>자격증과 학점은 다들 비슷합니다. 실제로 만들어서 돌아가는 것 하나가 면접의 화제를 바꿉니다.</p></div>
    </div>
    <p class="spots-after rv">세 서비스는 이 세 자리에 하나씩 대응합니다.<br><em>필요한 자리 하나만 채우셔도 됩니다.</em></p>
  </div>
</section>

<section class="sec svc" id="s-web">
  <div class="wrap svc-grid">
    <div>
      <p class="eyebrow rv">Service 01</p>
      <h2 class="rv"><span class="en">Ondo Web</span>온도 웹</h2>
      <p class="svc-role rv">검색에 보이게 — 반응형 홈페이지</p>
      <p class="svc-desc rv">손님이 가게 이름이나 “동네+업종”으로 검색했을 때 나오는 자리를 만듭니다. 전부 스마트폰 화면 기준으로 먼저 설계하고, 태블릿·PC는 그다음입니다. 완성되면 바로 쓸 수 있는 주소로 올려 드리고 소스 전체도 함께 드립니다.</p>
      <ul class="svc-list rv">
        <li><span><b>모바일 우선 반응형</b> — 375px 기준으로 만들고 데스크톱까지 대응</span></li>
        <li><span><b>한국형 필수 요소</b> — 전화 바로걸기, 카톡 채널, 네이버 지도, 사업자 정보</span></li>
        <li><span><b>카톡 문의 버튼</b> — 누르면 바로 대화창. 관리할 계정이 늘지 않습니다</span></li>
        <li><span><b>카톡 공유 미리보기</b> — 링크 보냈을 때 제목·설명·이미지가 뜨게</span></li>
      </ul>
      <div class="svc-cta rv">
        <span class="svc-price">5만원~<small>3~5일</small></span>
        <a class="btn btn-sv" href="web/">온도 웹 자세히 보기</a>
        <a class="btn btn-line" href="__K__" target="_blank" rel="noopener">카톡 상담</a>
      </div>
    </div>
    __PHONE__
  </div>
</section>

<section class="sec sec-mist svc s-clip rev" id="s-clip">
  <div class="wrap svc-grid">
    <div>
      <p class="eyebrow rv">Service 02</p>
      <h2 class="rv"><span class="en">Ondo Clip</span>온도 클립</h2>
      <p class="svc-role rv">피드에 보이게 — AI 홍보 영상</p>
      <p class="svc-desc rv">검색은 우리를 이미 아는 사람만 합니다. 모르는 사람에게 닿으려면 그 사람이 넘기던 화면에 우리가 끼어들어야 합니다. 그런데 찍을 시간이 없습니다. 그래서 <b>촬영 없이 AI로</b> 만듭니다.</p>
      <ul class="svc-list rv">
        <li><span><b>촬영이 필요 없습니다</b> — 알리고 싶은 내용만 주시면 됩니다</span></li>
        <li><span><b>연출을 고르실 수 있습니다</b> — 동물 캐릭터, AI 아나운서, 실사, 일러스트</span></li>
        <li><span><b>시나리오 · 대사부터 씁니다</b> — 만들기 전에 이미지와 대사를 확인받습니다</span></li>
        <li><span><b>자막 · 배경음 · 썸네일</b> — 올릴 수 있는 상태로 드립니다</span></li>
      </ul>
      <div class="svc-cta rv">
        <span class="svc-price">30초 25만원~<small>2~5일</small></span>
        <a class="btn btn-sv" href="clip/">온도 클립 자세히 보기</a>
        <a class="btn btn-line" href="__K__" target="_blank" rel="noopener">카톡 상담</a>
      </div>
    </div>
    __CLIPS__
  </div>
</section>

<section class="sec svc s-ai" id="s-ai">
  <div class="wrap svc-grid">
    <div>
      <p class="eyebrow rv">Service 03</p>
      <h2 class="rv"><span class="en">Ondo AI</span>온도 AI</h2>
      <p class="svc-role rv">이력서에 보이게 — 취업용 AI 결과물</p>
      <p class="svc-desc rv">지원하려는 직무에 맞는 AI 결과물을 실제로 작동하는 형태로 만들어 드립니다. 만든 다음이 더 중요해서, 이력서·자기소개서·면접에 어떻게 넣을지까지 함께 정리합니다. 직접 만들고 싶으신 분께는 제작 방법을 강의로 드립니다.</p>
      <ul class="svc-list rv">
        <li><span><b>작동하는 결과물</b> — 배포 주소, 소스, 설명 문서 한 세트</span></li>
        <li><span><b>이력서 반영 전략</b> — 이력서·자소서에 그대로 옮길 문단까지</span></li>
        <li><span><b>면접 대비</b> — 예상 질문과 설명 시나리오</span></li>
        <li><span><b>바이브코딩 강의</b> — 다음 결과물은 직접 만드실 수 있게</span></li>
      </ul>
      <div class="svc-cta rv">
        <span class="svc-price">8만원~<small>3~7일</small></span>
        <a class="btn btn-sv" href="ai/">온도 AI 자세히 보기</a>
        <a class="btn btn-line" href="__K__" target="_blank" rel="noopener">카톡 상담</a>
      </div>
    </div>
    __AICARD__
  </div>
</section>

<section class="sec sec-mist" id="s-cmp">
  <div class="wrap">
    <p class="eyebrow rv">Compare <span class="ko">뭘 고를까</span></p>
    <h2 class="rv">필요한 것만 고르시면 됩니다</h2>
    <p class="lede rv">세 가지는 순서대로 밟는 단계가 아닙니다. 홈페이지만, 영상만, 결과물만 하셔도 됩니다. 아래에서 본인에 해당하는 칸을 보세요.</p>
    __CMP__
    <p class="cmp-note rv">세 가지를 묶어서 파는 상품이 아닙니다. 하나만 하셔도 되고, 나중에 다른 걸 추가하셔도 됩니다. 고민되시면 상황만 카톡으로 알려 주세요.</p>
  </div>
</section>

<section class="sec" id="s-work">
  <div class="wrap">
    <p class="eyebrow rv">Work <span class="ko">실제로 만든 것</span></p>
    <h2 class="rv">말보다 눌러 보시는 게 빠릅니다</h2>
    <p class="lede rv">아래는 실제로 배포되어 지금 열리는 사이트입니다. 카드를 누르면 새 창으로 바로 열립니다.</p>
    <div class="pfs">__PFS__</div>
    <p class="cmp-note rv" style="margin-top:26px">
      업종별로 화면 구조를 어떻게 다르게 잡는지도 정리해 두었습니다.
      <a href="work/" style="color:var(--web);font-weight:700">작업물 전체 보기 →</a>
    </p>
  </div>
</section>

<section class="sec sec-mist" id="s-process">
  <div class="wrap">
    <p class="eyebrow rv">Process <span class="ko">문의부터 납품까지</span></p>
    <h2 class="rv">하실 일은<br>자료 보내주시는 것 하나입니다.</h2>
    <p class="lede rv">나머지는 저희가 합니다. 진행 상황은 카톡으로 그때그때 알려 드립니다. (온도 웹 기준 · 클립 2~5일 · AI 3~7일)</p>
    __STEPS__
  </div>
</section>

<section class="sec" id="s-faq">
  <div class="wrap">
    <p class="eyebrow rv">FAQ <span class="ko">자주 묻는 것</span></p>
    <h2 class="rv">먼저 물어보시는 것들</h2>
    __FAQ__
    <p class="cmp-note rv" style="margin-top:22px">여기 없는 게 궁금하시면 <a href="__K__" target="_blank" rel="noopener" style="color:var(--web);font-weight:700">카톡으로 물어봐 주세요</a>.</p>
  </div>
</section>
"""

body = (body
    .replace("__K__", K)
    .replace("__PHONE__", PHONE_WEB)
    .replace("__CLIPS__", CLIPS)
    .replace("__AICARD__", AICARD)
    .replace("__CMP__", cmp_table())
    .replace("__PFS__", "".join(pf(P, *x) for x in PORTFOLIO))
    .replace("__STEPS__", steps([
        ("DAY 0", "문의 · 접수", "카톡으로 편하게 연락 주세요. 필요한 정보를 정리한 질문지를 보내 드립니다. 자료는 있는 그대로 보내주시면 됩니다."),
        ("DAY 1–2", "시안 확인", "실제로 작동하는 주소로 시안을 보내 드립니다. 캡처가 아니라 스마트폰에서 직접 눌러보실 수 있습니다."),
        ("DAY 3–4", "수정", "고치고 싶은 부분을 말씀해 주세요. 기본 2회 수정이 포함되어 있고 문구·사진·순서 모두 바꿀 수 있습니다."),
        ("DAY 5", "배포 · 납품", "바로 쓸 수 있는 주소로 올려 드립니다. 소스 파일 전체와 함께, 나중에 수정 맡기는 방법도 안내해 드립니다."),
    ]))
    .replace("__FAQ__", faq([
        ("세 가지 중에 뭘 골라야 할까요?",
         "순서가 정해져 있지 않습니다. <b>필요한 것만</b> 고르시면 됩니다. 검색했을 때 나올 자리가 필요하면 <b>온도 웹</b>, 촬영 없이 홍보 영상을 만들고 싶으면 <b>온도 클립</b>, 취업·이직에 쓸 결과물이 필요하면 <b>온도 AI</b>입니다. 세 개가 서로를 필요로 하지 않으니, 하나만 하셔도 아무 문제 없습니다."),
        ("사진도 없고 글도 못 쓰는데 괜찮을까요?",
         "괜찮습니다. 업종과 강점 세 가지만 말씀해 주시면 소개 문구 초안을 써서 먼저 보여 드립니다. 마음에 안 드시면 그대로 고쳐 드립니다. 사진이 없으면 무료 이미지로 채우고 나중에 실제 사진이 생기면 교체해 드립니다. 영상도 촬영 없이 AI로 만들기 때문에 찍어둔 소재가 없어도 됩니다."),
        ("네이버나 구글 검색에 바로 나오나요?",
         "검색 등록에 필요한 기본 설정(제목·설명·구조화 데이터·공유 미리보기·검색엔진 제출)은 전부 해 드립니다. 다만 <b>검색 순위 상위 노출은 보장하지 않습니다.</b> 그건 광고비와 시간이 함께 필요한 영역이라, 확실하지 않은 것을 확실하다고 말씀드리지 않겠습니다."),
        ("주소는 어떻게 되나요? 매달 내는 돈이 있나요?",
         "기본은 무료 호스팅 주소로 드립니다. 월 이용료가 없습니다. ‘우리가게이름.com’ 같은 주소를 원하시면 도메인을 본인 명의로 구입하신 뒤(연 1~2만원 수준) 연결해 드립니다. 연결 작업은 2~3만원입니다."),
        ("만든 다음에 제가 직접 고칠 수 있나요?",
         "홈페이지는 직접 고치는 관리자 화면이 기본 상품에 없습니다. 대신 수정할 내용을 카톡으로 보내 주시면 반영해 드립니다. 베이직·스탠다드는 무료 수정 <b>1회</b>, 프리미엄은 2회가 포함됩니다. 이후는 건당 1~2만원이며, 자주 바꾸셔야 하면 월 유지보수가 저렴합니다."),
        ("결제는 어떻게 하나요? 증빙은 되나요?",
         "크몽으로 오시면 크몽 결제 절차를 그대로 따르고, 카톡으로 직접 오시면 계좌 이체로 진행합니다. <b>세금계산서나 현금영수증이 필요하시면 문의하실 때 먼저 말씀해 주세요.</b> 발행 가능한 방법을 확인해서 알려 드리겠습니다. 확실하지 않은 것을 된다고 말씀드리지 않겠습니다."),
    ])))

body += band(P, "지금 물어보세요", "견적만 물어보셔도 됩니다. 업종이나 상황만 알려 주시면 예상 금액과 일정을 바로 알려 드립니다.")

LD_ORG = {
 "@context": "https://schema.org",
 "@graph": [
  {"@type": "ProfessionalService", "@id": SITE + "#org", "name": "온도컴퍼니",
   "alternateName": ["ONDO", "ONDO Company", "온도"],
   "slogan": "온라인에 온도를 더합니다",
   "description": "소규모 사업자와 취업 준비생을 위해 반응형 홈페이지, AI 홍보 영상, 취업용 AI 결과물을 제작하는 온라인 제작소.",
   "url": SITE, "priceRange": "₩₩",
   "areaServed": {"@type": "Country", "name": "대한민국"},
   "knowsAbout": ["홈페이지 제작", "반응형 웹", "랜딩페이지", "AI 홍보 영상", "숏폼 영상", "취업 포트폴리오", "바이브코딩", "AI 웹앱 제작"],
   "sameAs": [KAKAO],
   "makesOffer": [
     {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "온도 웹", "serviceType": "반응형 홈페이지 제작", "url": SITE + "web/"}, "priceCurrency": "KRW", "price": "50000"},
     {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "온도 클립", "serviceType": "AI 홍보 영상 제작", "url": SITE + "clip/"}, "priceCurrency": "KRW", "price": "250000"},
     {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "온도 AI", "serviceType": "취업용 AI 결과물 제작 및 제작 강의", "url": SITE + "ai/"}, "priceCurrency": "KRW", "price": "80000"}
   ]},
  {"@type": "WebSite", "@id": SITE + "#site", "url": SITE, "name": "온도컴퍼니", "inLanguage": "ko-KR",
   "publisher": {"@id": SITE + "#org"}}
 ]}

page("index.html",
     "온도컴퍼니 ONDO° — 홈페이지 · AI 홍보 영상 · 취업용 AI 결과물",
     "보여야 연락이 옵니다. 반응형 홈페이지(온도 웹), 촬영 없이 만드는 AI 홍보 영상(온도 클립), 취업용 AI 결과물(온도 AI). 상담과 견적은 무료입니다.",
     body, P, None, ld=LD_ORG, canon="")
print("index.html")
