import sys, os, subprocess, math
sys.argv = ["x"]
import build_logo5 as G
L = G.L
BLUE, RED, WHITE, PAPER = G.BLUE, G.RED, G.WHITE, G.PAPER
ROOT = "/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/premier-service_assets-video/"
W, H, draw, stop = L.VARIANTS["C-compact"]; SANS = L.F["ExtraBold"]
def save(rel, w, h, body, px=None):
    f = ROOT + rel; os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f + ".svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>')
    subprocess.run(["rsvg-convert", "-w", str(int(px or 3840)), f + ".svg", "-o", f + ".png"], check=True)
M = 60
for suf, r, b in (("couleur", RED, BLUE), ("blanc", WHITE, WHITE)):
    save(f"01_logos/premier-service_logo_{suf}", W+2*M, H+2*M, draw(M, M, r, b))
    hs, hg = H*0.92, H*0.2
    save(f"01_logos/premier-service_logo-horizontal_{suf}", hs+hg+W+2*M, H+2*M, G.table(M+hs/2, M+H/2, hs, b, RED) + draw(M+hs+hg, M, r, b))
    ts, g = H*0.55, H*0.14
    save(f"01_logos/premier-service_logo-vertical_{suf}", W+2*M, ts+g+H+2*M, G.table(M+W/2, M+ts/2, ts, b, RED) + draw(M, M+ts+g, r, b))
    save(f"02_sigle-badge/premier-service_sigle_{suf}", 600, 600, G.table(300, 300, 540, b, RED), px=2160)
    bb = G.table(600, 600, 1080*0.56, b, RED) + G.arc_text(600,600,540*0.70,"PREMIER",SANS,1080*0.115,b,True,0.34) + G.arc_text(600,600,540*0.70+1080*0.115*0.7,"SERVICE",SANS,1080*0.115,(RED if suf=="couleur" else WHITE),False,0.34)
    for sx in (-1,1): bb += f'<circle cx="{600+sx*(540*0.70+1080*0.115*0.35):.1f}" cy="600" r="{1080*0.018:.1f}" fill="{b}"/>'
    save(f"02_sigle-badge/premier-service_badge_{suf}", 1200, 1200, bb, px=2160)
ic = 1024
save("02_sigle-badge/premier-service_icone", ic, ic, f'<rect width="{ic}" height="{ic}" rx="{ic*0.225}" fill="{BLUE}"/>' + G.table(ic/2, ic/2, ic*0.74, WHITE, RED), px=1024)

# ---- layers for animation: every layer on the SAME canvas, so they stack in place ----
CW, CH = W + 2*M, H + 2*M
src = draw(M, M)   # two paths: Premier (red) then SERVICE (blue)
premier, service = src.split("/>", 1)[0] + "/>", src.split("/>", 1)[1]
import wm7
for suf, col in (("ciel", wm7.SKY), ("blanc", WHITE)):
    save(f"03_calques-animation/logo/premier_{suf}", CW, CH, premier.replace(f'fill="{wm7.SKY}"', f'fill="{col}"'))
for suf, col in (("bleu", BLUE), ("blanc", WHITE)):
    save(f"03_calques-animation/logo/service_{suf}", CW, CH, service.replace(f'fill="{BLUE}"', f'fill="{col}"'))
# sigle layers: table, the 10 student chairs one by one, the guest chair
S = 600; k = 540/100.0; ox = oy = 30
def chair(i, col):
    return (f'<g transform="translate({ox},{oy}) scale({k:.4f})"><rect x="{50-G.CW/2}" y="{50-G.R_RING-G.CH/2}" width="{G.CW}" height="{G.CH}" rx="3.2" '
            f'fill="{col}" transform="rotate({i*360/G.N:.3f} 50 50)"/></g>')
save("03_calques-animation/sigle/sigle_table", S, S, f'<g transform="translate({ox},{oy}) scale({k:.4f})"><circle cx="50" cy="50" r="{G.R_TABLE}" fill="{BLUE}"/></g>', px=2160)
save("03_calques-animation/sigle/sigle_chaise-invite", S, S, chair(0, RED), px=2160)
for i in range(1, G.N):
    save(f"03_calques-animation/sigle/sigle_chaise-{i:02d}", S, S, chair(i, BLUE), px=2160)
