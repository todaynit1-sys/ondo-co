# -*- coding: utf-8 -*-
from _build import *
from _frag import *
K = KAKAO
P = "../"

body = """
<section class="phead">
  <div class="wrap phead-in">
    __CRUMB__
    <p class="eyebrow rv">Service 03 <span class="ko">이력서에 보이게</span></p>
    <h1><span class="en">Ondo AI</span>이력서에 쓸 게 없다면,<br>만들면 됩니다.</h1>
    <p class="phead-lede">자격증과 학점은 다들 비슷합니다. 실제로 <b>만들어서 돌아가는 것 하나</b>가 면접의 화제를 바꿉니다.
      지원하려는 직무에 맞는 AI 결과물을 함께 만들고, 그걸 이력서·면접에 어떻게 넣을지까지 정리해 드립니다.</p>
    <dl class="phead-facts">
      <div class="phead-fact"><dt>시작 가격</dt><dd>8<small>만원~</small></dd></div>
      <div class="phead-fact"><dt>제작 기간</dt><dd>3~7<small>일</small></dd></div>
      <div class="phead-fact"><dt>구성</dt><dd>3<small>단계</small></dd></div>
      <div class="phead-fact"><dt>납품</dt><dd>URL<small>+ 소스</small></dd></div>
    </dl>
    <div class="phead-btns">
      <a class="btn btn-kko btn-lg" href="__K__" target="_blank" rel="noopener">카카오톡으로 상담하기</a>
      <a class="btn btn-line btn-lg" href="#track">3단계 구성 보기</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Problem <span class="ko">이런 상태라면</span></p>
    <h2 class="rv">막힌 지점은 셋 중 하나입니다</h2>
    <p class="lede rv">셋 다 “실력이 없어서”가 아니라 “꺼내 놓은 게 없어서” 생기는 문제입니다.</p>
    <div class="spots">
      <div class="spot rv"><span class="spot-k">결과물</span>
        <h3>포트폴리오에 넣을 게 과제밖에 없다</h3>
        <p>수업 과제는 다들 냅니다. 지원하는 회사의 일과 닿아 있는 결과물이 하나라도 있으면 이야기가 달라집니다.</p></div>
      <div class="spot rv"><span class="spot-k">설명</span>
        <h3>만들긴 했는데 면접에서 설명이 안 된다</h3>
        <p>“어떻게 만드셨어요?”에서 막히면 오히려 감점입니다. 만드는 것보다 설명이 더 중요합니다.</p></div>
      <div class="spot rv"><span class="spot-k">주제</span>
        <h3>뭘 만들어야 할지부터 모르겠다</h3>
        <p>기술을 고르는 게 아니라 <b>문제를 고르는 일</b>입니다. 지원 직무에서 실제로 반복되는 일을 찾는 것부터 같이 합니다.</p></div>
    </div>
  </div>
</section>

<section class="sec sec-mist" id="track">
  <div class="wrap">
    <p class="eyebrow rv">Track <span class="ko">3단계 구성</span></p>
    <h2 class="rv">결과물만, 전략까지,<br>아니면 만드는 법까지.</h2>
    <p class="lede rv">필요한 만큼만 고르시면 됩니다. 아래로 갈수록 앞 단계를 전부 포함합니다.</p>
    __TRACK__
    <div class="note-box rv">
      <b>대신 만들어 주고 끝내지 않습니다.</b> 결과물은 함께 만들고, 어떤 구조로 되어 있는지 · 왜 그렇게 만들었는지를
      문서와 설명으로 넘겨 드립니다. 면접에서 본인이 설명하지 못하면 결과물이 있어도 소용이 없기 때문입니다.
      없는 경력이나 하지 않은 일을 지어내지 않으며, 결과물의 제작 방식에 대해 사실과 다르게 말씀드리라고 권하지 않습니다.
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Output <span class="ko">어떤 걸 만드나</span></p>
    <h2 class="rv">지원하는 직무에서 실제로 반복되는 일</h2>
    <p class="lede rv">화려한 기술을 쓰는 것보다, 그 회사 사람이 보고 “이거 우리 일인데”라고 느끼는 게 훨씬 셉니다. 아래는 방향 예시입니다.</p>
    <div class="outs">
      <div class="out rv"><span class="out-k">Marketing</span><h3>광고 문구 생성·비교 도구</h3><p>제품 정보를 넣으면 톤이 다른 카피 여러 개를 만들고, 어느 쪽이 왜 나은지 기준을 같이 보여 주는 화면.</p></div>
      <div class="out rv"><span class="out-k">Office</span><h3>반복 문서 자동 작성기</h3><p>매번 손으로 채우던 보고서·회의록 양식을 항목만 입력하면 문장으로 채워 주는 도구.</p></div>
      <div class="out rv"><span class="out-k">Data</span><h3>엑셀 올리면 요약해 주는 대시보드</h3><p>CSV를 올리면 자동으로 집계·차트·이상값을 표시해 주는 한 페이지 대시보드.</p></div>
      <div class="out rv"><span class="out-k">Service</span><h3>고객 문의 분류·응대 초안</h3><p>문의 내용을 붙여넣으면 유형을 나누고 답변 초안을 만들어 주는 상담 보조 화면.</p></div>
      <div class="out rv"><span class="out-k">Quality</span><h3>현장 점검 체크리스트 앱</h3><p>점검 항목을 스마트폰에서 체크하면 결과가 정리되고 미흡 항목만 뽑아 주는 도구.</p></div>
      <div class="out rv"><span class="out-k">Personal</span><h3>경력·프로젝트 정리 웹앱</h3><p>흩어진 경력과 성과를 넣으면 실적 중심으로 다시 정리해 링크 하나로 공유하는 개인 페이지.</p></div>
    </div>
    <p class="cmp-note rv" style="margin-top:26px">주제는 상담에서 함께 정합니다. 지원하려는 회사·직무·공고를 보여 주시면 그 안에서 찾습니다.</p>
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Work <span class="ko">실제 결과물</span></p>
    <h2 class="rv">이런 게 나옵니다</h2>
    <p class="lede rv">설명보다 직접 눌러 보시는 게 빠릅니다. 아래는 바이브코딩으로 만들어 실제로 배포한 웹앱입니다.</p>
    <div class="pfs">__PFS_AI__</div>
    <p class="cmp-note rv" style="margin-top:24px">
      두 개 모두 화면 여러 개와 외부 데이터 연동이 들어간 결과물입니다. 이 정도가 이력서에 링크로 들어갑니다.
      <a href="../work/" style="color:var(--sv);font-weight:700">작업물 전체 보기 →</a>
    </p>
  </div>
</section>

<section class="sec sec-mist svc" id="strategy">
  <div class="wrap svc-grid">
    <div>
      <p class="eyebrow rv">Strategy <span class="ko">이력서 반영</span></p>
      <h2 class="rv">만든 다음이<br>더 중요합니다.</h2>
      <p class="svc-desc rv">결과물이 있어도 이력서에 한 줄로 적어 놓으면 아무도 안 봅니다.
        무엇을 왜 만들었고 무엇이 달라졌는지를 <b>읽는 사람 기준</b>으로 다시 씁니다.
        STEP 02부터 아래가 포함됩니다.</p>
      <ul class="svc-list rv">
        <li><span><b>프로젝트 한 줄 정의</b> — 이력서 맨 앞에 들어갈 문장</span></li>
        <li><span><b>이력서 문단</b> — 역할 · 사용 기술 · 만든 결과 순서로 정리</span></li>
        <li><span><b>자기소개서 문단</b> — 지원 동기와 연결되는 형태로</span></li>
        <li><span><b>면접 예상 질문과 답변 뼈대</b> — “왜 그렇게 만들었나요”에 답할 수 있게</span></li>
        <li><span><b>공고별 맞춤 조정</b> — 공고를 주시면 강조할 부분을 바꿔 드립니다</span></li>
      </ul>
      <div class="svc-cta rv">
        <span class="svc-price">STEP 02부터<small>15만원~</small></span>
        <a class="btn btn-sv" href="__K__" target="_blank" rel="noopener">카톡으로 상담하기</a>
      </div>
    </div>
    __AICARD__
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Course <span class="ko">STEP 03 포함</span></p>
    <h2 class="rv">다음 결과물은 직접 만드실 수 있게</h2>
    <p class="lede rv">한 번 만들어 드리는 것보다, 만드는 방법을 아시는 편이 오래갑니다.
      코딩을 처음 하시는 분 기준으로 만든 영상 강의입니다. 보고 따라 하면 본인 결과물이 하나 더 생기는 구성입니다.</p>
    <div class="curri">
      <div class="cu rv"><span class="cu-n">1강</span><div><h3>무엇을 만들지 고르기</h3><p>기술이 아니라 문제를 고릅니다. 지원 직무에서 반복되는 일을 찾아 한 문장으로 정의하는 방법.</p></div></div>
      <div class="cu rv"><span class="cu-n">2강</span><div><h3>AI에게 제대로 시키는 법</h3><p>“만들어 줘”가 아니라 무엇을 어떤 순서로 요청해야 하는지. 요구사항을 쪼개는 연습.</p></div></div>
      <div class="cu rv"><span class="cu-n">3강</span><div><h3>작동하는 첫 화면까지</h3><p>설치와 설정에서 막히지 않게. 브라우저에서 바로 열리는 화면 하나를 완성합니다.</p></div></div>
      <div class="cu rv"><span class="cu-n">4강</span><div><h3>기능 붙이기</h3><p>입력 저장, 계산, 화면 전환. 안 될 때 오류 메시지를 읽고 고치는 방법까지 같이 다룹니다.</p></div></div>
      <div class="cu rv"><span class="cu-n">5강</span><div><h3>인터넷에 올리기</h3><p>주소가 생기는 순간입니다. 무료로 배포하고 이력서에 링크로 넣는 방법.</p></div></div>
      <div class="cu rv"><span class="cu-n">6강</span><div><h3>설명할 수 있게 만들기</h3><p>구조 문서 작성과 면접 답변 정리. “어떻게 만드셨어요?”에 막히지 않기 위한 마지막 단계.</p></div></div>
    </div>
    <div class="note-box rv">
      <b>수강 방식</b> · 녹화 영상과 실습 자료를 링크로 드리고, 질문은 카톡으로 <b>2주간</b> 받습니다.
      실시간 강의가 아니라 언제든 보실 수 있는 형태입니다. 강의 분량과 공개 시점은 상담 때 정확히 안내드립니다.
    </div>
    <div class="note-box rv">
      <b>비용 관련 안내</b> · AI 기능이 들어가는 결과물은 서비스에 따라 사용료가 별도로 발생할 수 있습니다.
      무료 범위 안에서 만드는 방법을 우선 안내드리고, 유료가 필요한 경우 얼마쯤 드는지 미리 말씀드립니다.
    </div>
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Process <span class="ko">문의부터 납품까지</span></p>
    <h2 class="rv">지원 공고 하나만 있으면 시작됩니다</h2>
    __STEPS__
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">FAQ <span class="ko">온도 AI</span></p>
    <h2 class="rv">가장 많이 묻는 것</h2>
    __FAQ__
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Next <span class="ko">다른 서비스</span></p>
    <h2 class="rv">취업이 아니라 다른 게 필요하시면</h2>
    <p class="lede rv">세 서비스는 각각 다른 일입니다. 가게를 알리는 쪽은 아래입니다.</p>
    __NEXTS__
  </div>
</section>
"""

