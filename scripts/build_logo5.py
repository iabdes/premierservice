import sys, math, subprocess, os
RED, BLUE, PAPER, WHITE, INK = "#E0313B", "#1E2F86", "#FAF7F0", "#FFFFFF", "#1B1B1B"
sys.argv = ["x", RED, BLUE, "ps-tmp"]
import build_logo3 as L          # reuses the fonts, the shaping and the B / C wordmarks

OUT = "/tmp/claude-0/-home-claude/6e78a7ef-414c-585b-8c47-287188e20848/scratchpad/ps-logo-v5/"
os.makedirs(OUT, exist_ok=True)
N = 11                     # 10 students + 1 guest
R_TABLE, R_RING, R_SEAT = 31.0, 42.5, 6.6
CW, CH = 14.0, 8.5   # chair: tangential width, radial depth   # in a 100-unit box centred on 50,50


def table(cx, cy, size, ink=BLUE, guest=RED, paper=None):
    """The table seen from above: a disc and eleven seats, the guest's seat (top) in red."""
    k = size / 100.0; out = [f'<g transform="translate({cx - size/2:.2f},{cy - size/2:.2f}) scale({k:.4f})">']
    out.append(f'<circle cx="50" cy="50" r="{R_TABLE}" fill="{ink}"/>')
    for i in range(N):
        out.append(f'<rect x="{50-CW/2}" y="{50-R_RING-CH/2}" width="{CW}" height="{CH}" rx="3.2" fill="{guest if i == 0 else ink}" transform="rotate({i*360/N:.3f} 50 50)"/>')
    out.append("</g>")
    return "".join(out)


def glyph(path, ch, size):
    d, b = L.shape(path, ch, size)
    adv = L._c[path]  # font cache
    font = adv[0]; buf = L.hb.Buffer(); buf.add_str(ch); buf.guess_segment_properties(); L.hb.shape(font, buf, {})
    a = buf.glyph_positions[0].x_advance * size / adv[3]
    return d, a


def arc_text(cx, cy, r, text, path, size, fill, top=True, track=0.12):
    gl = [glyph(path, c, size) for c in text]
    total = sum(a for _, a in gl) + track * size * (len(gl) - 1)
    out = []; cum = 0.0
    for d, a in gl:
        mid = cum + a / 2
        if top:
            th = -math.pi / 2 - (total / 2) / r + mid / r; rot = math.degrees(th) + 90
        else:
            th = math.pi / 2 + (total / 2) / r - mid / r; rot = math.degrees(th) - 90
        x, y = cx + r * math.cos(th), cy + r * math.sin(th)
        out.append(f'<path fill="{fill}" transform="translate({x:.2f},{y:.2f}) rotate({rot:.2f}) translate({-a/2:.2f},0)" d="{d}"/>')
        cum += a + track * size
    return "".join(out)


def badge(cx, cy, d, sans, line2=None, ink=BLUE, accent=RED):
    """PREMIER on the upper arc in red, SERVICE on the lower arc in blue, read upright; the table in the centre."""
    r = d / 2; size = d * 0.115; cap = size * 0.70
    out = [table(cx, cy, d * 0.56, ink, accent)]
    out.append(arc_text(cx, cy, r * 0.70, "PREMIER", sans, size, ink, top=True, track=0.34))
    out.append(arc_text(cx, cy, r * 0.70 + cap, "SERVICE", sans, size, accent, top=False, track=0.34))
    for sx in (-1, 1):
        out.append(f'<circle cx="{cx + sx * (r * 0.70 + cap / 2):.2f}" cy="{cy:.2f}" r="{d*0.018:.2f}" fill="{ink}"/>')
    return "".join(out)


def text(path, s, size, x, y, fill):
    d, b = L.shape(path, s, size)
    return f'<path fill="{fill}" transform="translate({x:.2f},{y:.2f})" d="{d}"/>'


def tile(x, y, w, h, fill, rx=28):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"/>'


def construction(x, y, w, h):
    """Grey construction drawing of the table on its circles and axes."""
    s = min(w, h) * 0.78; cx, cy = x + w / 2, y + h / 2; k = s / 100.0; G = "#B9B9B9"; F = "#DCDCDC"
    o = [tile(x, y, w, h, "#F4F4F4")]
    o.append(f'<g fill="none" stroke="{G}" stroke-width="2">')
    for v in (cx - (R_RING + R_SEAT) * k, cx - R_TABLE * k, cx, cx + R_TABLE * k, cx + (R_RING + R_SEAT) * k):
        o.append(f'<path d="M{v:.1f} {y} V{y+h}"/>')
    for v in (cy - (R_RING + R_SEAT) * k, cy - R_TABLE * k, cy, cy + R_TABLE * k, cy + (R_RING + R_SEAT) * k):
        o.append(f'<path d="M{x} {v:.1f} H{x+w}"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R_RING*k:.1f}"/><circle cx="{cx}" cy="{cy}" r="{(R_RING+R_SEAT)*k:.1f}"/>')
    for i in range(N):
        a = -math.pi / 2 + i * 2 * math.pi / N
        o.append(f'<path d="M{cx:.1f} {cy:.1f} L{cx + (R_RING+R_SEAT+8)*k*math.cos(a):.1f} {cy + (R_RING+R_SEAT+8)*k*math.sin(a):.1f}"/>')
    o.append("</g>")
    o.append(f'<g fill="{F}" stroke="{G}" stroke-width="2"><circle cx="{cx}" cy="{cy}" r="{R_TABLE*k:.1f}"/>')
    for i in range(N):
        o.append(f'<rect x="{cx-CW*k/2:.1f}" y="{cy-(R_RING+CH/2)*k:.1f}" width="{CW*k:.1f}" height="{CH*k:.1f}" rx="{3.2*k:.1f}" transform="rotate({i*360/N:.3f} {cx} {cy})"/>')
    o.append("</g>")
    return "".join(o)


