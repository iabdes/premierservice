import os, subprocess, base64, shutil
import wm7; G = wm7.G
SRC = "portraits-src/"; OUT = "invites/"; os.makedirs(OUT, exist_ok=True)
GUESTS = [("vedrenne","Marie-Pierre Vedrenne"),("lombard","Éric Lombard"),("attali","Jacques Attali"),
 ("bouamrane","Karim Bouamrane"),("buzyn","Agnès Buzyn"),("cazeneuve","Bernard Cazeneuve"),("faure","Olivier Faure"),
 ("guedj","Jérôme Guedj"),("landon","Landon"),("moutchou","Naïma Moutchou"),("pecresse","Valérie Pécresse"),("zeribi","Karim Zéribi")]
def b64(p): return "data:image/png;base64," + base64.b64encode(open(p,"rb").read()).decode()
def framed(img, cx, cy, D):
    u = D / (2 * (G.R_RING + G.CH / 2 + 1.5)); r = G.R_TABLE * u; s = 2 * r / 1180
    o = [f'<clipPath id="c"><circle cx="{cx}" cy="{cy}" r="{r:.1f}"/></clipPath>',
         f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="#FAF5EC"/>',
         f'<image clip-path="url(#c)" href="{b64(img)}" x="{cx-627*s:.1f}" y="{cy-600*s:.1f}" width="{1254*s:.1f}" height="{1254*s:.1f}"/>']
    for i in range(G.N):
        o.append(f'<rect x="{cx-G.CW*u/2:.1f}" y="{cy-(G.R_RING+G.CH/2)*u:.1f}" width="{G.CW*u:.1f}" height="{G.CH*u:.1f}" rx="{3.2*u:.1f}" fill="{G.RED if i==0 else G.BLUE}" transform="rotate({i*360/G.N:.3f} {cx} {cy})"/>')
    return "".join(o)
for k, name in GUESTS:
    slug = name.lower().replace(" ","-").replace("é","e").replace("è","e").replace("ï","i")
    shutil.copy(SRC + k + ".png", f"{OUT}premier-service_portrait_{slug}.png")
    p = f"{OUT}premier-service_portrait-a-table_{slug}"
    open(p+".svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">{framed(SRC+k+".png",500,500,980)}</svg>')
    subprocess.run(["rsvg-convert","-w","800",p+".svg","-o",p+".png"],check=True)
print("ok")
