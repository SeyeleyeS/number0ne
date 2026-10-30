"""Regenerate Number One brand images (OG card + favicons). Run from repo root: python3 tools/make_brand_images.py"""
from PIL import Image, ImageDraw, ImageFont
D="/usr/share/fonts/truetype/dejavu/"
INK=(11,22,48); TEAL=(45,212,191); GOLD=(201,150,58); WHITE=(255,255,255); MUTED=(160,176,200)
im=Image.new("RGB",(1200,630),INK); d=ImageDraw.Draw(im)
for i in range(0,1200,40): d.line([(i,0),(i,630)],fill=(16,30,60))
d.rectangle([0,616,1200,630],fill=TEAL)
d.rounded_rectangle([80,80,152,152],radius=16,fill=WHITE)
d.text((116,116),"N1",font=ImageFont.truetype(D+"DejaVuSans-Bold.ttf",32),fill=INK,anchor="mm")
d.text((172,116),"Number One",font=ImageFont.truetype(D+"DejaVuSans-Bold.ttf",40),fill=WHITE,anchor="lm")
serif=ImageFont.truetype(D+"DejaVuSerif-Bold.ttf",58)
d.text((80,225),"Every business is missing",font=serif,fill=WHITE)
d.text((80,302),"new business somewhere.",font=serif,fill=WHITE)
d.text((80,420),"We build custom AI agents that close the gap.",font=ImageFont.truetype(D+"DejaVuSans.ttf",32),fill=TEAL)
d.text((80,490),"number0ne.com  ·  Partner of Bay Area Media",font=ImageFont.truetype(D+"DejaVuSans.ttf",28),fill=MUTED)
im.save("assets/og-image.png",optimize=True)
def icon(n,path):
    i=Image.new("RGB",(n,n),INK); g=ImageDraw.Draw(i)
    g.rectangle([0,int(n*.875),n,n],fill=TEAL)
    g.text((n/2,n*.46),"N1",font=ImageFont.truetype(D+"DejaVuSans-Bold.ttf",int(n*.42)),fill=WHITE,anchor="mm")
    i.save(path,optimize=True)
icon(32,"favicon-32.png"); icon(180,"apple-touch-icon.png")
