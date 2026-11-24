import asyncio, pathlib
from playwright.async_api import async_playwright

R = pathlib.Path("/home/claude/premierservice")
F = pathlib.Path("/home/claude/landon/package/files")
OUT = pathlib.Path("/home/claude/landon/out"); OUT.mkdir(exist_ok=True)
u = lambda p: pathlib.Path(p).as_uri()

BLUE, NAVY2, SKY, RED, REDT, PAPER, INK, GRIS = "#1E2F86", "#2B3D97", "#2C86D1", "#E0313B", "#C42630", "#FAF7F0", "#1A1D33", "#4F546E"
ECUME, ABYSSE, ARGO, GALET = "#F5F1E8", "#010101", "#F10F23", "#5C5A56"

LOGO_C = u(R / "identite/logos/premier-service_logo_couleur.png")
LOGO_B = u(R / "identite/logos/premier-service_logo_blanc.png")
ARGO_L = u(R / "partenaire/les-argonautes/les-argonautes_logo_fond-clair.png")
LANDON_T = u(R / "portraits/a-table/premier-service_portrait-a-table_matthieu-landon.png")
GUEDJ = u(R / "portraits/web/premier-service_portrait_jerome-guedj.jpg")
ZERIBI = u(R / "portraits/web/premier-service_portrait_karim-zeribi.jpg")

fonts = "".join(
    f"@font-face{{font-family:Outfit;font-weight:{w};src:url('{u(F / f'outfit-latin-{w}-normal.woff2')}') format('woff2');}}"
    f"@font-face{{font-family:Outfit;font-weight:{w};src:url('{u(F / f'outfit-latin-ext-{w}-normal.woff2')}') format('woff2');unicode-range:U+0100-024F,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF;}}"
    for w in (400, 500, 600, 700, 800))

def sigle(size, disc, chairs, guest=RED, opacity=1):
    rects = "".join(
        f'<rect x="43" y="3.25" width="14" height="8.5" rx="3.2" fill="{guest if i == 0 else chairs}" transform="rotate({i*360/11:.3f} 50 50)"/>'
        for i in range(11))
    return (f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" style="opacity:{opacity}">'
            f'<circle cx="50" cy="50" r="31" fill="{disc}"/>{rects}</svg>')

SUN = lambda c, s=40: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}"><circle cx="12" cy="12" r="4.6" fill="{c}"/><path d="M12 1.8v3M12 19.2v3M1.8 12h3M19.2 12h3M4.8 4.8l2.1 2.1M17.1 17.1l2.1 2.1M4.8 19.2l2.1-2.1M17.1 6.9l2.1-2.1" stroke="{c}" stroke-width="2" stroke-linecap="round"/></svg>'
MOON = lambda c, s=40: f'<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M15.5 3.2A9 9 0 1 0 20.8 15 7.2 7.2 0 0 1 15.5 3.2Z" fill="{c}"/></svg>'
ARROW = lambda c, s=34, w=4: f'<svg viewBox="0 0 40 40" width="{s}" height="{s}"><path d="M6 20h28M22 8l12 12-12 12" stroke="{c}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHAIR = lambda c: f'<svg viewBox="0 0 14 8.5" width="34" height="21"><rect width="14" height="8.5" rx="3.2" fill="{c}"/></svg>'

BASE = f"""{fonts}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1920px}}
body{{font-family:Outfit;-webkit-font-smoothing:antialiased;position:relative;overflow:hidden}}
.logo{{position:absolute;left:88px;top:262px;width:236px}}
.safe{{position:absolute;left:88px;right:88px;top:250px;bottom:250px}}
h1{{font-weight:800;letter-spacing:-0.02em;line-height:1.0}}
.label{{font-weight:600}}
.tag{{display:inline-flex;align-items:center;gap:14px;border-radius:999px;font-weight:600}}
"""

