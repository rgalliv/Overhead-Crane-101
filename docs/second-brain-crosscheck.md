# OHC Build Spec — Cross-Check Against the Second Brain

**Subject.** CraneQualified Overhead Crane Operator Track (OHC-01 … OHC-12), ACS Build Specification, Working Draft.
**Date.** 7 August 2026.
**Method.** Every load-bearing citation in the spec was tested against the corpus the program actually holds — Notion `🧠 Second Brain` and the Google Drive crane library — not against titles or memory. Regulatory text was read from the archived copies, per the register's own standing rule ("build from the archive, never from a URL"). eCFR is unreachable from this environment, which made that rule binding rather than advisory.

**Headline.** The ACS decomposition is sound and the element architecture holds. The problems are in the citation layer and the build layer, not the pedagogy. Seven findings would change what gets built; four are corpus gaps that need closing before OHC-01 goes to slides.

---

## 1. What the Second Brain actually holds for overhead cranes

**Verified present and readable**

| Asset | Tier | Feeds |
|---|---|---|
| `1910.179 overhead and underhung cranes.pdf` — full paragraph text, (a) through (o) | 1 | the whole track |
| `EM 385-1-1 _EFFECTIVE 15 March 2024.pdf` | 1 | all 12 modules |
| `29 CFR 1926 Subpart CC.pdf` (incl. §1926.1438) | 1 | OHC-01 |
| `GuidelinesForInspectingOverheadCrane Structures.pdf` | — | OHC-02, OHC-05 |
| `IPT Section 11 Overhead Cranes` | 2b | OHC-02, OHC-03, OHC-07 |
| `IPT Section 6 Material Handling, Lifting Devices` | 2b | OHC-06 |
| CMAA 70 (`.docx` + `cmaa-70-20…pdf`) | 2a | OHC-02 |
| ASME B30.9 Slings · B30.10 Hooks · B30.20 BTH · B30.26 Rigging Hardware · B30.29 · P30.1-2014 | 2a | OHC-04, OHC-05, OHC-06 |
| ASME B30.17-2015 (LANL) | 2a | OHC-01, OHC-02 |
| NCCCO Signal Person Reference Manual | 2b | OHC-09 |
| EPRI *Lifting, Rigging and Small Hoist Usage Program Guide*; EPRI NMAC *Material Handling Application Guide* | — | OHC-05, OHC-06 |
| Notion `Overhead Crane` project: *Overhead Crane Training – With RIGGING*, `12_02_22_c3cs_sg_rev02`, *Federal Register* | 0 / 1 | OHC-01 |

**Tier 1 assets the spec never references but should**

- **DOE Hanford Hoisting & Rigging Manual (DOE/RL-92-36)** — Ch. 13 is overhead and gantry; Ch. 5 Hooks resolves the OSHA-vs-ASME hook-criteria conflict outright; Ch. 17 Interpretations. Quotable, currently maintained. Directly feeds OHC-05 Task C and OHC-06 Task A.
- **USBR FIST 4-1A (May 2024)** — §6.10 *Overhead and Gantry Cranes*, §6.5 Inspections, §6.7 Testing, §6.9 Critical Lifts, **Table 1 crane/hoist inspection criteria (p. 121)**. Content-verified 30 July. This is the PM-interval artifact OHC-05 needs and it is public domain.

---

## 2. Findings that change the build

### F1 — §1910.179(b)(8) is the Designation Gate, and the spec never cites it

Verbatim from the archived text:

> **1910.179(b)(8)** Designated personnel — Only designated personnel shall be permitted to operate a crane covered by this section.

This is the regulatory anchor for the entire Designation Gate architecture (`OHC.01.C.K2`, `OHC.12.C.K1`, §2 of the spec). It appears nowhere in the spec.

It also proves the two-branch model precisely: **(b)(8) is not in the §1926.1438(b)(2) list**, which is exactly why the construction branch reaches for §1926.1427 certification instead. The single paragraph that makes the spec's gate architecture legally legible is the one paragraph it omits. Add it to `OHC.01.C.K2` and `OHC.12.C.K1`.

