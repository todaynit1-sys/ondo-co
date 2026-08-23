# -*- coding: utf-8 -*-
from _build import *
from _frag import *
K = KAKAO
P = "../"

body = """
<section class="phead">
  <div class="wrap phead-in">
    __CRUMB__
    <p class="eyebrow rv">Service 02 <span class="ko">촬영 없이 만듭니다</span></p>
    <h1><span class="en">Ondo Clip</span>찍을 게 없어도,<br>영상은 만들 수 있습니다.</h1>
    <p class="phead-lede">카메라도, 찍어둔 소재도 필요 없습니다. <b>알리고 싶은 내용만 알려 주시면</b>
      AI로 화면과 목소리를 만들어 릴스·쇼츠 규격 세로 영상으로 완성합니다.</p>
    <dl class="phead-facts">
      <div class="phead-fact"><dt>30초 1편</dt><dd>20<small>만원</small></dd></div>
      <div class="phead-fact"><dt>60초 1편</dt><dd>40<small>만원</small></dd></div>
      <div class="phead-fact"><dt>제작 기간</dt><dd>2~5<small>일</small></dd></div>
      <div class="phead-fact"><dt>규격</dt><dd>9:16<small>세로</small></dd></div>
    </dl>
    <div class="phead-btns">
      <a class="btn btn-kko btn-lg" href="__K__" target="_blank" rel="noopener">카카오톡으로 상담하기</a>
      <a class="btn btn-line btn-lg" href="#price">요금 보기</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Why <span class="ko">왜 AI로 만드나</span></p>
    <h2 class="rv">영상이 없는 이유는<br>대체로 셋 중 하나입니다.</h2>
    <p class="lede rv">셋 다 "만들 마음이 없어서"가 아니라 "만들 여건이 안 돼서" 생기는 문제입니다. AI 영상은 이 세 개를 한 번에 없앱니다.</p>
    <div class="spots">
      <div class="spot rv"><span class="spot-k">촬영</span>
        <h3>찍을 시간도, 찍을 것도 없다</h3>
        <p>장사하면서 촬영 일정을 잡기가 어렵습니다. AI로 화면을 만들면 촬영 자체가 없어집니다.</p></div>
      <div class="spot rv"><span class="spot-k">노출</span>
        <h3>팔로워가 없어서 올려도 안 보인다</h3>
        <p>릴스·쇼츠는 팔로워가 아니라 관심사 기준으로 퍼집니다. 계정을 막 시작해도 시작할 수 있습니다.</p></div>
      <div class="spot rv"><span class="spot-k">얼굴</span>
        <h3>내 얼굴이 나오는 게 부담스럽다</h3>
        <p>동물 캐릭터나 AI 아나운서가 대신 말합니다. 사장님 얼굴도, 직원 얼굴도 나오지 않습니다.</p></div>
    </div>
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Style <span class="ko">연출 방식</span></p>
    <h2 class="rv">원하는 방식으로 잡습니다</h2>
    <p class="lede rv">같은 내용이어도 어떤 화면으로 말하느냐에 따라 전혀 다르게 보입니다. 업종과 손님 연령대를 보고 함께 고릅니다.</p>
    <div class="outs">
      <div class="out rv"><span class="out-k">Animal</span><h3>동물 캐릭터가 말하는 광고</h3><p>말하는 강아지·고양이가 가게를 소개합니다. 사람이 나오지 않고 시선이 잘 멈춥니다. 부담 없이 시작하기 좋은 방식입니다.</p></div>
      <div class="out rv"><span class="out-k">Anchor</span><h3>AI 아나운서 뉴스형</h3><p>또박또박 전달하는 구성. 진료 안내, 수업 과정, 수리 절차처럼 정보량이 많은 업종에 맞습니다.</p></div>
      <div class="out rv"><span class="out-k">Real</span><h3>실사 느낌 장면 전환</h3><p>실제로 촬영한 것 같은 화면을 이어 붙입니다. 분위기를 보여 줘야 하는 업종에 씁니다.</p></div>
      <div class="out rv"><span class="out-k">Illust</span><h3>일러스트 · 모션</h3><p>그림과 도형이 움직이는 방식. 설명이 필요한 서비스나 무형 상품에 잘 맞습니다.</p></div>
      <div class="out rv"><span class="out-k">Close-up</span><h3>손 · 제품 클로즈업</h3><p>만드는 과정이나 제품 디테일만 크게 보여 줍니다. 음식·공방·수공예에 씁니다.</p></div>
      <div class="out rv"><span class="out-k">Before / After</span><h3>전후 대조</h3><p>지저분한 화면에서 깨끗한 화면으로. 시공·청소·정리 업종에서 가장 반응이 확실한 구성입니다.</p></div>
    </div>
    <p class="cmp-note rv" style="margin-top:24px">어떤 게 맞을지 모르셔도 됩니다. 업종과 알리고 싶은 내용을 말씀해 주시면 두세 가지를 제안해 드립니다.</p>
  </div>
</section>

<section class="sec svc" id="what">
  <div class="wrap svc-grid">
    <div>
      <p class="eyebrow rv">What you get <span class="ko">받으시는 것</span></p>
      <h2 class="rv">올릴 수 있는 상태까지</h2>
      <p class="svc-desc rv">영상 파일만 던져 드리지 않습니다. 어떤 순서로 올리면 좋을지, 첫 문장은 뭐라고 쓸지까지 같이 드립니다.</p>
      <ul class="svc-list rv">
        <li><span><b>세로 영상 1편</b> — 30초 또는 60초 내외, 9:16 릴스·쇼츠 규격</span></li>
        <li><span><b>시나리오 · 대사 작성</b> — 무엇을 어떤 순서로 말할지 먼저 씁니다</span></li>
        <li><span><b>AI 화면 생성</b> — 고르신 연출로 장면을 만듭니다</span></li>
        <li><span><b>자막</b> — 소리를 꺼도 내용이 전달되게</span></li>
        <li><span><b>저작권 안전한 배경음</b> — 상업적 사용이 허용된 음원만 사용</span></li>
        <li><span><b>썸네일 1컷 · 업로드 문구 초안</b> — 첫 줄과 해시태그까지</span></li>
      </ul>
      <div class="svc-cta rv">
        <span class="svc-price">30초 20만원<small>60초 40만원</small></span>
        <a class="btn btn-sv" href="__K__" target="_blank" rel="noopener">카톡으로 상담하기</a>
      </div>
    </div>
    __CLIPS__
  </div>
</section>

<section class="sec sec-mist" id="how">
  <div class="wrap">
    <p class="eyebrow rv">How <span class="ko">진행 방식</span></p>
    <h2 class="rv">만들기 <em style="font-style:normal;color:var(--sv)">전에</em> 확인받습니다</h2>
    <p class="lede rv">AI 영상은 다 만든 다음에 한 장면만 고치는 것이 사실상 불가능합니다.
      그래서 <b>만들기 전에</b> 화면 이미지와 대사를 먼저 보여 드리고, 확인받은 다음에 제작에 들어갑니다.</p>
    <div class="curri">
      <div class="cu rv"><span class="cu-n">01</span><div><h3>알리고 싶은 것 한 줄</h3><p>무엇을 누구에게 알리고 싶은지만 말씀해 주세요. 문구를 다듬는 건 저희가 합니다.</p></div></div>
      <div class="cu rv"><span class="cu-n">02</span><div><h3>연출 고르기</h3><p>동물·아나운서·실사·일러스트 중에서 고릅니다. 두세 가지를 먼저 제안해 드립니다.</p></div></div>
      <div class="cu rv"><span class="cu-n">03</span><div><h3>이미지 · 대사 확인 ★</h3><p>실제로 쓸 화면 이미지와 대사 전문을 보내 드립니다. <b>여기서 OK하신 다음에</b> 영상 제작에 들어갑니다.</p></div></div>
      <div class="cu rv"><span class="cu-n">04</span><div><h3>있으면 좋은 자료</h3><p>로고, 간판 사진, 메뉴판, 가격표. 없어도 만들 수 있지만 있으면 훨씬 우리 가게처럼 나옵니다.</p></div></div>
    </div>

    <div class="note-box rv">
      <b>무료 수정을 두지 않았습니다.</b> AI 영상은 장면 하나를 바꾸려 해도 전체를 다시 생성해야 합니다.
      "수정 1회 포함"이라고 적어 두면 실제로는 재제작인데 무료처럼 보여서 서로 곤란해집니다.
      대신 <b>3단계에서 이미지와 대사를 확인받는 절차</b>를 넣었습니다. 이 단계에서는 몇 번이든 바꾸실 수 있습니다.
      완성 후에 방향을 바꾸고 싶으시면 새 제작으로 견적을 다시 내 드립니다.
    </div>

    <div class="note-box rv">
      <b>지키는 선이 있습니다.</b><br>
      · 실존 인물이나 연예인의 얼굴·목소리는 만들지 않습니다.<br>
      · 실제로 없는 메뉴·시설·자격·수상 이력을 있는 것처럼 만들지 않습니다.<br>
      · 화면이 실제 매장 모습이 아닌 경우, <b>AI로 만든 영상이라는 점을 영상 설명이나 화면에 밝히시는 편</b>을 권합니다.
      광고로 문제가 되면 사장님께 돌아가는 일이라, 처음부터 안전한 쪽으로 잡습니다.
    </div>
  </div>
</section>

<section class="sec" id="price">
  <div class="wrap">
    <p class="eyebrow rv">Price <span class="ko">오픈 기념 할인</span></p>
    <h2 class="rv">길이로 계산합니다</h2>
    <p class="lede rv">길이가 두 배면 만들어야 할 장면도 두 배입니다. 금액도 그만큼입니다.
      기획·시나리오·AI 화면 생성·자막·배경음·썸네일이 <b>모두 포함된</b> 금액입니다.</p>
    <div class="plans" style="margin-top:32px">__PLANS__</div>
    <div class="plan-note rv">
      <b>할인</b> · 표시된 금액은 오픈 기념 할인가입니다. 할인 종료 시 정가로 돌아갑니다<br>
      <b>길이</b> · 30초·60초는 내외 기준입니다. 그보다 길게 필요하시면 별도로 견적을 내 드립니다<br>
      <b>월 관리</b> · 30초 4편 기준입니다. 60초 영상은 포함되지 않으며 필요하실 때 건별로 추가합니다<br>
      <b>수정</b> · 무료 수정은 없습니다. 대신 제작 전에 이미지와 대사를 확인받고 진행합니다<br>
      <b>촬영</b> · 촬영이 필요 없습니다. 화면은 AI로 만듭니다<br>
      <b>해지</b> · 월 관리는 월 단위로 해지하실 수 있습니다. 위약금이 없습니다<br>
      <b>확정</b> · 표시 금액은 상담에서 연출과 장면 수를 확인한 뒤 확정합니다
    </div>
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Process <span class="ko">문의부터 납품까지</span></p>
    <h2 class="rv">확인 한 번, 그다음은 기다리시면 됩니다</h2>
    __STEPS__
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">FAQ <span class="ko">온도 클립</span></p>
    <h2 class="rv">AI 영상 관련해 자주 묻는 것</h2>
    __FAQ__
  </div>
</section>

<section class="sec sec-mist">
  <div class="wrap">
    <p class="eyebrow rv">Next <span class="ko">다른 서비스</span></p>
    <h2 class="rv">영상이 아니라 다른 게 필요하시면</h2>
    <p class="lede rv">세 서비스는 각각 다른 일입니다. 영상 없이 아래만 하셔도 됩니다.</p>
    __NEXTS__
  </div>
</section>
"""