TRACK = """<div class="track">
  <div class="tr rv">
    <span class="tr-step">결과물</span>
    <h3>취업용 AI 결과물 제작</h3>
    <p>지원 직무에 맞는 주제를 함께 정하고, 실제로 작동하는 결과물 한 개를 만들어 배포까지 끝냅니다.</p>
    <ul>
      <li><span><b>주제 선정 상담</b> — 공고·직무 기준으로 함께 결정</span></li>
      <li><span><b>작동하는 결과물 1개</b> — 데모가 아니라 실제로 열리는 것</span></li>
      <li><span><b>배포 주소</b> — 이력서에 링크로 넣을 수 있는 형태</span></li>
      <li><span><b>소스 파일 전체</b> — 이후 직접 손보셔도 됩니다</span></li>
      <li><span><b>구조 설명 문서</b> — 어떤 구조인지 본인이 설명할 수 있게</span></li>
    </ul>
    <div class="tr-foot">
      <p class="tr-price">8<small>~12만원</small></p>
      <p class="tr-when">3~4일 · 무료 수정 2회</p>
      <a class="btn btn-line" href="__K__" target="_blank" rel="noopener">이 구성으로 문의</a>
    </div>
  </div>

  <div class="tr rv tr-best">
    <span class="tr-step">＋ 전략</span>
    <h3>결과물 + 이력서 반영 전략</h3>
    <p>만든 결과물을 이력서·자기소개서·면접 답변으로 옮겨 적을 수 있는 형태까지 정리해 드립니다.</p>
    <ul>
      <li><span><b>앞 단계 전부 포함</b></span></li>
      <li><span><b>이력서 문단 초안</b> — 역할·기술·결과 순서로</span></li>
      <li><span><b>자기소개서 문단 초안</b> — 지원 동기와 연결</span></li>
      <li><span><b>면접 예상 질문 + 답변 뼈대</b></span></li>
      <li><span><b>공고 1건 맞춤 조정</b> — 강조점을 그 공고에 맞게</span></li>
    </ul>
    <div class="tr-foot">
      <p class="tr-price">15<small>~18만원</small></p>
      <p class="tr-when">4~6일 · 무료 수정 2회</p>
      <a class="btn btn-sv" href="__K__" target="_blank" rel="noopener">이 구성으로 문의</a>
    </div>
  </div>

  <div class="tr rv">
    <span class="tr-step">＋ 강의</span>
    <h3>결과물 + 전략 + 바이브코딩 강의</h3>
    <p>다음 결과물은 직접 만드실 수 있도록, 제작 방법을 영상 강의로 함께 드립니다.</p>
    <ul>
      <li><span><b>앞 단계 전부 포함</b></span></li>
      <li><span><b>바이브코딩 제작 강의 6강</b> — 녹화 영상 + 실습 자료</span></li>
      <li><span><b>실습용 예제 파일</b> — 보면서 따라 만들 수 있게</span></li>
      <li><span><b>2주간 카톡 질문</b> — 막히는 지점 그때그때</span></li>
      <li><span><b>두 번째 결과물 점검 1회</b> — 직접 만드신 것 피드백</span></li>
    </ul>
    <div class="tr-foot">
      <p class="tr-price">25<small>만원~</small></p>
      <p class="tr-when">5~7일 · 무료 수정 2회</p>
      <a class="btn btn-line" href="__K__" target="_blank" rel="noopener">이 구성으로 문의</a>
    </div>
  </div>
</div>"""

