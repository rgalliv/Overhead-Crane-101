---
title: OHC — Load Handling Source Pack (verified)
type: source-harvest
status: verified
track: Overhead Crane Operator (OCO301C)
modules: [OHC-07, OHC-08]
tiers: [Tier 0, Tier 1]
created: 2026-08-08
tags: [load-handling, 1910-179-n, load-swing, clearance, overhead-crane, harvest]
---

# OHC — Load Handling Source Pack

Everything verified and ready for `OHC-07 Load Handling and Movement Control`, staged ahead
of the module build. **§1910.179(n) is transcribed complete below** — it is the densest
operator-conduct paragraph in the whole standard and it is where most of OHC-07 lives.

> [!important] Paragraph (n) applies on **both** branches
> **(n)** is in the §1926.1438(b)(2) incorporation list. Unlike (j), (l) and (m) — which are
> facility-branch only — everything on this page binds whether the crane is permanently
> installed or not. OHC-07 is the one module that does not need a branch caveat.

Related: [[OHC — 1910.179 Citation Pack (verified)]] · [[OHC — EM 385 Section 16 Overhead and Gantry (verified)]] · [[OHC — Rigging Knowledge Harvest (verified)]] · [[OHC — Tier 0 Knowledge Harvest]]

---

## 1. §1910.179(n) — complete transcription

### (n)(1) Size of load
> The crane shall not be loaded beyond its rated load except for test purposes as provided in paragraph (k) of this section.

### (n)(2) Attaching the load
| ¶ | Text |
|---|---|
| **(n)(2)(i)** | The hoist chain or hoist rope shall be **free from kinks or twists** and shall **not be wrapped around the load**. |
| **(n)(2)(ii)** | The load shall be attached to the load block hook **by means of slings or other approved devices**. |
| **(n)(2)(iii)** | Care shall be taken to make certain that **the sling clears all obstacles**. |

### (n)(3) Moving the load

| ¶ | Text |
|---|---|
| **(n)(3)(i)** | The load shall be **well secured and properly balanced** in the sling or lifting device **before it is lifted more than a few inches**. |
| **(n)(3)(ii)** | Before starting to hoist, the following conditions shall be noted: **(a)** hoist rope shall not be kinked; **(b)** multiple part lines shall not be twisted around each other; **(c)** the hook shall be brought over the load **in such a manner as to prevent swinging**. |
| **(n)(3)(iii)** | During hoisting care shall be taken that: **(a)** there is **no sudden acceleration or deceleration** of the moving load; **(b)** the load **does not contact any obstructions**. |
| **(n)(3)(iv)** | Cranes shall not be used for **side pulls except when specifically authorized by a responsible person** who has determined that the stability of the crane is not thereby endangered and that various parts of the crane will not be overstressed. |
| **(n)(3)(v)** | While any employee is **on the load or hook**, there shall be **no hoisting, lowering, or traveling**. |
| **(n)(3)(vi)** | The employer shall require that the operator **avoid carrying loads over people**. |
| **(n)(3)(vii)** | The operator shall **test the brakes each time a load approaching the rated load is handled**. The brakes shall be tested by **raising the load a few inches and applying the brakes**. |
| **(n)(3)(viii)** | The load shall **not be lowered below the point where less than two full wraps of rope remain on the hoisting drum**. |
| **(n)(3)(ix)** | When **two or more cranes** are used to lift a load, **one qualified responsible person shall be in charge** of the operation. He shall analyze the operation and instruct all personnel involved in the **proper positioning, rigging of the load, and the movements to be made**. |
| **(n)(3)(x)** | The employer shall insure that the operator **does not leave his position at the controls while the load is suspended**. |
| **(n)(3)(xi)** | When **starting the bridge** and when the **load or hook approaches near or over personnel**, the **warning signal shall be sounded**. |

