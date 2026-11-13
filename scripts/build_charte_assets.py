import sys, os, subprocess
sys.argv = ["x"]
import build_logo5 as G
L = G.L
OUT = "/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/charte-assets/"
os.makedirs(OUT, exist_ok=True)
BLUE, RED, WHITE, PAPER = G.BLUE, G.RED, G.WHITE, G.PAPER
W, H, draw, stop = L.VARIANTS["C-compact"]
SANS = L.F["ExtraBold"]; MED = L.F["SemiBold"]

def save(name, w, h, body, px=None):
    f = OUT + name
    open(f + ".svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>')
    subprocess.run(["rsvg-convert", "-w", str(int(px or w*2)), f + ".svg", "-o", f + ".png"], check=True)

M = 60
save("logo", W + 2*M, H + 2*M, draw(M, M))
save("logo-blanc", W + 2*M, H + 2*M, draw(M, M, WHITE, WHITE))
hs = H*0.92; hg = H*0.2
save("logo-horizontal", hs+hg+W+2*M, H+2*M, G.table(M+hs/2, M+H/2, hs) + draw(M+hs+hg, M))
save("badge", 1200, 1200, G.badge(600, 600, 1080, SANS), px=1200)
save("badge-blanc", 1200, 1200, G.badge(600, 600, 1080, SANS, ink=WHITE, accent=WHITE).replace(f'fill="{WHITE}"/></g>', f'fill="{WHITE}"/></g>'), px=1200)
# white badge but guest chair kept red: rebuild table with red guest
b = G.table(600, 600, 1080*0.56, WHITE, RED) + G.arc_text(600,600,540*0.70,"PREMIER",SANS,1080*0.115,WHITE,True,0.34) + G.arc_text(600,600,540*0.70+1080*0.115*0.7,"SERVICE",SANS,1080*0.115,WHITE,False,0.34)
for sx in (-1,1): b += f'<circle cx="{600+sx*(540*0.70+1080*0.115*0.35):.1f}" cy="600" r="{1080*0.018:.1f}" fill="{WHITE}"/>'
save("badge-blanc", 1200, 1200, b, px=1200)
ic = 1024
save("icone", ic, ic, f'<rect width="{ic}" height="{ic}" rx="{ic*0.225}" fill="{BLUE}"/>' + G.table(ic/2, ic/2, ic*0.74, WHITE, RED), px=1024)
save("sigle-construction", 1200, 1200, G.construction(0, 0, 1200, 1200), px=1200)

# logo construction: x = cap height of SERVICE
x = stop  # wordmark-local y of SERVICE top
d0, sb = L.shape(L.F["ExtraBold"], "SERVICE", 100.0)
import wm7; cap = wm7.CAPH
P = cap  # protection = 1x
CW, CH = W + 2*P + 2*M + 300, H + 2*P + 2*M + 160
ox, oy = M + P + 150, M + P + 60
g = []
GR = "#9A9AA6"
g.append(f'<rect x="{ox-P}" y="{oy-P}" width="{W+2*P}" height="{H+2*P}" fill="none" stroke="{RED}" stroke-width="3" stroke-dasharray="14 10"/>')
g.append(f'<rect x="{ox}" y="{oy}" width="{W}" height="{H}" fill="none" stroke="{GR}" stroke-width="2"/>')
for yy in (oy + stop, oy + stop + cap):
    g.append(f'<path d="M{ox-P-40} {yy:.1f} H{ox+W+P+40}" stroke="{GR}" stroke-width="2"/>')
g.append(draw(ox, oy))
def lab(s, xx, yy, col=GR, size=34, anchor="start"):
    d, b = L.shape(MED, s, size); adv = b[2]-b[0]
    if anchor == "end": xx -= adv
    if anchor == "middle": xx -= adv/2
    return f'<path fill="{col}" transform="translate({xx:.1f},{yy:.1f})" d="{d}"/>'
# x marker
g.append(f'<path d="M{ox+W+P+20} {oy+stop:.1f} V{oy+stop+cap:.1f}" stroke="{BLUE}" stroke-width="4"/>')
g.append(lab("x", ox+W+P+40, oy+stop+cap/2+12, BLUE, 44))
g.append(lab("zone de protection = x", ox-P, oy-P-24, RED, 34))
g.append(lab("x = hauteur des capitales de SERVICE", ox-P, oy+H+P+70, GR, 34))
save("logo-construction", CW, CH, "".join(g))
print("ok", round(W), round(H), round(stop))
