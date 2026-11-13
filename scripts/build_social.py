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
# ================= v2 : grille, progression, carte Argonautes « Gréement » =================
PLEX = "fnt/PlexMono-Medium.ttf"
ECUME, ABYSSE, ARGO, ARGO_T, GALET = "#F5F1E8", "#010101", "#F10F23", "#C40C1D", "#5C5A56"
NAVY2 = "#2B3D97"   # pas de ton sur marine
M = 88
CONSEIL = b64("argo/conseil.jpg", "image/jpeg")
def progress(i, n, dark, y=None):
    y = H - 64 if y is None else y
    g = 10; w = (W - 2*M - g*(n-1)) / n; o = []
    for k in range(n):
        on = k < i
        col = (WHITE if on else "#4A5AA6") if dark else (BLUE if on else "#D6D9E6")
        o.append(f'<rect x="{M + k*(w+g):.1f}" y="{y}" width="{w:.1f}" height="6" rx="3" fill="{col}"/>')
    return "".join(o)
def frame(i, n, dark=False, pdark=None):
    o = [logo(72, 60, 200, dark)]
    o.append(progress(i, n, dark if pdark is None else pdark))
    return "".join(o)
def arrow(x, y, s, c, sw=4):
    return f'<path d="M{x} {y}h{s}M{x+s-s*0.38} {y-s*0.38}l{s*0.38} {s*0.38}-{s*0.38} {s*0.38}" stroke="{c}" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
def swipe(dark=True):
    c = WHITE if dark else BLUE
    return T(SEMI, "Faites glisser", 30, W - M - 56, H - 112, c, "end") + arrow(W - M - 40, H - 122, 40, c)
def chair(x, y, ang, u, col):
    return f'<rect x="{x - G.CW*u/2:.1f}" y="{y - G.CH*u/2:.1f}" width="{G.CW*u:.1f}" height="{G.CH*u:.1f}" rx="{3.2*u:.1f}" fill="{col}" transform="rotate({ang:.1f} {x:.1f} {y:.1f})"/>'
def lock(x, y, k, c, hole):
    return f'<g transform="translate({x},{y}) scale({k})"><path d="M18 36V24a14 14 0 0 1 28 0v12" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/><rect x="8" y="36" width="48" height="38" rx="9" fill="{c}"/><circle cx="32" cy="52" r="5" fill="{hole}"/><rect x="29.5" y="54" width="5" height="10" rx="2.5" fill="{hole}"/></g>'
def cover(title, sub):
    o = [f'{G.table(905, 300, 760, NAVY2, RED)}', frame(1, n, True)]
    lines = wrap(XB, title, 116, 900); y0 = 1000 - (len(lines)-1)*116*1.0
    t, y = para(XB, title, 116, M, y0, WHITE, 900, 1.0); o.append(t)
    o.append(T(MED, sub, 38, M, y + 86, SB)); o.append(swipe())
    return "".join(o)

def argo_card(prefix, i, n, tall=False):
    """Carte de fin minimaliste : phrase centrée, logo, site en étiquette."""
    Hh = 1920 if tall else 1350
    cy = Hh/2 - (10 if tall else 30); f = 1.3 if tall else 1.0
    o = [f'<g transform="translate({W/2},{cy}) scale({f}) translate({-W/2},{-cy})">']
    o.append(T(SEMI, "Ce projet est soutenu par", 46, W/2, cy - 150, ABYSSE, "middle"))
    lw = 640
    o.append(f'<image href="{ARGO_C}" x="{W/2 - lw/2:.0f}" y="{cy - 105:.0f}" width="{lw}" height="{lw*AR:.0f}"/>')
    yy = cy - 105 + lw*AR + 96
    for k, l in enumerate(["Cabinet de conseil et d’exécution", "dédié au secteur public."]):
        o.append(T(REG, l, 38, W/2, yy + k*52, GALET, "middle"))
    yy += 52 + 70
    lab = "lesargos.fr"; tw = wid(SEMI, lab, 36); pw = tw + 64 + 46
    x0 = W/2 - pw/2
    o.append(f'<rect x="{x0:.0f}" y="{yy:.0f}" width="{pw:.0f}" height="76" rx="38" fill="{ABYSSE}"/>')
    o.append(T(SEMI, lab, 36, x0 + 32, yy + 51, WHITE))
    o.append(arrow(x0 + 32 + tw + 18, yy + 38, 26, ARGO, 3.5))
    o.append('</g>'); o.append(logo(72, 60, 200, False))
    if not tall: o.append(progress(i, n, False))
    global H; H0 = H; H = Hh
    p = save(f"{prefix}-{i:02d}" if not tall else prefix, "".join(o), ECUME); H = H0
    return p