def board(key, label):
    W, H, draw, _ = L.VARIANTS[key]
    sans = {"B-pinceau-affirme": L.F["SemiBold"], "C-compact": L.F["ExtraBold"]}[key]
    BW, BH = 2400, 1880; o = [f'<rect width="{BW}" height="{BH}" fill="{INK}"/>']
    # tile 1: vertical lockup on white
    t1 = (20, 20, 1170, 760); o.append(tile(*t1, WHITE))
    ts = 230; gap = 50; kk = min(760 / W, (t1[3] - 2 * 80 - ts - gap) / H)
    blk_h = ts + gap + H * kk; y0 = t1[1] + (t1[3] - blk_h) / 2
    o.append(table(t1[0] + t1[2] / 2, y0 + ts / 2, ts))
    o.append(f'<g transform="translate({t1[0] + (t1[2] - W*kk)/2:.1f},{y0 + ts + gap:.1f}) scale({kk:.4f})">{draw(0, 0)}</g>')
    # tile 2: horizontal lockup on paper
    t2 = (20, 800, 1170, 400); o.append(tile(*t2, PAPER))
    kh = 230 / H; ts2 = H * kh * 0.92; g2 = 50; tw = ts2 + g2 + W * kh; x0 = t2[0] + (t2[2] - tw) / 2
    o.append(table(x0 + ts2 / 2, t2[1] + t2[3] / 2, ts2))
    o.append(f'<g transform="translate({x0 + ts2 + g2:.1f},{t2[1] + (t2[3] - H*kh)/2:.1f}) scale({kh:.4f})">{draw(0, 0)}</g>')
    # tile 3: construction
    o.append(construction(1210, 20, 1170, 1180))
    # row 2: palette, app icon, badge
    y2, h2 = 1220, 640
    sw = [(BLUE, WHITE), (PAPER, BLUE), (RED, WHITE)]
    for i, (c, tc) in enumerate(sw):
        x = 20 + i * 400; o.append(tile(x, y2, 380, h2, c))
        o.append(text(L.F["SemiBold"], c.upper(), 54, x + 40, y2 + h2 - 50, tc))
    xi = 1220; o.append(tile(xi, y2, 560, h2, "#2A2A2A"))
    ic = 300; ix, iy = xi + (560 - ic) / 2, y2 + (h2 - ic) / 2 - 30
    o.append(f'<rect x="{ix}" y="{iy}" width="{ic}" height="{ic}" rx="{ic*0.225:.1f}" fill="{BLUE}"/>')
    o.append(table(ix + ic / 2, iy + ic / 2, ic * 0.74, WHITE, RED))
    o.append(text(L.F["SemiBold"], "Premier Service", 34, ix + ic / 2 - 128, iy + ic + 60, "#E8E8E8"))
    xb = 1800; o.append(tile(xb, y2, 580, h2, PAPER))
    o.append(badge(xb + 290, y2 + h2 / 2, 520, sans, "N°1 · PLACE BEAUVAU"))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BW} {BH}" width="{BW}" height="{BH}">{"".join(o)}</svg>'
    p = OUT + f"planche-{label}"
    open(p + ".svg", "w").write(svg)
    subprocess.run(["rsvg-convert", p + ".svg", "-o", p + ".png"], check=True)

    # separate deliverables for this version
    def save(name, w, h, body):
        f = OUT + f"premier-service-{label}-{name}"
        open(f + ".svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>')
        subprocess.run(["rsvg-convert", "-w", str(int(w * 2)), f + ".svg", "-o", f + ".png"], check=True)
    M = 60; ts = H * 0.55; g = H * 0.14
    save("vertical", W + 2*M, ts + g + H + 2*M, table(M + W/2, M + ts/2, ts) + draw(M, M + ts + g))
    hs = H * 0.92; hg = H * 0.2
    save("horizontal", hs + hg + W + 2*M, H + 2*M, table(M + hs/2, M + H/2, hs) + draw(M + hs + hg, M))
    save("badge-rdv1", 1200, 1200, badge(600, 600, 1080, sans, "N°1 · PLACE BEAUVAU"))
    save("sigle", 600, 600, table(300, 300, 540))


board("B-pinceau-affirme", "B")
board("C-compact", "C")
print("ok")