### F2 — Four EM 385 attributions are actually §1910.179, and the branch behaviour differs

| Spec element | Attributed to | Actually | In the §1438(b)(2) list? |
|---|---|---|---|
| `OHC.02.C.K4`, `OHC.08.A.K3` warning device | EM 385 16-8.aa(4) | **§1910.179(i)** verbatim — *"Except for floor-operated cranes a gong or other effective warning signal shall be provided for each crane equipped with a power traveling mechanism."* | **No** |
| `OHC.04.A.K1` rated load marking | EM 385 16-8.aa(3) | **§1910.179(b)(5)** verbatim, including *"clearly legible from the ground or floor"* | **Yes** |
| `OHC.07.B.K4`, `OHC.08.B.K1` clearances | EM 385 16-8.aa(5) | **§1910.179(b)(6)** (3 in overhead / 2 in lateral, per **CMAA Spec No. 61**) and **(b)(7)** parallel cranes | **Yes** |
| `OHC.08.C.K2` outdoor securing | EM 385 16-8.aa(7) | **§1910.179(b)(4)** — automatic rail clamps and a wind-indicating device for outdoor storage bridges | **No** |

Two consequences. First, sourcing a universal rule to EM 385 makes it look like federal-work-only content — `OHC.04.A.K1` and the clearance elements apply on **both** branches and should lead with the CFR. Second, the warning device and the wind/rail-clamp rule genuinely **drop out** on the §1926.1438(b) construction branch; the spec presents them as branch-neutral. That asymmetry is teachable content the spec currently flattens.

Also note **CMAA Spec No. 61** is incorporated by reference at (b)(6)(i). The spec's standing disciplines name CMAA 70 and 74 only.

### F3 — §1926.1438(b)(2) incorporates ASME B30.2-2005 by reference, and the spec omits half the rule

`OHC.01.B.K3` enumerates only the §1910.179 paragraphs. The archived Subpart CC text shows §1926.1438(b)(2)(ii) splits on equipment manufacture date — **before vs. on or after 19 September 2001** — with §1910.179(b)(2) governing the older equipment and an **enumerated list of ASME B30.2-2005 sections, incorporated by reference under §1926.6**, governing the newer, with *"29 CFR 1910.147"* substituted for *"ANSI Z244.1"*.

> Caveat on confidence: the Subpart CC PDF is a column-interleaved OCR and is badly scrambled at this passage. The **structure**, the **date**, and the **fact of B30.2-2005 incorporation** are legible. The exact section list is not reliably readable and must be confirmed against a clean copy before it reaches a slide.

This matters beyond completeness. On the construction branch, named B30.2-2005 sections are **regulation**, not consensus guidance — which materially changes how the §3 "cite by name only" rule applies there. The paragraph-letter list in `OHC.01.B.K3` is verified correct as far as it goes: (b)(5)–(7); (e)(1),(3),(5),(6); (f)(1),(4); (g); (h)(1),(3); (k); (n); (a) definitions except *hoist* and *load*. It is just not the whole of (b)(2).

### F4 — OHC-05 and OHC-06 have no construction-branch inspection authority

**§1910.179(j)** (Inspection) and **(m)** (Rope inspection) are **not** in the §1926.1438(b)(2) list. Neither is **(l)** (Maintenance — *"A preventive maintenance program based on the crane manufacturer's recommendations shall be established"*).

OHC-05's References cite 1910.179, EM 385 and ASME only. On the §1926.1438(b) branch the inspection duty comes from **§1926.1412**, and wire rope from **§1926.1413**. Neither section appears anywhere in the 12 modules. OHC-06 has the same hole (§1926.1413, §1926.251). As written, OHC-05 teaches the facility branch and silently drops the construction branch it spent OHC-01 establishing.

### F5 — The gate the spec promises has no deliverable that can enforce it

§1 mandates a **"server-authoritative 100% mastery gate."** §4 specifies deliverables of **PPTX + Facilitator Guide DOCX only**.

Neither format can enforce any gate. In the corpus, the 100% mastery gate exists only in the **single-file HTML module architecture** — FNV-1a hashed answers, hard forward-nav lock, completion handshake (CM-101, built and behaviourally verified). Meanwhile the established PPTX standard this spec inherits carries a different gate entirely: **"8-question Final KC (80% pass)."**

