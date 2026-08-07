---
title: OHC — Tier 0 Knowledge Harvest
type: knowledge-harvest
domain: owned-ip
tags: [tier-0, ohc, overhead-crane, acs, trace-table, knowledge-check, exam, reuse, conflicts]
sources_read: ["General Iron-Overhead Crane Training.pptx (118 slides / 101 notes)", "answer_key.docx — Overhead Crane Operator Safety Training Written Examination (50 items)"]
harvested: 2026-08-07
authority: ours-quote-freely
---

# ⭐ OHC — Tier 0 Knowledge Harvest

What the owned overhead-crane material actually teaches, mapped to ACS element codes — plus the places where it **contradicts the new spec**. ⬅ [[OHC — Tier 0 Deck Map]] · [[OHC — 1910.179 Citation Pack (verified)]]

> [!note] What was read
> **Read in full:** `General Iron-Overhead Crane Training.pptx` (118 slides, 101 instructor-note slides) and `answer_key.docx` (50-item written examination with rationale). **Inventoried only:** the remaining ~10 overhead-crane decks — see [[OHC — Tier 0 Deck Map]].

---

## 🚨 The headline — a predecessor curriculum already exists

The answer key is not a loose quiz. It is a **complete, validated written examination** for a **six-module overhead crane operator safety curriculum**, with every item sourced to a specific section and slide.

| | |
| --- | --- |
| Total questions | **50** (38 multiple choice · 12 true/false) |
| Passing score | **40 / 50 — 80%** |
| Structure | 7 parts mapping to Sections 1–6 of the curriculum |
| Retake rule | below 40/50 → retake training before a second attempt |

Its companion deck is `Overhead_Crane_Train_the_Trainer_condensed.pptx` in `Documents/Overhead Crane/outputs/` — *"Train-the-Trainer instructor deck for delivering the six-module overhead crane operator safety curriculum, OSHA 1910.179 / ASME B30 / …"*.

> [!warning] The 12-module ACS is a rebuild of something that already ships
> This changes the framing of the whole build. OHC-01…12 is not greenfield — it is a **re-architecture of a working six-module course with a validated 50-item assessment.** Before authoring, decide explicitly whether the new track supersedes, absorbs, or runs alongside it. Silently shipping a second, differently-scoped overhead crane course is the worst of the three outcomes.
>
> Note also the sibling file `Overhead_Crane_Train_the_Trainer_before_kc_delete_20260705_142114.pptx` — the filename says a knowledge-check bank was deleted from that deck on 2026-07-05. **That deck likely holds in-deck KC items the condensed version no longer has.** Worth opening before rebuilding KC from scratch.

---

## ⚠️ Four conflicts to resolve before OHC authoring

### 1. Plugging — shipped material endorses what the ACS treats as a hazard

> `General Iron` **Slide 93**: *"Never allow the crane to coast to a stop, use plugging (control reversal) or the braking system to stop (loaded or unloaded)."*

The ACS runs the other way: `OHC.03.A.K5` frames *"plugging and its consequences vs. controlled deceleration"*, and `OHC.07.B.K2` lists plugging among the **causes of load swing**.

Both positions are defensible — plugging beats coasting, and plugging induces swing — but they cannot both be taught without reconciliation. **Decide the house position and state it once.** Currently a student could take both courses and receive opposite instruction.

### 2. Hook rejection criteria — two different numbers, both in the corpus

| Source | Criteria |
| --- | --- |
| `General Iron` Slide 65 + exam **Q19** | deformation **0%** · throat distortion **≥5% or ¼ in** · wear **≥10%** · missing/non-functioning latch |
| **§1910.179(j)(2)(iii)** | cracks · **>15%** throat opening · **>10° twist** |

The decks teach the ASME figures; the regulation states looser ones. Per the DOE Hanford resolution (*Inconsistent Standards*): **follow ASME on criteria, follow OSHA on records.** The ACS should teach both figures and the rule for choosing — see [[OHC — 1910.179 Citation Pack (verified)]].

### 3. The 80% pass mark is already in production

The examination passes at **80%**. The established PPTX build standard also specifies *"8-question Final KC (80% pass)."* The OHC ACS §1 mandates a **server-authoritative 100% mastery gate**.

Three gate models, one program. Raising a live assessment from 80% to 100% is a real decision with real consequences for pass rates and for anyone already credentialed under the 80% instrument — not a formatting detail.

### 4. Verbatim ASME reproduction in shipped material

`General Iron` reproduces ASME B30.2 text word-for-word in several places — **2-3.1.4** (floor-operated operator qualification), **2-3.1.6** (remote control), **2-3.1.1** (cab/pulpit operators, in instructor notes), and the full **planned engineered lift** sequence (e)(1)–(8) in Slide 80's notes.

