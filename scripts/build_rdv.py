import sys, os, subprocess, base64, math
sys.argv = ["x"]
import build_logo5 as G
L = G.L
BLUE, RED, WHITE, PAPER = G.BLUE, G.RED, G.WHITE, G.PAPER
INK, GRIS = "#1A1D33", "#4F546E"
A = "/mnt/user-data/attachments/6e78a7ef-414c-585b-8c47-287188e20848/"
REG, SEMI, XB = A + "d9641225-Outfit-Regular.ttf", L.F["SemiBold"], L.F["ExtraBold"]
D = "/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/rdv/"
OUT = D + "out/"; os.makedirs(OUT, exist_ok=True)
W, H, draw, stop = L.VARIANTS["C-compact"]
ARGO_DARK = open("/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/sb-assets/argonautes-logo.svg").read()
def b64(p): return "data:image/png;base64," + base64.b64encode(open(p, "rb").read()).decode()
ARGO_DARK_PNG = b64("/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/premier-service_assets-video/05_les-argonautes/les-argonautes_logo_fond-clair.png")
ARGO_LIGHT_PNG = b64("/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/premier-service_assets-video/05_les-argonautes/les-argonautes_logo_fond-sombre.png")
ARGO_RATIO = 263.3 / 1088.21

GUESTS = [
 dict(key="vedrenne", n="1", first="Marie-Pierre", last="Vedrenne", title="Ministre déléguée à la Citoyenneté", place="Place Beauvau", when="Dîner, 9 novembre, place Beauvau"),
 dict(key="lombard", n="3", first="Éric", last="Lombard", title="Ancien ministre de l’Économie", place="[LIEU]", when="Petit-déjeuner, 18 novembre, [LIEU]"),
]
DATE = "[DATE]"

def text(path, s, size, x, y, fill, anchor="start", track=0.0):
    d, b = L.shape(path, s, size, track)
    adv = b[2] - b[0]
    if anchor == "middle": x -= adv / 2 + b[0]
    elif anchor == "end": x -= adv + b[0]
    else: x -= b[0]
    return f'<path fill="{fill}" transform="translate({x:.1f},{y:.1f})" d="{d}"/>'
def width(path, s, size):
    d, b = L.shape(path, s, size); return b[2] - b[0]

def framed(g, cx, cy, D_total, chair=BLUE, guest=RED, uid="a"):
    """Portrait cropped in a circle = the table; eleven chairs around it, the guest's (top) in red."""
    u = D_total / (2 * (G.R_RING + G.CH / 2 + 1.5))        # units -> px
    r = G.R_TABLE * u
    img = b64(D + g["key"] + ".png")
    s = 2 * r / 1180  # portrait crop: circle of radius 590 centred at (627, 600) in the 1254 image
    o = [f'<clipPath id="c{uid}"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}"/></clipPath>',
         f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#FAF5EC"/>',
         f'<image clip-path="url(#c{uid})" href="{img}" x="{cx - 627*s:.1f}" y="{cy - 600*s:.1f}" width="{1254*s:.1f}" height="{1254*s:.1f}"/>']
    for i in range(G.N):
        o.append(f'<rect x="{cx - G.CW*u/2:.1f}" y="{cy - (G.R_RING + G.CH/2)*u:.1f}" width="{G.CW*u:.1f}" height="{G.CH*u:.1f}" rx="{3.2*u:.1f}" '
                 f'fill="{guest if i == 0 else chair}" transform="rotate({i*360/G.N:.3f} {cx:.1f} {cy:.1f})"/>')
    return "".join(o)

def logo(x, y, w, r=RED, b=BLUE):
    k = w / W; return f'<g transform="translate({x:.1f},{y:.1f}) scale({k:.4f})">{draw(0, 0, r, b)}</g>'

