# Overhead-Crane-101

CraneQualified — **Overhead Crane Operator Track (OHC)**. Twelve modules, ACS format, decomposed to Knowledge / Risk Management / Skills elements under the code pattern `OHC.[module].[task].[category][n]`.

**North America pack (2026-08):** Canada jurisdiction (CSA B167 + ON/BC/AB/QC/federal), PES + bilingual designation forms, buyer audit binder, generated training imagery, and interactive jurisdiction tree.

## Contents

| Path | What it is |
|---|---|
| `docs/OHC-0n-trace-table.md` | Element-to-item trace tables — **generated** from the same question data that builds each module. |
| `docs/OHC-Canada-jurisdiction-pack.md` | Canada mapping — CSA B167 spine + federal/provincial overlays. |
| `docs/OHC-ACS-Canada-amendment.md` | ACS Task D (Canada) + OHC-12 routing amendments. |
| `docs/OHC-buyer-audit-binder.md` | Safety-director evidence checklist and folder map. |
| `forms/pes/` | Printable Performance Evaluation Sheets (108 S + Canada addendum). |
| `forms/designation/` | Employer designation certificate — **EN** and **FR**. |
| `assets/images/` | Generated training visuals (inlined into self-contained HTML). |
| `out/interactive/OHC_Jurisdiction_Tree.html` | Standalone US/Canada jurisdiction decision tree. |
| `build/cq_authoring.py` | Shared authoring scaffold — HTML shell, hero media, flip cards, decision tree. |
| `build/retrofit.py` | Pre.html → gated HTML (FNV-1a hashes + gate engine). |
| `build/enhance_visuals.py` | Visual-pack CSS + module imagery for M02–M11. |
| `build/build_OHC_M0n.py` | Per-module question data. |
| `build/gen_trace.py` | Parameterised trace-table generator (`python3 build/gen_trace.py 05 06`). Supersedes the copy-pasted `gen_trace_M0n.py` scripts still used by OHC-01…-04. |
| `manifests/OHC_M0n.json` | Rebuild source of truth per module — salt, gate set, answer key. |
| `out/OHC_M01_EquipmentAndJurisdiction.html` | OHC-01. US + **Canada Task D**, hero/interactive tree, 36 gate items. |
| `out/OHC_M02_ComponentsAndSystems.html` | OHC-02. 59 slides, 24 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M03_ControlsAndOperatingModes.html` | OHC-03. 62 slides, 27 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M04_RatedLoadAndWeight.html` | OHC-04. 60 slides, 25 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M05_InspectionRegime.html` | OHC-05. 63 slides, 28 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M06_RiggingInterface.html` | OHC-06. 65 slides, 29 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M07_LoadHandling.html` | OHC-07. 69 slides, 31 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M08_OperationalRules.html` | OHC-08. 66 slides, 28 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M09_CommunicationAndSignals.html` | OHC-09. 66 slides, 28 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M10_EnvironmentalHazards.html` | OHC-10. 67 slides, 29 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M11_MalfunctionsAndEmergencies.html` | OHC-11. 66 slides, 28 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M12_Capstone.html` | OHC-12. Capstone + Canada designation routing, 30 gate items. |
| `docs/OHC-ACS-build-spec.md` | **The ACS itself** — all twelve modules, 398 elements, committed verbatim from the authoritative HTML breakdown. Source of truth for every build. |
| `docs/OHC-build-format-spec.md` | Build format, packaging and question architecture for the OHC track, derived from the mobile-crane Developer Handoff (structure only). |
| `docs/second-brain-crosscheck.md` | Cross-check of the OHC build spec against the CraneQualified Second Brain corpus — citation verification, corpus gaps, build-pipeline conflicts, and recommended order of work. |

## Status

Track status: **all twelve modules built.** Every module audits at **0 gaps, CONFORMANT**, and every gate is behaviourally verified at 100% with the completion handshake chaining `OHC_M01 → … → OHC_M12 → (end)`.

**North America / buyer pack:** Canada Task D authored into OHC-01; Canada designation routing in OHC-12; PES HTML for all modules; EN+FR designation certificates; interactive jurisdiction tree; generated imagery inlined for self-contained LMS files; visual CSS pack across M02–M11.

**Track totals (pre-Canada census):** 771 slides · **333 gate items** · 292 gated K+R elements · 108 S elements on Performance Evaluation Sheets. OHC-01/12 rebuilt with additional Canada gates — see manifests for current counts.

