# Vestas Combined Curriculum Map — Rigging + Overhead Crane

**Client:** Vestas · **Course codes:** Stage 2 (rigging and communication) + OCO301C / gate OHC-1 (overhead crane)
**Scope:** factory / workshop bridge cranes · port / staging / logistics cranes
**Repos:** `MSC-Safety-Solutions/Stage-2-core` (22 modules) · `rgalliv/Overhead-Crane-101` (12 modules)

**34 modules total.** Both tracks are built, gated at 100% mastery, and behaviourally verified. This document defines how they join — it does not modify either track's internal content.

---

## Design principle

**Chain the tracks; do not interleave them.**

Both tracks carry verified internal handshake chains and 0-gap audits. Interleaving at module granularity would rewrite ~30 `next` pointers across two repos and invalidate two independent verification runs to gain sequencing that prerequisite notes deliver for free.

The combined program is therefore **two intact tracks joined at one seam**, with prerequisite annotations doing the pedagogical work.

---

## Recommended sequence

```
STAGE 2 CORE          S2_M01 → … → S2_M12      rigging + communication foundation
STAGE 2 ADVANCED      S2_M13 → … → S2_M22      applied rigging, load share, BTH-1
      │
      └── JOIN ────────────────────────────────  S2_M22.next → OHC_M01
      │
OVERHEAD CRANE        OHC_M01 → … → OHC_M12     equipment → capstone / Designation Gate
                                        │
                                        └── (end)
```

**Rigging first, crane second, capstone last.**

Three reasons, in order of weight:

1. **OHC-12 must be terminal.** It is the Designation Gate capstone — integrated scenario performance plus the documentation package that evidences the employer's qualification determination. A program cannot issue its designation and then continue teaching.
2. **The Vestas amendment's new content depends on rigging.** `OHC-04 Task D` (engineered lift planning and the rigging plan) and `OHC-07 Task D` (tandem load share) both assume sling tension, hitch geometry, centre of gravity and below-the-hook device competence. Those live in Stage 2. Running crane-first would gate learners on content they have not been taught.
3. **One pointer changes.** `S2_M22 → OHC_M01`. Nothing else moves.

### Alternative, if Vestas needs crane-first

If the population is existing crane operators being upskilled in rigging rather than riggers being trained on cranes, invert to `OHC_M01 … OHC_M12 → S2_M01 … S2_M22`. The cost is real: the Designation Gate stops being terminal, and OHC-04/07 Task D content must either move or carry inline rigging primers. **This is a program decision, not a formatting one** — same class as the 80%-versus-100% question still open in `docs/OHC-build-format-spec.md` §8.

---

## Prerequisite map — where the tracks actually interlock

These are the dependencies that justify the ordering. Each Stage 2 module below is load-bearing for the OHC element beside it.

| Stage 2 module | Feeds | OHC element |
|---|---|---|
| **S2_M01** Rigging Fundamentals | → | `OHC.06.A` rigging interface; load path and rated capacity language |
| **S2_M02** Gear Inspection | → | `OHC.05` inspection regime — sling and hardware condition at the interface |
| **S2_M03** Hitch Configurations | → | `OHC.06.A`; hitch effect on total lifted load in `OHC.04.D.K3` |
| **S2_M04** Load Weight & CoG | → | **`OHC.04.D.K1–K4`** — the lift plan's weight and CoG inputs |
| **S2_M05** Dynamic Load Control | → | `OHC.07.A/B` — slack removal, swing, dynamic amplification |
| **S2_M06 / M11 / M12** Signals & directive communication | → | `OHC.09` signals; **`OHC.07.D.K4`** single-point control on tandem picks |
| **S2_M08** Hardware Selection & Rating | → | `OHC.06.A`; hardware ratings in the rigging plan |
| **S2_M09** Sling Geometry | → | **`OHC.04.D.K3`** — sling angle and tension per leg into total lifted load |
| **S2_M10** Spotter Authority & Stop-Work | → | `OHC.07.D.K4` — *either operator may stop* |
| **S2_M13** CoG Determination | → | **`OHC.07.D.K2`** — CoG position sets tandem load share |
| **S2_M14** Unequal Leg Loading | → | **`OHC.07.D.K2/K3`** — share shift and derating |
| **S2_M19** Multi-Point & Trolley Beam Load Share | → | **`OHC.07 Task D` — the direct prerequisite.** Trolley beam load share *is* the bridge-crane case |
| **S2_M21** Below-the-Hook Devices & BTH-1 | → | `OHC.06.B`; device weight in `OHC.04.D.K4` |
| **S2_M22** Sling Angles & Multi-Spreader | → | `OHC.04.D.K3`; multi-spreader assemblies on tandem picks |

