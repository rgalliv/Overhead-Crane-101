# OHC-01 — Element-to-Item Trace Table

**Module:** OHC-01 Equipment Types, Configurations, and Jurisdictional Framework
**Course:** OCO301C · **Gate:** OHC-1 · **File:** `OHC_M01_EquipmentAndJurisdiction.html`
**Gate items:** 26 · **Performance items:** 9 · **Pass:** 100%, server-authoritative

This is the pattern module. The other eleven follow this shape.

---

## Standing rules

- **One element, one gate item.** An item testing two elements cannot be traced, and an untraceable item cannot be defended.
- **All 26 K and R elements are gated.** The ACS states every element is a gateable claim; none are taught-but-untested.
- **Practice items sit on top, not inside.** Practice previews the gate, is unscored, and reveals nothing. It does not reduce gate coverage.
- **The correct option is never revealed on a miss.** Wrong retries, correct locks.
- **S elements never appear here.** They live on the Performance Evaluation Sheet (`OHC_M01_PES.docx`) and are signed by an evaluator, not scored by the bridge.

**Source status column:** ✅ verified against archived source · ⚠️ source held but claim unverified · 🔴 blocked, do not author until resolved.

---

## Task A — Equipment Identification and Classification

| Item | Element | Assessment focus | Form | Source | Status |
|---|---|---|---|---|---|
| `OHC01-G01` | `OHC.01.A.K1` | Which equipment falls inside the overhead/gantry family — including that it applies **irrespective of travel means** | MC | §1926.1438(b)(1) | ✅ |
| `OHC01-G02` | `OHC.01.A.K2` | Distinguish top-running from underhung bridge and trolley configuration | MC | ASME B30.2 / B30.17 (by name) | ✅ |
| `OHC01-G03` | `OHC.01.A.K3` | Single- vs double-girder: capacity and service implications, incl. that **longer span permits lower capacity** for a given girder design | MC | CMAA 70 (by name) | ✅ |
| `OHC01-G04` | `OHC.01.A.K4` | Monorail, underhung and wall/jib systems as related but distinct classes | MC | ASME B30.11 (by name) | ✅ |
| `OHC01-G05` | `OHC.01.A.K5` | Match configuration to governing volume — top-running → B30.2, underhung trolley or bridge → B30.17 | MC | B30.2 / B30.17 | ⚠️ *edition note below* |
| `OHC01-G06` | `OHC.01.A.K6` | The hoist as a distinct component class with its own standard | TF | ASME B30.16 (by name) | ✅ |
| `OHC01-G07` | `OHC.01.A.R1` | Consequence of misclassification — the wrong inspection, marking and operating rule set attaches | MC | derived | ✅ |
| `OHC01-G08` | `OHC.01.A.R2` | Mobile-crane logic does **not** transfer: no radius-based load chart, no outrigger set, capacity does not vary with trolley position | MC | §1910.179(b)(5) | ✅ |
| `OHC01-G09` | `OHC.01.A.R3` | Operating an unfamiliar configuration without familiarization — locate the emergency power panel, verify control functions and safety devices, run motions before loading | TF | Tier 0 (owned) | ✅ |

> [!warning] `OHC01-G05` — edition dependency
> The corpus holds **B30.17-2015**, titled *Top Running Bridge, Single Girder, Underhung Hoist*, and **B30.11-1998** *Monorails and Underhung Cranes* as a separate volume. B30.11 was folded into B30.17 only at the **2020** edition. Author this item against the editions actually held, or acquire B30.17-2020+. Do not write "B30.17 covers monorails" while holding a 2015 copy.

---

## Task B — Jurisdictional Determination

