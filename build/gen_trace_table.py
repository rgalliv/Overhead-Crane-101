#!/usr/bin/env python3
"""Emit docs/OHC-01-trace-table.md from the build script's own question data.

Generated, not hand-maintained: the trace table and the module can never drift
apart, because both come from the same list.
"""
import importlib.util
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

spec = importlib.util.spec_from_file_location("b", os.path.join(HERE, "build_OHC_M01.py"))
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

MAN = json.load(open(os.path.join(ROOT, "manifests", "OHC_M01.json")))

# element -> (assessment focus, source, status)
META = {
    "OHC.01.A.K1": ("Equipment family, including that it applies **irrespective of travel means**", "&sect;1926.1438(b)(1)", "OK"),
    "OHC.01.A.K2": ("Top-running vs underhung bridge and trolley configuration", "ASME B30.2 / B30.17", "OK"),
    "OHC.01.A.K3": ("Single- vs double-girder; **longer span permits lower capacity**", "CMAA 70", "OK"),
    "OHC.01.A.K4": ("Monorail, underhung and wall/jib as related but distinct classes", "ASME B30.11", "OK"),
    "OHC.01.A.K5": ("Match configuration to governing volume", "B30.2 / B30.17", "EDITION"),
    "OHC.01.A.K6": ("Hoist as a distinct component class", "ASME B30.16", "OK"),
    "OHC.01.A.K7": ("**Incorporation by reference** &mdash; a standard named is guidance; a standard incorporated is regulation", "&sect;1910.6 &middot; &sect;1910.179(b)(2),(b)(6)(i)", "NEW"),
    "OHC.01.A.R1": ("Misclassification attaches the wrong inspection, marking and operating rule set", "derived", "OK"),
    "OHC.01.A.R2": ("Mobile-crane logic does not transfer", "&sect;1910.179(b)(5)", "OK"),
    "OHC.01.A.R3": ("Unfamiliar configuration without familiarization", "Tier 0 (owned)", "OK"),
    "OHC.01.B.K1": ("Permanently installed in construction &rarr; &sect;1910.179 except (b)(1)", "&sect;1926.1438(a)", "OK"),
    "OHC.01.B.K2": ("Not permanently installed &rarr; designated Subpart CC incl. &sect;1926.1427", "&sect;1926.1438(b)", "OK"),
    "OHC.01.B.K3": ("Which &sect;1910.179 paragraphs survive on the construction branch", "&sect;1926.1438(b)(2)(i)", "OK"),
    "OHC.01.B.K4": ("General-industry facility &rarr; &sect;1910.179 direct", "&sect;1910.179", "OK"),
    "OHC.01.B.K5": ("Federal/USACE &mdash; applies whether or not permanently installed", "EM 385 &sect;16 scope", "OK"),
    "OHC.01.B.K6": ("Indicators of permanent installation", "&sect;1926.1438(a)", "OK"),
    "OHC.01.B.K7": ("**Two editions** &mdash; ANSI B30.2.0-1967 (facility, installed on/after 31 Aug 1971) vs ASME B30.2-2005 sections (construction, manufactured on/after 19 Sep 2001)", "&sect;1910.179(b)(2) &middot; &sect;1926.1438(b)(2)(ii)", "NEW"),
    "OHC.01.B.R1": ("Facility rules on a construction-branch crane &rarr; misses &sect;1926.1427", "derived", "OK"),
    "OHC.01.B.R2": ("Assuming Subpart CC applies to a permanently installed crane", "&sect;1926.1438(a)", "OK"),
    "OHC.01.B.R3": ("Failing to re-evaluate when crane or context changes", "derived", "OK"),
    "OHC.01.C.K1": ("The **controlling entity** determines qualification", "Gate Master Rev 1.3 &sect;11.2, A2", "OK"),
    "OHC.01.C.K2": ("Designation Gate &mdash; only designated personnel may operate", "**&sect;1910.179(b)(8)** + **(a)(35)**", "OK"),
    "OHC.01.C.K3": ("Certification Gate on the construction branch", "&sect;1926.1427", "NCCCO"),
    "OHC.01.C.K4": ("Competent Person for Crane and Rigging signs the **Certificate of Compliance** for each piece of LHE brought on site", "**EM 385 &sect;16.A.02**", "NEW"),
    "OHC.01.C.K5": ("Designation vs **appointed person** vs maintenance qualified person", "&sect;1910.179(b)(8), (l)(3)(i), (m)(1)", "OK"),
    "OHC.01.C.R1": ("Course completion is not qualification", "Gate Master &sect;11.2", "OK"),
    "OHC.01.C.R2": ("LHE operated **only by trained, qualified and designated personnel**", "**EM 385 &sect;16.B.01**", "NEW"),
    "OHC.01.C.R3": ("Blurred accountability when roles are undocumented", "derived", "OK"),
}