**S2_M19 is the keystone.** The OHC track previously gated the *risk* of unengineered multiple-hoist picks (`OHC.04.C.R3`) without teaching load share anywhere. Stage 2 M19 already teaches it — multi-point and trolley beam load share — and `OHC-07 Task D` now carries it into crane execution. Joining the tracks is what closes that gap properly; the amendment alone would only half-close it.

---

## Lift planning and load sharing — where they live

The client requirement was that lift planning and load sharing sit inside the rigging plan. They now resolve across three places, with no duplication:

| Concern | Home | Status |
|---|---|---|
| Rigging plan mechanics — sling tension, angle, hitch, D/d, hardware rating | **Stage 2** M03, M09, M15, M22 | Built |
| Load share theory — multi-point, trolley beam, unequal legs | **Stage 2** M14, M19 | Built |
| Below-the-hook device weight and selection | **Stage 2** M21 · `OHC.06.B` | Built |
| **Written lift plan — contents, classification, currency; rigging plan as a component** | **`OHC-04 Task D`** | **Amendment — to build** |
| **Tandem execution — derating, single-point control, share verification** | **`OHC-07 Task D`** | **Amendment — to build** |
| Total lifted load assembled and checked against rated capacity | `OHC.04.D.K4`, `OHC.04.B.K4`, `OHC.04.A.K5` | Partly built |

The rigging plan is taught as a **component of the lift plan**, not a parallel document — `OHC.04.D.K3` states this explicitly, so learners do not leave with two artifacts where the facility expects one.

---

## Implementation — the join

**One edit, in `Stage-2-core`.** Stage 2 ordering is held in `course-shell.js`, not in per-module `next` pointers; the OHC track holds ordering in `manifests/OHC_Mnn.json`.

1. Extend the shell's module list to carry the OHC track after `S2_M22`, or set `S2_M22`'s completion handshake to hand off to `OHC_M01`.
2. Leave `OHC_M12.next` as `""` — the capstone stays terminal.
3. Leave every other pointer untouched.

**Progress rail:** the shell currently reads `0/22`. Combined delivery is **`/34`**. The `stage-progress` block in `index.html` and its counter in `course-shell.js` need the new denominator.

**Deployment:** both tracks are self-contained single-file HTML with no external references. They can serve from one origin without cross-repo asset resolution. Per `docs/OHC-build-format-spec.md` §3, the inlined bridge pins to `window.location.origin` — **the combined shell and both module sets must share an origin**, which is the one real deployment constraint here.

---

## Delivery totals

| | Stage 2 | OHC | Combined |
|---|---:|---:|---:|
| Modules | 22 | 12 | **34** |
| Gate items | — | 347 → **373** | — |
| ACS elements | — | 413 → **449** | — |
| PES lines (S elements) | — | 111 → **121** | — |
| Languages | EN + es-LA | EN (+ FR/ES forms) | **es-LA required across both for the Mexico branch** |

**Language gap.** Stage 2 already ships EN + Latin American construction Spanish across all 22 modules. The OHC track is English with EN/FR designation forms. For the Mexico branch the OHC modules need an es-LA pass to match — Stage 2's existing register is the reference, and it should not be re-translated to a European Spanish register. This is scoped but not built.

---

## Open decisions

1. **Sequence** — rigging-first (recommended) or crane-first. Program decision.
2. **Single shell or two** — one combined 34-module shell, or two shells with a handoff. Recommend one shell.
3. **es-LA pass on the OHC track** — required for Mexico delivery, not yet scoped for effort.
4. **Vestas internal lifting procedures** — not supplied. Where they exceed OSHA/NOM they govern, and `OHC-04 Task D` should cite them directly.
5. **Whether Vestas wants both tracks gated as one credential** or two — affects whether the Designation Gate at OHC-12 covers rigging scope as well.
