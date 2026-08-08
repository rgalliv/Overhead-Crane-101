#!/usr/bin/env python3
"""Emit docs/OHC-02-trace-table.md from build_OHC_M02's own data."""
import importlib.util, json, os
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
spec=importlib.util.spec_from_file_location("m2",os.path.join(HERE,"build_OHC_M02.py"))
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
MAN=json.load(open(os.path.join(ROOT,"manifests","OHC_M02.json")))
ST={"OK":"&#9989;","CMAA74":"&#9888;&#65039; *CMAA 74*","BRANCH":"&#9888;&#65039; *branch*"}
T={"A":"Task A &mdash; Structural Systems","B":"Task B &mdash; Mechanical Systems",
   "C":"Task C &mdash; Electrical and Control Systems"}
L=["# OHC-02 &mdash; Element-to-Item Trace Table","",
   "> **Generated file.** Emitted by `build/gen_trace_M02.py` from the same question data "
   "that builds the module. Do not hand-edit &mdash; regenerate.","",
   "**Module:** OHC-02 Crane Components and Systems  ",
   "**Course:** OCO301C &middot; **Gate:** OHC-1 &middot; **File:** `OHC_M02_ComponentsAndSystems.html`  ",
   "**Slides:** %d &middot; **Gate items:** %d &middot; **Practice:** %d &middot; "
   "**Performance:** %d &middot; **Pass:** 100%%, server-authoritative  "
   %(MAN["total"],len(MAN["gate"]),len(m.PRACTICE),len(m.TRACE_PERF)),
   "**Salt:** `%s` &middot; **Next:** `%s` &middot; **review_offset:** %d"
   %(MAN["salt"],MAN["next"],MAN["review_offset"]),"","---",""]
rows={"A":[],"B":[],"C":[]}
for gi,q in enumerate(m.GATE):
    n=len(m.PRACTICE)+1+gi; e=q[0]; t=e.split(".")[2][0]
    src,st=m.TRACE_SOURCE.get(e,("&mdash;","OK"))
    rows[t].append("| `OHC_M02_q%02d` | `%s` | %s | %s | %s | %s |"
                   %(n,e,q[1].replace("|","&#124;"),"TF" if len(q[2])==2 else "MC",src,ST[st]))
for t in "ABC":
    L+=["## "+T[t],"","| Item | Element | Stem | Form | Source | Status |","|---|---|---|---|---|---|"]+rows[t]+[""]
L+=["---","","## Practice items (unscored)","","| Item | Element previewed | Stem |","|---|---|---|"]
for i,q in enumerate(m.PRACTICE):
    L.append("| `OHC_M02_q%02d` | `%s` | %s |"%(i+1,q[0],q[1].replace("|","&#124;")))
L+=["","---","","## Performance items &mdash; `OHC_M02_PES.docx`","",
    "Not scored by the bridge. Evaluator sign-off, dated, scoped to named equipment and control modes.","",
    "| Item | Element | Demonstration |","|---|---|---|"]
for i,(e,d) in enumerate(m.TRACE_PERF):
    L.append("| `OHC02-P%02d` | `%s` | %s |"%(i+1,e,d))
L+=["","---","","## Source notes",""]
for h,b in m.TRACE_NOTES:
    L+=["**%s** &mdash; %s"%(h,b),""]
L+=["---","",
    "## Coverage","",
    "All **15 K** and **9 R** elements are gated, one item each &mdash; 24 gate items, "
    "no held-back items. The **9 S** elements sit on the Performance Evaluation Sheet. "
    "OHC-02 carries 33 elements, unchanged from the published ACS.",""]
out=os.path.join(ROOT,"docs","OHC-02-trace-table.md")
if os.path.exists(out): os.remove(out)
open(out,"w",encoding="utf-8").write("\n".join(L)+"\n")
print("wrote",out)