def page(body, bg, extra=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{BASE}{extra}</style></head><body style='background:{bg}'>{body}</body></html>"

S = {}

# 1 — ATTENTION
S[1] = page(f"""
<div style="position:absolute;right:-330px;top:520px">{sigle(1040, NAVY2, NAVY2, RED)}</div>
<img class="logo" src="{LOGO_B}">
<div class="safe">
  <div style="position:absolute;top:330px;left:0">
    <span class="tag" style="background:{RED};color:#fff;font-size:38px;padding:16px 30px 16px 24px">{SUN('#fff',40)} Demain matin</span>
  </div>
  <h1 style="position:absolute;top:470px;left:0;color:#fff;font-size:128px;width:880px">On parle économie avec l’Élysée.</h1>
  <p style="position:absolute;top:1010px;left:0;color:#DDE0EF;font-size:44px;line-height:1.3;width:800px">Un petit-déjeuner à huis clos, dix étudiants, un invité.</p>
  <div style="position:absolute;bottom:0;left:0;display:flex;align-items:center;gap:18px;color:#fff;font-size:40px;font-weight:600">Découvrez notre invité {ARROW('#fff',40)}</div>
</div>""", BLUE)

# 2 — INTEREST : l'invité
S[2] = page(f"""
<img class="logo" src="{LOGO_C}">
<div class="safe">
  <div style="position:absolute;top:205px;left:0;right:0;text-align:center">
    <span class="tag" style="background:{BLUE};color:#fff;font-size:36px;padding:14px 30px 14px 24px">{SUN('#fff',38)} Petit-déjeuner · mercredi 25 novembre</span>
  </div>
  <img src="{LANDON_T}" style="position:absolute;top:300px;left:50%;transform:translateX(-50%);width:820px">
  <div style="position:absolute;top:1140px;left:0;right:0;text-align:center">
    <h1 style="color:{BLUE};font-size:104px">Matthieu Landon</h1>
    <p style="margin-top:28px;color:{GRIS};font-size:46px;line-height:1.25">Secrétaire général adjoint<br>de l’Élysée</p>
  </div>
</div>""", PAPER)

# 3 — INTEREST : le parcours
steps = [
    ("Formation", "École polytechnique"),
    ("Formation", "Doctorat en biologie synthétique à Harvard"),
    ("2017", "Direction générale des entreprises, à Bercy, puis sous-directeur de l’innovation"),
    ("Ensuite", "Conseiller industrie et recherche à Matignon et à l’Élysée"),
    ("2023", "Chef du pôle économie du cabinet du Président"),
    ("2026", "Secrétaire général adjoint de l’Élysée"),
]
items = "".join(
    f"""<div style="position:relative;padding-left:76px;margin-bottom:{0 if k==len(steps)-1 else 46}px">
      <div style="position:absolute;left:0;top:6px;width:34px;height:21px;border-radius:7px;background:{RED if k==len(steps)-1 else '#fff'}"></div>
      <p class="label" style="color:{'#F7A7AC' if k==len(steps)-1 else '#9FB0F0'};font-size:32px">{a}</p>
      <p style="color:#fff;font-size:{46 if k==len(steps)-1 else 40}px;font-weight:{700 if k==len(steps)-1 else 400};line-height:1.22;margin-top:6px">{b}</p>
    </div>""" for k, (a, b) in enumerate(steps))
S[3] = page(f"""
<div style="position:absolute;left:-260px;bottom:-300px">{sigle(760, NAVY2, NAVY2, NAVY2)}</div>
<img class="logo" src="{LOGO_B}">
<div class="safe">
  <h1 style="position:absolute;top:230px;left:0;color:#fff;font-size:100px;width:880px">Du laboratoire à l’Élysée.</h1>
  <div style="position:absolute;top:560px;left:0;right:0">
    <div style="position:absolute;left:16px;top:20px;bottom:30px;width:3px;background:#4A5AA6"></div>
    {items}
  </div>
</div>""", BLUE)

# 4 — DESIRE
qs = ["Comment une décision économique se prépare au sommet de l’État.",
      "Comment passer de la recherche à l’action publique.",
      "À quoi ressemble, au quotidien, le travail d’un secrétaire général adjoint de l’Élysée."]
qitems = "".join(
    f"""<div style="display:flex;gap:30px;align-items:flex-start;background:#fff;border-radius:32px;padding:40px 44px;margin-bottom:28px;box-shadow:0 14px 40px rgba(30,47,134,.10)">
      <div style="flex:none;margin-top:16px">{CHAIR(BLUE)}</div>
      <p style="color:{INK};font-size:44px;line-height:1.25">{q}</p></div>""" for q in qs)
S[4] = page(f"""
<img class="logo" src="{LOGO_C}">
<div class="safe">
  <h1 style="position:absolute;top:230px;left:0;color:{BLUE};font-size:96px;width:900px">Ce qu’il peut nous aider à comprendre.</h1>
  <div style="position:absolute;top:600px;left:0;right:0">{qitems}</div>
  <div style="position:absolute;bottom:0;left:0;right:0;display:flex;align-items:center;gap:26px">
    {sigle(110, BLUE, BLUE, RED)}
    <p style="color:{BLUE};font-size:40px;font-weight:600;line-height:1.25">10 étudiants, 1 invité.<br><span style="color:{REDT}">Ce qui se dit à table reste à table.</span></p>
  </div>
</div>""", PAPER)

# 5 — ACTION (engagement)
S[5] = page(f"""
<div style="position:absolute;right:-300px;top:180px">{sigle(700, NAVY2, NAVY2, NAVY2)}</div>
<img class="logo" src="{LOGO_B}">
<div class="safe">
  <h1 style="position:absolute;top:230px;left:0;color:#fff;font-size:112px;width:900px">Votre question pour Matthieu Landon ?</h1>
  <div style="position:absolute;top:740px;left:0;right:0;height:440px;border:4px dashed #6E7DC4;border-radius:44px"></div>
  <p style="position:absolute;top:1240px;left:0;color:#DDE0EF;font-size:42px;line-height:1.3;width:880px">Les fondateurs en retiendront une pour la table de demain.</p>
</div>""", BLUE)

# 6 — ACTION (recrutement)
def mini(img, date, fmt, icon, nom, fonc):
    return f"""<div style="display:flex;align-items:center;gap:36px;background:#fff;border-radius:36px;padding:34px 40px;box-shadow:0 14px 40px rgba(30,47,134,.10);margin-bottom:30px">
      <img src="{img}" style="width:170px;height:170px;border-radius:50%;object-fit:cover;flex:none;background:{PAPER}">
      <div><div style="display:flex;align-items:center;gap:12px">{icon}<span class="label" style="color:{REDT};font-size:34px">{date} · {fmt}</span></div>
      <p style="color:{BLUE};font-size:52px;font-weight:800;letter-spacing:-0.01em;margin-top:8px">{nom}</p>
      <p style="color:{GRIS};font-size:36px;margin-top:4px">{fonc}</p></div></div>"""
S[6] = page(f"""
<img class="logo" src="{LOGO_C}">
<div class="safe">
  <h1 style="position:absolute;top:230px;left:0;color:{BLUE};font-size:104px;width:900px">Les prochaines tables.</h1>
  <div style="position:absolute;top:520px;left:0;right:0">
    {mini(GUEDJ, "Mer. 2 déc.", "Dîner", MOON(BLUE, 36), "Jérôme Guedj", "Député de l’Essonne")}
    {mini(ZERIBI, "Jeu. 3 déc.", "Petit-déjeuner", SUN(BLUE, 36), "Karim Zéribi", "Ancien député européen")}
  </div>
  <p style="position:absolute;top:1060px;left:0;color:{INK};font-size:42px;line-height:1.3;width:880px">Rejoignez le club, puis candidatez aux tables qui vous intéressent.</p>
  <div style="position:absolute;bottom:40px;left:0;right:0;display:flex;justify-content:center">
    <span class="tag" style="background:{BLUE};color:#fff;font-size:42px;padding:30px 52px">Rejoindre le club {ARROW('#fff',38)}</span>
  </div>
</div>""", PAPER)

# 7 — cartouche Les Argonautes
S[7] = page(f"""
<img class="logo" src="{LOGO_C}">
<div style="position:absolute;left:0;right:0;top:50%;transform:translateY(-50%);text-align:center">
  <p class="label" style="color:{ABYSSE};font-size:58px">Ce projet est soutenu par</p>
  <img src="{ARGO_L}" style="width:820px;margin:56px auto 0;display:block">
  <p style="color:{GALET};font-size:48px;line-height:1.35;margin-top:64px">Cabinet de conseil et d’exécution<br>dédié au secteur public.</p>
  <span class="tag" style="background:{ABYSSE};color:#fff;font-size:46px;padding:24px 40px;margin-top:70px">lesargos.fr {ARROW(ARGO,36,4.5)}</span>
</div>""", ECUME)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for k, html in S.items():
            f = OUT / f"s{k}.html"; f.write_text(html)
            await pg.goto(f.as_uri()); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(OUT / f"premier-service_story_landon_{k:02d}.png"))
        await b.close()
asyncio.run(main())
