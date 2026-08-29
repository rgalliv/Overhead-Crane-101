# OHC Build Format & Question Architecture

**Derived from the CraneQualified mobile-crane Developer Handoff (July).**
Structure, gating contract, packaging and question architecture only. **No instructional content, no question text, no answers, and no narration were taken from the mobile track** — those remain equipment-specific and are authored fresh for OHC.

---

## 1. The finding that resolves the spec's central contradiction

The OHC ACS build spec §1 mandates a *"server-authoritative 100% mastery gate."* Its §4 specifies deliverables of *"PPTX deck + Facilitator Guide DOCX (2 files/module)."*

Those two sentences come from **two different product lines**:

| | **ILT line** — `EQ-TRAIN-003/004` | **Workforce LMS line** — CraneQualified Workforce |
|---|---|---|
| Deliverable | PPTX + Facilitator Guide DOCX | **Single self-contained HTML file per module** |
| Scale | 43 modules, 86 files | **72 modules across 7 stages** |
| Gate | 8-question final KC, **80% pass** | **Server-authoritative, 100% required** |
| Scoring authority | facilitator | `CQ.scoreAnswer()` on the server |
| Build stack | Node · PptxGenJS · docx | HTML with inlined bridge |

**A PPTX cannot enforce a server-authoritative gate.** The 100% mastery gate the OHC spec asks for exists, is built, and is in production — but only in the HTML line.

**Resolution:** OHC ships **both**, and the spec should say so.

| Deliverable | Purpose | Carries the gate? |
|---|---|---|
| `OHC_Mnn_*.html` | LMS module — the gated deliverable | **Yes** — server-scored |
| `OHC_Mnn_*.pptx` | ILT delivery | No |
| `OHC_Mnn_*_FG.docx` | Facilitator guide | No |
| `OHC_Mnn_*_PES.docx` | Performance evaluation sheet — the S elements | Field sign-off |

Four files per module, 48 at track completion. The current spec says two files per module and 24 at completion; that count assumes the gate lives somewhere it cannot live.

---

## 2. Package structure

Mirror the mobile handoff exactly. One folder, one shape, no per-stage variation:

```
OHC - <month>/
  modules/              <- deployable HTML files (edit or upload these)
  platform/             <- server answer key(s) — SERVER-SIDE ONLY, never served to learners
  docs/                 <- QA, manifest, source notes
  MODULE_MANIFEST.csv   <- per-module inventory
```

A `OHC - <month>.zip` sits beside the folder and is regenerated **from the accepted folder** whenever modules change. The mobile handoff carries an explicit warning that its Stage 2–4 root ZIPs went stale against their folders — treat the unpacked folder as source of truth and the ZIP as a build artifact, never the reverse.

**`MODULE_MANIFEST.csv` columns**, unchanged from mobile:

```
Module,File,SizeMB,EmbeddedImages,EmbeddedAudio,TTSFallback,GateArch,SelfContained
```

**Naming:** `OHC_M01_EquipmentAndJurisdiction.html` — track prefix, zero-padded module number, CamelCase title. Filename and in-module title must match; the mobile track had to correct one module where they had drifted apart.

**Self-containment (hard requirement):** every image, script, style and narration asset inlined. Audio as `data:audio`. **No external references of any kind.** Mobile achieved 72/72 self-contained with 2,454 embedded MP3s and zero external audio references.

**Size ceiling: every module below 15 MB.** Mobile enforced this retroactively and it cost real work — Stage 4 came down from 807 MB to 129 MB, Stage 5 from 205 MB to 72 MB. Narration recompressed to **32 kbps mono MP3** to get there. Build to the ceiling from day one rather than remediating.

---

## 3. Gating contract

**Adopt verbatim. Do not re-invent this layer** — it is built, audited and in production across 72 modules.

```
CQ.scoreAnswer(questionId, selectedIndex)   -> production correctness authority
CQ.requestComplete()                         -> completion only after all gate questions verified correct
```