body = (body
  .replace("__CRUMB__", crumb(P, [(None, "온도 AI")]))
  .replace("__TRACK__", TRACK)
  .replace("__PFS_AI__", "".join(pf(P, *x) for x in PORTFOLIO if x[-2] == "ai"))
  .replace("__AICARD__", AICARD)
  .replace("__NEXTS__", nexts(P, "ai"))
  .replace("__STEPS__", steps([
     ("DAY 0", "상담 · 주제 정하기", "지원하려는 직무나 공고를 보여 주세요. 그 안에서 만들 만한 주제를 두세 개 뽑아 함께 고릅니다."),
     ("DAY 1–2", "제작", "실제로 작동하는 형태로 만듭니다. 중간에 화면을 보여 드리고 방향을 맞춥니다."),
     ("DAY 3–4", "배포 · 인수인계", "인터넷에 올려 주소를 드리고, 어떤 구조인지 설명해 드립니다. 여기서 본인이 설명할 수 있는 상태를 만듭니다."),
     ("DAY 5–7", "전략 · 강의", "STEP 02는 이력서·면접 자료를, STEP 03은 강의와 실습 자료를 함께 드립니다."),
  ]))
  .replace("__FAQ__", faq([
     ("제가 만들지 않은 걸 제 것처럼 써도 되나요?",
      "그래서 <b>인수인계와 설명이 상품에 포함</b>되어 있습니다. 주제 선정부터 함께 하고, 만들면서 화면을 보여 드리고, 마지막에 구조와 판단 근거를 문서로 넘겨 드립니다. 면접에서 설명하지 못하면 결과물이 있어도 오히려 마이너스이기 때문입니다. 다만 <b>혼자 처음부터 끝까지 만들었다고 말씀드리라고 권하지 않습니다.</b> 어디까지 직접 하셨는지는 사실대로 말씀하시는 편이 안전하고, 실제로 그렇게 답해도 문제되지 않는 방향으로 구성을 잡습니다."),
     ("코딩을 전혀 모르는데 괜찮을까요?",
      "괜찮습니다. STEP 01·02는 만들어 드리는 구성이라 코딩을 몰라도 진행됩니다. STEP 03 강의는 <b>처음 하시는 분 기준</b>으로 만들었고, 설치나 설정에서 막히는 지점을 먼저 다룹니다."),
     ("바이브코딩이 정확히 뭔가요?",
      "AI에게 요구사항을 말로 설명해서 코드를 만들어 나가는 방식입니다. 문법을 외우는 대신 <b>무엇을 만들지 정확히 말하는 능력</b>이 중요해집니다. 강의도 문법이 아니라 그 부분을 다룹니다."),
     ("결과물 주제를 제가 정해 가도 되나요?",
      "네. 이미 하고 싶은 게 있으시면 그걸로 진행합니다. 다만 범위가 너무 크면 기간 안에 안 끝나서, 첫 버전에서 뭘 빼고 갈지 같이 정리하는 것부터 합니다."),
     ("AI 사용료가 따로 드나요?",
      "결과물에 어떤 기능이 들어가느냐에 따라 다릅니다. <b>무료 범위 안에서 만드는 방법을 우선</b> 안내드리고, 유료 서비스가 필요한 경우 상담에서 대략 얼마가 드는지 먼저 말씀드립니다. 몰래 붙는 비용은 없습니다."),
     ("합격을 보장하나요?",
      "보장하지 않습니다. 합격은 결과물 하나로 결정되지 않습니다. 저희가 책임지는 건 <b>이력서에 넣을 수 있는 결과물과, 그것을 설명할 수 있는 상태</b>까지입니다."),
     ("수정은 몇 번까지 되나요?",
      "모든 구성에 무료 수정 2회가 포함됩니다. 이후는 내용에 따라 협의합니다. 고칠 곳을 한 번에 모아서 주시면 더 빠릅니다."),
  ])))