# one layered SVG with named groups, for After Effects / Figma import
lay = (f'<g id="table"><g transform="translate({ox},{oy}) scale({k:.4f})"><circle cx="50" cy="50" r="{G.R_TABLE}" fill="{BLUE}"/></g></g>'
       f'<g id="chaise-invite">{chair(0, RED)}</g>' + "".join(f'<g id="chaise-{i:02d}">{chair(i, BLUE)}</g>' for i in range(1, G.N)))
save("03_calques-animation/sigle/sigle_calques-nommes", S, S, lay, px=2160)
lay2 = f'<g id="premier">{premier}</g><g id="service">{service}</g>'
save("03_calques-animation/logo/logo_calques-nommes", CW, CH, lay2)

# colours
os.makedirs(ROOT + "04_couleurs", exist_ok=True)
open(ROOT + "04_couleurs/couleurs.txt", "w").write(
"Premier Service — couleurs\n\nBleu marine  #1E2F86   RVB 30 47 134    SERVICE, table du sigle, titres\nCiel profond #2C86D1   RVB 44 134 209   « Premier » uniquement\nRouge        #E0313B   RVB 224 49 59    chaise de l'invité, SERVICE du badge\nBlanc cassé  #FAF7F0   RVB 250 247 240  fonds\nBlanc        #FFFFFF                    fond du logo, logo blanc sur bleu\n\nValeurs CMJN / Pantone : à établir avec l'imprimeur.\n")
sw = "".join(f'<rect x="{i*400}" y="0" width="400" height="400" fill="{c}"/>' for i, c in enumerate((BLUE, '#2C86D1', RED, PAPER, WHITE)))
save("04_couleurs/palette", 2000, 400, sw, px=2000)

open(ROOT + "LISEZ-MOI.txt", "w").write("""PREMIER SERVICE — ASSETS POUR LA VIDÉO ET LE MOTION DESIGN
Version 2, 13 novembre 2026

01_logos
  Logo seul, logo horizontal (sigle à gauche), logo vertical (sigle au-dessus).
  Chaque version en couleur et en blanc. SVG vectoriel + PNG transparent 3840 px de large.

02_sigle-badge
  Sigle (la table et ses onze chaises), badge rond « PREMIER / SERVICE », icône.
  PNG transparent 2160 px.

03_calques-animation
  logo/   « Premier » et « SERVICE » séparés, chacun sur le même canevas que le logo complet :
          les empiler à la même position reconstitue le logo exact.
          logo_calques-nommes.svg : un seul fichier, groupes « premier » et « service ».
  sigle/  la table, les dix chaises des étudiants (01 à 10) et la chaise de l'invité, chacune
          sur le même canevas de 600 × 600 (PNG 2160 px). sigle_calques-nommes.svg : un seul
          fichier, groupes « table », « chaise-01 » à « chaise-10 », « chaise-invite ».

04_couleurs
  Bleu marine #1E2F86 · Ciel profond #2C86D1 · Rouge #E0313B · Blanc cassé #FAF7F0 · Blanc #FFFFFF

RÈGLES
  - Ne jamais déformer, pivoter, recolorer ni ajouter d'ombre ou de contour.
  - Zone de protection autour du logo : la hauteur des capitales de SERVICE.
  - Fond clair : version couleur. Fond bleu, sombre ou image : version blanche.
  - Le ciel profond est réservé à « Premier » ; le rouge à la chaise de l'invité (et à SERVICE dans le badge).
  - Jamais le logo et le badge dans le même plan.
  - Le texte du logo est vectorisé : aucune police à installer pour l'utiliser.
  - Pour les textes à l'écran : police Outfit (gratuite, Google Fonts), ExtraBold pour les titres.
    La police de « Premier » (Breathing) ne sert jamais à composer d'autre texte.

PISTES D'ANIMATION (suggestions)
  - Sigle : la table apparaît, puis les dix chaises une à une autour, la chaise rouge de
    l'invité en dernier, en haut.
  - Logo : « Premier » se trace comme une écriture à la main, puis « SERVICE » se pose dessous.
  - Mouvements doux, sans rebond ; durée totale d'une signature : 1,5 à 2,5 s.
""")
print("ok")