So the spec adopts the 100% gate, the 80% deliverable, and no gate engine. Pick one: add an HTML module to the per-module deliverable set, or restate §1 against the 80% PPTX model.

### F6 — The 43-slide structure is a lossy restatement, and OHC-01 does not fit it

The established standard is exact:

```
Title · Navigation · Objectives · Module Bridge          =  4
4 sections × [Header + 2 content + 4 KC]                 = 28
Final KC (8 questions)                                   =  8
Takeaways · Resources · Completion                       =  3
                                                    Total = 43
```

The spec writes "content slides" and "KC questions" unquantified — built as written it will not land on 43.

The arithmetic then bites. The template carries **24 KC items** (16 section + 8 final). Eleven modules have 15 K + 9 R = **24** knowledge/risk elements — an exact 1:1 trace. **OHC-01 has 17 K + 9 R = 26**, over-running the template by two. Either OHC-01 gets a non-standard slide count, or two elements go untested and that becomes a visible decision rather than an accident (the CM-101 precedent).

Separately: the **9 S elements per module have no home in a PPTX at all.** They are graded performance items. The spec requires "every graded performance item to an S element code" but specifies no artifact that carries them — no evaluation form, no checklist, no field record. That is a missing deliverable across all 12 modules.

### F7 — Two standing disciplines are out of date against adopted amendments

**"Employer" vs "controlling entity."** Gate Master Rev 1.3 amendment **A2** replaced *controlling employer* with **controlling entity**, and `05 — Modules` states plainly: *"the determination belongs to the controlling entity and is not delegable to a training vendor."* The OHC spec says **employer** throughout — §2, `OHC.01.C.K1`, `OHC.01.C.K2`, `OHC.12.C.K1`. Terminology drift from an amendment already adopted effective 31 July.

**The ASME paraphrase rule is stricter than the program allows.** Gate Master Rev 1.3 amendment **A1** permits ASME/OEM to be **paraphrased with attribution** — the register's Tier 2a rule reads *"State requirements in our own words with attribution — 'per ASME B30.5…'. Never reproduce their tables, figures or wording."* The OHC spec §3 says *"cite by name only. Never quote **or paraphrase**."*

The spec forbids something the program has explicitly authorized. The cost is concentrated in OHC-02, OHC-04, OHC-06 and OHC-07, which are left naming standards they are not allowed to state the content of.

---

## 3. Corpus gaps to close before OHC-01 builds

| # | Missing | Cited in | Severity |
|---|---|---|---|
| G1 | **ASME B30.2** — Overhead and Gantry Cranes (top running bridge / top running trolley) | **9 of 12 modules**; also incorporated by reference into §1926.1438(b)(2)(ii) as B30.2-2005 | **Blocking.** The spine standard for the equipment class the track is about is not in the corpus in any form. |
| G2 | **ASME B30.16** — Overhead Underhung and Stationary Hoists | OHC-01, OHC-02, OHC-05 | High. `OHC.01.A.K6` and `OHC.02.B.K3` cite it directly. |
| G3 | **CMAA 74** (single girder) | OHC-02 | Medium. Only CMAA 70 is held. `OHC.02.A.K2`/`K5` and `OHC.02.B.K5` lean on the pair. |
| G4 | **ASME B30.11** / monorail and underhung crane coverage | `OHC.01.A.K4`, `OHC.01.A.K5` | Medium — see §4 below. |
| G5 | **NAVFAC P-307** (Jan 2025) | not cited, should be | High. Flagged 🔒 on 30 July and **still unfetched**. It is the best public-domain analogue for a facility-branch designation and certification program — the exact architecture OHC-12 and OHC-05 are building. Needs a human with a browser. |
| G6 | **Navy Crane Center — Crane Corner archive** | not cited, should be | High. Documented weight-handling incidents in the public domain. It would turn OHC-11 from assertion into evidence. Same 🔒 block, same fix. |
| G7 | **Any NCCCO overhead crane material** | `OHC.01.C.K3`, `OHC.12.C.K2` | **Verify before building.** The corpus holds NCCCO Signal Person, NCCCO mobile test questions and the A/D candidate handbook — nothing for overhead crane. The Certification Gate on the §1926.1438(b) branch rests on "nationally recognized certification administered via NCCCO," and nothing in the Second Brain substantiates that offering for this equipment class. If it does not map, the Certification Gate needs rewriting, not re-sourcing. |

