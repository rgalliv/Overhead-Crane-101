---
title: OHC — Rigging Knowledge Harvest (verified)
type: source-harvest
status: verified
track: Overhead Crane Operator (OCO301C)
modules: [OHC-05, OHC-06]
tiers: [Tier 0, Tier 1]
created: 2026-08-08
tags: [rigging, asme-b30, slings, below-the-hook, hooks, overhead-crane, harvest]
---

# OHC — Rigging Knowledge Harvest

Sweep of the Second Brain for **rigging** knowledge feeding `OHC-05 Inspection Regime` and
`OHC-06 Rigging Interface and Below-the-Hook Devices`.

The organising premise, and it is correct: **rigging is rigging.** It is governed by the
ASME B30 volumes and by practice, and it does not change because the hook above it belongs
to an overhead crane rather than a mobile or tower crane. That makes the whole Tier 0
rigger corpus directly available to the overhead track — 527 SharePoint hits, not the
handful the original cross-check assumed.

Related: [[OHC — 1910.179 Citation Pack (verified)]] · [[OHC — EM 385 Section 16 Overhead and Gantry (verified)]] · [[OHC — Tier 0 Knowledge Harvest]] · [[OHC — OSHA Part 1910 Map]]

---

## 1. What the sweep found

### Tier 0 — own IP, quote freely

| Source | What it carries |
|---|---|
| `FG_S2-M1_Rigging_Fundamentals` (Stage 2, Rigger I/II) | Sling types, tags, hitch derates by sling type, hardware, EM 385 §15 rigging relocation |
| `WD-SCN-002 / FG_S4-M10_Rigging_Fundamentals` (Stage 3 LMS) | Deepest technical coverage: leg-tension formula, angle factors, multi-leg bridle rule, master-link sizing, shackle side-load, CG and trial lift, tag lines, 7-step pre-lift sequence |
| `ETS-Rigger-2024-Level-I` · `1. Advanced Rigger` · Bull Rigging series · `AB Rigging Foundations` | Rigger I/II prep decks; B30 volume mapping |
| `Appendix_D_B30_Reference.docx` (Forgen EQ-OPS-001) | ASME B30 volume reference guide |
| `SEP_Chapter_12_Rigging_Inspection.docx` (Scout Energy) | Client rigging-inspection chapter |

### Tier 1 — US Government, public domain, quotable

> [!important] **DOE Hanford Hoisting and Rigging manual — `HoistingRigging_Fundamentals.pdf`, TR244C Rev 5**
> This is the highest-value find of the sweep. Public domain, currently maintained,
> directly on-topic, and it **resolves conflicts the Tier 0 guides leave open**. It is now
> the tiebreaker source of record for rigging in the OHC track.

### 🔴 Correction to the existing cross-check

**`ASME B30.2-2016.pdf` IS in the corpus** — `Shared Documents/ANSI-ASME-NFPA70-E and OSHA
Standards/ANSI Standards/`. The cross-check lists "ASME B30.2 is not in the corpus" as
**blocking item #1**. That is wrong and should be struck.

Caveat that survives: 2016 is **neither** of the two legally operative editions — the
facility branch incorporates **ANSI B30.2.0-1967** at §1910.179(b)(2), and the construction
branch incorporates **ASME B30.2-2005** sections at §1926.1438(b)(2)(ii). The 2016 edition
is excellent context and useless as a citation for either branch. Also present:
`Rigger_Reference_Manual_0411.pdf` and `Riggers_Reference_Manual_0209.pdf` (NCCCO, Tier 2b —
reference, never quote).

---

## 2. Verified rigging facts now gated in OHC-06

Sourced to Hanford TR244C unless marked otherwise.

**Hooks**
- *"The designed SWL applies only when the load is applied in the saddle of the hook."*
- Off-centre derate table: **100% / 86% / 80% / 70%**, and roughly **40%** as a point load at the tip.
- Hooks are provided with a **latch to bridge the throat** and prevent release of load lines. Remote in-cell cranes are the noted exception.
- **Hook tips should point out and away from the load**, so that as slack comes up the hook does not tip-load itself.
- Design philosophy: *"the hook should be the weakest member of the lifting equipment, so it will bend if overloaded before any other piece of equipment fails."*

**Slings and hitches**
- Choker: when the angle of choke is drawn below **120°**, the table choker rating must be reduced again. In controlled destructive tests below 120°, **the sling body always failed at the point of choke**.
- Multi-leg: *"unless the load is flexible, it is wrong to assume that a 3- or 4-leg hitch will safely"* share proportionally. Working basis — **two legs carry, the others balance**. Hanford states the same rule as `SWL = (hitch) × HL × 2`.
- **Load Angle Factor** method: LAF = sling length ÷ vertical height; multiply LAF × the portion of weight at that pick point.
- **D/d ratio**: efficiency loss of about **50%** when the ratio falls to 1:1.
- Softeners or blocking at corners and sharp bends; arc of contact at least equal to the rope diameter.
- Design factor of safety **at least 5** for safe working loads.
- Slings shall not be shortened or lengthened by **knotting, twisting or wire rope clips** — legs are levelled with turnbuckles or lever hoists.

**Below-the-hook (ASME B30.20)**
- Marking is **three things, all required**: rated capacity, manufacturer/fabricator identification, and design for the load configuration in use.
- **Inspection Tag** — permanent, on slings, hooks and below-the-hook devices: safe working load, inspection date, serial number.
- Spreader beams get a **frequent (pre-use) inspection at the beginning of each shift**: structural deformation, cracks, excessive wear, loose or missing fasteners. Recommended for loads over 12 ft.

