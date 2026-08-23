from PIL import Image, ImageDraw, ImageFont
import os
INK=(11,16,32,255); BLUE=(27,91,255,255); WHITE=(255,255,255,255)
def mark(size, ink=INK, blue=BLUE, pad=0.10, ss=4):
    S=size*ss
    im=Image.new("RGBA",(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    u=S*(1-2*pad)/44.0; o=S*pad
    X=lambda v:o+v*u
    cx,cy,r,w=19,25,14,5.4
    d.ellipse([X(cx-r-w/2),X(cy-r-w/2),X(cx+r+w/2),X(cy+r+w/2)],fill=ink)
    d.ellipse([X(cx-r+w/2),X(cy-r+w/2),X(cx+r-w/2),X(cy+r-w/2)],fill=(0,0,0,0))
    d.ellipse([X(34.5-6.4),X(12-6.4),X(34.5+6.4),X(12+6.4)],fill=blue)
    return im.resize((size,size),Image.LANCZOS)
def icon(size, ss=4):
    S=size*ss
    im=Image.new("RGBA",(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle([0,0,S-1,S-1],radius=int(S*0.22),fill=WHITE)
    im.alpha_composite(mark(S,pad=0.17,ss=1))
    return im.resize((size,size),Image.LANCZOS)
os.makedirs("images",exist_ok=True)
icon(64).save("images/favicon.png")
icon(180).save("images/apple-touch-icon.png")
icon(512,ss=2).save("images/app-icon-512.png")
print("icons ok")
