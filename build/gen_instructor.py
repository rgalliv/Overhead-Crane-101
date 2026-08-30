#!/usr/bin/env python3
"""Emit instructor run-of-show HTML from each module's build script + manifest.

Usage: python3 build/gen_instructor.py

Does not read or print answer keys. Knowledge-gate item counts only.
Tracking, designation, and practical sign-off are out of scope.
"""
from __future__ import annotations

import importlib.util
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(ROOT, "instructor")

MODULES = [
    ("01", "OHC_M01_EquipmentAndJurisdiction.html"),
    ("02", "OHC_M02_ComponentsAndSystems.html"),
    ("03", "OHC_M03_ControlsAndOperatingModes.html"),
    ("04", "OHC_M04_RatedLoadAndWeight.html"),
    ("05", "OHC_M05_InspectionRegime.html"),
    ("06", "OHC_M06_RiggingInterface.html"),
    ("07", "OHC_M07_LoadHandling.html"),
    ("08", "OHC_M08_OperationalRules.html"),
    ("09", "OHC_M09_CommunicationAndSignals.html"),
    ("10", "OHC_M10_EnvironmentalHazards.html"),
    ("11", "OHC_M11_MalfunctionsAndEmergencies.html"),
    ("12", "OHC_M12_Capstone.html"),
]

# Suggested classroom minutes. Not an OSHA or ASME duration.
PACE = {
    "01": (75, 20, "Walk the facility path first. Construction CC and EM 385 are the other customer."),
    "02": (50, 15, "Teach the components on this plant's cranes. Do not tour equipment the cohort will not run."),
    "03": (50, 15, "Stay on the control modes this plant actually uses (pendant, radio, cab)."),
    "04": (50, 15, "Rated-load markings and verified weight before the hook takes load."),
    "05": (55, 15, "Facility inspection spine is &#167;1910.179(j). Construction &#167;1926.1412 is the other customer."),
    "06": (55, 15, "Facility sling law is &#167;1910.184. ASME B30.9 is consensus, not the plant default regulation."),
    "07": (90, 20, "Do not rush. Operators must leave able to hoist, travel, and place &#8212; not just pass a quiz."),
    "08": (55, 15, "Personnel-under-load and securing rules from &#167;1910.179(n)."),
    "09": (55, 15, "Plant signals first. Subpart CC signal sections apply on the construction branch (other customer)."),
    "10": (55, 15, "Name &#167;1910.147 for energy control / LOTO. Do not invent this plant's procedure numbers."),
    "11": (50, 15, "Malfunction response on the assigned crane. Do not invent emergency numbers."),
    "12": (50, 20, "This hour is the knowledge test wrap. Designation and practical records live in the company's system."),
}

FACILITY = (
    "<b>Plant default (this in-house program):</b> 29 CFR 1910.179; ANSI B30.2.0-1967 as "
    "incorporated at &#167;1910.179(b)(2); slings under &#167;1910.184; energy control under "
    "&#167;1910.147; designated personnel under &#167;1910.179(b)(8)."
)

OTHER = (
    "<b>Other customer (in the ACS, not this plant's default):</b> construction branch "
    "&#167;1926.1438 / Certification Gate &#167;1926.1427, and EM 385-1-1 Chapter 16 "
    "(federal / USACE). Canada (CSA B167 + provincial OH&amp;S) is an overlay, not a fork."
)