def carton(slug, nom, fonction, jour, num, mois, fmt):
    """Carte invité inspirée des cartons du site : portrait, pastille format, étiquette date, ticket."""
    X, Y, CW, CH, R = M, 190, W - 2*M, 1050, 40
    PH = 600
    img = b64(f"ds-up/portraits/premier-service_portrait_{slug}.jpg", "image/jpeg")
    o = ['<defs><filter id="ombre" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="20" flood-color="#1E2F86" flood-opacity="0.16"/></filter>'
         '<filter id="ombre2" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#1E2F86" flood-opacity="0.22"/></filter></defs>']
    o.append(f'<rect x="{X}" y="{Y}" width="{CW}" height="{CH}" rx="{R}" fill="{WHITE}" filter="url(#ombre)"/>')
    o.append(f'<clipPath id="cp"><path d="M{X} {Y+PH}V{Y+R}a{R} {R} 0 0 1 {R} -{R}H{X+CW-R}a{R} {R} 0 0 1 {R} {R}V{Y+PH}Z"/></clipPath>')
    o.append(f'<image clip-path="url(#cp)" href="{img}" x="{X}" y="{Y + PH/2 - CW/2 + 40:.0f}" width="{CW}" height="{CW}" preserveAspectRatio="xMidYMid slice"/>')
    # pastille format
    pt = fmt; pw = wid(SEMI, pt, 32) + 110
    px = X + CW - 28 - pw; py = Y + 28
    if fmt == "Dîner":
        o.append(f'<rect x="{px:.0f}" y="{py}" width="{pw:.0f}" height="68" rx="34" fill="{BLUE}"/>' + moon(px + 26, py + 17, 34, WHITE) + T(SEMI, pt, 32, px + 74, py + 46, WHITE))
    else:
        o.append(f'<rect x="{px:.0f}" y="{py}" width="{pw:.0f}" height="68" rx="34" fill="{WHITE}"/>' + sun(px + 26, py + 17, 34, BLUE) + T(SEMI, pt, 32, px + 74, py + 46, BLUE))
    # étiquette date à cheval
    tx, ty, tw_, th = X + 40, Y + PH - 150, 170, 196
    o.append(f'<rect x="{tx}" y="{ty-70}" width="{wid(XB, "Prochain", 28)+44:.0f}" height="52" rx="26" fill="{RED}"/>' + T(XB, "Prochain", 28, tx + 22, ty - 34, WHITE))
    o.append(f'<rect x="{tx}" y="{ty}" width="{tw_}" height="{th}" rx="32" fill="{WHITE}" filter="url(#ombre2)"/>')
    o.append(T(SEMI, jour, 30, tx + tw_/2, ty + 50, "#C42630", "middle") + T(XB, num, 92, tx + tw_/2, ty + 140, BLUE, "middle") + T(MED, mois, 30, tx + tw_/2, ty + 178, GRIS, "middle"))
    # ticket
    ky = Y + PH + 96
    o.append(f'<line x1="{X+36}" y1="{ky}" x2="{X+CW-36}" y2="{ky}" stroke="#E6E1D6" stroke-width="4" stroke-dasharray="14 12"/>')
    o.append(f'<circle cx="{X}" cy="{ky}" r="22" fill="{PAPER}"/><circle cx="{X+CW}" cy="{ky}" r="22" fill="{PAPER}"/>')
    # texte
    o.append(T(XB, nom, 92, X + 48, ky + 130, BLUE))
    t, y = para(REG, fonction, 40, X + 48, ky + 196, GRIS, CW - 96, 1.25); o.append(t)
    by = Y + CH - 56
    o.append(T(XB, "Dix places, à huis clos", 32, X + 48, by, "#C42630"))
    sw = wid(SEMI, "S’inscrire", 34)
    o.append(T(SEMI, "S’inscrire", 34, X + CW - 48 - 40 - sw, by, BLUE) + arrow(X + CW - 48 - 28, by - 12, 28, BLUE, 3.5))
    return "".join(o)

files = {}
# ---------- C1 teasing ----------
n = 6; c = []
c.append(save("c1-01", cover("Servir l’État, ça s’apprend comment ?", "Une question que beaucoup d’étudiants se posent."), BLUE))
o = [f'<rect x="0" y="690" width="{W}" height="{H-690}" fill="{BLUE}"/>', frame(2, n, False, True)]
t, y = para(XB, "Les étudiants qui veulent s’engager ont des questions.", 80, M, 330, BLUE, 900, 1.05); o.append(t)
t, y = para(XB, "Celles et ceux qui ont exercé ont des réponses.", 80, M, 880, WHITE, 900, 1.05); o.append(t)
c.append(save("c1-02", "".join(o)))
o = [frame(3, n)]
t, y = para(XB, "Mais ils se croisent rarement.", 100, M, 330, BLUE, 900, 1.0); o.append(t)
t, y = para(REG, "Un amphithéâtre, une conférence, une photo. Rarement le temps d’une vraie conversation.", 40, M, y + 100, INK, 880, 1.35); o.append(t)
cx, cy, R, u = 300, 1000, 150, 5.2
for k in range(10):
    a = k * 36; ax = cx + R*math.sin(math.radians(a)); ay = cy - R*math.cos(math.radians(a))
    o.append(chair(ax, ay, a, u, BLUE))