Message contract across the bridge:

```
cq:kc_attempt      -> cq:kc_result
cq:complete_request -> cq:complete_granted | cq:complete_denied
```

**Non-negotiables carried over from the mobile handoff:**

- **The server is the authority.** The protected registry in `platform/` determines correctness. The client flag `window.__cqGateComplete` is UI and navigation state only, never the source of truth.
- **FNV / `Math.imul` code stays, but only for standalone preview.** All 72 mobile modules contain it. The handoff is blunt that client-side fallback *"must never be accepted as production scoring authority."* The same applies here.
- **`platform/` is never served to a browser.** Not to learners, not to previews, not to a staging path.
- **Same-origin deployment.** The inlined bridge pins to `window.location.origin`; module HTML and platform shell must share it.
- **Retry semantics:** wrong responses stay retryable, verified-correct responses lock. Mobile had to issue corrections across Stage 5 (8 modules) and Stage 6 (7 modules) to fix retry behaviour — inherit the corrected behaviour, not the original.
- **Ungated modules** are marked explicitly with `data-cq-ungated="true"`. If any OHC module is intentionally ungated, mark it; do not leave it inferred.

**Option indices:** use ordinary visible option indices `0,1,2,…`. Mobile hit a defect where nested letter/text elements submitted independent indices and had to be corrected. Flat indices only.

---

## 4. Question architecture

### 4.1 Density is a function of module type, not a constant

Registry size per module across the mobile stages:

| Stage | Modules | Registry records | Per module | Character |
|---|---:|---:|---:|---|
| 2 | 10 | 259 | ~26 | knowledge-dense foundational |
| 3 | 13 | 291 | ~22 | knowledge-dense foundational |
| 4 | 14 | 112 | 8 | applied |
| 5 | 8 | 43 | ~5 | leadership |
| 6 | 7 | 35 | 5 | lift director |
| 7 | 7 | 36 | ~5 | capstone |

Foundational stages carry 22–26 gate items per module; applied and capstone stages carry 5–8. **OHC-01 through OHC-11 are foundational in character; OHC-12 is a capstone.** Size accordingly.

### 4.2 The OHC element arithmetic lands cleanly

The ACS carries **400 elements: 184 K · 108 R · 108 S** (OHC-01 includes net-new `A.K7` and `B.K7`).

- **K and R elements are gateable by knowledge check.** 184 + 108 = **292 items** on the US table, ≈24 per module — squarely in the mobile foundational band. OHC-01's extra K pair and Canada Task D increase that module's gate.
- **S elements are not.** 108 skills elements are graded performance and cannot be assessed by multiple choice. They need their own instrument.

**Proposed per-module gate:** 24 gate questions for OHC-01…OHC-11, tracing 1:1 to that module's K and R elements. **OHC-12 capstone: 5–6 gate questions** in the mobile capstone pattern, since its assessment weight sits in the practical.

Two arithmetic notes:
- **OHC-01 carries 19 K + 9 R = 28** on the US table (net-new `A.K7` / `B.K7`), not 24 — plus Canada Task D on that module. Record the extras in the manifest rather than dropping elements.
- Eleven modules at 15 K + 9 R = 24 ACS elements exactly. Second items (`*b`) hold independently testable facts on the same element; they do not change the census.

**Track total: ~290 gate records.** Comparable to mobile Stage 3 (291) — a known-good registry size.

### 4.3 Practice-versus-gate split

The crane-technician module CM-101 uses **6 practice questions followed by 6 gate questions**, with `review_offset` set so the first gate item renders as "Final Question 1". Carry that pattern: practice items are unscored and reveal nothing; gate items are server-scored and count toward the 100%.

For a 24-item OHC module, a 12 practice / 12 gate split keeps the gate meaningful without doubling authoring load. **Every gate item traces to a K or R element code; practice items may span several.**

### 4.4 Item form

