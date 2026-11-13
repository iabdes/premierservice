"""Wordmark v7 — reproduit le logo fourni (Premier.png) : Premier ciel, SERVICE bleu, SERVICE inséré sous Premier."""
import sys
_a = sys.argv; sys.argv = ["x"]
import build_logo5 as G
sys.argv = _a
L = G.L
SKY = "#2C86D1"; SBLUE = "#1E2F86"
# mesures relevées sur Premier.png (largeur d'encre de Premier = 885 px)
PW = 900.0; K = PW / 885.0
S_LEFT, S_RIGHT = (242 - 195) * K, (1047 - 195) * K + K   # bords d'encre de SERVICE
S_TOP, CAP = (364 - 113) * K, (490 - 364 + 1) * K
def build():
    _, pb0 = L.shape(L.SCRIPT, "Premier", 100.0)
    psz = 100.0 * PW / (pb0[2] - pb0[0])
    pd, pb = L.shape(L.SCRIPT, "Premier", psz)
    XB = L.F["ExtraBold"]
    _, b0 = L.shape(XB, "SERVICE", 100.0); size = 100.0 * CAP / (b0[3] - b0[1])
    _, b1 = L.shape(XB, "SERVICE", size)
    track = ((S_RIGHT - S_LEFT) - (b1[2] - b1[0])) / 6 / size
    sd, sb = L.shape(XB, "SERVICE", size, track)
    # repère local : Premier encre en (0, 0)
    px, py = -pb[0], -pb[1]
    sx, sy = S_LEFT - sb[0], S_TOP - sb[1]
    H = max(pb[3] - pb[1], S_TOP + CAP)
    def draw(ox, oy, p=None, s=None):
        p = SKY if p in (None, G.RED) else p
        s = SBLUE if s in (None, G.BLUE) else s
        return (f'<path fill="{p}" transform="translate({ox + px:.2f},{oy + py:.2f})" d="{pd}"/>'
                f'<path fill="{s}" transform="translate({ox + sx:.2f},{oy + sy:.2f})" d="{sd}"/>')
    return PW, H, draw, S_TOP, CAP
W, H, draw, STOP, CAPH = build()
L.VARIANTS["C-compact"] = (W, H, draw, STOP)
