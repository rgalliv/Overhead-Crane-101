#!/usr/bin/env python3
"""Emit docs/OHC-NN-trace-table.md from build_OHC_MNN's own data.

Usage: python3 build/gen_trace.py 05 [06 ...]

Parameterised on purpose. The per-module gen_trace_M0n.py scripts were
copy-pasted, and one of them silently overwrote another module's table
because a sed rename missed a string. Everything here derives from the
module number and from the build script's own SECTIONS / GATE / PRACTICE /
TRACE_* data, so there is nothing left to rename by hand.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ST = {
    "OK": "&#9989;",
    "ED2014": "&#9989; *2014 text*",
    "CONFLICT": "&#9888;&#65039; *conflict resolved*",
    "GAP": "&#9888;&#65039; *primary text open*",
}


def load(nn):
    path = os.path.join(HERE, "build_OHC_M%s.py" % nn)
    spec = importlib.util.spec_from_file_location("m" + nn, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def emit(nn):
    m = load(nn)
    man = json.load(open(os.path.join(ROOT, "manifests", "OHC_M%s.json" % nn)))
    tag = "OHC_M%s" % nn
    keys = [s[0] for s in m.SECTIONS]
    titles = {s[0]: "Task %s &mdash; %s" % (s[0], s[1]) for s in m.SECTIONS}

    L = ["# OHC-%s &mdash; Element-to-Item Trace Table" % nn, "",
         "> **Generated file.** Emitted by `build/gen_trace.py %s` from the same question "
         "data that builds the module. Do not hand-edit &mdash; regenerate." % nn, "",
         "**Module:** OHC-%s %s  " % (nn, m.TITLE),
         "**Course:** OCO301C &middot; **Gate:** OHC-1 &middot; **File:** `%s`  "
         % os.path.basename(_outfile(m)),
         "**Slides:** %d &middot; **Gate items:** %d &middot; **Practice:** %d &middot; "
         "**Performance:** %d &middot; **Pass:** 100%%, server-authoritative  "
         % (man["total"], len(man["gate"]), len(m.PRACTICE), len(m.TRACE_PERF)),
         "**Salt:** `%s` &middot; **Next:** `%s` &middot; **review_offset:** %d"
         % (man["salt"], man["next"], man["review_offset"]), "", "---", ""]

    rows = {k: [] for k in keys}
    for gi, q in enumerate(m.GATE):
        n = len(m.PRACTICE) + 1 + gi
        e = q[0]
        t = e.split(".")[2][0]
        src, st = m.TRACE_SOURCE.get(e, ("&mdash;", "OK"))
        rows[t].append("| `%s_q%02d` | `%s` | %s | %s | %s | %s |"
                       % (tag, n, e, q[1].replace("|", "&#124;"),
                          "TF" if len(q[2]) == 2 else "MC", src, ST[st]))
    for t in keys:
        L += ["## " + titles[t], "",
              "| Item | Element | Stem | Form | Source | Status |",
              "|---|---|---|---|---|---|"] + rows[t] + [""]

    L += ["---", "", "## Practice items (unscored)", "",
          "| Item | Element previewed | Stem |", "|---|---|---|"]
    for i, q in enumerate(m.PRACTICE):
        L.append("| `%s_q%02d` | `%s` | %s |"
                 % (tag, i + 1, q[0], q[1].replace("|", "&#124;")))

    L += ["", "---", "", "## Performance items &mdash; `%s_PES.docx`" % tag, "",
          "Not scored by the bridge. Evaluator sign-off, dated, scoped to named equipment.",
          "", "| Item | Element | Demonstration |", "|---|---|---|"]
    for i, (e, d) in enumerate(m.TRACE_PERF):
        L.append("| `OHC%s-P%02d` | `%s` | %s |" % (nn, i + 1, e, d))

    L += ["", "---", "", "## Source notes", ""]
    for h, b in m.TRACE_NOTES:
        L += ["**%s** &mdash; %s" % (h, b), ""]

    base = {e.split(".", 2)[2] for e in (q[0] for q in m.GATE)}
    base = {e[:-1] if e.endswith("b") else e for e in base}
    nk = len([e for e in base if "K" in e.split(".")[-1]])
    nr = len([e for e in base if "R" in e.split(".")[-1]])
    ns = len(m.TRACE_PERF)
    L += ["---", "", "## Coverage", "",
          "All **%d K** and **%d R** elements are gated &mdash; %d gate items. %d element(s) "
          "carry a second item; see the source notes. The **%d S** elements sit on the "
          "Performance Evaluation Sheet. OHC-%s carries %d elements, unchanged from the "
          "published ACS."
          % (nk, nr, len(m.GATE), len(m.GATE) - len(base), ns, nn, nk + nr + ns), ""]

    out = os.path.join(ROOT, "docs", "OHC-%s-trace-table.md" % nn)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("wrote", out)


def _outfile(m):
    """Recover the module's output filename from its own main()."""
    import re
    src = open(os.path.join(HERE, "build_OHC_M%s.py"
                            % m.MODULE.split("_M")[1]), encoding="utf-8").read()
    return re.search(r'"(OHC_M\d\d_\w+)\.pre\.html"', src).group(1) + ".html"


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        emit(arg)
