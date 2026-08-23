from PIL import Image, ImageDraw, ImageFont
from _img import mark
import os
W,H=1200,630
base=Image.new("RGB",(W,H))
d=ImageDraw.Draw(base)
stops=[(0.0,(13,40,150)),(0.40,(27,91,255)),(0.70,(109,59,224)),(1.0,(226,88,18))]
for x in range(W):
    t=x/(W-1); c=(0,0,0)
    for i in range(len(stops)-1):
        a,ca=stops[i]; b,cb=stops[i+1]
        if a<=t<=b:
            k=(t-a)/(b-a)
            c=tuple(int(ca[j]+(cb[j]-ca[j])*k) for j in range(3)); break
    d.line([(x,0),(x,H)],fill=c)
ov=Image.new("RGBA",(W,H),(6,9,20,140))
base=Image.alpha_composite(base.convert("RGBA"),ov)
d=ImageDraw.Draw(base,"RGBA")
KB="/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc"
KM="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
KR="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
F=lambda p,s: ImageFont.truetype(p,s)
m=mark(70,ink=(255,255,255,255),blue=(130,175,255,255),pad=0.02)
base.paste(m,(82,66),m)
d.text((172,70),"ONDO°",font=F(KB,40),fill=(255,255,255,255))
d.text((174,120),"온도컴퍼니",font=F(KR,20),fill=(255,255,255,185))
d.text((82,204),"보여야, 연락이 옵니다.",font=F(KB,72),fill=(255,255,255,255))
d.text((82,312),"찾아봤을 때 안 나오면 없는 겁니다.",font=F(KR,25),fill=(255,255,255,210))
d.text((82,350),"가게와 사람이 온라인에서 보이게 만듭니다.",font=F(KR,25),fill=(255,255,255,210))
chips=[("온도 웹","반응형 홈페이지",300),("온도 클립","홍보 숏폼",270),("온도 AI","취업용 AI 결과물",330)]
x=82
for t,s,w in chips:
    d.rounded_rectangle([x,432,x+w,532],radius=22,fill=(255,255,255,40),outline=(255,255,255,90),width=2)
    d.text((x+26,452),t,font=F(KM,30),fill=(255,255,255,255))
    d.text((x+26,492),s,font=F(KR,19),fill=(255,255,255,195))
    x+=w+16
d.text((82,562),"배포 주소까지 납품 · 월 호스팅비 0원 · 상담과 견적은 무료",font=F(KR,21),fill=(255,255,255,175))
base.convert("RGB").save("images/og.png",optimize=True)
print("og ok",os.path.getsize("images/og.png"))