---

## 4. Verification items (flagged, not resolved)

- **EM 385 16-2 and 16-8.aa are unverified.** Cited in **all 12 modules**. The Source Verification Log of 30 July lists EM 385-1-1 under **F. Unverified ◻️** — *"already in project knowledge, not re-checked."* Chapter 16 body text could not be extracted from the archived 2024 PDF with available tooling, so the sub-paragraph numbering (16-2.g/h Class I/II, 16-8.aa(2)–(7)) remains unconfirmed against the corpus. §3 of the spec calls these paragraphs "pre-verified." **Nothing in the Second Brain supports that claim.** This collides with CM-101's stated discipline — *"the module cites no document the team has not read"* — which declined EM 385 §18-4 on exactly these grounds.
- **B30.17 edition scope.** The held copy is **B30.17-2015**, titled *Top Running Bridge, Single Girder, Underhung Hoist*. `OHC.01.A.K5` assigns "underhung trolley or bridge" to B30.17. B30.11 (Monorails and Underhung Cranes) was folded into B30.17 only at the 2020 edition. The B30.2/B30.17 split in `OHC.01.A.K5` needs an edition note, or a newer copy. The PDF is an image-only scan with no text layer, so this could not be confirmed from the file itself.

---

## 5. Corpus hygiene — three traps that will bite a builder

1. **The EM 385 decoy.** `EM_385-1-1.pdf` — present in *both* crane folders, and the file anyone would grab by name — is the **30 Nov 2014** edition. The cited edition lives elsewhere as `EM 385-1-1 _EFFECTIVE 15 March 2024.pdf`. The 2014 edition numbers Chapter 16 as letter subsections (16.A–16.S; **M** Overhead and Gantry, **N** Monorails and Under Hung), so *"16-2"* and *"16-8.aa"* **do not exist in it**. A builder who opens the wrong file will conclude the citations are wrong and may "correct" them into nonsense. Rename or remove the 2014 copy.
2. **B30.17-2015 has no text layer.** Image-only scan; returns empty on extraction. Cannot be searched or verified programmatically. Needs OCR before it can support a claim.
3. **The Subpart CC PDF OCR is scrambled.** Column-interleaved to the point that §1926.1438 is barely legible (see F3). Do not quote from it. A clean §1926.1438 copy is needed for OHC-01, which is the module that depends on it most.

Underlying all three: the register's "48 sources archived locally with SHA256, build from the archive" discipline lives in `rgalliv/mobilecranetech` and the Obsidian vault. **The overhead crane sources in Drive are not under it.** Bringing them under it is the durable fix.

---

## 6. The largest missed asset — Tier 0

The register's first build rule is unambiguous:

> **Tier 0** ⭐ MSC / CCOS / CraneQualified own IP — 141 decks, 17,094 slides. **It is ours. Quote freely, reuse freely. Check here first, before any external source.**

**The OHC spec's twelve Reference blocks cite zero Tier 0 material.**

The `EQ-TRAIN-003/004` seven-stage program is **complete — 43 modules, 43 PPTXs, 43 Facilitator Guides**, built to the identical PptxGenJS standard this spec inherits. Substantial parts of the OHC track are already written:

| OHC module | Existing Tier 0 coverage |
|---|---|
| OHC-06 Rigging Interface and Below-the-Hook | Stage 2 rigger modules; ITI Rigging; SC&RA Bull Rigging Competency Guidebook |
| OHC-09 Communication and Signals | NCCCO Signal Person Reference Manual; existing signal modules; **EM 385 Figure 16-4 *Crane Hand Signals – Overhead and Gantry*** (confirmed present in the EM 385 TOC — an overhead-specific signal chart already in the corpus) |
| OHC-04 Load weight determination | Stage 3/4 load-weight and lift-planning modules; ASME P30.1 |
| OHC-10 Environmental | SC&RA Severe Weather Guidelines |
| OHC-12 Documentation | Stage 7 Lift Director documentation architecture |

