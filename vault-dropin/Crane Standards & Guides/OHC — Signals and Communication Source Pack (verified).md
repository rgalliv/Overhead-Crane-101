---
title: OHC — Signals and Communication Source Pack (verified)
type: source-harvest
status: verified
track: Overhead Crane Operator (OCO301C)
modules: [OHC-09]
tiers: [Tier 0, Tier 1]
created: 2026-08-08
tags: [signals, hand-signals, signal-person, radio, em-385, subpart-cc, overhead-crane]
---

# OHC — Signals and Communication Source Pack

Sourcing for `OHC-09 Communication and Signals`.

Related: [[OHC — EM 385 Section 16 Overhead and Gantry (verified)]] · [[OHC — 1910.179 Citation Pack (verified)]] · [[OHC — Load Handling Source Pack (verified)]] · [[OHC — Rigging Knowledge Harvest (verified)]]

---

## 1. ⭐ The branch profile is the inverse of OHC-05

This is the most consequential finding in the module.

| Branch | Authority | What it says about signals |
|---|---|---|
| **Facility** — permanently installed, §1926.1438(a) | **§1910.179 only**; Subpart CC does not apply | **Almost nothing.** A warning device at **(i)**, a warning signal at **(n)(3)(xi)**. No signal chart, no signal person qualification, no voice or radio protocol. |
| **Construction** — not permanently installed, §1926.1438(b) | Enumerated §1910.179 paragraphs **plus** the Subpart CC sections listed at (b)(2)(i) | **The entire Subpart CC signals regime.** |

The enumeration at **§1926.1438(b)(2)(i)** brings in **§§1926.1400–1414**, **§§1926.1417–1425**, **§1926.1426(d)**, **§§1926.1427–1434**, **§§1926.1437–1439**, and **§1926.1441**. Two of those ranges matter here:

- **§§1926.1417–1425** contains **1419** (signals, general), **1420** (radio, telephone or other electronic transmission), **1421** (voice signals), **1422** (hand signal chart).
- **§§1926.1427–1434** contains **1428** (signal person qualifications).

> [!important] In OHC-05 the facility branch was rich and construction was the gap. Here it is exactly reversed — the detailed signal rules live on the branch the ACS says least about.

Gated as `OHC.09.A.K5b`.

---

## 2. ⚠️ Section-level verified; paragraph text NOT held

The applicability above was read from the §1926.1438(b)(2)(i) enumeration and from the
section headings. **The paragraph-level text of §§1926.1419–1422 and §1926.1428 is not held
in usable form.**

- The corpus copy of Subpart CC is a heavily OCR-degraded scan — word order is scrambled and numerals are corrupted. Readable enough to reconstruct a section-number enumeration, **not** readable enough to quote a paragraph.
- **osha.gov and ecfr.gov are both blocked** by this environment's egress policy (403 at CONNECT). Verified against the proxy status endpoint, not assumed.

**Nothing below section level is gated from those sections.** This is now the largest
remaining sourcing hole in the track, and it is the same shape as the **§1926.1412/1413**
gap in OHC-05 (`B.R3`).

**To close it:** a clean copy of §§1926.1419, 1420, 1421, 1422 and 1428 — from a machine
readable PDF, or fetched in an environment whose egress policy allows osha.gov.

---

## 3. ⚠️ Edition caveat — these are 2014 numbers

Every §16.G.05 and §16.B.06 citation below was read **verbatim** from the standalone
Section 16 extract, which is the **2014** edition (page headers read `EM 385-1-1 XX Jul 14`)
and numbers Section 16 **by letter**.

The ACS references the **15 Mar 2024** edition. Its Section 16 paragraph numbers could not
be re-read — every reader available here caps around **page 92 of 757**, and Chapter 16 sits
well beyond that.

- For **16-8.aa(6)** the 1:1 crosswalk is already established, so the ACS number is used.
- For **§16.G.05** and **§16.B.06** the ACS cites nothing, so there is **no crosswalk anchor** and **the 2024 equivalents are unconfirmed**.

