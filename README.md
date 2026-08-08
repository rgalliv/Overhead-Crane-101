# Overhead-Crane-101

CraneQualified — **Overhead Crane Operator Track (OHC)**. Twelve modules, ACS format, decomposed to Knowledge / Risk Management / Skills elements under the code pattern `OHC.[module].[task].[category][n]`.

## Contents

| Path | What it is |
|---|---|
| `docs/OHC-0n-trace-table.md` | Element-to-item trace tables — **generated** from the same question data that builds each module. |
| `build/cq_authoring.py` | Shared authoring scaffold — HTML shell and slide renderers for all OCO301C modules. |
| `build/build_OHC_M0n.py` | Per-module question data. |
| `build/gen_trace.py` | Parameterised trace-table generator (`python3 build/gen_trace.py 05 06`). Supersedes the copy-pasted `gen_trace_M0n.py` scripts still used by OHC-01…-04. |
| `manifests/OHC_M0n.json` | Rebuild source of truth per module — salt, gate set, answer key. |
| `out/OHC_M01_EquipmentAndJurisdiction.html` | OHC-01. 63 slides, 28 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M02_ComponentsAndSystems.html` | OHC-02. 59 slides, 24 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M03_ControlsAndOperatingModes.html` | OHC-03. 59 slides, 24 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M04_RatedLoadAndWeight.html` | OHC-04. 60 slides, 25 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M05_InspectionRegime.html` | OHC-05. 63 slides, 28 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M06_RiggingInterface.html` | OHC-06. 65 slides, 29 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M07_LoadHandling.html` | OHC-07. 69 slides, 31 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M08_OperationalRules.html` | OHC-08. 66 slides, 28 gate items, 0 gaps, CONFORMANT. |
| `docs/OHC-ACS-build-spec.md` | **The ACS itself** — all twelve modules, 396 elements, committed verbatim from the authoritative HTML breakdown. Source of truth for every build. |
| `docs/OHC-build-format-spec.md` | Build format, packaging and question architecture for the OHC track, derived from the mobile-crane Developer Handoff (structure only). |
| `docs/second-brain-crosscheck.md` | Cross-check of the OHC build spec against the CraneQualified Second Brain corpus — citation verification, corpus gaps, build-pipeline conflicts, and recommended order of work. |

## Status

Track status: **OHC-01 … OHC-08 built** (0 gaps, gates verified); OHC-09 … OHC-12 not started. Course code **OCO301C**, gate code **OHC-1**, modules **OHC-01 … OHC-12**. Runs **parallel to** the existing six-module overhead course, which continues unchanged. Gate is **100%, server-authoritative**. No revision change to the CraneQualified Competency and Gate Master is made by anything in this repo.

The ACS is committed at `docs/OHC-ACS-build-spec.md`, flattened from the authoritative HTML breakdown rather than re-keyed — element codes and paragraph-letter citations are exactly the content a re-keying would corrupt.

## Before building

Read the cross-check first. Four items are blocking or near-blocking:

1. ~~**ASME B30.2 is not in the corpus**~~ — **struck 2026-08-08.** `ASME B30.2-2016.pdf` **is** held (`ANSI Standards/`). The surviving caveat is narrower: 2016 is neither operative edition — the facility branch incorporates **ANSI B30.2.0-1967**, the construction branch **ASME B30.2-2005** sections.
2. ~~EM 385-1-1 Chapter 16 citations are unverified~~ — **resolved 2026-08-07.** Section 16 verified, 1:1 crosswalk to `16-8.aa(2)–(7)`. A 2014-edition decoy file still shares the obvious filename with the cited 2024 edition; rename it.
3. **NAVFAC P-307 is held** (2000 and 2006 editions, SharePoint) — dated, not missing. **Crane Corner** is still unfetched. Also found: Navy Crane Center *Category 3 (Non-Cab) Crane Safety* student guide, 163 pages, directly on-topic.
4. **The NCCCO overhead crane certification premise** underpinning the Certification Gate needs confirming before OHC-01 or OHC-12 is authored.
5. **Part 1910 beyond .179 is uncited and unheld.** §1910.184 (slings) and §1910.147 (energy control) govern the facility branch and the corpus has no primary text for either — only decks and client policies. §1910.179 also routes to Subpart D and Subpart S by name. Cheap to close; Part 1910 is public domain.

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

Both carry Obsidian frontmatter and `[[wikilinks]]` matching the existing index convention. After dropping them in, add seven lines to `_Crane Standards — Index.md` so they are reachable from the index.

This is the remote-run delivery path described in the vault's own `CLAUDE.md` — the Microsoft 365 connector available to this session has read access to the vault but not `Files.ReadWrite.All`, so it cannot write directly.