def svg(w, h, body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'
def save(name, w, h, body, px=None):
    p = OUT + name; open(p + ".svg", "w").write(svg(w, h, body))
    subprocess.run(["rsvg-convert", "-w", str(px or w), p + ".svg", "-o", p + ".png"], check=True); return p + ".png"

def post(g):
    w, h = 1080, 1350; o = [f'<rect width="{w}" height="{h}" fill="{PAPER}"/>']
    o.append(logo(64, 56, 300))
    o.append(text(SEMI, f"Rendez-vous n°{g['n']}", 36, w - 72, 128, RED, "end"))
    o.append(framed(g, w/2, 610, 700, uid="p"))
    o.append(text(XB, f"{g['first']} {g['last']}", 78 if len(g['first']+g['last']) < 20 else 70, 72, 1095, BLUE))
    o.append(text(REG, g["title"], 34, 72, 1150, INK))
    o.append(text(SEMI, g["when"], 36, 72, 1262, BLUE))
    o.append(f'<image href="{ARGO_DARK_PNG}" x="{w - 72 - 190}" y="{1262 - 190*ARGO_RATIO + 6:.1f}" width="190" height="{190*ARGO_RATIO:.1f}"/>')
    return save(f"insta-{g['key']}", w, h, "".join(o))

def story(g):
    w, h = 1080, 1920; o = [f'<rect width="{w}" height="{h}" fill="{PAPER}"/>']
    o.append(logo((w - 420) / 2, 120, 420))
    o.append(framed(g, w/2, 840, 860, uid="s"))
    o.append(text(SEMI, f"Rendez-vous n°{g['n']}", 40, w/2, 1400, RED, "middle"))
    o.append(text(XB, g["first"], 92, w/2, 1500, BLUE, "middle"))
    o.append(text(XB, g["last"], 92, w/2, 1598, BLUE, "middle"))
    o.append(text(REG, g["title"], 34, w/2, 1666, INK, "middle"))
    o.append(text(SEMI, g["when"], 38, w/2, 1736, BLUE, "middle"))
    o.append(text(REG, "Avec le soutien des", 26, w/2 - 10, 1846, GRIS, "end"))
    o.append(f'<image href="{ARGO_DARK_PNG}" x="{w/2 + 10}" y="{1846 - 150*ARGO_RATIO + 8:.1f}" width="150" height="{150*ARGO_RATIO:.1f}"/>')
    return save(f"story-{g['key']}", w, h, "".join(o))

def linkedin(g):
    w, h = 1200, 627; o = [f'<rect width="{w}" height="{h}" fill="{BLUE}"/>']
    o.append(framed(g, 320, h/2, 540, chair=PAPER, uid="l"))
    o.append(logo(640, 64, 250, WHITE, WHITE))
    o.append(text(SEMI, f"Rendez-vous n°{g['n']}", 30, 640, 270, PAPER))
    o.append(text(XB, g["first"], 64, 640, 340, WHITE))
    o.append(text(XB, g["last"], 64, 640, 410, WHITE))
    o.append(text(REG, g["title"], 25, 640, 462, "#DDE0EF"))
    o.append(text(SEMI, g["when"], 30, 640, 540, WHITE))
    return save(f"linkedin-{g['key']}", w, h, "".join(o))

def affiche(g):
    w, h = 1190, 1684; o = [f'<rect width="{w}" height="{h}" fill="{BLUE}"/>']
    o.append(logo((w - 560) / 2, 90, 560, WHITE, WHITE))
    o.append(framed(g, w/2, 790, 780, chair=PAPER, uid="f"))
    o.append(text(SEMI, f"Rendez-vous n°{g['n']}", 40, w/2, 1250, PAPER, "middle"))
    o.append(text(XB, f"{g['first']} {g['last']}", 86 if len(g['first']+g['last']) < 20 else 78, w/2, 1350, WHITE, "middle"))
    o.append(text(REG, g["title"], 36, w/2, 1414, "#DDE0EF", "middle"))
    o.append(text(SEMI, g["when"], 40, w/2, 1490, WHITE, "middle"))
    o.append(text(REG, "Dix étudiants, une invitée, une table." if g["key"] == "vedrenne" else "Dix étudiants, un invité, une table.", 30, w/2, 1556, "#DDE0EF", "middle"))
    o.append(text(REG, "Avec le soutien des", 24, w/2 - 10, 1630, "#C9CDE3", "end"))
    o.append(f'<image href="{ARGO_LIGHT_PNG}" x="{w/2 + 10}" y="{1630 - 140*ARGO_RATIO + 8:.1f}" width="140" height="{140*ARGO_RATIO:.1f}"/>')
    return save(f"affiche-{g['key']}", w, h, "".join(o))

def portrait_only(g):
    return save(f"portrait-cadre-{g['key']}", 1000, 1000, framed(g, 500, 500, 980, uid="o"), px=1200)

files = {}
for g in GUESTS:
    files[g["key"]] = dict(insta=post(g), story=story(g), linkedin=linkedin(g), affiche=affiche(g), portrait=portrait_only(g))

# ---------- mockups ----------
SH = '<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="24" stdDeviation="28" flood-color="#1A1D33" flood-opacity="0.22"/></filter>'
def phone(x, y, w, img, rot=0, avatar=True):
    """generic phone: dark body, screen with a profile row, the post, and an action row (generic glyphs)."""
    h = w * 1.86; pad = w * 0.045; sw = w - 2 * pad; sx = x + pad; sy = y + pad
    ph = sw * 1350 / 1080; top = sy + w * 0.20
    badge = b64("/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/premier-service_assets-video/02_sigle-badge/premier-service_badge_couleur.png")
    o = [f'<g transform="rotate({rot} {x + w/2:.1f} {y + h/2:.1f})" filter="url(#sh)">',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h:.1f}" rx="{w*0.13:.1f}" fill="#16171D"/>',
         f'<rect x="{sx:.1f}" y="{sy:.1f}" width="{sw:.1f}" height="{h - 2*pad:.1f}" rx="{w*0.10:.1f}" fill="#FFFFFF"/>',
         f'<rect x="{x + w*0.36:.1f}" y="{sy + w*0.03:.1f}" width="{w*0.28:.1f}" height="{w*0.07:.1f}" rx="{w*0.035:.1f}" fill="#16171D"/>',
         f'<image href="{badge}" x="{sx + sw*0.04:.1f}" y="{top - sw*0.115:.1f}" width="{sw*0.09:.1f}" height="{sw*0.09:.1f}"/>',
         text(SEMI, "premierservice", sw * 0.042, sx + sw * 0.15, top - sw * 0.052, INK),
         f'<image href="{b64(img)}" x="{sx:.1f}" y="{top:.1f}" width="{sw:.1f}" height="{ph:.1f}"/>']
    ay = top + ph + sw * 0.07; s = sw * 0.06
    gx = sx + sw * 0.05
    o.append(f'<path d="M{gx+s/2:.1f} {ay+s*0.85:.1f} C{gx-s*0.2:.1f} {ay+s*0.3:.1f} {gx+s*0.1:.1f} {ay-s*0.2:.1f} {gx+s/2:.1f} {ay+s*0.15:.1f} C{gx+s*0.9:.1f} {ay-s*0.2:.1f} {gx+s*1.2:.1f} {ay+s*0.3:.1f} {gx+s/2:.1f} {ay+s*0.85:.1f}Z" fill="{RED}"/>')
    o.append(f'<circle cx="{gx + s*1.9:.1f}" cy="{ay + s*0.4:.1f}" r="{s*0.42:.1f}" fill="none" stroke="{INK}" stroke-width="{s*0.1:.1f}"/>')
    o.append(f'<path d="M{gx+s*2.8:.1f} {ay+s*0.8:.1f} L{gx+s*3.6:.1f} {ay:.1f} L{gx+s*3.2:.1f} {ay+s*0.9:.1f}Z" fill="none" stroke="{INK}" stroke-width="{s*0.1:.1f}" stroke-linejoin="round"/>')
    o.append(text(SEMI, "128 J’aime", sw * 0.038, sx + sw * 0.05, ay + s * 1.9, INK))
    o.append(text(REG, "Premier rendez-vous. Dix étudiants, une table.", sw * 0.034, sx + sw * 0.05, ay + s * 2.8, GRIS))
    o.append("</g>")
    return "".join(o)

