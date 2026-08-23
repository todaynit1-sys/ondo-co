# -*- coding: utf-8 -*-
from _build import *
from _frag import *
K = KAKAO
P = "../"

body = """
<section class="phead">
  <div class="wrap phead-in">
    __CRUMB__
    <p class="eyebrow rv">Contact <span class="ko">지금 물어보세요</span></p>
    <h1>여기까지 오셨으면,<br>이미 반은 오신 겁니다.</h1>
    <p class="phead-lede">견적만 물어보셔도 됩니다. 업종이나 상황만 알려 주시면
      예상 금액과 일정을 <b>영업일 기준 하루 안에</b> 알려 드립니다.</p>
  </div>
</section>

<section class="sec contact">
  <div class="wrap">
    <div class="cgrid" style="margin-top:0">
      <div>
        <div class="kko-card rv">
          <h3>카카오톡으로 바로 물어보기</h3>
          <p>가장 빠릅니다. 오픈채팅이라 친구 추가 없이 바로 대화할 수 있고, 영업일 기준 하루 안에 답변드립니다.</p>
          <a class="btn btn-lg" href="__K__" target="_blank" rel="noopener">오픈채팅 열기</a>
        </div>

        <ul class="ways rv">
          <li><a class="row" href="__K__" target="_blank" rel="noopener">
            <span><span class="w-k">카카오톡 오픈채팅</span><span class="w-v">바로 대화 시작</span></span>
            <span class="w-go">열기 →</span></a></li>
          <li><div class="row">
            <span><span class="w-k">답변 시간</span><span class="w-v">영업일 하루 안에</span></span>
            <span class="w-go">평일 09–19시</span></div></li>
          <li><div class="row">
            <span><span class="w-k">상담 비용</span><span class="w-v">무료</span></span>
            <span class="w-go">견적만도 OK</span></div></li>
        </ul>

        <!-- 카톡 QR 이미지를 images/kakao-qr.png 로 저장한 뒤 아래 주석을 풀면 QR 카드가 나옵니다
        <div class="qr rv">
          <img src="../images/kakao-qr.png" alt="온도컴퍼니 카카오톡 오픈채팅 QR 코드" width="96" height="96" loading="lazy">
          <div><b>QR로 열기</b>카메라로 찍으면 오픈채팅이 바로 열립니다.</div>
        </div>
        -->

        <!-- 전화·이메일을 공개하실 거면 아래 주석을 풀고 값을 채우세요
        <ul class="ways rv" style="margin-top:14px">
          <li><div class="row">
            <span><span class="w-k">전화</span><span class="w-v">010-0000-0000</span></span>
            <button class="copybtn" type="button" data-copy="01000000000">복사</button></div></li>
          <li><div class="row">
            <span><span class="w-k">이메일</span><span class="w-v">hello@example.com</span></span>
            <button class="copybtn" type="button" data-copy="hello@example.com">복사</button></div></li>
        </ul>
        -->
      </div>

      <div>
        <div class="note-box rv" style="margin-top:0;--sv:var(--web);--sv-t:#EDF2FF">
          <b>문의폼을 두지 않았습니다.</b><br>
          서버 없이 이메일로 문의를 받으려면 외부 서비스를 거쳐야 하고, 무료 구간에는 월 건수 제한이 있습니다.
          한도를 넘기면 보내신 문의가 조용히 사라집니다. 그래서 <b>유실 없이 확실하게 닿는 카카오톡 한 곳</b>으로 모았습니다.
          고객 사이트를 만들 때도 같은 이유로 전화·카톡을 기본으로 잡습니다.
        </div>

        <!--
          이메일로 문의를 받고 싶으시면 아래 순서로 되살릴 수 있습니다.
          1) formspree.io 가입 → 새 폼 생성 → 발급된 주소 복사
          2) 아래 주석을 풀고 action 의 주소를 교체
          3) 위 note-box 는 지우기
          (assets/js/ondo.js 의 문의폼 검증·폴백 코드는 그대로 남아 있어 바로 동작합니다)

        <form class="form rv" id="cForm" action="https://formspree.io/f/REPLACE_FORMSPREE" method="POST">
          <div class="form-row">
            <label for="f-name">성함 또는 업체명 <span class="req">*</span></label>
            <input id="f-name" name="name" type="text" autocomplete="organization" placeholder="예) 온도세탁 / 홍길동">
            <span class="form-err" id="e-name" hidden>성함이나 업체명을 적어 주세요.</span>
          </div>
          <div class="form-row">
            <label for="f-contact">연락처 <span class="req">*</span></label>
            <input id="f-contact" name="contact" type="text" autocomplete="tel" placeholder="010-0000-0000 또는 name@email.com">
            <span class="form-err" id="e-contact" hidden>연락받으실 번호나 이메일을 적어 주세요.</span>
          </div>
          <div class="form-row">
            <label for="f-svc">관심 있는 서비스</label>
            <select id="f-svc" name="service">
              <option value="">아직 모르겠어요 · 추천 부탁드립니다</option>
              <option value="web">온도 웹 — 반응형 홈페이지</option>
              <option value="clip">온도 클립 — AI 홍보 영상</option>
              <option value="ai">온도 AI — 취업용 AI 결과물</option>
            </select>
          </div>
          <div class="form-row">
            <label for="f-msg">문의 내용 <span class="req">*</span></label>
            <textarea id="f-msg" name="message" placeholder="업종과 원하시는 느낌을 적어 주세요."></textarea>
            <span class="form-err" id="e-msg" hidden>어떤 게 필요하신지 한 줄만 적어 주세요.</span>
          </div>
          <label class="hp" aria-hidden="true">이 칸은 비워 두세요<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label>
          <button class="btn btn-pri btn-lg btn-block" type="submit">문의 보내기</button>
          <p class="form-note">보내주신 내용은 문의 답변에만 사용합니다.</p>
        </form>
        <div class="form form-done rv" id="cDone" hidden>
          <div class="fd-i" aria-hidden="true">&#10003;</div>
          <h3>문의가 전송되었습니다</h3>
          <p id="cDoneMsg">영업일 기준 하루 안에 답변드리겠습니다.</p>
        </div>
        -->

        <p class="eyebrow rv" style="margin-top:26px">Before you ask <span class="ko">이것만 알려 주시면 빨라요</span></p>
        <h2 class="rv" style="font-size:clamp(21px,2.6vw,26px)">첫 메시지에 이 세 가지만</h2>
        <ul class="ways rv" style="margin-top:18px">
          <li><div class="row"><span><span class="w-k">01 · 어떤 일을 하시는지</span><span class="w-v" style="font-size:14.5px;font-weight:600">업종과 하시는 일</span></span></div></li>
          <li><div class="row"><span><span class="w-k">02 · 왜 필요해지셨는지</span><span class="w-v" style="font-size:14.5px;font-weight:600">손님이 없어서 / 보낼 링크가 없어서 / 이력서에 쓸 게 없어서</span></span></div></li>
          <li><div class="row"><span><span class="w-k">03 · 언제까지 필요하신지</span><span class="w-v" style="font-size:14.5px;font-weight:600">급한 일정이 있으면 먼저</span></span></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>

"""
body = (body
  .replace("__CRUMB__", crumb(P, [(None, "문의")]))
  .replace("__K__", K)
  )

