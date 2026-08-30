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
      <b>무엇을 만들지 정하는 것부터</b> 함께 하고, 그걸 이력서·면접에 어떻게 넣을지까지 정리해 드립니다.</p>
    <dl class="phead-facts">
      <div class="phead-fact"><dt>시작 가격</dt><dd>8<small>만원~</small></dd></div>
      <div class="phead-fact"><dt>제작 기간</dt><dd>3~7<small>일</small></dd></div>
      <div class="phead-fact"><dt>구성</dt><dd>3<small>가지</small></dd></div>
      <div class="phead-fact"><dt>납품</dt><dd>URL<small>+ 소스</small></dd></div>
    </dl>
    <div class="phead-btns">
      <a class="btn btn-kko btn-lg" href="__K__" target="_blank" rel="noopener">카카오톡으로 상담하기</a>
      <a class="btn btn-line btn-lg" href="#track">구성 보기</a>
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
    <p class="eyebrow rv">Track <span class="ko">구성 고르기</span></p>
    <h2 class="rv">정해 오셨는지,<br>같이 정해야 하는지.</h2>
    <p class="lede rv">구성을 가르는 기준은 <b>만들 주제가 정해졌는지</b>입니다.
      이력서·자기소개서 문장과 면접 답변 뼈대는 <b>어느 구성이든 함께</b> 드립니다.</p>
    __TRACK__
    <div class="note-box rv">
      <b>기획이 갈리는 지점입니다.</b> 만들 것이 이미 정해진 경우와, 무엇을 만들지부터 정해야 하는 경우는
      들어가는 일이 다릅니다. 그래서 그 기준으로 구성을 나눴습니다.
      <b>이력서·자기소개서 문장과 면접 답변 뼈대는 어느 구성을 고르셔도 값에 포함</b>되어 있습니다.
      결과물만 있고 설명하지 못하면 소용이 없어서, 그건 빼고 팔지 않습니다.
    </div>
    <div class="note-box rv">
      <b>만들어 주고 끝내지 않습니다.</b> 결과물을 함께 만들고, 어떤 구조인지와 왜 그렇게 만들었는지를
      문서와 설명으로 넘겨 드립니다. 면접에서 본인이 설명하지 못하면 결과물이 있어도 소용이 없습니다.
      다만 없는 경력을 만들어 드리지는 않습니다. 어디까지 직접 하셨는지는 사실대로 말씀하시는 편이 안전합니다.
    </div>
  </div>
</section>