PLANS = "".join([
 plan("숏폼 30초", "짧게 빠르게 알리고 싶을 때", "20", "만원 · 1편",
      ["AI 생성 세로 영상 1편 (30초 내외)", "시나리오 · 대사 작성", "연출 선택 (동물·아나운서·실사 등)",
       "자막 · 저작권 안전 배경음", "썸네일 1컷 · 업로드 문구 초안", "제작 전 이미지·대사 확인"],
      "30초 문의", K, was="25만원"),
 plan("숏폼 60초", "설명이 필요한 업종이라면", "40", "만원 · 1편",
      ["AI 생성 세로 영상 1편 (60초 내외)", "30초 구성 전부 포함", "장면 수 2배 · 구성 분기",
       "상세 시나리오 · 컷 구성표", "제작 전 이미지·대사 확인"],
      "60초 문의", K, best=True, tag="추천 구성", was="50만원"),
 plan("월 관리", "꾸준히 올려야 효과가 납니다", "70", "만원 · 월 4편",
      ["30초 세로 영상 4편 (편당 17만 5천원)", "30초 구성 전부 포함",
       "매달 주제 기획 · 대사 작성", "업로드 순서 · 문구 제안",
       "반응 보고 다음 편 방향 조정", "월 단위 해지 가능"],
      "월 관리 문의", K, was="100만원", note="월 단위 · 상담 후 확정"),
])