**Element coverage is complete and verified.** A census cross-check against `docs/OHC-ACS-build-spec.md` confirms **every ACS Knowledge and Risk Management element in all twelve modules carries at least one gate item** — 290 ACS elements plus the 2 net-new in OHC-01 = 292, with 41 elements carrying a second item where they hold two independently testable facts. Re-run the check any time with the script in the commit for `Build OHC-12`.

**Census amendment.** The ACS census table totals **398** elements. OHC-01 carries two net-new elements from the Part 1910 map (`A.K7` incorporation by reference, `B.K7` the two-edition split), moving OHC-01 from 17 K to 19 K and the **track total to 400**. The ACS census table needs the same amendment.

Course code **OCO301C**, gate code **OHC-1**, modules **OHC-01 … OHC-12**. Runs **parallel to** the existing six-module overhead course, which continues unchanged. Gate is **100%, server-authoritative**. No revision change to the CraneQualified Competency and Gate Master is made by anything in this repo.

The ACS is committed at `docs/OHC-ACS-build-spec.md`, flattened from the authoritative HTML breakdown rather than re-keyed — element codes and paragraph-letter citations are exactly the content a re-keying would corrupt.

## Before building

Read the cross-check first. Four items are blocking or near-blocking:

1. ~~**ASME B30.2 is not in the corpus**~~ — **struck 2026-08-08.** `ASME B30.2-2016.pdf` **is** held (`ANSI Standards/`). The surviving caveat is narrower: 2016 is neither operative edition — the facility branch incorporates **ANSI B30.2.0-1967**, the construction branch **ASME B30.2-2005** sections.
2. ~~EM 385-1-1 Chapter 16 citations are unverified~~ — **resolved 2026-08-07.** Section 16 verified, 1:1 crosswalk to `16-8.aa(2)–(7)`. A 2014-edition decoy file still shares the obvious filename with the cited 2024 edition; rename it.
3. **NAVFAC P-307 is held** (2000 and 2006 editions, SharePoint) — dated, not missing. **Crane Corner** is still unfetched. Also found: Navy Crane Center *Category 3 (Non-Cab) Crane Safety* student guide, 163 pages, directly on-topic.
4. **The NCCCO overhead crane certification premise** underpinning the Certification Gate needs confirming before OHC-01 or OHC-12 is authored.
5. **Subpart CC signals paragraph text is unheld — largest remaining sourcing hole.** §§1926.1419–1422 and §1926.1428 **apply** to overhead cranes on the construction branch (verified from the §1926.1438(b)(2)(i) enumeration), but the corpus copy is a degraded OCR scan and osha.gov / ecfr.gov are blocked by this environment's egress policy. Section-level only is gated in OHC-09. Same cause and fix as §1926.1412/1413 in OHC-05.
6. **Part 1910 beyond .179 is uncited and unheld.** §1910.184 (slings) and §1910.147 (energy control) govern the facility branch and the corpus has no primary text for either — only decks and client policies. §1910.179 also routes to Subpart D and Subpart S by name. Cheap to close; Part 1910 is public domain.

## Standing disciplines

Content establishes the operator's standard of care. It never confers qualification — the determination belongs to the **controlling entity** (Gate Master Rev 1.3, amendment A2) and is not delegable to a training vendor.

## Vault drop-in

`vault-dropin/` mirrors the Obsidian vault (`OneDrive - MSC Safety Solutions/Documents/Obsidian/My Second Brain/`). Files land in the matching folder:

| File | Destination |
|---|---|
| `vault-dropin/Crane Standards & Guides/OHC — 1910.179 Citation Pack (verified).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — Tier 0 Deck Map.md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — Tier 0 Knowledge Harvest.md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — EM 385 Section 16 Overhead and Gantry (verified).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — OSHA Part 1910 Map.md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — Rigging Knowledge Harvest (verified).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — Load Handling Source Pack (verified).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — Signals and Communication Source Pack (verified).md` | `📚 Resources/Crane Standards & Guides/` |

Both carry Obsidian frontmatter and `[[wikilinks]]` matching the existing index convention. After dropping them in, add eight lines to `_Crane Standards — Index.md` so they are reachable from the index.

This is the remote-run delivery path described in the vault's own `CLAUDE.md` — the Microsoft 365 connector available to this session has read access to the vault but not `Files.ReadWrite.All`, so it cannot write directly.