<section class="sec" id="samples">
  <div class="wrap">
    <p class="eyebrow rv">Work <span class="ko">실제 결과물</span></p>
    <h2 class="rv">결과물은 이런 모양입니다</h2>
    <p class="lede rv">실제로 만들어 배포한 결과물입니다. 눌러서 직접 만져 보실 수 있습니다.</p>
    <div class="pfs">__PFS_AI__</div>

    <h3 class="rex-h rv">이력서에는 이렇게 들어갑니다</h3>
    <p class="rex-lede rv">결과물마다 이력서 문장·자기소개서 문단·면접 답변을 같이 만들어 드립니다.
      아래는 위 두 결과물로 실제로 만든 것에서 일부를 덜어낸 것입니다.</p>
    <div class="faq rex rv">
          <details>
            <summary>CLEANSHEET — 표 검증·대사 도구</summary>
            <div class="faq-a">
              <p class="rex-t">이력서 한 줄 · 프로젝트 항목</p>
              <div class="rex-box">
                <b>거래처 실적 데이터 검증·대사 도구 제작·배포</b>
                <ul>
                  <li>표 붙여넣기 기반 자동 집계 · 이상값 탐지 · 두 표 대조(월 마감 대사) 웹 도구 개발</li>
                  <li>중복 입력, 거래처명 표기 불일치, 날짜 형식 혼재를 자동 검출하는 규칙 설계</li>
                  <li>상호 표기·날짜 형식이 서로 달라도 같은 건으로 인식하는 정규화 매칭 구현</li>
                </ul>
              </div>

              <p class="rex-t">자기소개서 첫 문단</p>
              <div class="rex-box">
                영업관리 직무를 준비하며 월 마감 자료의 구조를 들여다보니, 오류의 대부분이 계산식이 아니라
                원본 데이터에서 발생한다는 점을 알게 되었습니다. 같은 거래처가 <b>㈜한울상사</b>와 <b>한울상사</b>로
                나뉘어 입력되면 피벗 합계가 두 줄로 쪼개지고, 날짜 형식이 섞이면 정렬 순서가 어긋납니다.
              </div>

              <p class="rex-t">면접에서 이렇게 나옵니다</p>
              <div class="rex-box">
                <p class="rex-q">Q. “그거 VLOOKUP으로 되는 거 아닌가요?”</p>
                VLOOKUP은 글자가 정확히 같아야 찾습니다. ㈜한울상사와 한울상사는 #N/A가 뜹니다.
                그리고 한 방향만 봅니다 — 상대 명세서에만 있는 건은 반대로 한 번 더 돌려야 나옵니다.
              </div>
              <div class="rex-box">
                <p class="rex-q">Q. “실제 회사 데이터로 써 보신 건가요?”</p>
                아닙니다. 직무를 이해하려고 공개된 자료 형식에 맞춰 직접 만든 도구입니다.
                다만 마감 업무의 병목이 계산이 아니라 데이터 정합성이라는 걸 알게 됐고, 지금 화면에서 바로 보여드릴 수 있습니다.
              </div>

              <p class="rex-t">이렇게는 쓰지 마세요</p>
              <div class="rex-box">
                <ul>
                  <li><b>“실무에 도입해 업무 효율 30% 개선”</b> — 근거를 물으면 답할 수 없습니다. 한 번에 신뢰를 잃습니다.</li>
                  <li><b>“AI가 만들어 줬습니다”</b>(이 말만) — 사실이지만 절반입니다. 무엇을 정했는지를 반드시 함께 말하세요.</li>
                </ul>
              </div>
            </div>
          </details>
          <details>
            <summary>지글의 주린이 가이드 — 관심사에서 나온 결과물</summary>
            <div class="faq-a">
              <p class="rex-t">이력서 한 줄 · 프로젝트 항목</p>
              <div class="rex-box">
                <b>배당·적립 투자 시뮬레이션 웹앱 제작·배포</b>
                <ul>
                  <li>종목·초기 투자금·월 적립금·배당성장률을 입력하면 최대 30년까지 자산과 월 배당금을 계산하는 웹 도구 개발</li>
                  <li>일반계좌 15.4% · ISA 9.9% · 연금저축 5.5% 계좌별 세율과 배당금 재투자(DRIP)를 반영한 계산 로직 구현</li>
                  <li>입력·결과·비교·세금으로 화면을 나누고 결과를 CSV로 내보내도록 구성</li>
                </ul>
              </div>

              <p class="rex-t">자기소개서 한 문단 — 관심사에서 출발한 경우</p>
              <div class="rex-box">
                배당주에 관심이 생겨 매달 얼마를 넣으면 언제쯤 월 배당이 얼마가 되는지 계산해 보다가,
                같은 표를 매번 다시 만들고 있다는 걸 알게 됐습니다. 계좌 종류에 따라 세율이 달라지는 것까지 넣으면
                손으로는 감당이 안 돼서, 조건을 바꿔 가며 바로 볼 수 있는 웹 도구로 만들어 <b>지금도 직접 쓰고 있습니다</b>.
              </div>

              <p class="rex-t">면접에서 이렇게 나옵니다</p>
              <div class="rex-box">
                <p class="rex-q">Q. “이게 지원 직무랑 무슨 상관인가요?”</p>
                직접 연결되지는 않습니다. 다만 제가 반복해서 하던 계산을 규칙으로 정리해 도구로 바꿔 본 경험이고,
                지금도 제가 쓰고 있습니다. 필요한 게 있으면 만들어서 쓰는 편이라는 걸 보여드릴 수 있는 결과물입니다.
              </div>
              <div class="rex-box">
                <p class="rex-q">Q. “계산기 앱은 이미 많지 않나요?”</p>
                많습니다. 그런데 계좌 종류별 세율과 배당 성장률까지 같이 넣어 비교해 주는 걸 못 찾았습니다.
                필요한 조건이 이미 정해져 있어서 찾아다니는 것보다 만드는 편이 빨랐습니다.
              </div>

              <p class="rex-t">이렇게는 쓰지 마세요</p>
              <div class="rex-box">
                <ul>
                  <li><b>“투자 수익률 OO% 달성”</b> — 도구를 만든 것이지 수익을 낸 게 아닙니다. 완전히 다른 이야기가 됩니다.</li>
                  <li><b>“핀테크 서비스 개발”</b> — 열어 보면 계산 도구입니다. 부풀린 만큼 실망이 커집니다.</li>
                </ul>
              </div>

              <p class="rex-foot">취미에서 나온 결과물이라도 “필요해서 만들었고 지금도 쓰고 있다”까지 말하면 충분합니다.</p>
            </div>
          </details>
    </div>

    <p class="cmp-note rv" style="margin-top:22px">
      지원 직무가 다르면 그 직무의 자료와 용어로 결과물부터 다시 만듭니다. 문장도 같이 다시 씁니다.
      <a href="../work/" style="color:var(--sv-on);font-weight:700">작업물 전체 보기 →</a>
    </p>
  </div>