def mock_insta():
    w, h = 2400, 1500; o = [SH, f'<rect width="{w}" height="{h}" fill="#1E2F86"/>']
    o.append(f'<circle cx="1200" cy="760" r="620" fill="#26389A"/>')
    o.append(phone(560, 150, 560, files["vedrenne"]["insta"], -4))
    o.append(phone(1280, 170, 560, files["lombard"]["insta"], 4))
    return save("mockup-instagram", w, h, "".join(o), px=2400)

def mock_story():
    w, h = 2400, 1500; o = [SH, f'<rect width="{w}" height="{h}" fill="{PAPER}"/>']
    for i, (g, rot) in enumerate((("vedrenne", -3), ("lombard", 3))):
        x = 700 + i * 560; ww = 460; hh = ww * 2.05; pad = ww * 0.045
        o.append(f'<g transform="rotate({rot} {x + ww/2} {130 + hh/2})" filter="url(#sh)"><rect x="{x}" y="130" width="{ww}" height="{hh:.1f}" rx="{ww*0.13:.1f}" fill="#16171D"/>'
                 f'<clipPath id="st{i}"><rect x="{x+pad:.1f}" y="{130+pad:.1f}" width="{ww-2*pad:.1f}" height="{hh-2*pad:.1f}" rx="{ww*0.10:.1f}"/></clipPath>'
                 f'<image clip-path="url(#st{i})" href="{b64(files[g]["story"])}" x="{x+pad:.1f}" y="{130+pad + (hh-2*pad - (ww-2*pad)*1920/1080)/2:.1f}" width="{ww-2*pad:.1f}" height="{(ww-2*pad)*1920/1080:.1f}" preserveAspectRatio="xMidYMid slice"/></g>')
    return save("mockup-stories", w, h, "".join(o), px=2400)