The Tier 2a rule is *"state requirements in our own words with attribution — never reproduce their tables, figures or wording."* Gate Master Rev 1.3 amendment **A1** permits paraphrase with attribution; it does not permit reproduction. **This is an existing exposure in shipped client-facing material**, not a new-build question — worth a remediation pass independent of the OHC track.

---

## 📋 Exam item bank → ACS element map

All 50 items trace cleanly to the new ACS. This is a ready-made seed for the element-to-item trace table the spec requires.

| Part | Items | Maps to |
| --- | --- | --- |
| 1 — Regulations & Operator Requirements | Q1–Q7 | **OHC-01** Tasks B, C |
| 2 — Crane Types & Components | Q8–Q15 | **OHC-01** A · **OHC-02** A, B, C |
| 3 — Inspections & Rejection Criteria | Q16–Q22 | **OHC-05** A, C |
| 4 — Procedures & Documentation | Q23–Q28 | **OHC-05** C · **OHC-12** B |
| 5 — Safe Operating Procedures | Q29–Q36 | **OHC-04** B · **OHC-07** A · **OHC-08** A · **OHC-09** A · **OHC-10** B |
| 6 — Rigging Fundamentals | Q37–Q44 | **OHC-06** A, B |
| 7 — Sling Angle Stress & Calculations | Q45–Q50 | **OHC-06** A, C |

**Coverage gaps against the 12-module ACS** — no items exist for: **OHC-03** (control modes: pendant / wireless / cab), **OHC-11** (malfunctions and emergency response), **OHC-12 Task C** (gate architecture and certification routing). Those three need net-new items; everything else can be adapted.

---

## 🎯 Hard values worth banking

Teachable numbers extracted from the two sources. Each needs a citation before it reaches a slide — the deck is Tier 0 and quotable, but a *number* still needs its standard named.

**Capacity, marking, duty**
- Rated-capacity data plate fields (Q13, per ASME B30.2): manufacturer · model · serial · rated capacity · **span** · voltage · **CMAA service class**. Any field illegible → crane out of service. → `OHC.04.A.K1`, `OHC.04.A.R3`
- **CMAA Class A = standby · Class F = continuous severe service** (mills, hot metal) (Q9) → `OHC.02.B.K5`
- **Span and capacity are inversely related** for a given girder design (Q14) → `OHC.01.A.K3`
- Reeving: 4-part = **4:1 mechanical advantage**, hook speed **¼** of drum line speed (Q12) → `OHC.02.B.K1`

**Inspection and rejection**
- Three inspection classes (Slide 52): **Initial · Frequent (daily–monthly) · Periodic (1–12 months)** → matches §1910.179(j)(1)(ii)
- Three inspector roles per ASME B30.2 (Q16): **operator** (frequent) · **designated person** (monthly/periodic) · **certified inspector** (annual) → `OHC.05.B.K1`
- Wire rope, ASME B30.2 (Slide 59, Q17): **4 broken wires in one strand** or **12 in all strands** per rope lay · **hot-metal cranes 3 / 6** · **2+ broken wires in an end socket** · flat spots where outer wires are **<⅔ normal thickness** · valley breaks / fishhooks → `OHC.05.C.K2`
- Alloy chain (Q18, Q22): remove at **10% wear** on any link or **3% stretch**; **Grade 30 proof-coil is never acceptable for overhead lifting** — Grade 80 or 100 only → `OHC.02.B.K3`, `OHC.06.A.R1`
- **Wheel tread flat spot: ⅛ inch** removes from service; often detected by thumping during bridge travel (Q20) → `OHC.02.A.K5`, `OHC.11.B.K4`
- **Holding-brake drift test** (Q21): lift a few inches, controller to neutral, verify **no downward drift**; any detectable drift is immediate out-of-service → `OHC.02.B.S2`, `OHC.05.A.K2`

**Construction and clearance**
- Clearance **3 in overhead / 2 in laterally** (Slide 31) → §1910.179(b)(6)(i)
- Service platforms (Slide 33): **48 in overhead clearance · 18 in clear passageway · 42 in guardrails**; instructor note carries the **two-wrap minimum** → `OHC.02.A.K4`
- Bumpers (Slide 34): stop the **bridge at ≥40%** and the **trolley at ≥50%** of rated load speed → `OHC.02.A.K3`
- Rail sweeps (Slide 35): extend below the rail head top by **≥50% of rail head thickness**, both sides
- **Cab fire extinguisher: minimum 10 BC rating** (Slide 30) → `OHC.03.C.K5`
- Holding brake engages **automatically when power is removed**; control brake decelerates moving loads (Q11) → `OHC.02.B.K2`, `OHC.11.A.K1`
- Festoon encloses conductors; conductor bar has exposed live rails — **both require LOTO** (Q15) → `OHC.02.C.K1`, `OHC.10.C.K1`

