---
title: OHC — Tier 0 Deck Map
type: source-map
domain: owned-ip
tags: [tier-0, ohc, overhead-crane, decks, deck-text, reuse, acs, build-spec]
generated: 2026-08-07
authority: ours-quote-freely
---

# ⭐ OHC — Tier 0 Deck Map

The owned overhead-crane material that already exists, mapped to the OHC ACS. ⬅ [[_Deck Text — Index]] · [[_Crane Standards — Index]] · [[🗺️ Home]]

> [!important] The build rule this note exists to enforce
> **Tier 0 — MSC / CCOS / CraneQualified own IP. It is ours. Quote freely, reuse freely. Check here first, before any external source.**
> The OHC ACS build spec's twelve Reference blocks cite **zero** Tier 0 material. That is avoidable rework, and worse — it risks the new track contradicting material already shipped to clients.

> [!note] Scope of this pass
> These decks were **inventoried, not read.** Slide and note counts come from deck-text frontmatter. Content mining is the next pass — the point of this note is that the seam exists and where it is.

---

## 📊 The overhead-crane Tier 0 corpus

Extracted text lives under `📚 Resources/🔎 Deck Text (searchable)/`, mirroring the source tree.

| Deck | Slides | Notes | Primary OHC fit |
| --- | --- | --- | --- |
| **`2. Overhead Crane Training - With RIGGING.pptx`** ⭐ | **151** | — | OHC-06 rigging interface + OHC-02/03/07 — the broadest single source |
| **`Overhead Crane Training Rev 2.pptx`** ⭐ | **141** | — | full-track spine; likely the most current revision |
| `General Iron-Overhead Crane Training.pptx` | 118 | **101** ⭐ | OHC-02/03/05 — **highest note density in the set** |
| `General Iron-Overhead Crane Training2.pptx` | 121 | **101** ⭐ | sibling revision — diff against the above before reusing |
| `Introduction To Overhead Crane.pptx` | 47 | — | OHC-01 equipment identification and classification |
| `Overhead Cranes - MSC 7-29-2017.pptx` | — | — | delivered-course lineage |
| `Overhead Cranes - MSC 1-24-2019.pptx` | — | — | delivered-course lineage |
| `Overhead Cranes - Dickenson SD 3-18-19.pptx` | — | — | delivered-course lineage |
| `CRC Subpart CC Cranes & Derricks.pptx` | 166 | 91 | **OHC-01 Task B jurisdiction** — Subpart CC framing |
| `Cranes-and-Derricks-Safety.pptx` | — | — | general safety framing |

Roughly **700+ overhead-crane-specific slides**, of which **200+ carry instructor notes** — the notes being the part that holds the teaching voice the facilitator guides need.

**Also directly on-topic, non-deck:**
- [[IPT Section 11 — Overhead Cranes]] — full verbatim OCR text, `📚 Resources/Crane Standards & Guides/IPT Handbook — Missing Sections (text)/`. **Tier 2b — reference, never quote, always reword.**
- `Overhead Evaluation Test-2019` + `--key` — existing evaluation instrument. Direct input to the OHC-12 capstone and to the element→item trace table.
- `ETS Overhead Crane` / `ETS Overhead Crane Book Scanned` — course book lineage.
- `Overhead crane inspection notes` — field notes, OHC-05.

---

## 🚨 The blocked seam — 6 decks invisible to search

Six overhead-crane-relevant decks are **OLE2 legacy binary PowerPoint** and could not be extracted. They do not appear in vault search, and Claude cannot read them.

| File | Why it matters |
| --- | --- |
| **`Overhead Cranes.ppt`** | on-topic by title; unknown depth |
| **`mar09_Overhead_Crane_Inspections.ppt`** | **OHC-05** — inspection is the module with the thinnest sourcing |
| **`Precast Institute Overhead Crane Inspection.ppt`** | **OHC-05** — second independent inspection treatment |
| **`Cranes - Inspection Layton Truck April 2010.ppt`** | inspection practice |
| **`Subpart CC 10-1-16.ppt`** | **OHC-01 Task B** — jurisdiction |
| **`1412 - 1414 - Inspection [Autosaved].ppt`** | **§1926.1412/1413/1414** — exactly the construction-branch inspection authority the ACS is missing |

