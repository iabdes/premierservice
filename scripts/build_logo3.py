import sys
import os, subprocess
import numpy as np
from PIL import Image
import potrace
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

A = "/mnt/user-data/attachments/6e78a7ef-414c-585b-8c47-287188e20848/"
OUT = "/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/" + (sys.argv[3] if len(sys.argv) > 3 else "ps-logo-v3") + "/"
SCRIPT = A + "d6b38989-Breathing_Personal_Use_Only.ttf"
F = {"SemiBold": A + "7164757e-Outfit-SemiBold.ttf", "Bold": A + "a976a5a1-Outfit-Bold.ttf", "ExtraBold": A + "b647ff33-Outfit-ExtraBold.ttf"}
import sys
RED, BLUE, WHITE = (sys.argv[1] if len(sys.argv) > 1 else "#F10F23"), (sys.argv[2] if len(sys.argv) > 2 else "#1800AD"), "#FFFFFF"
_c = {}


def shape(path, text, size, track=0.0):
    if path not in _c:
        tt = TTFont(path)
        _c[path] = (hb.Font(hb.Face(hb.Blob.from_file_path(path))), tt.getGlyphSet(), tt.getGlyphOrder(), tt["head"].unitsPerEm)
    font, gs, order, upm = _c[path]
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(font, buf, {"kern": True})
    s = size / upm; pen = SVGPathPen(gs); bp = BoundsPen(gs); x = 0
    for i, p in zip(buf.glyph_infos, buf.glyph_positions):
        t = (s, 0, 0, -s, x + p.x_offset * s, -p.y_offset * s); g = order[i.codepoint]
        gs[g].draw(TransformPen(pen, t)); gs[g].draw(TransformPen(bp, t)); x += p.x_advance * s + track * size
    return pen.getCommands(), bp.bounds


# ---- the toque sigle sent by the user: background removed, white made blue, traced ----
im = np.asarray(Image.open(A + "78dbfd35-image.png").convert("RGB")).astype(float)
al = np.clip((im[:, :, 1] - 152) / 103, 0, 1); ys, xs = np.where(al > 0.5)
cr = Image.fromarray((al[ys.min()-4:ys.max()+5, xs.min()-4:xs.max()+5] * 255).astype(np.uint8)); K = 6
big = np.asarray(cr.resize((cr.width*K, cr.height*K), Image.BICUBIC)) > 127
parts = []
for c in potrace.Bitmap(~big).trace(turdsize=20, alphamax=1.0, opticurve=True, opttolerance=0.2):
    d = [f"M{c.start_point.x/K:.2f},{c.start_point.y/K:.2f}"]
    for sg in c.segments:
        d.append(f"L{sg.c.x/K:.2f},{sg.c.y/K:.2f}L{sg.end_point.x/K:.2f},{sg.end_point.y/K:.2f}" if sg.is_corner else
                 f"C{sg.c1.x/K:.2f},{sg.c1.y/K:.2f} {sg.c2.x/K:.2f},{sg.c2.y/K:.2f} {sg.end_point.x/K:.2f},{sg.end_point.y/K:.2f}")
    parts.append("".join(d) + "Z")
SIG, SIG_W, SIG_H = "".join(parts), cr.width, cr.height


def sigle(ox, oy, h, col=None):
    col = col or BLUE
    return f'<path fill="{col}" fill-rule="evenodd" transform="translate({ox:.2f},{oy:.2f}) scale({h/SIG_H:.4f})" d="{SIG}"/>'