### (n)(4) Hoist limit switch
| ¶ | Text |
|---|---|
| **(n)(4)(i)** | At the beginning of each operator's shift, the upper limit switch of each hoist shall be **tried out under no load**. Extreme care shall be exercised; the block shall be **"inched" into the limit or run in at slow speed**. If the switch does not operate properly, **the appointed person shall be immediately notified**. |
| **(n)(4)(ii)** | The hoist limit switch which controls the upper limit of travel of the load block shall **never be used as an operating control**. |

---

## 2. 🔴 Two corrections the ACS needs in OHC-07

### `OHC.07.A.K3` — side pulls are **not** flatly prohibited

The ACS states a flat prohibition. **(n)(3)(iv) is conditional**: side pulls are permitted
*when specifically authorized by a responsible person* who has determined both that crane
stability is not endangered and that parts will not be overstressed.

Teaching it as absolute is wrong, and it will be contradicted by any experienced operator in
the room — which costs the instructor the rest of the session. Teach the **two-part test and
who applies it**, not a ban.

### `OHC.07.A` is missing **two full wraps** entirely

**(n)(3)(viii)** — *the load shall not be lowered below the point where less than two full
wraps of rope remain on the hoisting drum* — does not appear anywhere in the ACS. It is a
hard, numeric, operator-owned limit on the lowering side, and the lower limit switch is not
always present to enforce it. **This needs a new K element in OHC-07 Task A.**

---

## 3. Elements already confirmed against source

| Element | ACS content | Verified source |
|---|---|---|
| `OHC.07.A.K2` | Functional/brake checks | **(n)(3)(vii)** — brake test at loads approaching rated, by raising a few inches |
| `OHC.07.A.K3` | Side pulls | **(n)(3)(iv)** — ⚠️ conditional, see above |
| `OHC.07.A.K5` | Limit switch not an operating control | **(n)(4)(ii)** verbatim; **(k)(1)(ii)** gives the *why* (trip setting is a test with an empty hook) |
| `OHC.07.A.R3` | Using the limit switch as a control | **(n)(4)(ii)** |
| `OHC.07.A.S2` | "Lift · Hold · Check" | Tier 0 `Overhead Crane Training Rev 2` Q32 — house-voice mnemonic already in use |
| `OHC.07.B.K1` | Diagonal movement | Tier 0 Slide 91 — best achieved by **simultaneously moving bridge and trolley** |
| `OHC.07.B.K2` | Causes of load swing, incl. plugging | Tier 0; cross-ref `OHC.03.A.K5` |
| `OHC.07.B.K4` | Clearances | **§1910.179(b)(6)(i)** — min **3 in overhead, 2 in lateral**, per **CMAA Spec No. 61** (incorporated via §1910.6); **(b)(6)(ii)** walkway obstruction; **(b)(7)** parallel cranes. Also **EM 385 16-8.aa(5)** |

---

## 4. Supporting material in hand

**DOE Hanford TR244C (public domain, quotable)**
- Shock loading *"can very easily cause the load to double the load tension on the crane, hoist, and rigging equipment."*
- At the test-lift pause: **no downward drift** of the load.
- *"Do not carry loads over people. All personnel including the rigger shall stay clear of the load. Use a tag line to help control the load. Never raise the load higher than necessary."*
- Before starting to lift: **load path clear of obstructions**; hoist rope or chain not kinked; multiple-part lines not twisted; if the load line is slack, ensure the line **seats on the drum and in the sheaves**.
- Outdoor equipment: wind speeds over **25 mph** evaluated by a qualified person.

**EM 385-1-1 (15 Mar 2024) §16** — verified 1:1 crosswalk to the old `16-8.aa(n)` numbering
lives in [[OHC — EM 385 Section 16 Overhead and Gantry (verified)]]. `16-8.aa(5)` is the
clearance provision feeding `OHC.07.B.K4` and `OHC.08.B.K1`.

**Tier 0** — `Overhead Crane Training Rev 2` (Section 5, Q29–Q36 safe operating procedures)
and [[IPT Section 11 — Overhead Cranes]].

---

## 5. ✅ Was blocked on the ACS

**Closed 2026-08-08.** The ACS was supplied and is committed at `docs/OHC-ACS-build-spec.md`. OHC-07 is built.