page("contact/index.html",
     "문의 — 상담과 견적은 무료입니다 | 온도컴퍼니",
     "카카오톡 오픈채팅으로 바로 물어보세요. 친구 추가 없이 대화가 열립니다. 업종이나 상황만 알려 주시면 예상 금액과 일정을 영업일 하루 안에 알려 드립니다.",
     body, P, "contact/")
print("contact/index.html")

# ══════════════ 404 ══════════════
P404 = ""
b404 = """
<section class="wrap nf">
  <div>
    <p class="nf-code">404</p>
    <h1>이 주소에는 페이지가 없습니다</h1>
    <p>주소가 바뀌었거나 잘못 입력되었을 수 있습니다. 아래에서 찾으시는 곳으로 가 보세요.</p>
    <div class="nf-btns">
      <a class="btn btn-pri btn-lg" href="./">홈으로 가기</a>
      <a class="btn btn-line btn-lg" href="./pricing/">요금 보기</a>
      <a class="btn btn-kko btn-lg" href="__K__" target="_blank" rel="noopener">카톡으로 물어보기</a>
    </div>
  </div>
</section>
""".replace("__K__", K)

page("404.html", "페이지를 찾을 수 없습니다 — 온도컴퍼니",
     "요청하신 주소에는 페이지가 없습니다. 온도컴퍼니 홈에서 다시 찾아보세요.",
     b404, P404, None, canon="404.html")
print("404.html")