def mock_linkedin():
    w, h = 2400, 1500; o = [SH, f'<rect width="{w}" height="{h}" fill="#EEF0F4"/>']
    badge = b64("/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/premier-service_assets-video/02_sigle-badge/premier-service_badge_couleur.png")
    cw = 1500; cx = (w - cw) / 2; cy = 60
    ih = cw * 627 / 1200
    o.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ih + 360:.0f}" rx="18" fill="#FFFFFF" filter="url(#sh)"/>')
    o.append(f'<image href="{badge}" x="{cx+36}" y="{cy+36}" width="84" height="84"/>')
    o.append(text(SEMI, "Premier Service", 40, cx + 150, cy + 76, INK))
    o.append(text(REG, "Il y a 2 heures", 26, cx + 140, cy + 110, "#6B6F85"))
    lines = ["Premier rendez-vous de Premier Service : dix étudiants dînent avec",
             "Marie-Pierre Vedrenne, place Beauvau. Ce qui se dit à table reste à table."]
    for i, ln in enumerate(lines): o.append(text(REG, ln, 36, cx + 40, cy + 178 + i * 46, INK))
    o.append(f'<image href="{b64(files["vedrenne"]["linkedin"])}" x="{cx}" y="{cy + 250}" width="{cw}" height="{ih:.0f}"/>')
    ry = cy + 250 + ih + 64
    o.append(f'<circle cx="{cx+56}" cy="{ry-10}" r="18" fill="{BLUE}"/><circle cx="{cx+86}" cy="{ry-10}" r="18" fill="{RED}"/>')
    o.append(text(REG, "Réactions et commentaires", 28, cx + 120, ry, "#6B6F85"))
    return save("mockup-linkedin", w, h, "".join(o), px=2400)

def mock_affiches():
    w, h = 2400, 1500; o = [SH, f'<rect width="{w}" height="{h}" fill="#E7E1D6"/>', f'<rect y="1260" width="{w}" height="240" fill="#CFC7B8"/>']
    pw = 640; ph = pw * 1684 / 1190
    for i, g in enumerate(("vedrenne", "lombard")):
        x = 440 + i * (pw + 240); y = 130
        o.append(f'<rect x="{x-18}" y="{y-18}" width="{pw+36}" height="{ph+36:.0f}" fill="#F7F5F0" filter="url(#sh)"/>')
        o.append(f'<image href="{b64(files[g]["affiche"])}" x="{x}" y="{y}" width="{pw}" height="{ph:.0f}"/>')
    return save("mockup-affiches", w, h, "".join(o), px=2400)

print(mock_insta(), mock_story(), mock_linkedin(), mock_affiches())