</section>


<section class="sec sec-mist">
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


<section class="sec sec-mist svc" id="strategy">
  <div class="wrap svc-grid">
    <div>
      <p class="eyebrow rv">Strategy <span class="ko">이력서 반영</span></p>
      <h2 class="rv">만든 다음이<br>더 중요합니다.</h2>
      <p class="svc-desc rv">결과물이 있어도 이력서에 한 줄로 적어 놓으면 아무도 안 봅니다.
        무엇을 왜 만들었고 무엇이 달라졌는지를 <b>읽는 사람 기준</b>으로 다시 씁니다.
        아래는 <b>어느 구성을 고르셔도 함께</b> 나갑니다.</p>
      <ul class="svc-list rv">
        <li><span><b>프로젝트 한 줄 정의</b> — 이력서 맨 앞에 들어갈 문장</span></li>
        <li><span><b>이력서 문단</b> — 역할 · 사용 기술 · 만든 결과 순서로 정리</span></li>
        <li><span><b>자기소개서 문단</b> — 지원 동기와 연결되는 형태로</span></li>
        <li><span><b>면접 예상 질문과 답변 뼈대</b> — “왜 그렇게 만들었나요”에 답할 수 있게</span></li>
        <li><span><b>공고별 맞춤 조정</b> — 기획 포함 구성부터</span></li>
      </ul>
      <p class="svc-note rv">실제로 어떤 문장이 나오는지는
        <a href="#samples">위 결과물마다 예시</a>로 붙여 뒀습니다.</p>
      <div class="svc-cta rv">
        <span class="svc-price">전 구성 공통<small>추가 비용 없음</small></span>
        <a class="btn btn-sv" href="__K__" target="_blank" rel="noopener">카톡으로 상담하기</a>
      </div>
    </div>
    __AICARD__
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Course <span class="ko">강의 포함 구성</span></p>
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
    <span class="tr-step">제작</span>
    <h3>만들 것이 정해진 경우</h3>
    <p>이미 만들고 싶은 게 있으시면 그대로 만들어 배포까지 끝냅니다. 주제를 찾는 과정이 빠지는 구성입니다.</p>
    <ul>
      <li><span><b>정해 오신 주제로 제작</b> — 범위만 첫 버전에 맞게 정리</span></li>
      <li><span><b>작동하는 결과물 1개</b> — 데모가 아니라 실제로 열리는 것</span></li>
      <li><span><b>배포 주소 + 소스 파일 전체</b></span></li>
      <li><span><b>구조 설명 문서</b> — 본인이 설명할 수 있게</span></li>
      <li><span><b>이력서·면접 문장</b> — 전 구성 공통</span></li>
    </ul>
    <div class="tr-foot">
      <p class="plan-was">정가 <s>12만원</s> <em>오픈 기념 할인</em></p>
      <p class="tr-price">8<small>만원</small></p>
      <p class="tr-when">3~4일 · 무료 수정 2회</p>
      <a class="btn btn-line" href="__K__" target="_blank" rel="noopener">이 구성으로 문의</a>
    </div>
  </div>

  <div class="tr rv tr-best">
    <span class="tr-step">기획 ＋ 제작</span>
    <h3>뭘 만들지부터 같이</h3>
    <p>지원 공고와 직무를 보고 만들 주제부터 함께 찾습니다. 대부분 여기서 시작하십니다.</p>
    <ul>
      <li><span><b>공고·직무 분석</b> — 그 일에서 반복되는 지점을 찾습니다</span></li>
      <li><span><b>주제 후보 2~3개 제안</b> — 왜 그 주제인지, 면접에서 어떻게 읽히는지까지</span></li>
      <li><span><b>제작 구성 전부 포함</b></span></li>
      <li><span><b>공고 1건 맞춤 조정</b> — 강조점을 그 공고에 맞게</span></li>
      <li><span><b>이력서·면접 문장</b> — 전 구성 공통</span></li>
    </ul>
    <div class="tr-foot">
      <p class="plan-was">정가 <s>22만원</s> <em>오픈 기념 할인</em></p>
      <p class="tr-price">15<small>만원</small></p>
      <p class="tr-when">4~6일 · 무료 수정 2회</p>
      <a class="btn btn-sv" href="__K__" target="_blank" rel="noopener">이 구성으로 문의</a>
    </div>
  </div>

  <div class="tr rv">
    <span class="tr-step">＋ 강의</span>
    <h3>다음은 직접 만들 수 있게</h3>
    <p>기획과 제작을 함께 하고, 만드는 방법을 영상 강의로 남겨 드립니다.</p>
    <ul>
      <li><span><b>앞 구성 전부 포함</b></span></li>
      <li><span><b>바이브코딩 제작 강의 6강</b> — 녹화 영상 + 실습 자료</span></li>
      <li><span><b>실습용 예제 파일</b> — 보면서 따라 만들 수 있게</span></li>
      <li><span><b>2주간 카톡 질문</b> — 막히는 지점 그때그때</span></li>
      <li><span><b>두 번째 결과물 점검 1회</b> — 직접 만드신 것 피드백</span></li>
    </ul>
    <div class="tr-foot">
      <p class="plan-was">정가 <s>36만원~</s> <em>오픈 기념 할인</em></p>
      <p class="tr-price">25<small>만원~</small></p>
      <p class="tr-when">5~7일 · 무료 수정 2회</p>
      <a class="btn btn-line" href="__K__" target="_blank" rel="noopener">이 구성으로 문의</a>
    </div>
  </div>
