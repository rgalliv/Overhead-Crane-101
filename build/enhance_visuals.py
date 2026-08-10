#!/usr/bin/env python3
"""Inject visual-pack CSS + optional hero strip into existing gated HTML modules.

Does not rewrite question banks. Safe for M02-M11 that were not fully rebuilt.
"""
from __future__ import annotations

import base64
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET = os.path.join(ROOT, "assets", "images")

EXTRA_CSS = r"""
/* --- visual pack overlay --- */
.slide{background:
  radial-gradient(1200px 500px at 10% -10%, rgba(27,52,100,.55), transparent 60%),
  linear-gradient(160deg,#111a2c,#0d1522 55%,#0a101c)!important;
  transition:opacity .35s ease, transform .35s ease;transform:translateY(8px)}
.slide.active{transform:translateY(0)}
.slide.section-header,.slide.divider{background:linear-gradient(160deg,#1B3464,#12203c 70%,#0d1522)!important}
h1{font-family:Georgia,"Source Serif 4",serif;letter-spacing:-.01em}
.media-frame{margin:0 0 1em;border-radius:12px;overflow:hidden;border:1px solid #2b4478;
  box-shadow:0 12px 40px rgba(0,0,0,.35)}
.media-frame img{width:100%;display:block;max-height:38vh;object-fit:cover}
.media-cap{font-size:.78rem;color:#7d8ba6;margin:.45em 0 0;letter-spacing:.04em}
.progress-rail{height:3px;background:#1a2744;border-radius:2px;overflow:hidden;margin:0 0 14px}
.progress-rail>span{display:block;height:100%;width:0;background:linear-gradient(90deg,#C8991A,#e6c15a);
  transition:width .35s ease}
#score-chip{box-shadow:0 0 24px rgba(200,153,26,.35)}
.quiz-option{transition:border-color .15s, background .15s}
.quiz-option:hover{border-color:#C8991A}
"""

MODULE_IMAGE = {
    "OHC_M02": ("01-top-vs-underhung.jpg", "Structural configuration reference"),
    "OHC_M03": ("03-pendant-operator.jpg", "Pendant / floor operating mode"),
    "OHC_M04": ("01-hero-bridge.jpg", "Rated load marked on the bridge"),
    "OHC_M05": ("05-hook-inspection.jpg", "Hook and rope inspection"),
    "OHC_M06": ("06-rigging-spreader.jpg", "Below-the-hook interface"),
    "OHC_M07": ("06-rigging-spreader.jpg", "Load handling in progress"),
    "OHC_M08": ("03-pendant-operator.jpg", "Operational rules on the floor"),
    "OHC_M09": ("09-hand-signals.jpg", "Communication and signals"),
    "OHC_M10": ("01-canada-shop.jpg", "Site and environmental context"),
    "OHC_M11": ("11-emergency-stop.jpg", "Malfunction and emergency stop"),
}


def data_uri(name: str) -> str:
    raw = open(os.path.join(ASSET, name), "rb").read()
    return "data:image/jpeg;base64," + base64.b64encode(raw).decode("ascii")


def enhance(path: str, module: str) -> None:
    html = open(path, encoding="utf-8").read()
    if "visual pack overlay" not in html:
        html = html.replace("</style>", EXTRA_CSS + "\n</style>", 1)

    img = MODULE_IMAGE.get(module)
    if img and 'class="media-frame"' not in html.split('<section class="slide" id="s2"')[0]:
        uri, cap = data_uri(img[0]), img[1]
        block = (
            '<div class="media-frame"><img src="%s" alt=""></div>'
            '<p class="media-cap">%s</p>\n' % (uri, cap)
        )
        # Insert after first lede paragraph on slide 1
        html = re.sub(
            r'(<section class="slide" id="s1">[\s\S]*?<p class="lede">[\s\S]*?</p>)',
            r'\1\n    ' + block,
            html,
            count=1,
        )

    # progress rails on content slides lacking them
    if "progress-rail" not in html:
        html = html.replace(
            '<section class="slide" id="',
            '<section class="slide" id="',
        )  # no-op placeholder
        html = re.sub(
            r'(<section class="slide(?: section-header| divider)?" id="s\d+">)\s*'
            r'(?![\s\S]{0,80}progress-rail)',
            r'\1\n    <div class="progress-rail"><span></span></div>\n    ',
            html,
        )

    # Update render() to drive progress rail if not present
    if "progress-rail > span" not in html and "function render()" in html:
        html = html.replace(
            "var st=document.getElementById('stage'); if(st) st.scrollTop=0;\n}",
            "var st=document.getElementById('stage'); if(st) st.scrollTop=0;\n"
            "  var rail=document.querySelector('#s'+current+' .progress-rail > span');\n"
            "  if(rail) rail.style.width=Math.round((current/TOTAL)*100)+'%';\n}",
        )

    open(path, "w", encoding="utf-8").write(html)
    print("enhanced", path)


def main():
    out = os.path.join(ROOT, "out")
    for name in sorted(os.listdir(out)):
        if not name.endswith(".html") or name.endswith(".pre.html"):
            continue
        if not name.startswith("OHC_M"):
            continue
        mod = name.split("_")[0] + "_" + name.split("_")[1]  # OHC_M02
        # skip M01/M12 if freshly rebuilt with full pack — still safe to enhance
        enhance(os.path.join(out, name), mod)


if __name__ == "__main__":
    main()