| Item | Element | Assessment focus | Form | Source | Status |
|---|---|---|---|---|---|
| `OHC01-G10` | `OHC.01.B.K1` | Permanently installed, used in construction → §1910.179 applies **except (b)(1)**; Subpart CC does not | MC | §1926.1438(a) | ✅ |
| `OHC01-G11` | `OHC.01.B.K2` | Not permanently installed, used in construction → designated Subpart CC sections **including §1926.1427**, plus specified §1910.179 paragraphs | MC | §1926.1438(b) | ✅ |
| `OHC01-G12` | `OHC.01.B.K3` | Recognise which §1910.179 paragraphs survive on the construction branch | MC | §1926.1438(b)(2)(i) | ✅ |
| `OHC01-G13` | `OHC.01.B.K3` *(second aspect)* | **ASME B30.2-2005 sections are incorporated by reference**, split on a 19 Sep 2001 manufacture date | MC | §1926.1438(b)(2)(ii) | 🔴 *see below* |
| `OHC01-G14` | `OHC.01.B.K4` | General-industry facility operation → §1910.179 as the direct spine | TF | §1910.179 | ✅ |
| `OHC01-G15` | `OHC.01.B.K5` | Federal/USACE work → EM 385-1-1 Ch. 16 supplemental requirements | MC | EM 385 16-2 | 🔴 *unverified* |
| `OHC01-G16` | `OHC.01.B.K6` | Indicators of permanent installation — fastened to the building, not readily assembled/disassembled, irremovable part of the property | MC | §1926.1438(a) | ✅ |
| `OHC01-G17` | `OHC.01.B.R1` | Applying facility rules to a non-permanently-installed construction crane, and thereby missing §1926.1427 | MC | derived | ✅ |
| `OHC01-G18` | `OHC.01.B.R2` | Assuming Subpart CC applies to a permanently installed crane used for a construction task | TF | §1926.1438(a) | ✅ |
| `OHC01-G19` | `OHC.01.B.R3` | Failing to re-evaluate jurisdiction when the crane or work context changes | MC | derived | ✅ |

> [!danger] `OHC01-G13` is blocked on a clean source
> The archived Subpart CC PDF is a column-interleaved OCR; §1926.1438(b)(2)(ii)'s **structure**, the **2001 date**, and the **fact of B30.2-2005 incorporation** are legible, but the enumerated section list is not reliably readable. **Do not author this item from that scan.** Resolve against a clean copy — B30.2-2005 is now in the vault, so the incorporation can be checked from both ends.

> [!danger] `OHC01-G15` and `OHC01-G26` are blocked on EM 385 verification
> Chapter 16 body text could not be extracted from either archived EM 385 PDF, and the Source Verification Log still lists EM 385-1-1 as **unverified**. Two further traps: the file named plainly `EM_385-1-1.pdf` is the **30 Nov 2014** edition, whose Chapter 16 uses letter subsections (16.A–16.S) and contains no "16-2" or "16-8.aa" at all. **Verify against the 15 Mar 2024 edition before authoring either item.**

---

## Task C — Roles, Qualification Architecture, and Standard of Care

| Item | Element | Assessment focus | Form | Source | Status |
|---|---|---|---|---|---|
| `OHC01-G20` | `OHC.01.C.K1` | The **controlling entity** makes the qualification determination; training establishes the operator's standard of care and does not confer qualification | MC | Gate Master Rev 1.3 §11.2, A2 | ✅ |
| `OHC01-G21` | `OHC.01.C.K2` | Designation Gate on the facility branch — **"only designated personnel shall be permitted to operate"**, and *designated* means selected or assigned by the employer as qualified for specific duties | MC | **§1910.179(b)(8)** + **(a)(35)** | ✅ |
| `OHC01-G22` | `OHC.01.C.K3` | Certification Gate on the §1926.1438(b) branch — §1926.1427 certified operator | MC | §1926.1427 | ⚠️ *NCCCO premise* |
| `OHC01-G23` | `OHC.01.C.K4` | Competent Person (Cranes and Rigging) on federal work | MC | EM 385 16-2.i | 🔴 *unverified* |
| `OHC01-G24` | `OHC.01.C.K5` | Distinguish operator designation from **appointed person**, inspection personnel, and maintenance qualified persons | MC | §1910.179(b)(8), (l)(3)(i), (m)(1) | ✅ |
| `OHC01-G25` | `OHC.01.C.R1` | Treating course completion as qualification absent the employer determination | TF | Gate Master §11.2 | ✅ |
| `OHC01-G26` | `OHC.01.C.R2` | Operating on federal work without the required written designation | MC | EM 385 16-2 | 🔴 *unverified* |
| `OHC01-G27` | `OHC.01.C.R3` | Blurred accountability when roles are undocumented | MC | derived | ✅ |