</div>"""

body = (body
  .replace("__CRUMB__", crumb(P, [(None, "온도 AI")]))
  .replace("__TRACK__", TRACK)
  .replace("__PFS_AI__", "".join(pf(P, *x) for x in PORTFOLIO if x[8] == "ai"))
  .replace("__AICARD__", AICARD)
  .replace("__NEXTS__", nexts(P, "ai"))
  .replace("__STEPS__", steps([
     ("DAY 0", "상담 · 기획", "지원하려는 직무나 공고를 보여 주세요. 그 안에서 만들 만한 주제를 두세 개 뽑아 함께 고릅니다. 이미 정해 오셨으면 이 단계는 범위 정리만 하고 넘어갑니다."),
     ("DAY 1–2", "제작", "실제로 작동하는 형태로 만듭니다. 중간에 화면을 보여 드리고 방향을 맞춥니다."),
     ("DAY 3–4", "배포 · 인수인계", "인터넷에 올려 주소를 드리고, 어떤 구조인지 설명해 드립니다. 여기서 본인이 설명할 수 있는 상태를 만듭니다."),
     ("DAY 5–7", "이력서 문장 · 강의", "이력서·자기소개서 문장과 면접 답변 뼈대는 전 구성 공통으로 드립니다. 강의 포함 구성은 강의와 실습 자료가 함께 나갑니다."),
  ]))
  .replace("__FAQ__", faq([
     ("제가 만들지 않은 걸 제 것처럼 써도 되나요?",
      "그래서 <b>인수인계와 설명이 상품에 포함</b>되어 있습니다. 주제 선정부터 함께 하고, 만드는 동안 화면을 보여 드리고, 마지막에 구조와 판단 근거를 문서로 넘겨 드립니다. 면접에서 설명하지 못하면 결과물이 있어도 오히려 마이너스입니다.<br><br>어디까지 직접 하셨는지는 <b>사실대로 말씀하시는 편이 안전합니다.</b> 그렇게 답해도 문제되지 않는 방향으로 구성을 잡아 드립니다."),
     ("코딩을 전혀 모르는데 괜찮을까요?",
      "괜찮습니다. 제작·기획 구성은 만들어 드리는 쪽이라 코딩을 몰라도 진행됩니다. 강의 포함 구성은 <b>처음 하시는 분 기준</b>으로 만들었고, 설치나 설정에서 막히는 지점을 먼저 다룹니다."),
     ("바이브코딩이 정확히 뭔가요?",
      "AI에게 요구사항을 말로 설명해서 코드를 만들어 나가는 방식입니다. 문법을 외우는 대신 <b>무엇을 만들지 정확히 말하는 능력</b>이 중요해집니다. 강의도 문법이 아니라 그 부분을 다룹니다."),
     ("뭘 만들어야 할지 전혀 모르겠는데요.",
      "그 경우가 대부분이라 <b>기획을 따로 나눠 뒀습니다.</b> 지원할 공고나 직무만 알려 주시면 그 일에서 반복되는 지점을 찾아 주제 후보를 두세 개 만들어 드리고, 각각이 면접에서 어떻게 읽힐지까지 같이 보여 드립니다. 고르시는 건 그다음입니다.<br><br><b>상담과 주제 제안까지는 무료입니다.</b> 후보를 보고 진행하지 않으셔도 됩니다."),
     ("결과물 주제를 제가 정해 가도 되나요?",
      "네. 그런 경우가 <b>제작 구성</b>입니다. 기획이 빠지는 만큼 값이 내려갑니다. 다만 범위가 너무 크면 기간 안에 안 끝나서, 첫 버전에서 뭘 빼고 갈지 정리하는 것부터 합니다."),
     ("이력서 문장은 비싼 구성에서만 주나요?",
      "아닙니다. <b>어느 구성이든 값에 포함</b>됩니다. 이력서 한 줄, 자기소개서 문단, 면접 예상 질문과 답변 뼈대까지 같이 나갑니다. 결과물만 있고 설명하지 못하면 오히려 마이너스라, 그건 빼고 팔지 않습니다. 공고 1건에 맞춘 조정은 기획 포함 구성부터입니다."),
     ("AI 사용료가 따로 드나요?",
      "결과물에 어떤 기능이 들어가느냐에 따라 다릅니다. <b>무료 범위 안에서 만드는 방법을 우선</b> 안내드리고, 유료 서비스가 필요한 경우 상담에서 대략 얼마가 드는지 먼저 말씀드립니다. 몰래 붙는 비용은 없습니다."),
     ("합격을 보장하나요?",
      "보장하지 않습니다. 합격은 결과물 하나로 결정되지 않습니다. 저희가 드리는 건 <b>이력서에 넣을 결과물과, 그걸 설명할 수 있는 상태</b>까지입니다."),
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