**Load control**
- **§1910.179(n)(3)(i)** — *the load shall be well secured and properly balanced in the sling or lifting device before it is lifted more than a few inches.* Paragraph (n) **is** in the §1926.1438(b)(2) list, so this binds on **both branches**.
- At the pause: **no downward drift** of the load. Shock loading *"can very easily cause the load to double the load tension on the crane, hoist, and rigging equipment."*
- *"Do not carry loads over people. All personnel including the rigger shall stay clear of the load. Use a tag line to help control the load. Never raise the load higher than necessary."*
- Outdoor equipment: wind speeds **over 25 mph** should be evaluated by a qualified person.
- Bridle stability requires all three: load distributed equally among legs, **hook directly over the CG**, load raised level.

---

## 3. ⚠️ Conflicts between two shipped Tier 0 guides

`FG_S2-M1` and `WD-SCN-002` are both live training documents and they **contradict each
other on four testable facts**. None of the four is gated in OHC-06. They need an SME
ruling.

| Fact | `FG_S2-M1` | `WD-SCN-002` | Status |
|---|---|---|---|
| **Hook throat limit** | 5% or ¼" | 15% | ✅ **Resolved** — see below |
| **Choker derate** | 75% wire rope / 80% chain, synthetic, roundsling / 100% metal mesh | flat "75–80%" range | 🔴 Open — S2-M1 is the more precise reading |
| **Chain elongation** | >5% | 3% | 🔴 Open |
| **Roundsling colour capacities** | purple 2,100 · green 4,200 · yellow 6,300 · tan 8,400 · red 10,600 · white 13,200 · blue 16,800 · orange 21,200 | purple 2,100 · green 5,300 · yellow 8,400 · orange 13,200 · red 21,200 · white 37,000 · blue 66,000 | 🔴 Open — **and both may be wrong to teach as standard** |

> [!warning] Roundsling colour code is not an ASME standard
> ASME B30.9 does not standardise colour-to-capacity. It is a **manufacturer convention**.
> Two guides can each be internally consistent and still disagree, because they are
> describing different manufacturers' ranges. Teaching either table as *the* standard is a
> defect in both. The defensible rule is the one both guides already state elsewhere:
> **read the tag.**

### ✅ The hook conflict is resolved

- **OSHA §1910.179(j)(2)(iii)** — cracks, **more than 15%** in excess of normal throat opening, **more than 10°** twist from the plane of the unbent hook.
- **ASME B30.10** — **5%, not to exceed ¼ in**, plus any visible bend or twist. Stricter.
- **Hanford TR244C Ch. 5**, under a heading called *Inconsistent Standards*: **follow ASME on the criteria, follow OSHA on the records.** ASME sets the tighter number; OSHA is what requires the *monthly documented* hook inspection.

Hanford's own inspection text independently states 15% throat / 10° twist / 10% saddle wear —
i.e. it teaches the OSHA figures in the body and the choosing rule in Ch. 5. Both figures
and the rule are gated in **OHC-05 `A.K4` and `A.K4b`**.

---

## 4. 🐛 Defect found in a shipped Tier 0 guide

`WD-SCN-002` / `FG_S4-M10` — **the leg-tension answer key is wrong by a factor of two in two
places.**

| Item | Keyed answer | Correct |
|---|---|---|
| Section 2 KC **Q5** — 30,000 lb, 2-leg, 45° | 10,606 lb | **21,213 lb** |
| Final KC **Q2** — 40,000 lb, 2-leg, 45° | 14,142 lb | **28,284 lb** |

Both key entries contain an unresolved **"Wait —"** editorial note left in the shipped text,
where the author caught the discrepancy and did not finish resolving it.

The method is correct everywhere else: the Slide 15 worked example (24,000 lb ÷ 1.414 =
16,969 lb) and both debrief calculations are right. It is **the keys that are wrong, not the
formula**. Learners scoring against this key are being marked wrong for the correct answer,
and right for an answer that would under-specify sling capacity by half.

**Action: fix at source.** OHC-06 `A.K3` is keyed to the correct value.

---

## 5. EM 385 rigging moved sections

`FG_S2-M1` records that the **2024 edition relocated rigging from §16 to §15** (§15.H),
and that material still citing §16 for *rigging* is superseded. `WD-SCN-002` still cites
"EM 385-1-1 Section 16.F" and is therefore on the old numbering.

> [!note] This does not affect OHC-01 … OHC-05
> Those modules cite **§16 for overhead and gantry crane requirements**, which is where
> §16 still lives. Only the *rigging* content moved to §15. The verified §16 crosswalk in
> [[OHC — EM 385 Section 16 Overhead and Gantry (verified)]] stands unchanged.

---

## 6. Open items

1. **SME ruling** on choker derate, chain elongation, and whether roundsling colour is taught at all.
2. **Fix `WD-SCN-002`'s two answer keys** and strike the "Wait —" text.
3. **Strike blocking item #1** from the cross-check — B30.2 is held (2016 edition).
4. **§1926.1412 / §1926.1413** paragraph text still not held. This is the construction-branch inspection and wire-rope authority for OHC-05 and OHC-06 (cross-check finding **F4**). `OHC.05.B.R3` now names both sections so the branch is no longer silently dropped, but nothing below section level is gated.
5. **§1910.184** (slings) still not held as primary text — the general-industry sling standard, and the facility-branch companion to everything in OHC-06 Task A.