body += band(P, "지원할 공고 하나만 보여 주세요", "그 공고에서 뭘 만들면 좋을지 먼저 봐 드립니다. 상담과 주제 제안은 무료입니다.", "ai")

LD = {"@context": "https://schema.org", "@type": "Service", "name": "온도 AI",
      "serviceType": "취업용 AI 결과물 제작 및 바이브코딩 제작 강의", "url": SITE + "ai/",
      "provider": {"@type": "ProfessionalService", "name": "온도컴퍼니", "@id": SITE + "#org"},
      "areaServed": {"@type": "Country", "name": "대한민국"},
      "description": "지원 직무에 맞는 취업용 AI 결과물을 함께 만들어 배포 주소와 소스로 납품하고, 이력서·자기소개서·면접 반영 전략과 바이브코딩 제작 강의까지 제공합니다.",
      "offers": {"@type": "AggregateOffer", "priceCurrency": "KRW", "lowPrice": "80000", "highPrice": "250000",
                 "offerCount": "3"}}

page("ai/index.html",
     "온도 AI — 취업용 AI 결과물 제작 · 이력서 전략 · 바이브코딩 강의 | 온도컴퍼니",
     "이력서에 쓸 결과물이 없다면 만들면 됩니다. 지원 직무에 맞는 AI 결과물 제작부터 이력서·면접 반영 전략, 직접 만드는 바이브코딩 강의까지 3단계. 8만원부터, 3~7일.",
     body, P, "ai/", ld=LD, theme="t-ai")
print("ai/index.html")