def build(sans, cap, width, p_width, p_left, gap, boost=0.0):
    """All in the reference's own units: SERVICE cap height `cap`, ink width `width`;
    Premier ink width `p_width`, its left edge `p_left` from SERVICE's left, its bottom `p_bottom` below SERVICE's top."""
    d0, b0 = shape(F[sans], "SERVICE", 100.0)
    size = 100.0 * cap / (b0[3] - b0[1])
    d0, b0 = shape(F[sans], "SERVICE", size)
    n = 6  # gaps between 7 letters
    track = (width - (b0[2] - b0[0])) / n / size
    sd, sb = shape(F[sans], "SERVICE", size, track)
    pd0, pb0 = shape(SCRIPT, "Premier", 100.0)
    psz = 100.0 * p_width / (pb0[2] - pb0[0])
    pd, pb = shape(SCRIPT, "Premier", psz)
    _, rb = shape(SCRIPT, "remier", psz)
    pdx = sb[0] + p_left - pb[0]; pdy = sb[1] - gap * cap - rb[3] - boost
    x0 = min(sb[0], pb[0] + pdx); y0 = min(sb[1], pb[1] + pdy)
    x1 = max(sb[2], pb[2] + pdx); y1 = max(sb[3], pb[3] + pdy)
    W, H = x1 - x0, y1 - y0
    st = f' stroke="{{r}}" stroke-width="{boost}" stroke-linejoin="round"' if boost else ""

    def draw(ox, oy, r=None, b=None):
        r = r or RED; b = b or BLUE
        return (f'<path fill="{r}"{st.format(r=r)} transform="translate({ox - x0 + pdx:.2f},{oy - y0 + pdy:.2f})" d="{pd}"/>'
                f'<path fill="{b}" transform="translate({ox - x0:.2f},{oy - y0:.2f})" d="{sd}"/>')
    return W, H, draw, (sb[1] - y0)  # last: y of SERVICE top inside the wordmark


VARIANTS = {
    # A: the model's own proportions, measured on the image sent (cap 126, SERVICE 806 wide, Premier 859 wide, 79 to the left, 68 into SERVICE)
    "A-fidele": build("Bold", 126, 806, 859, -79, 0.41),
    # B: a fuller brush and a lighter, more open SERVICE: the two words closer in weight
    "B-pinceau-affirme": build("SemiBold", 112, 806, 900, -60, 0.34, boost=5.0),
    # C: compact block, heavier SERVICE, Premier overlapping it more
    "C-compact": build("ExtraBold", 140, 760, 900, -95, 0.20, boost=2.5),
}
os.makedirs(OUT, exist_ok=True)
M = 70
for name, (W, H, draw, stop) in VARIANTS.items():
    sh = H * 0.74; sw = SIG_W * sh / SIG_H; g = sh * 0.26
    for suf, r, b in (("", RED, BLUE), ("-blanc", WHITE, WHITE)):
        body = sigle(M, M + (H - sh) / 2, sh, b) + draw(M + sw + g, M, r, b)
        w, h = sw + g + W + 2 * M, H + 2 * M
        p = OUT + f"premier-service-{name}{suf}"
        open(p + ".svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>')
        subprocess.run(["rsvg-convert", "-w", str(int(w * 2)), p + ".svg", "-o", p + ".png"], check=True)
    # wordmark alone
    p = OUT + f"premier-service-{name}-sans-sigle"
    open(p + ".svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W+2*M:.0f} {H+2*M:.0f}" width="{W+2*M:.0f}" height="{H+2*M:.0f}">{draw(M, M)}</svg>')
    subprocess.run(["rsvg-convert", "-w", str(int((W + 2*M) * 2)), p + ".svg", "-o", p + ".png"], check=True)

# comparison sheet: three variants stacked, labelled
SW = 2000; rows = []; y = 0
for name, (W, H, draw, stop) in VARIANTS.items():
    sh = H * 0.74; sw = SIG_W * sh / SIG_H; g = sh * 0.26; tw = sw + g + W
    k = 1500 / tw; rh = H * k + 260
    lab = {"A-fidele": "A  Fidèle au modèle", "B-pinceau-affirme": "B  Pinceau affirmé", "C-compact": "C  Compact"}[name]
    lab_d, lab_b = shape(F["SemiBold"], lab, 44)
    rows.append(f'<path fill="#5C5A56" transform="translate(80,{y+90})" d="{lab_d}"/>')
    rows.append(f'<g transform="translate({(SW - tw*k)/2:.1f},{y+150:.1f}) scale({k:.4f})">{sigle(0, (H - sh)/2, sh)}{draw(sw + g, 0)}</g>')
    y += rh + 40
open(OUT + "planche-variantes.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SW} {y:.0f}" width="{SW}" height="{y:.0f}"><rect width="100%" height="100%" fill="#FFFFFF"/>{"".join(rows)}</svg>')
subprocess.run(["rsvg-convert", OUT + "planche-variantes.svg", "-o", OUT + "planche-variantes.png"], check=True)
print("ok")