> [!note] Numbering
> G01–G27 with **G13 counted as a second aspect of `OHC.01.B.K3`** gives **26 distinct elements across 27 item slots**. If G13 is dropped rather than resolved, the module returns to 26 items and `OHC.01.B.K3` is tested by G12 alone — but the ASME incorporation then goes untaught, which is a real loss on the construction branch. **Recommendation: resolve the source and keep G13.**

> [!warning] `OHC01-G22` — the NCCCO premise
> `OHC.01.C.K3` asserts certification *"administered via NCCCO."* Nothing in the corpus substantiates an NCCCO overhead crane operator offering — the NCCCO material held is Signal Person, mobile test questions and the A/D candidate handbook. Author the item against **§1926.1427** (the regulation), not against a named provider, until the provider question is resolved. This is also the safer construction under the standing discipline: *cite the regulation, not NCCCO.*

---

## Performance items — `OHC_M01_PES.docx`

Not scored by the bridge. Evaluator sign-off, dated, scoped to named equipment and control modes.

| Item | Element | Demonstration |
|---|---|---|
| `OHC01-P01` | `OHC.01.A.S1` | Identify crane type, girder configuration and trolley arrangement on sight |
| `OHC01-P02` | `OHC.01.A.S2` | Match a given crane to its governing ASME volume by name |
| `OHC01-P03` | `OHC.01.A.S3` | Locate and interpret equipment identification and capacity markings |
| `OHC01-P04` | `OHC.01.B.S1` | Walk the installation-status decision tree and state the governing regime |
| `OHC01-P05` | `OHC.01.B.S2` | Identify which certification or designation attaches on each branch |
| `OHC01-P06` | `OHC.01.B.S3` | Classify a crane as EM 385 Class I or Class II 🔴 *blocked with G15* |
| `OHC01-P07` | `OHC.01.C.S1` | State who issued their designation, what equipment and modes it covers, and its limits |
| `OHC01-P08` | `OHC.01.C.S2` | Produce designation and training records on request |
| `OHC01-P09` | `OHC.01.C.S3` | Refuse an assignment outside the scope of designation |

`P07`–`P09` are the Designation Gate rehearsed. They are also the evidence layer OHC-12 Task B assembles.

---

## Build state

| | |
|---|---|
| Authorable now | **21 of 27** gate items · **8 of 9** performance items |
| Blocked on EM 385 Ch. 16 verification | G15 · G23 · G26 · P06 |
| Blocked on a clean §1926.1438 source | G13 |
| Author against the regulation, not a provider | G22 |
| Edition-dependent | G05 |

**OHC-01 cannot be completed until EM 385 Chapter 16 is verified.** Four items and one performance element depend on it, and it is cited in all twelve modules — so this blocks the track, not just this module. It is the highest-value unblock available.

---

## Parallel-track rules

The existing six-module overhead course **continues to run unchanged**. This track is additive.

1. **Separate registry, separate gate.** `cq_keys_OHC.json` under gate `OHC-1`. No shared IDs with the existing course.
2. **Re-author, don't lift.** The existing 50-item exam is Tier 0 and reusable in principle, but the two instruments must not become near-duplicates at different pass marks. Use it as a **coverage reference** — what is already assessed, and how the house phrases things — and write new items to the element trace.
3. **Two pass marks now coexist.** The existing course passes at 80%; OCO301C passes at 100%. That is a deliberate product difference, not a defect — but it must be stated plainly in both course descriptions, or it will read as an error.
4. **The existing course's two known defects stay its own.** Its Q2 rationale cites §1926.550 rather than §1926.1438, and its Q5 teaches NAVFAC P-307 from a document the register records as never opened. Neither is inherited here. Both still warrant a separate fix on that course.