> [!tip] The fix is about two minutes per file
> Open each in PowerPoint and **Save As** a real `.pptx`, then re-run `scratchpad/extract.sh`. That last one — `1412 - 1414 - Inspection` — is the highest-value single file in the vault for OHC-05 and OHC-06 right now, because §1926.1412 and §1926.1413 appear **nowhere** in the current ACS.
>
> Same fix applies to the three mislabeled modern-extension files (`AB Rigging Foundations.pptx`, `1. Lift Director Certification 6.pptm`, `1 - Confined Space for Construction.pptx`), which are also OLE2 inside.

---

## 🗺️ Where to look first, by module

| Module | Start here |
| --- | --- |
| **OHC-01** Equipment & jurisdiction | `Introduction To Overhead Crane` · `CRC Subpart CC Cranes & Derricks` · 🚨 `Subpart CC 10-1-16.ppt` |
| **OHC-02** Components & systems | `General Iron-Overhead Crane Training` (101 notes) · [[IPT Section 11 — Overhead Cranes]] |
| **OHC-03** Controls & modes | `General Iron` · `Overhead Crane Training Rev 2` |
| **OHC-04** Rated load & weight | Lift Director decks (`Certification 6/7`, 177/166 slides) · `P30-1_2014` |
| **OHC-05** Inspection | 🚨 `mar09_Overhead_Crane_Inspections.ppt` · 🚨 `Precast Institute Overhead Crane Inspection.ppt` · 🚨 `1412 - 1414 - Inspection.ppt` · `Overhead crane inspection notes` |
| **OHC-06** Rigging interface | `2. Overhead Crane Training - With RIGGING` (151) · `30107-11 Rigging Practices` (187) · `38301-11 Advanced Rigging` (98/69) |
| **OHC-07** Load handling | `Overhead Crane Training Rev 2` · [[IPT Section 11 — Overhead Cranes]] |
| **OHC-08** Operational rules | `General Iron` series · `Cranes-and-Derricks-Safety` |
| **OHC-09** Communication & signals | `nccco-signalperson-reference-manual-0418.pdf` · **EM 385 Figure 16-4 *Crane Hand Signals – Overhead and Gantry*** (overhead-specific chart, already in the corpus) |
| **OHC-10** Environment | `Severe_Weather_Guidelines_v5_062518.pdf` |
| **OHC-11** Malfunctions & emergency | thinnest Tier 0 coverage — see gap note below |
| **OHC-12** Capstone & documentation | `Overhead Evaluation Test-2019` + key · Lift Director documentation architecture |

---

## ⚠️ Remaining gaps after this pass

| Gap | Status |
| --- | --- |
| **ASME B30.2** | ✅ **closed 2026-08-07** — `B30.2-2005` (the edition incorporated by reference at §1926.1438(b)(2)(ii)) + a 2016 copy. Still syncing to OneDrive at time of writing. |
| **ASME B30.11** monorails & underhung | ✅ closed — `B30.11-1998 - LANL` |
| **ASME B30.16** overhead hoists | ✅ closed — `B30.16-2007` |
| **CMAA 74** | ❌ still missing — only CMAA 70 held |
| **CMAA Specification No. 61** | ❌ missing, and it is **incorporated by reference into §1910.179(b)(6)(i)** — i.e. law, not just guidance |
| **NAVFAC P-307** | ❌ still unfetched — flagged 🔒 since 30 July. Best public-domain analogue for the Designation Gate (OHC-12) and facility inspection/certification (OHC-05). Needs a manual browser pull. |
| **Navy Crane Center — Crane Corner** | ❌ still unfetched — the incident case-study library for **OHC-11**, which has the thinnest Tier 0 coverage of any module. Same manual-pull fix. |
| **NCCCO overhead crane material** | ❌ none in the corpus. The Certification Gate in `OHC.01.C.K3` / `OHC.12.C.K2` rests on a premise nothing here substantiates. **Resolve before authoring OHC-01 or OHC-12.** |
| **EM 385 Ch. 16 body** | ⚠️ unverified. `16-2` / `16-8.aa` citations appear in all 12 modules; Chapter 16 text could not be extracted from either archived PDF. The Source Verification Log still lists EM 385 as **unverified**. |

---

## 🔗 Where this connects

- [[OHC — 1910.179 Citation Pack (verified)]] — the regulatory layer this sits beside
- [[_Deck Text — Index]] — how to search inside the decks
- [[_Crane Safety Library]] · [[_Training Decks Index]] · [[_NCCER Curriculum — Index]]