Re-deriving these from scratch is avoidable rework, and it risks contradicting shipped material. **Do the Tier 0 pass before authoring OHC-04, -06, -09.**

---

## 7. What is confirmed correct

Worth stating plainly, because most of the spec holds up:

- The **§1910.179 paragraph-letter list** in `OHC.01.B.K3` matches the archived Subpart CC text exactly, including the *hoist*/*load* definitional carve-out.
- **§1926.1438(a)**'s "except §1910.179(b)(1)" carve-out is correctly handled, and the spec is right to source the equipment-family list from §1926.1438(b)(1) rather than §1910.179(b)(1) — the archived §1910.179(b)(1) does **not** include launching gantry cranes, and §1926.1438(b)(1) does.
- The **two-gate architecture** is correct and is corroborated by the paragraph list itself (see F1).
- `OHC.02.B.K4` / `OHC.07.A.K5` — treating the upper limit switch as **not an operating control** — is directly supported by **§1910.179(k)(1)(ii)**, which defines limit-switch trip setting as a *test* determined with an empty hook.
- `OHC.06.C.K1`/`K2` test-lift discipline maps cleanly onto **§1910.179(n)(3)(i)**: *"The load shall be well secured and properly balanced in the sling or lifting device before it is lifted more than a few inches."*
- The **QA sequence in §4 is an improvement on the established standard** — adding the `pdftoppm -bbox` collision test *and* the `pdftotext` page dump, on the finding that "bbox alone has missed interleaving defects." This should be back-ported to the mobile track's workflow, not just used here.

---

## 8. Recommended order of work

1. **Acquire ASME B30.2** (G1). Nothing in OHC-01, -02, -03, -04, -07 through -11 can be built honestly without it, and §1926.1438(b)(2)(ii) makes it partly regulatory.
2. **Pull NAVFAC P-307 and Crane Corner by hand** (G5, G6). Flagged 🔒 since 30 July, both directly serve OHC-05, -11 and -12.
3. **Verify EM 385 Chapter 16 numbering** against the 2024 edition and either confirm or correct every 16-2 / 16-8.aa citation in the spec. Remove the 2014 decoy file first.
4. **Resolve the NCCCO overhead crane question** (G7) before OHC-01 or OHC-12 is authored — it determines whether the Certification Gate survives as written.
5. **Amend the spec** for F1, F2, F4 and F7 (citation and terminology corrections — cheap, and they harden the standard of care).
6. **Decide the gate model** (F5) and fix the slide arithmetic (F6), including an artifact for the 108 S elements.
7. **Run the Tier 0 pass** (§6) before authoring OHC-04, -06 and -09.
8. Add **§1926.1438(b)(2)(ii)** and the ASME B30.2-2005 incorporation to `OHC.01.B.K3` once a clean Subpart CC copy confirms the section list (F3).

---

*Sources read for this cross-check: 29 CFR 1910.179 (complete, archived copy); 29 CFR 1926 Subpart CC §1926.1438 (archived copy, degraded OCR); EM 385-1-1 30 Nov 2014 (front matter and TOC only); EM 385-1-1 15 Mar 2024 (front matter and references only — Chapter 16 body not extractable); Notion `🧠 Second Brain`, `🏗️ CraneQualified HQ`, `Crane Technician — Open Source Register` and its tier pages, `Source Verification Log — 30 July 2026`, `Government Crane Programs`, `05 — Modules`, `ProLevari — Master Knowledge Base`, `Crane Safety & Workforce Development Training Program`, `Overhead Crane`; full Google Drive crane-library inventory.*

*Not read: ASME B30.17-2015 (no text layer), EM 385 Chapter 16 body (not extractable), NAVFAC P-307 (not in corpus), Crane Corner (not in corpus), Tier 0 deck contents (not enumerated in Drive or Notion).*