Items are marked *2014 text* in the OHC-09 trace table. **Confirm the 2024 numbers before
publication.**

---

## 4. Verified EM 385 text now gated in OHC-09

### §16.G.05 Communications

- **a.** A **standard signal system** shall be used on all LHE (by hand, voice, audible or comparable signals).
- **a(1)** Manual (hand) signals may be used when the distance between the operator and signal person is **not more than 100 ft (30.4 m)**. If using hand signals, **Standard Method must be used per Figure 16-1**.
- **a(2)** Radio, telephone, or a visual and audible electrically-operated system **shall** be used when the distance is **more than 100 ft**, **or when they cannot see each other**.
- **b.** A signal person **must** be used: **(1)** when the point of operation, load travel, or area near or at load placement **is not in full view of the operator**; **(2)** when the equipment is **traveling and the view in the direction of travel is obstructed**; **(3)** due to **site-specific safety concerns, either the operator or the person handling the load determines that it is necessary**.
- **c.** The ability to transmit signals **shall be maintained**. If interrupted **at any time**, the operator shall **safely stop operations requiring signals until it is re-established and a proper signal is given and understood**.
- **d.** **Only one person gives signals to a LHE operator at a time unless an emergency stop signal is given (which may be given by anyone and must be obeyed by the operator).**

> [!tip] §16.G.05.d carries both the single-signaler rule and its one exception in a single sentence. Gated as `A.K3` and `A.K3b`.

### §16.B.06 Signal Person Qualifications

- **a.** Qualified by a **third-party Qualified Evaluator** or the **employer's Qualified Evaluator / LHE trainer**.
- **b.** Documentation must **specify each type of signaling** (hand, radio, etc.) the person is qualified for.
- **c.** If subsequent actions indicate the individual does not meet the requirement, the employer **must not allow them to continue** until retraining and re-assessment.
- **d.** Qualification requires: **(1)** know and understand the signal types used, and the **Standard Method** if hand signals; **(2)** be **competent in the application**; **(3)** have a **basic understanding of crane operation and limitations, including crane dynamics involved in swinging and stopping loads** (and boom deflection — written for LHE generally); **(4)** demonstrate this through **written and practical test**.
- **e.** ⚠️ An employer's Qualified Evaluator assessment is **not portable**. **Other employers are not permitted to use it.**

### Also present

- **16.G.05** preamble: all personnel involved shall **understand the communication systems and their responsibilities**.
- Where a signal person is **not** used, the operator **shall ensure full view of the load and the load travel paths at all times the load is rigged**.
- **16.C.02** classifies **cab-operated** and **remote-operated (wireless) overhead, bridge, gantry, underhung and monorail cranes over 30T** as Class I — relevant to OHC-01 / OHC-12, not gated here.

---

## 5. DOE Hanford TR244C (public domain, quotable)

> The standard overhead crane and hoist hand signals **adopted by ANSI standards** are to be
> used. **If compliance with these hand signals is impractical for the job being performed,
> other hand signals shall be agreed on by the operator and signal person.** Radio
> communication may be substituted for hand signals when agreed on between the operator and
> signal person.

This is the cleanest available statement of a rule the ACS does not make explicit:
**non-standard signals are permitted; invented ones are not.** The distinguishing feature is
**advance agreement**. Gated as `A.K5`.

Hanford also carries the STOP-in-advance technique — signal the stop early enough that the
load does not travel past its landing spot.

---

## 6. Open items

1. **Close the §§1926.1419–1422 / §1926.1428 paragraph-text gap** (§2 above). Largest sourcing hole in the track.
2. **Confirm the 2024 EM 385 numbers** for §16.G.05 and §16.B.06 (§3 above).
3. **§1926.1412 / §1926.1413** still open from OHC-05 — same cause, same fix.
4. Consider whether the ACS should carry the **100 ft hand-signal boundary** and the **signal person qualification / non-portability** rule as elements of their own; both are currently gated as second items (`A.K1b`, `A.K2b`).