body = (body
  .replace("__CRUMB__", crumb(P, [(None, "온도 클립")]))
  .replace("__K__", K)
  .replace("__CLIPS__", CLIPS)
  .replace("__PLANS__", PLANS)
  .replace("__NEXTS__", nexts(P, "clip"))
  .replace("__STEPS__", steps([
     ("DAY 0", "문의 · 방향 잡기", "알리고 싶은 내용 한 줄만 카톡으로 보내 주세요. 업종에 맞는 연출을 두세 가지 제안해 드립니다."),
     ("DAY 1", "이미지 · 대사 확인", "실제로 쓸 화면 이미지와 대사 전문을 보내 드립니다. 이 단계에서 몇 번이든 바꾸실 수 있습니다."),
     ("DAY 2–4", "제작", "확인받은 대로 AI 화면을 만들고 자막·음악을 붙입니다. 30초는 보통 이틀, 60초는 사나흘 걸립니다."),
     ("DAY 3–5", "납품", "영상 파일과 썸네일, 업로드 문구를 함께 드립니다. 인스타·유튜브 규격으로 같이 출력합니다."),
  ]))
  .replace("__FAQ__", faq([
     ("촬영은 안 하나요? 정말 아무것도 안 찍어도 되나요?",
      "네, <b>촬영이 필요 없습니다.</b> 화면을 AI로 만들기 때문입니다. 다만 로고나 간판 사진, 메뉴판처럼 가게를 알 수 있는 자료가 있으면 훨씬 우리 가게처럼 나옵니다. 없어도 진행됩니다."),
     ("수정이 정말 안 되나요?",
      "완성된 영상을 부분 수정하는 건 사실상 불가능합니다. AI 영상은 장면 하나를 바꾸려 해도 전체를 다시 생성해야 하기 때문입니다. 그래서 <b>만들기 전에 화면 이미지와 대사를 먼저 보여 드리고</b>, 그 단계에서는 몇 번이든 바꾸실 수 있게 했습니다. 완성 후 방향을 바꾸고 싶으시면 새 제작으로 견적을 다시 내 드립니다."),
     ("왜 60초가 30초의 두 배인가요?",
      "만들어야 할 장면 수가 두 배이기 때문입니다. AI 영상은 장면 단위로 생성하고, 장면이 늘면 그만큼 다시 만들 확률과 이어 붙이는 작업이 함께 늘어납니다. 60초는 구성도 더 촘촘하게 짜야 합니다. <b>30초 두 편을 만드는 것과 비슷한 작업량</b>이라 그렇게 잡았습니다."),
     ("AI로 만든 영상이라고 밝혀야 하나요?",
      "법으로 정해진 표기 의무를 저희가 단정해서 말씀드리지는 않겠습니다. 다만 화면이 실제 매장 모습과 다른 경우에는 <b>영상 설명이나 화면에 밝히시는 편을 권합니다.</b> 나중에 광고 관련 문제가 생기면 사장님께 돌아가는 일이라, 처음부터 안전한 쪽으로 잡는 게 낫습니다. 실존 인물의 얼굴·목소리는 만들지 않고, 실제로 없는 메뉴나 자격을 있는 것처럼 만들지도 않습니다."),
     ("어떤 내용을 만들어야 할지 모르겠어요.",
      "업종과 손님이 자주 묻는 질문 세 가지만 알려 주세요. 대부분 그 안에 소재가 있습니다. 시공은 전후 대조, 카페는 대표 메뉴, 학원·병원은 절차 안내가 기본입니다."),
     ("유행하는 음원을 써 주실 수 있나요?",
      "저희가 편집 단계에서 넣어 드리지는 않습니다. 그 음원들은 대부분 상업적 사용 허가가 없어서 문제가 생기면 사장님 계정에 돌아갑니다. 대신 <b>업로드하실 때 앱 안에서 직접 붙이는 방법</b>을 알려 드립니다. 그 방법은 플랫폼이 허용하는 정상 경로입니다."),
     ("조회수가 얼마나 나오나요?",
      "보장할 수 없습니다. 조회수는 알고리즘과 업종, 올리는 시점에 따라 크게 달라지고 한 편으로 결정되지도 않습니다. 확실하지 않은 것을 확실하다고 말씀드리지 않겠습니다. 저희가 책임지는 건 <b>올릴 수 있는 상태의 결과물</b>입니다."),
     ("영상 파일은 어떤 형식으로 주시나요?",
      "MP4 파일로 드립니다. 인스타그램·유튜브 규격에 맞춘 9:16 세로 영상과 썸네일 이미지를 함께 보내 드립니다. 원본을 드리니 나중에 직접 잘라 쓰셔도 됩니다."),
  ])))