o.append(chair(880, 1000, -90, u*1.15, RED))
o.append(T(SEMI, "Les étudiants", 32, cx, 1222, GRIS, "middle") + T(SEMI, "Les responsables", 32, 880, 1180, GRIS, "middle") + T(SEMI, "publics", 32, 880, 1222, GRIS, "middle"))
c.append(save("c1-03", "".join(o)))
o = [frame(4, n)]
t, y = para(XB, "Entre ceux qui ont servi l’État et ceux qui le serviront, il manquait une table.", 76, M, 320, BLUE, 904, 1.06); o.append(t)
o.append(G.table(540, 920, 640, BLUE, RED))
c.append(save("c1-04", "".join(o)))
o = [f'<rect x="0" y="1010" width="{W}" height="{H-1010}" fill="{BLUE}"/>', frame(5, n, False, True)]
o.append(T(XB, "10", 220, M, 470, BLUE) + T(XB, "étudiants", 64, 400, 440, BLUE))
o.append(T(XB, "1", 220, M + 30, 730, RED) + T(XB, "personnalité", 64, 400, 650, BLUE) + T(XB, "publique", 64, 400, 720, BLUE))
o.append(lock(M + 10, 790, 2.9, BLUE, PAPER) + T(XB, "à huis clos", 64, 400, 930, BLUE))
o.append(T(XB, "Bientôt.", 120, M, 1210, WHITE))
c.append(save("c1-05", "".join(o)))
c.append(argo_card("c1", 6, n))
files["c1"] = c