STATUS = {
    "OK": "&#9989;",
    "NEW": "&#9989; **new**",
    "EDITION": "&#9888;&#65039; *edition*",
    "NCCCO": "&#9888;&#65039; *cite the reg*",
}

HELD = [
    ("`OHC.01.B.K3` *(2nd aspect)*", "The enumerated ASME B30.2-2005 section list at &sect;1926.1438(b)(2)(ii)",
     "Archived Subpart CC scan is column-interleaved OCR and unreadable at that passage. B30.2-2005 is now in the vault, so it can be checked from both ends."),
]

PERF = [
    ("OHC.01.A.S1", "Identify crane type, girder configuration and trolley arrangement on sight"),
    ("OHC.01.A.S2", "Match a given crane to its governing ASME volume by name"),
    ("OHC.01.A.S3", "Locate and interpret equipment identification and capacity markings"),
    ("OHC.01.B.S1", "Walk the installation-status decision tree and state the governing regime"),
    ("OHC.01.B.S2", "Identify which certification or designation attaches on each branch"),
    ("OHC.01.B.S3", "Classify a crane as EM 385 Class I or Class II &mdash; &sect;16.C.02 / &sect;16.C.05"),
    ("OHC.01.C.S1", "State who issued their designation, what it covers, and its limits"),
    ("OHC.01.C.S2", "Produce designation and training records on request"),
    ("OHC.01.C.S3", "Refuse an assignment outside the scope of designation"),
]


def strip(t):
    t = re.sub(r"&#\d+;", lambda m: {"&#8212;": "-", "&#183;": "-"}.get(m.group(0), ""), t)
    return t.strip()


