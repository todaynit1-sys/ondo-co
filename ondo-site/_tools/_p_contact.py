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
        <form class="form rv" id="cForm" action="__FORM__" method="POST">
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
            <select id="f-svc" name="service"
              style="width:100%;background:var(--paper);border:1.5px solid var(--line);border-radius:var(--r1);padding:13px 14px;font-size:16px">
              <option value="">아직 모르겠어요 · 추천 부탁드립니다</option>
              <option value="web">온도 웹 — 반응형 홈페이지</option>
              <option value="clip">온도 클립 — 홍보 숏폼</option>
              <option value="ai">온도 AI — 취업용 AI 결과물</option>
            </select>
          </div>
          <div class="form-row">
            <label for="f-msg">문의 내용 <span class="req">*</span></label>
            <textarea id="f-msg" name="message" placeholder="업종과 원하시는 느낌을 적어 주세요. 참고하고 싶은 사이트가 있으면 주소도 좋습니다."></textarea>
            <span class="form-err" id="e-msg" hidden>어떤 게 필요하신지 한 줄만 적어 주세요.</span>
          </div>
          <label class="hp" aria-hidden="true">이 칸은 비워 두세요<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label>
          <button class="btn btn-pri btn-lg btn-block" type="submit">문의 보내기</button>
          <p class="form-note">보내주신 내용은 문의 답변에만 사용합니다. 급하시면 카카오톡이 더 빠릅니다.</p>
        </form>

        <div class="form form-done rv" id="cDone" hidden>
          <div class="fd-i" aria-hidden="true">✓</div>
          <h3>문의가 전송되었습니다</h3>
          <p id="cDoneMsg">영업일 기준 하루 안에 답변드리겠습니다.<br>급하시면 카카오톡으로 연락 주세요.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow rv">Before you ask <span class="ko">이것만 알려 주시면 빨라요</span></p>
    <h2 class="rv">첫 메시지에 이 세 가지만</h2>
    <div class="curri">
      <div class="cu rv"><span class="cu-n">01</span><div><h3>어떤 일을 하시는지</h3><p>업종과 하시는 일. 취업 목적이면 지원하려는 직무나 공고면 충분합니다.</p></div></div>
      <div class="cu rv"><span class="cu-n">02</span><div><h3>왜 필요해지셨는지</h3><p>손님이 없어서인지, 보낼 링크가 없어서인지, 이력서에 쓸 게 없어서인지.</p></div></div>
      <div class="cu rv"><span class="cu-n">03</span><div><h3>언제까지 필요하신지</h3><p>급하신 일정이 있으면 먼저 말씀해 주세요. 가능한지 바로 알려 드립니다.</p></div></div>
      <div class="cu rv"><span class="cu-n">＋</span><div><h3>있으면 좋은 것</h3><p>참고하고 싶은 사이트 주소, 가지고 계신 사진, 예산 범위. 없어도 상담은 됩니다.</p></div></div>
    </div>
  </div>
</section>
"""

body = (body
  .replace("__CRUMB__", crumb(P, [(None, "문의")]))
  .replace("__K__", K)
  .replace("__FORM__", FORM_ACTION))

page("contact/index.html",
     "문의 — 상담과 견적은 무료입니다 | 온도컴퍼니",
     "카카오톡 오픈채팅으로 바로 물어보시거나 문의폼을 남겨 주세요. 업종이나 상황만 알려 주시면 예상 금액과 일정을 영업일 하루 안에 알려 드립니다.",
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
