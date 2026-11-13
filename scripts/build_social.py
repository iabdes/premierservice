import os, subprocess, base64, math
import wm7; G = wm7.G; L = wm7.L
A = "/mnt/user-data/attachments/6e78a7ef-414c-585b-8c47-287188e20848/"
REG, MED, SEMI, BOLD, XB = A+"d9641225-Outfit-Regular.ttf", A+"6936f351-Outfit-Medium.ttf", A+"7164757e-Outfit-SemiBold.ttf", A+"a976a5a1-Outfit-Bold.ttf", A+"b647ff33-Outfit-ExtraBold.ttf"
BLUE, SKY, RED, PAPER, WHITE, INK, GRIS = "#1E2F86", "#2C86D1", "#E0313B", "#FAF7F0", "#FFFFFF", "#1A1D33", "#4F546E"
SB, SM = "#DDE0EF", "#C9CDE3"
OUT = "social/"; os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350
LW, LH, ldraw, _ = L.VARIANTS["C-compact"]
def b64(p, mime="image/png"): return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()
ARGO_C = b64("premier-service_assets-video/05_les-argonautes/les-argonautes_logo_fond-clair.png")
ARGO_S = b64("premier-service_assets-video/05_les-argonautes/les-argonautes_logo_fond-sombre.png")
AR = 263.3 / 1088.21
def T(font, s, size, x, y, fill, anchor="start", track=0.0):
    d, b = L.shape(font, s, size, track); adv = b[2]-b[0]
    if anchor == "middle": x -= adv/2 + b[0]
    elif anchor == "end": x -= adv + b[0]
    else: x -= b[0]
    return f'<path fill="{fill}" transform="translate({x:.1f},{y:.1f})" d="{d}"/>'
def wid(font, s, size): _, b = L.shape(font, s, size); return b[2]-b[0]
def wrap(font, s, size, maxw):
    lines, cur = [], ""
    for w in s.split(" "):
        t = (cur + " " + w).strip()
        if cur and wid(font, t, size) > maxw: lines.append(cur); cur = w
        else: cur = t
    lines.append(cur); return lines
def para(font, s, size, x, y, fill, maxw, lh=1.18, anchor="start"):
    out = []; ls = wrap(font, s, size, maxw)
    for i, l in enumerate(ls): out.append(T(font, l, size, x, y + i*size*lh, fill, anchor))
    return "".join(out), y + (len(ls)-1)*size*lh
def logo(x, y, w, white=False):
    k = w / LW; c = (WHITE, WHITE) if white else (None, None)
    return f'<g transform="translate({x:.1f},{y:.1f}) scale({k:.4f})">{ldraw(0, 0, *c)}</g>'