def main():
    n_prac = len(b.PRACTICE)
    rows_by_task = {"A": [], "B": [], "C": []}
    for gi, q in enumerate(b.GATE):
        qnum = n_prac + 1 + gi
        elem = q[1]
        task = elem.split(".")[2][0]
        focus, src, st = META.get(elem, ("&mdash;", "&mdash;", "OK"))
        rows_by_task[task].append(
            "| `OHC_M01_q%02d` | `%s` | %s | %s | %s | %s |"
            % (qnum, elem, focus, "TF" if len(q[3]) == 2 else "MC", src, STATUS[st]))

    prac_rows = []
    for i, q in enumerate(b.PRACTICE):
        prac_rows.append("| `OHC_M01_q%02d` | `%s` | %s |"
                         % (i + 1, q[1], strip(q[2])))

    L = []
    L.append("# OHC-01 &mdash; Element-to-Item Trace Table")
    L.append("")
    L.append("> **Generated file.** Emitted by `build/gen_trace_table.py` from the same "
             "question data that builds the module. Do not hand-edit &mdash; regenerate.")
    L.append("")
    L.append("**Module:** OHC-01 Equipment Types, Configurations, and Jurisdictional Framework  ")
    L.append("**Course:** OCO301C &middot; **Gate:** OHC-1 &middot; **File:** `%s`  " % "OHC_M01_EquipmentAndJurisdiction.html")
    L.append("**Slides:** %d &middot; **Gate items:** %d &middot; **Practice:** %d &middot; "
             "**Performance:** %d &middot; **Pass:** 100%%, server-authoritative  "
             % (MAN["total"], len(MAN["gate"]), n_prac, len(PERF)))
    L.append("**Salt:** `%s` &middot; **Next:** `%s` &middot; **review_offset:** %d"
             % (MAN["salt"], MAN["next"], MAN["review_offset"]))
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Standing rules")
    L.append("")
    L.append("- **One element, one gate item.** An item testing two elements cannot be traced, "
             "and an untraceable item cannot be defended.")
    L.append("- **Every K and R element is gated.** The ACS states every element is a gateable "
             "claim; none are taught-but-untested.")
    L.append("- **Practice sits on top, not inside.** Practice previews the gate, is unscored, "
             "and reveals the answer. It does not reduce gate coverage.")
    L.append("- **The correct option is never revealed on a gate miss.** Wrong retries, correct locks.")
    L.append("- **S elements never appear here.** They live on `OHC_M01_PES.docx` and are signed "
             "by an evaluator, not scored by the bridge.")
    L.append("")
    L.append("---")
    L.append("")

    titles = {"A": "Task A &mdash; Equipment Identification and Classification",
              "B": "Task B &mdash; Jurisdictional Determination",
              "C": "Task C &mdash; Roles, Qualification Architecture, and Standard of Care"}
    for t in "ABC":
        L.append("## " + titles[t])
        L.append("")
        L.append("| Item | Element | Assessment focus | Form | Source | Status |")
        L.append("|---|---|---|---|---|---|")
        L.extend(rows_by_task[t])
        L.append("")

    L.append("---")
    L.append("")
    L.append("## Practice items (unscored)")
    L.append("")
    L.append("| Item | Element previewed | Stem |")
    L.append("|---|---|---|")
    L.extend(prac_rows)
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Performance items &mdash; `OHC_M01_PES.docx`")
    L.append("")
    L.append("Not scored by the bridge. Evaluator sign-off, dated, scoped to named equipment "
             "and control modes.")
    L.append("")
    L.append("| Item | Element | Demonstration |")
    L.append("|---|---|---|")
    for i, (e, d) in enumerate(PERF):
        L.append("| `OHC01-P%02d` | `%s` | %s |" % (i + 1, e, d))
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Held back &mdash; not authored")
    L.append("")
    L.append("%s below %s no gate item because the source cannot yet be read. Absent "
             "rather than invented \u2014 adding it is a manifest edit plus a pipeline "
             "re-run, not a rebuild."
             % ("One element" if len(HELD) == 1 else "%d elements" % len(HELD),
                "has" if len(HELD) == 1 else "have"))
    L.append("")
    L.append("| Element | Claim | Blocked on |")
    L.append("|---|---|---|")
    for e, c, w in HELD:
        L.append("| %s | %s | %s |" % (e, c, w))
    L.append("")
    L.append("---")
    L.append("")
    L.append("## ACS amendment recorded here")
    L.append("")
    L.append("Two elements are **net-new** and are not in the published ACS. They came out of "
             "the Part 1910 map and both are verified against &sect;1910.179's own text:")
    L.append("")
    L.append("- **`OHC.01.A.K7`** &mdash; incorporation by reference. A consensus standard cited "
             "by name is guidance; one incorporated under &sect;1910.6 or &sect;1926.6 is "
             "regulation for the sections named.")
    L.append("- **`OHC.01.B.K7`** &mdash; the two-edition split. ANSI B30.2.0-1967 on the "
             "facility branch for cranes installed on or after 31 Aug 1971; ASME B30.2-2005 "
             "sections on the construction branch for equipment manufactured on or after "
             "19 Sep 2001.")
    L.append("")
    L.append("**Census effect.** OHC-01 moves from 17 K to 19 K, so the module carries "
             "19 K + 9 R + 9 S = 37 elements and the track total moves 398 &rarr; 400. "
             "The ACS census table in &sect;7 needs the same amendment.")
    L.append("")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    out = os.path.join(ROOT, "docs", "OHC-01-trace-table.md")
    if os.path.exists(out):
        os.remove(out)
    with open(out, "w", encoding="utf-8") as f:
        f.write(main())
    print("wrote", out)