# ---------- C3 concept ----------
n = 7; c = []
c.append(save("c3-01", cover("Premier Service, c’est quoi ?", "En cinq images."), BLUE))
o = [frame(2, n)]
o.append(G.table(540, 560, 620, BLUE, RED))
o.append(T(XB, "Une table.", 96, M, 1020, BLUE))
t, y = para(REG, "Dix étudiants et une personnalité de la vie publique. Assez peu pour que chacun parle.", 40, M, 1100, INK, 900, 1.32); o.append(t)
c.append(save("c3-02", "".join(o)))
o = [frame(3, n)]
o.append(lock(M - 10, 250, 6.2, BLUE, PAPER))
o.append(T(XB, "À huis clos.", 96, M, 830, BLUE))
t, y = para(XB, "Ce qui se dit à table reste à table.", 60, M, 940, RED, 900, 1.1); o.append(t)
t, y = para(REG, "Pas de caméra pendant l’échange, pas de citation sans accord.", 40, M, y + 96, INK, 900, 1.3); o.append(t)
c.append(save("c3-03", "".join(o)))
o = [frame(4, n)]
o.append(T(XB, "Deux formats.", 96, M, 340, BLUE))
o.append(f'<rect x="{M}" y="430" width="904" height="350" rx="28" fill="{BLUE}"/>' + moon(M+56, 500, 120, WHITE) + T(XB, "Le dîner", 72, M+220, 610, WHITE) + T(REG, "Le soir, pour prendre le temps.", 38, M+220, 676, SB))
o.append(f'<rect x="{M}" y="810" width="904" height="350" rx="28" fill="{WHITE}"/>' + sun(M+56, 880, 120, RED) + T(XB, "Le petit-déjeuner", 72, M+220, 990, BLUE) + T(REG, "Le matin, quand l’agenda est serré.", 38, M+220, 1056, GRIS))
c.append(save("c3-04", "".join(o)))
o = [frame(5, n)]
o.append(T(XB, "Saison 1 : douze invités.", 76, M, 320, BLUE))
o.append(T(MED, "Novembre et décembre 2026", 38, M, 384, INK))
SL = ["marie-pierre-vedrenne","olivier-faure","eric-lombard","valerie-pecresse","matthieu-landon","jerome-guedj","karim-zeribi","agnes-buzyn","jacques-attali","karim-bouamrane","naima-moutchou","bernard-cazeneuve"]
for i, s in enumerate(SL):
    cx = 190 + (i % 4) * 233; cy = 560 + (i // 4) * 240
    o.append(portrait(s, cx, cy, 98, WHITE, f"g{i}"))
c.append(save("c3-05", "".join(o)))
o = [frame(6, n, True)]
o.append(G.table(905, 210, 760, NAVY2, RED))
t, y = para(XB, "Après la table, le club.", 100, M, 560, WHITE, 900, 1.0); o.append(t)
for k, s in enumerate(["L’annuaire des membres", "Les rendez-vous et les rencontres", "La lettre des prochains invités"]):
    yy = y + 120 + k * 76
    o.append(f'<circle cx="{M+12}" cy="{yy-14}" r="10" fill="{RED}"/>' + T(SEMI, s, 42, M + 46, yy, WHITE))
o.append(f'<rect x="{M}" y="1040" width="904" height="116" rx="58" fill="{WHITE}"/>' + T(XB, "Rejoindre le club", 48, 540, 1115, BLUE, "middle"))
o.append(T(MED, "alumniplatform.net/join/premierservice", 32, 540, 1218, SB, "middle"))
c.append(save("c3-06", "".join(o), BLUE))
c.append(argo_card("c3", 7, n))
files["c3"] = c

# ---------- C4 invité ----------
n = 5; c = []
o = [carton("olivier-faure", "Olivier Faure", "Premier secrétaire du Parti socialiste", "MAR", "17", "NOV", "Dîner"), frame(1, n)]
c.append(save("c4-01", "".join(o)))
o = [frame(2, n, True)]
o.append(f'<rect x="{M}" y="230" width="904" height="960" rx="32" fill="{WHITE}"/>')
o.append(f'<rect x="{M+56}" y="286" width="220" height="250" rx="24" fill="{RED}"/>')
o.append(T(SEMI, "MAR", 34, M+166, 346, WHITE, "middle") + T(XB, "17", 130, M+166, 470, WHITE, "middle") + T(SEMI, "NOV", 34, M+166, 516, WHITE, "middle"))
o.append(moon(M+330, 300, 64, BLUE) + T(XB, "Un dîner", 80, M+330, 450, BLUE) + T(REG, "Mardi 17 novembre 2026", 38, M+330, 512, INK))
o.append(T(XB, "[Lieu à confirmer]", 58, M+56, 660, BLUE))
t, y = para(REG, "Dix étudiants autour de la table, une conversation à huis clos.", 40, M+56, 740, INK, 790, 1.3); o.append(t)
o.append(at_table("olivier-faure", 540, 1000, 300, BLUE, "t2"))
c.append(save("c4-02", "".join(o), BLUE))
o = [frame(3, n)]
t, y = para(XB, "Vous avez une question à lui poser ?", 88, M, 330, BLUE, 904, 1.05); o.append(t)
for k, (a, b2) in enumerate([("Créez votre profil", "sur Alumni Platform"), ("Choisissez ce dîner", "et préparez votre question"), ("Recevez l’invitation", "dix places par table")]):
    yy = y + 190 + k * 190
    col = RED if k == 2 else BLUE
    o.append(f'<circle cx="{M+40}" cy="{yy-22}" r="40" fill="{col}"/>' + T(XB, str(k+1), 44, M+40, yy - 6, WHITE, "middle"))
    o.append(T(XB, a, 52, M+120, yy - 22, BLUE) + T(REG, b2, 38, M+120, yy + 30, INK))
c.append(save("c4-03", "".join(o)))
o = [frame(4, n, True)]
o.append(at_table("olivier-faure", M + 150, 380, 300, "#3B4DA8", "t3"))
t, y = para(XB, "Inscrivez-vous pour participer.", 100, M, 680, WHITE, 904, 1.02); o.append(t)
o.append(f'<rect x="{M}" y="{y+100:.0f}" width="904" height="116" rx="58" fill="{WHITE}"/>' + T(XB, "S’inscrire sur Alumni Platform", 44, 540, y + 175, BLUE, "middle"))
o.append(T(MED, "alumniplatform.net/join/premierservice", 32, 540, y + 282, SB, "middle"))
c.append(save("c4-04", "".join(o), BLUE))
c.append(argo_card("c4", 5, n))
files["c4"] = c

# ---------- vidéo ----------
W, H = 1080, 1920
o = [logo(290, 180, 500)]
o.append(G.table(540, 920, 640, BLUE, RED))
o.append(T(XB, "Le film", 120, 540, 1440, BLUE, "middle"))
o.append(T(MED, "Premier Service en 1 min 30", 46, 540, 1520, INK, "middle"))
files["v"] = [save("v-couverture-9x16", "".join(o))]
files["v"].append(argo_card("v-fin-argonautes-9x16", 0, 0, True))
print({k: len(v) for k, v in files.items()})