**Operating**
- **"Lift · Hold · Check"** — the named core handling sequence, every load without exception (Q32) → `OHC.07.A.S2`, `OHC.06.C.S1`. *A ready-made mnemonic already in the house voice.*
- **Critical lift at >75% of rated capacity** (Slide 97, Q31); other triggers: two cranes on one load · load left elevated for an extended period · costly or critical item · exceeding rated capacity → `OHC.04.B.K5`, `OHC.04.C.R3`
- **Outdoor operations cease at 20–25 mph sustained wind**, or per OEM (Q33) → `OHC.10.B.K1`, `OHC.10.B.S1`
- Unfamiliar crane (Slide 80): locate the **emergency power panel** · become familiar with all control functions and safety devices · **operate hoisting and travel functions before lifting a load** → `OHC.01.A.R3`, `OHC.05.B.S1`
- Diagonal movement is best achieved by **simultaneously moving bridge and trolley** (Slide 91) → `OHC.07.B.K1`
- **Rough travel** may indicate a broken wheel, track flat spot, misalignment, or debris on the rail (Slide 91) → `OHC.11.B.K4`
- Four-step qualification (Slide 45): **core classroom → site-specific → practical instruction and practice time → pass a practical evaluation** → `OHC.12.C.S3`. *This is the Designation Gate already expressed in the house's own words.*

**Rigging**
- Design factors (Q38): wire rope **5:1** · alloy chain **4:1** · personnel platforms **7:1+**
- Hitch factors (Q42, Slide 110): vertical **100%** · choker **75%** · basket **200%**
- **The Two-Leg Rule** (Q43): 3- and 4-leg bridles rate for **only two legs carrying**, because equal distribution cannot be guaranteed → `OHC.06.A.K2`, `OHC.06.C.K3`
- **D/d ratio** (Q44, Slide 111): **25:1 preserves full strength**; **10:1 → ~75%**
- Shackles (Q39, Slide 102): in-line **100%** · 45° **70%** · 90° **50%**
- Non-shouldered eyebolts: **vertical loads only**, angles beyond 5° prohibited (Q40)
- **"Never saddle a dead horse"** (Q41): U-bolt saddle on the **live** side
- **Master formula (Q49): WLL × Hitch Factor ÷ Angle Multiplier** — divide, because the multiplier is a stress increase, not a capacity gain
- Sling angle (Q45, Q46, Slide 113): minimum **30°**, multiplier **2.00** · 45° **1.414** · 60° **1.155** · 90° **1.00**. Full stress table 90°→5° on Slide 113
- **D/L field check (Q48): drop = half sling length → 30°**
- At **30° the horizontal squeeze equals the vertical lift** (Q50) → `OHC.06.A.K3`

**Below-the-hook magnets** (Slides 115–117) — Type 1 close-proximity (battery-powered · electrically controlled · manually controlled) · Type 2 remote-operated. ID tags carry manufacturer · model · **magnet weight and duty cycle** · supply voltage · load rating. → `OHC.06.B.K1`, `OHC.06.B.K2`, `OHC.06.B.K3`

---

## 🔴 Two defects in the existing exam

**Q2 rationale is jurisdictionally stale.** It says *"1926.550 is for construction (and is largely superseded by newer construction standards)."* §1926.550 was replaced by **Subpart CC in 2010**, and for overhead cranes the operative construction cite is **§1926.1438** — which routes back to §1910.179 or to the hybrid regime depending on installation status. The new ACS is built on exactly that distinction. **Fix the rationale before reusing the item.**

**Q5 teaches NAVFAC P-307 from a document nobody has opened.** The item asserts P-307's scope, yet the register has flagged P-307 as blocked-to-automation and **unopened** since 30 July. The item's answer is correct, but the program is currently teaching from a source it cannot produce. That is precisely the failure mode CM-101's discipline exists to prevent — *"the module cites no document the team has not read."* Either pull P-307 by hand or drop the item.

---

## ➡️ What to do with this

1. **Decide the relationship** between the existing six-module course and the new 12-module ACS before authoring anything.
2. **Open `..._before_kc_delete_...pptx`** — it likely holds the in-deck KC bank that was stripped on 2026-07-05.
3. **Adapt the 50 items** into the ACS trace table; author net-new items for OHC-03, OHC-11 and OHC-12 Task C, which have no coverage.
4. **Resolve the four conflicts** above — plugging, hook criteria, pass mark, ASME reproduction.
5. **Fix Q2 and Q5** before either is reused.

---

## 🔗 Where this connects

- [[OHC — 1910.179 Citation Pack (verified)]] — the regulatory layer
- [[OHC — Tier 0 Deck Map]] — the full owned-source inventory and the six OLE2-blocked decks
- [[_Deck Text — Index]] · [[_Crane Standards — Index]]