def load_mod(nn):
    path = os.path.join(HERE, "build_OHC_M%s.py" % nn)
    spec = importlib.util.spec_from_file_location("m" + nn, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mdish(s):
    """Light markdown used in TRACE_NOTES → HTML. Does not invent citations."""
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    return s


def content_bits(entry):
    title, body = entry[0], entry[1]
    note = entry[2] if len(entry) > 2 else ""
    return title, body, note


CSS = """:root{--navy:#1B3464;--gold:#C8991A;--ink:#0d1522;--mist:#445;--line:#c9ced8;--paper:#f4f6f9}
*{box-sizing:border-box}
body{margin:0;font-family:"Source Sans 3",Calibri,system-ui,sans-serif;color:var(--ink);background:var(--paper);line-height:1.5}
.wrap{max-width:880px;margin:0 auto;padding:28px 20px 64px}
.brand{letter-spacing:.14em;text-transform:uppercase;font-size:.72rem;color:var(--gold);font-weight:700}
h1{font-family:Georgia,"Source Serif 4",serif;color:var(--navy);font-size:1.65rem;margin:.3em 0 .4em}
h2{font-family:Georgia,serif;color:var(--navy);font-size:1.15rem;margin:1.6em 0 .5em;border-bottom:2px solid var(--navy);padding-bottom:.25em}
h3{color:var(--navy);font-size:1.02rem;margin:1.2em 0 .35em}
.lede{color:#334;max-width:46rem}
.meta{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px;margin:16px 0}
.meta div{background:#fff;border:1px solid var(--line);border-radius:8px;padding:10px 12px}
.meta b{display:block;font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:#667}
.path{background:#eef2fa;border-left:4px solid var(--navy);padding:12px 14px;margin:14px 0;font-size:.92rem}
.warn{background:#fff8e8;border-left:4px solid var(--gold);padding:12px 14px;margin:14px 0}
.gate{background:#e8f6ee;border-left:4px solid #2f9e64;padding:12px 14px;margin:14px 0}
.note{color:#445;font-size:.92rem;margin:.4em 0 .8em}
.talk{margin:0 0 1em;padding-left:1.15em}
.talk li{margin:0 0 .7em}
.talk .aside{display:block;color:#445;font-size:.9rem;margin-top:.25em}
nav a,a{color:var(--navy)}
.bar{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 8px}
.bar a{display:inline-block;padding:8px 14px;background:var(--navy);color:#fff;text-decoration:none;border-radius:8px;font-weight:700;font-size:.9rem}
.bar a.ghost{background:#fff;color:var(--navy);border:1px solid var(--navy)}
table{width:100%;border-collapse:collapse;background:#fff;font-size:.92rem}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:#e8eef8;color:var(--navy)}
.fine{font-size:.82rem;color:#556;margin-top:28px}
ol.day{padding-left:1.2em}
ol.day li{margin:0 0 .45em}
@media print{
  body{background:#fff}
  .bar a.ghost, .noprint{display:none}
  .bar a{border:1px solid #000;color:#000;background:#fff}
  .wrap{padding:0}
}
"""


def emit_module(nn, outfile):
    m = load_mod(nn)
    man = json.load(open(os.path.join(ROOT, "manifests", "OHC_M%s.json" % nn)))
    present, gatem, pace_note = PACE[nn]
    gate_n = len(man["gate"])
    prac_n = len(getattr(m, "PRACTICE", []))
    next_mod = man.get("next") or ""
    next_label = "OHC-%s" % next_mod.replace("OHC_M", "") if next_mod else "end of track"
    next_href = ""
    for n2, f2 in MODULES:
        if "OHC_M%s" % n2 == next_mod:
            next_href = "OHC_M%s.html" % n2
            break

    talk = []
    for code, title, obj in m.SECTIONS:
        items = []
        for entry in m.CONTENT.get(code, []):
            ht, body, note = content_bits(entry)
            aside = ('<span class="aside">%s</span>' % note) if note else ""
            items.append("<li><b>%s.</b> %s%s</li>" % (ht, body, aside))
        talk.append(
            "<h3>Task %s &#8212; %s</h3>\n<p class=\"note\">%s</p>\n<ol class=\"talk\">\n%s\n</ol>"
            % (code, title, obj, "\n".join(items))
        )

    notes = getattr(m, "TRACE_NOTES", []) or []
    note_html = ""
    if notes:
        lis = "".join("<li><b>%s.</b> %s</li>" % (mdish(h), mdish(b)) for h, b in notes)
        note_html = "<h2>Teach it correctly &#8212; do not guess</h2>\n<ul class=\"talk\">%s</ul>" % lis

    banner = ""
    if nn == "07":
        banner = (
            "<div class=\"warn\"><b>OHC-07 is the session that cannot be waved through.</b> "
            "Present the full talk track, then run the knowledge gate. "
            "&#167;1910.179(n)(3)(iv) does <b>not</b> flatly ban side pulls &#8212; they require "
            "a responsible person and two determinations (stability, overstress). "
            "Teaching a flat ban will lose the room. Two-blocking is not solved by riding "
            "the upper limit switch. Two full wraps must remain on the drum.</div>"
        )
    if nn == "12":
        banner = (
            "<div class=\"warn\"><b>Knowledge test wrap, not a records desk.</b> "
            "Capstone still teaches that designation is an employer determination "
            "(&#167;1910.179(b)(8)). Do not run roster, PES, or certificate workflows "
            "from this repo &#8212; those live in the company's tracking system. "
            "This hour: present, then the 30-item knowledge gate.</div>"
        )

    objs = "".join("<li>%s</li>" % o for o in m.OBJECTIVES)
    prev = ""
    n_int = int(nn)
    if n_int > 1:
        prev = '<a class="ghost" href="OHC_M%02d.html">Previous script</a>' % (n_int - 1)
    nxt_script = ""
    if next_href:
        nxt_script = '<a class="ghost" href="%s">Next script (%s)</a>' % (next_href, next_label)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Instructor script &#8212; OHC-%s %s</title>
<link rel="stylesheet" href="instructor.css">
</head>
<body>
<div class="wrap">
  <div class="brand">CraneQualified &#183; OCO301C &#183; In-house instructor script</div>
  <h1>OHC-%s &#8212; %s</h1>
  <p class="lede">%s</p>
  <div class="meta">
    <div><b>Present</b> ~%d min</div>
    <div><b>Knowledge gate</b> ~%d min &#183; %d items &#183; 100%%</div>
    <div><b>Practice (unscored)</b> %d items during presentation</div>
    <div><b>Slides</b> %d</div>
    <div><b>Next</b> %s</div>
  </div>
  <p class="note">%s Suggested plant pacing, not a regulatory duration.</p>
  %s
  <div class="path">%s<br>%s</div>
  <div class="bar">
    <a href="../out/%s">Open gated module</a>
    <a class="ghost" href="index.html">All scripts</a>
    %s
    %s
    <a class="ghost noprint" href="#" onclick="window.print();return false">Print / Save PDF</a>
  </div>

  <h2>How this hour runs</h2>
  <ol class="day">
    <li><b>Instructor presents</b> using this script and the gated HTML. Operators do not self-enroll or skip ahead.</li>
    <li>Use the <b>unscored practice</b> questions as teaching checks. Those show the correct option.</li>
    <li>Then run the <b>Final Knowledge Check</b> in the module. That is the corporate knowledge test. It requires <b>100%%</b>. Missed gate items do <b>not</b> reveal the answer. Operators review and retest.</li>
    <li>Do <b>not</b> open the next module until the instructor releases it. The M01&#8594;M12 handshake stays; pace is instructor-controlled.</li>
    <li>Practical evaluation, designation, attendance, and records are <b>not</b> in this file. They live in the company's tracking system.</li>
  </ol>

  <h2>What they should be able to do after the presentation</h2>
  <ul>%s</ul>

  <h2>Talk track &#8212; present this, then gate</h2>
  %s

  %s

  <div class="gate">
    <h2 style="margin-top:0;border:0">Knowledge test</h2>
    <p>After the talk track, operators take the gate in <code>out/%s</code>.
    <b>%d items</b>, gate code <b>OHC-1</b>, pass mark <b>100%%</b>.
    Do not read answers aloud. Do not skip the gate.
    Record pass/fail in the company's system if the plant requires it &#8212; this page does not store people.</p>
  </div>

  <p class="fine">Content author: CraneQualified / CCOS. Training establishes standard of care; the controlling entity designates. Generated from module build data by <code>build/gen_instructor.py</code>. Do not hand-edit &#8212; regenerate.</p>
</div>
</body>
</html>
""" % (
        nn, m.TITLE,
        nn, m.TITLE,
        m.SUBTITLE,
        present, gatem, gate_n, prac_n, man["total"], next_label,
        pace_note,
        banner,
        FACILITY, OTHER,
        outfile,
        prev, nxt_script,
        objs,
        "\n".join(talk),
        note_html,
        outfile, gate_n,
    )
    path = os.path.join(OUT_DIR, "OHC_M%s.html" % nn)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


def emit_index(rows):
    body_rows = "\n".join(rows)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Instructor run-of-show &#8212; OCO301C</title>
<link rel="stylesheet" href="instructor.css">
</head>
<body>
<div class="wrap">
  <div class="brand">CraneQualified &#183; OCO301C &#183; In-house program</div>
  <h1>Instructor run-of-show</h1>
  <p class="lede">Twelve instructor scripts for plant trainers. Present the module, then run the knowledge gate. Do not skip ahead. Tracking and designation are not here.</p>
  <div class="path">%s<br>%s</div>
  <div class="bar">
    <a href="../index.html">Program hub</a>
    <a class="ghost" href="../PROGRAM.md">PROGRAM.md</a>
    <a class="ghost noprint" href="#" onclick="window.print();return false">Print this index</a>
  </div>
  <h2>Run in order</h2>
  <table>
    <thead><tr><th>Module</th><th>Present ~</th><th>Gate</th><th>Open</th></tr></thead>
    <tbody>
%s
    </tbody>
  </table>
  <p class="note">OHC-07 load handling is the session that must not be waved through. Rebuild these pages with <code>python3 build/gen_instructor.py</code>.</p>
  <p class="fine">Content author: CraneQualified / CCOS. Canada pack is an overlay on OHC-01 / OHC-12, not a fork.</p>
</div>
</body>
</html>
""" % (FACILITY, OTHER, body_rows)
    path = os.path.join(OUT_DIR, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "instructor.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    rows = []
    for nn, outfile in MODULES:
        emit_module(nn, outfile)
        m = load_mod(nn)
        man = json.load(open(os.path.join(ROOT, "manifests", "OHC_M%s.json" % nn)))
        present, gatem, _ = PACE[nn]
        rows.append(
            "<tr><td><b>OHC-%s</b><br>%s</td><td>%d min</td><td>%d items / %d min / 100%%</td>"
            "<td><a href=\"OHC_M%s.html\">Script</a> &#183; "
            "<a href=\"../out/%s\">Module</a></td></tr>"
            % (nn, m.TITLE, present, len(man["gate"]), gatem, nn, outfile)
        )
    emit_index(rows)


if __name__ == "__main__":
    main()