def frame(i, n, dark=False):
    """header logo + page counter + swipe cue"""
    o = [logo(64, 56, 210, dark)]
    o.append(T(SEMI, f"{i}/{n}", 26, W-64, 104, SM if dark else GRIS, "end"))
    if i < n:
        col = WHITE if dark else BLUE
        o.append(f'<g transform="translate({W-64-44},{H-92})"><circle cx="22" cy="22" r="22" fill="{col}"/><path d="M15 22h14M23 15l7 7-7 7" stroke="{BLUE if dark else WHITE}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return "".join(o)
def portrait(slug, cx, cy, r, ring=WHITE, uid="p"):
    img = b64(f"ds-up/portraits/premier-service_portrait_{slug}.jpg", "image/jpeg")
    return (f'<clipPath id="{uid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<circle cx="{cx}" cy="{cy}" r="{r+8}" fill="{ring}"/>'
            f'<image clip-path="url(#{uid})" href="{img}" x="{cx-r}" y="{cy-r}" width="{2*r}" height="{2*r}" preserveAspectRatio="xMidYMid slice"/>')
def at_table(slug, cx, cy, D, chair=BLUE, uid="t"):
    u = D / (2*(G.R_RING + G.CH/2 + 1.5)); r = G.R_TABLE*u
    o = [portrait(slug, cx, cy, r, PAPER, uid)]
    for i in range(G.N):
        o.append(f'<rect x="{cx-G.CW*u/2:.1f}" y="{cy-(G.R_RING+G.CH/2)*u:.1f}" width="{G.CW*u:.1f}" height="{G.CH*u:.1f}" rx="{3.2*u:.1f}" fill="{RED if i==0 else chair}" transform="rotate({i*360/G.N:.3f} {cx} {cy})"/>')
    return "".join(o)
def moon(x, y, s, c): return f'<g transform="translate({x},{y}) scale({s/24:.3f})"><path d="M15.5 3.2A9 9 0 1 0 20.8 15 7.2 7.2 0 0 1 15.5 3.2Z" fill="{c}"/></g>'
def sun(x, y, s, c): return f'<g transform="translate({x},{y}) scale({s/24:.3f})"><circle cx="12" cy="12" r="4.6" fill="{c}"/><path d="M12 1.8v3M12 19.2v3M1.8 12h3M19.2 12h3M4.8 4.8l2.1 2.1M17.1 17.1l2.1 2.1M4.8 19.2l2.1-2.1M17.1 6.9l2.1-2.1" stroke="{c}" stroke-width="2" stroke-linecap="round"/></g>'
def save(name, body, bg=PAPER):
    p = OUT + name
    open(p + ".svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}"><rect width="{W}" height="{H}" fill="{bg}"/>{body}</svg>')
    subprocess.run(["rsvg-convert", "-w", str(W), p + ".svg", "-o", p + ".png"], check=True); os.remove(p + ".svg"); return p + ".png"
def argo_slide(prefix, i, n, cta):
    o = [frame(i, n, True)]
    t, y = para(XB, "Ce projet est soutenu par Les Argonautes.", 64, 96, 420, WHITE, 880, 1.08); o.append(t)
    t, y = para(REG, "Cabinet de conseil et d’exécution dédié au secteur public.", 38, 96, y + 90, SB, 860, 1.3); o.append(t)
    o.append(f'<rect x="96" y="{y+70:.0f}" width="560" height="{560*AR+56:.0f}" rx="24" fill="{PAPER}"/>')
    o.append(f'<image href="{ARGO_C}" x="124" y="{y+98:.0f}" width="504" height="{504*AR:.0f}"/>')
    o.append(T(SEMI, "lesargos.fr", 40, 96, y + 70 + 560*AR + 56 + 90, WHITE))
    if cta: o.append(T(MED, cta, 30, 96, H - 120, SM))
    return save(f"{prefix}-{i:02d}", "".join(o), BLUE)

files = {}
# ---------- Carrousel 1 : teasing ----------
n = 6; c = []
o = [frame(1, n, True)]
t, y = para(XB, "Servir l’État, ça s’apprend comment ?", 104, 96, 520, WHITE, 900, 1.02); o.append(t)
o.append(T(MED, "Une question que beaucoup d’étudiants se posent.", 34, 96, y + 110, SB))
c.append(save("c1-01", "".join(o), BLUE))
o = [frame(2, n)]
t, y = para(XB, "Les étudiants qui veulent s’engager ont des questions.", 76, 96, 420, BLUE, 900, 1.06); o.append(t)
t, y = para(XB, "Celles et ceux qui ont exercé ont des réponses.", 76, 96, y + 140, SKY, 900, 1.06); o.append(t)
c.append(save("c1-02", "".join(o)))
o = [frame(3, n)]
t, y = para(XB, "Mais ils se croisent rarement.", 92, 96, 470, BLUE, 900, 1.04); o.append(t)
t, y = para(REG, "Un amphithéâtre, une conférence, une photo. Rarement le temps d’une vraie conversation.", 40, 96, y + 120, GRIS, 860, 1.35); o.append(t)
c.append(save("c1-03", "".join(o)))
o = [frame(4, n)]
t, y = para(XB, "Entre ceux qui ont servi l’État et ceux qui le serviront, il manquait une table.", 74, 96, 380, BLUE, 900, 1.08); o.append(t)
sx = 540; o.append(f'<g transform="translate({sx-150},{y+90}) scale(0.5)">{G.table(300, 300, 540)}</g>')
c.append(save("c1-04", "".join(o)))
o = [frame(5, n)]
o.append(f'<g transform="translate(270,250) scale(0.9)">{G.table(300, 300, 540)}</g>')
o.append(T(XB, "Dix étudiants.", 70, 540, 930, BLUE, "middle"))
o.append(T(XB, "Une personnalité publique.", 70, 540, 1012, BLUE, "middle"))
o.append(T(XB, "À huis clos.", 70, 540, 1094, RED, "middle"))
o.append(T(SEMI, "Bientôt.", 44, 540, 1190, GRIS, "middle"))
c.append(save("c1-05", "".join(o)))
c.append(argo_slide("c1", 6, n, None))
files["c1"] = c

# ---------- Carrousel 3 : concept + club ----------
n = 7; c = []
o = [frame(1, n, True)]
t, y = para(XB, "Premier Service, c’est quoi ?", 110, 96, 560, WHITE, 900, 1.0); o.append(t)
o.append(T(MED, "En six images.", 36, 96, y + 110, SB))
c.append(save("c3-01", "".join(o), BLUE))
o = [frame(2, n)]
o.append(f'<g transform="translate(240,210)">{G.table(300, 300, 600)}</g>')
o.append(T(XB, "Une table.", 84, 96, 1000, BLUE))
t, y = para(REG, "Dix étudiants et une personnalité de la vie publique. Assez peu pour que chacun parle.", 38, 96, 1075, GRIS, 880, 1.32); o.append(t)
c.append(save("c3-02", "".join(o)))
o = [frame(3, n)]
o.append(f'<g transform="translate(96,330) scale(4)"><path d="M18 36V24a14 14 0 0 1 28 0v12" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linecap="round"/><rect x="8" y="36" width="48" height="38" rx="9" fill="{BLUE}"/><circle cx="32" cy="52" r="5" fill="{PAPER}"/><rect x="29.5" y="54" width="5" height="10" rx="2.5" fill="{PAPER}"/></g>')
o.append(T(XB, "À huis clos.", 84, 96, 790, BLUE))
t, y = para(XB, "Ce qui se dit à table reste à table.", 56, 96, 900, RED, 880, 1.12); o.append(t)
t, y = para(REG, "Pas de caméra pendant l’échange, pas de citation sans accord.", 36, 96, y + 90, GRIS, 880, 1.3); o.append(t)
c.append(save("c3-03", "".join(o)))
o = [frame(4, n)]
o.append(T(XB, "Deux formats.", 84, 96, 360, BLUE))
o.append(f'<rect x="96" y="440" width="888" height="300" rx="28" fill="{BLUE}"/>' + moon(140, 500, 110, WHITE) + T(XB, "Le dîner", 64, 300, 590, WHITE) + T(REG, "Le soir, pour prendre le temps.", 34, 300, 650, SB))
o.append(f'<rect x="96" y="780" width="888" height="300" rx="28" fill="{WHITE}"/>' + sun(140, 840, 110, RED) + T(XB, "Le petit-déjeuner", 64, 300, 930, BLUE) + T(REG, "Le matin, quand l’agenda est serré.", 34, 300, 990, GRIS))
c.append(save("c3-04", "".join(o)))
o = [frame(5, n)]
o.append(T(XB, "Saison 1 : douze invités.", 70, 96, 300, BLUE))
o.append(T(MED, "Novembre – décembre 2026", 34, 96, 360, GRIS))
SL = ["marie-pierre-vedrenne","olivier-faure","eric-lombard","jerome-guedj","valerie-pecresse","matthieu-landon","karim-zeribi","agnes-buzyn","jacques-attali","karim-bouamrane","naima-moutchou","bernard-cazeneuve"]
for i, s in enumerate(SL):
    cx = 186 + (i % 4) * 236; cy = 520 + (i // 4) * 236
    o.append(portrait(s, cx, cy, 92, WHITE, f"g{i}"))
c.append(save("c3-05", "".join(o)))
o = [frame(6, n, True)]
t, y = para(XB, "Après la table, le club.", 92, 96, 400, WHITE, 900, 1.04); o.append(t)
for k, s in enumerate(["L’annuaire des membres", "Les rendez-vous et les rencontres", "La lettre des prochains invités"]):
    yy = y + 130 + k * 84
    o.append(f'<circle cx="116" cy="{yy-14}" r="10" fill="{RED}"/>' + T(SEMI, s, 40, 150, yy, WHITE))
o.append(f'<rect x="96" y="1010" width="888" height="110" rx="55" fill="{WHITE}"/>' + T(XB, "Rejoindre le club", 46, 540, 1082, BLUE, "middle"))
o.append(T(MED, "alumniplatform.net/join/premierservice", 30, 540, 1180, SB, "middle"))
c.append(save("c3-06", "".join(o), BLUE))
c.append(argo_slide("c3", 7, n, None))
files["c3"] = c

# ---------- Carrousel 4 : invité n°2 ----------
n = 5; c = []
o = [frame(1, n)]
o.append(T(SEMI, "Prochain rendez-vous", 38, 540, 230, RED, "middle"))
o.append(at_table("olivier-faure", 540, 600, 640))
o.append(T(XB, "Olivier Faure", 92, 540, 1080, BLUE, "middle"))
o.append(T(REG, "Premier secrétaire du Parti socialiste", 38, 540, 1145, GRIS, "middle"))
c.append(save("c4-01", "".join(o)))
o = [frame(2, n, True)]
o.append(moon(96, 300, 150, WHITE))
o.append(T(XB, "Un dîner.", 104, 96, 600, WHITE))
o.append(T(XB, "Mardi 17 novembre", 72, 96, 710, WHITE))
o.append(T(SEMI, "[Lieu à confirmer]", 52, 96, 800, SB))
t, y = para(REG, "Dix étudiants autour de la table, une conversation à huis clos.", 38, 96, 930, SB, 860, 1.3); o.append(t)
c.append(save("c4-02", "".join(o), BLUE))
o = [frame(3, n)]
t, y = para(XB, "Vous avez une question à lui poser ?", 84, 96, 400, BLUE, 900, 1.06); o.append(t)
for k, (a, b2) in enumerate([("Créez votre profil", "sur Alumni Platform"), ("Choisissez ce dîner", "et préparez votre question"), ("Recevez l’invitation", "dix places par table")]):
    yy = y + 160 + k * 150
    col = RED if k == 2 else BLUE
    o.append(f'<circle cx="130" cy="{yy-20}" r="34" fill="{col}"/>' + T(XB, str(k+1), 38, 130, yy - 6, WHITE, "middle"))
    o.append(T(XB, a, 46, 196, yy - 20, BLUE) + T(REG, b2, 32, 196, yy + 24, GRIS))
c.append(save("c4-03", "".join(o)))
o = [frame(4, n, True)]
t, y = para(XB, "Inscrivez-vous pour participer.", 96, 96, 470, WHITE, 900, 1.04); o.append(t)
o.append(f'<rect x="96" y="{y+110:.0f}" width="888" height="110" rx="55" fill="{WHITE}"/>' + T(XB, "S’inscrire sur Alumni Platform", 42, 540, y + 182, BLUE, "middle"))
o.append(T(MED, "alumniplatform.net/join/premierservice", 30, 540, y + 290, SB, "middle"))
c.append(save("c4-04", "".join(o), BLUE))
c.append(argo_slide("c4", 5, n, None))
files["c4"] = c

# ---------- Post 2 : couverture vidéo (9:16 + 4:5) ----------
W, H = 1080, 1920
o = [logo(290, 180, 500)]
o.append(f'<g transform="translate(240,620)">{G.table(300, 300, 600)}</g>')
o.append(T(XB, "Le film", 110, 540, 1420, BLUE, "middle"))
o.append(T(MED, "Premier Service en 1 min 30", 44, 540, 1500, GRIS, "middle"))
files["v"] = [save("v-couverture-9x16", "".join(o))]
print({k: len(v) for k, v in files.items()})

# carton de fin vidéo (3 s) : soutien Argonautes
o = [logo(96, 140, 360, True)]
t, y = para(XB, "Ce projet est soutenu par Les Argonautes.", 76, 96, 760, WHITE, 900, 1.08); o.append(t)
t, y = para(REG, "Cabinet de conseil et d’exécution dédié au secteur public.", 42, 96, y + 100, SB, 860, 1.3); o.append(t)
o.append(f'<rect x="96" y="{y+80:.0f}" width="640" height="{640*AR+64:.0f}" rx="28" fill="{PAPER}"/>')
o.append(f'<image href="{ARGO_C}" x="128" y="{y+112:.0f}" width="576" height="{576*AR:.0f}"/>')
o.append(T(SEMI, "lesargos.fr", 48, 96, y + 80 + 640*AR + 64 + 110, WHITE))
files["v"].append(save("v-fin-argonautes-9x16", "".join(o), BLUE))
print({k: len(v) for k, v in files.items()})