body += band(P, "알리고 싶은 것 한 줄만 주세요", "업종에 맞는 연출을 두세 가지 제안해 드립니다. 상담과 제안은 무료입니다.", "clip")

LD = {"@context": "https://schema.org", "@type": "Service", "name": "온도 클립",
      "serviceType": "AI 홍보 영상 제작", "url": SITE + "clip/",
      "provider": {"@type": "ProfessionalService", "name": "온도컴퍼니", "@id": SITE + "#org"},
      "areaServed": {"@type": "Country", "name": "대한민국"},
      "description": "촬영 없이 AI로 만드는 소상공인 홍보 영상. 동물 캐릭터·AI 아나운서·실사 등 원하는 연출로 30초 또는 60초 세로 영상을 제작하고, 시나리오·자막·배경음·썸네일까지 포함해 릴스·쇼츠 규격으로 납품합니다.",
      "offers": {"@type": "AggregateOffer", "priceCurrency": "KRW", "lowPrice": "200000", "highPrice": "700000"}}

page("clip/index.html",
     "온도 클립 — 촬영 없이 만드는 AI 홍보 영상 | 온도컴퍼니",
     "카메라도 소재도 필요 없습니다. 알리고 싶은 내용만 주시면 AI로 화면과 목소리를 만들어 세로 영상으로 완성합니다. 30초 20만원, 60초 40만원. 동물·아나운서 등 연출 선택.",
     body, P, "clip/", ld=LD, theme="t-clip")
print("clip/index.html")