- Multiple choice and true/false only — the two forms the existing 50-item overhead exam already uses (38 MC / 12 TF) and the two the bridge scores.
- **The correct option is never revealed on a miss.** CM-101's gate does this and it is what makes retry meaningful rather than a process of elimination.
- One element per gate item. An item testing two elements cannot be traced, and an untraceable item cannot be defended.

### 4.5 The S elements need a fourth deliverable

108 skills elements have **no home in HTML, PPTX or DOCX facilitator guides**. Mobile handles the equivalent through field evaluation outside the module package — which is why its capstone stages carry only ~5 gate questions each.

Add a **Performance Evaluation Sheet (`_PES.docx`)** per module: each S element as a line item with evaluator sign-off, date, and equipment/mode scope. This is also what feeds the Designation Gate documentation in OHC-12 Task B, and it is the artifact §1910.179(b)(8) implicitly requires an employer to hold.

---

## 5. Verification gates

Mobile's QA is stated as pass/fail counts, not prose. Adopt the same discipline — a stage is not accepted until every line reads N/N.

**Registry integrity**
- Unique question IDs: `N/N` match between registry and modules
- FNV records: `N/N` match
- Mobile precedent: Stage 3 at 291/291, Stage 7 at 36/36 on both

**Behavioural verification** — the four checks, per module:
1. Wrong answer retries
2. Correct answer locks
3. Completion **blocked** pre-mastery
4. Completion navigation **granted** post-mastery

**Package**
- `N/N` modules call the scoring and completion APIs
- `N/N` self-contained, no external references
- `N/N` modules below 15 MB
- Narration arrays, embedded MP3s and images counted and matched to manifest
- SHA-256 hashes recorded in the platform manifest and matching actual module sizes

**Responsive** — every quiz screen hit-tested on desktop and phone. Mobile ran Chrome desktop plus phone hit-testing across all 7 Stage 7 quiz screens.

---

## 6. Narration

- Embedded MP3, `data:audio`, **32 kbps mono**.
- Speech-synthesis fallback present in every module.
- Narration scripts and audio are **versioned together**. Mobile lost a module's audio to exactly this failure: an archived build held 60 embedded clips, but the scripts had been rewritten (4,718 archived words versus 13,283 current), so the clips could not be restored without pairing stale narration to current content. **Never restore audio across a script revision.**
- One mobile module shipped with neither embedded audio nor a TTS fallback and no recoverable export existed anywhere. **Track narration state in the manifest from the first build**, not at package time.

---

## 7. What OHC does *not* inherit

- **No instructional content, question text, answers, distractors or narration.** Mobile-crane content is equipment-specific and does not transfer — load charts by radius, outrigger and ground-bearing, assembly/disassembly, and boom geometry have no analogue on fixed-path equipment. `OHC.01.A.R2` exists precisely to break that transfer.
- **No stage structure.** Mobile is 7 stages × N modules with per-stage gate codes. OHC is a single 12-module track with one gate code.
- **Gate code:** OHC needs its own, assigned alongside the module codes that §5 of the ACS still lists as provisional pending Gate Master assignment.

---

## 8. Open decisions

1. **Gate code and module codes** — OHC-01…12 remain provisional. Needs Gate Master assignment.
2. **80% versus 100%** — a validated 50-item overhead exam already passes at 80%, and people may already be credentialed under it. Moving to 100% is a program decision with consequences for existing holders, not a formatting change.
3. **Supersede, absorb, or parallel** — a six-module overhead curriculum with a working assessment already ships. Decide before authoring.
4. **Deliverable count** — this document proposes 4 files/module (48 at completion) against the spec's 2 (24). Confirm.
5. **OHC-01's 26 items** versus 24 elsewhere — confirm the exception rather than trimming elements.

---

*Structure derived from `Crane Qualified Build Files/Developer Handoff - July` — `README_DEVELOPER_HANDOFF.md`, `STAGE7_HANDOFF.md`, `MODULE_MANIFEST.csv`, and the stage folder layout. Content deliberately not carried over.*
