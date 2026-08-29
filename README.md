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
| `out/OHC_M05_InspectionRegime.html` | OHC-05. 64 slides, 29 gate items. 1412/1413 and 1910.147 held. |
| `out/OHC_M06_RiggingInterface.html` | OHC-06. 66 slides, 30 gate items. §1910.184 / §1926.251 held. |
| `out/OHC_M07_LoadHandling.html` | OHC-07. 69 slides, 31 gate items, 0 gaps, CONFORMANT. |
| `out/OHC_M08_OperationalRules.html` | OHC-08. 67 slides, 29 gate items. §1910.147 mapped on `C.K1b`. |
| `out/OHC_M09_CommunicationAndSignals.html` | OHC-09. 69 slides, 28 gate items. CC signals paragraphs held. |
| `out/OHC_M10_EnvironmentalHazards.html` | OHC-10. 67 slides, 29 gate items. §1910.147 held; Subpart D still OPEN. |
| `out/OHC_M11_MalfunctionsAndEmergencies.html` | OHC-11. 67 slides, 29 gate items. §1910.147 on `A.K3b`. |
| `out/OHC_M12_Capstone.html` | OHC-12. Capstone + Canada designation routing, 30 gate items. |
| `docs/OHC-ACS-build-spec.md` | **The ACS itself** — all twelve modules, **400** elements (184 K · 108 R · 108 S), committed from the authoritative HTML breakdown. Source of truth for every build. |
| `docs/OHC-build-format-spec.md` | Build format, packaging and question architecture for the OHC track, derived from the mobile-crane Developer Handoff (structure only). |
| `docs/second-brain-crosscheck.md` | Cross-check of the OHC build spec against the CraneQualified Second Brain corpus — citation verification, corpus gaps, build-pipeline conflicts, and recommended order of work. |

## Status

Track status: **all twelve modules built.** Every module audits at **0 gaps, CONFORMANT**, and every gate is behaviourally verified at 100% with the completion handshake chaining `OHC_M01 → … → OHC_M12 → (end)`.

**North America / buyer pack:** Canada Task D authored into OHC-01; Canada designation routing in OHC-12; PES HTML for all modules; EN+FR designation certificates; interactive jurisdiction tree; generated imagery inlined for self-contained LMS files; visual CSS pack across M02–M11.

**Track totals:** 802 slides · **347 gate items**. Handshake `OHC_M01 → … → OHC_M12 → (end)` at 100% gate. See manifests for per-module salts and answer keys.

**Element coverage is complete and verified.** A census cross-check against `docs/OHC-ACS-build-spec.md` confirms **every ACS Knowledge and Risk Management element in all twelve modules carries at least one gate item** — 290 ACS elements plus the 2 net-new in OHC-01 = 292, with 41 elements carrying a second item where they hold two independently testable facts. Re-run the check any time with the script in the commit for `Build OHC-12`.

**Census.** The ACS census table totals **400** elements (OHC-01 is 19 K including net-new `A.K7` incorporation by reference and `B.K7` the two-edition split). Canada overlay: OHC-01 Task D → **411**; plus OHC-12 `C.K6`/`C.R4` → **413**. See `docs/OHC-ACS-Canada-amendment.md`.

Course code **OCO301C**, gate code **OHC-1**, modules **OHC-01 … OHC-12**. Runs **parallel to** the existing six-module overhead course, which continues unchanged. Gate is **100%, server-authoritative**. No revision change to the CraneQualified Competency and Gate Master is made by anything in this repo.

The ACS is committed at `docs/OHC-ACS-build-spec.md`, flattened from the authoritative HTML breakdown rather than re-keyed — element codes and paragraph-letter citations are exactly the content a re-keying would corrupt.

## Before building

Read the cross-check first. Items that were blocking are closed below, or listed as **still blocked** with why.

### Closed 2026-08-28 (held OSHA.gov text, not eCFR)

1. **Subpart CC signals** — §§1926.1419–1422 and §1926.1428 paragraph text **held** (`vault-dropin/held-cfr/`). OHC-09 gates from held paragraphs (Standard Method / prior agreement, chart posting, QSP documentation, radio on-site test). Same fetch closed **§1926.1412 / §1926.1413** in OHC-05 (`B.R3` is 1412(d)(1), not section numbers alone). eCFR was CAPTCHA-blocked and was not used.
2. **Part 1910 beyond .179** — **§1910.184** (slings) and **§1910.147** (energy control) **held**. Mapped: OHC-06 `A.K1b` / `A.R1`; OHC-05 `C.K3b`; OHC-08 `C.K1b`; OHC-10 `C.K5`; OHC-11 `A.K3b`. Construction companion **§1926.251** held. **Part 1910 Subpart D** (walking-working surfaces, reached from §1910.179(c)(2)) remains **unheld** — OHC-10 `A.K4` / `A.K5b` stay OPEN.
3. **ASME B30.2 edition mismatch** — not pirated. Facility IBR is **ANSI B30.2.0-1967** (§1910.179(b)(2)); construction IBR is named **ASME B30.2-2005** sections (§1926.1438(b)(2)(iii)). Vault **B30.2-2016** is consensus held, **not** either governing edition. See `OHC — B30.2 edition scope.md`.
4. **NCCCO overhead-crane certification premise** — public overview **held** (documentation fetch; live `curl` 403). OSHA §1926.1427 **held** and does **not** name NCCCO. ACS / OHC-01 / OHC-12 treat NCCCO CCO Overhead Crane Operator as the programme path (CCOS), not a CFR name. No exam-item scrape.
5. **ACS census 398 → 400** — table in `docs/OHC-ACS-build-spec.md` matches the modules (OHC-01 `A.K7` / `B.K7`).
6. **EM 385 2014 decoy filename** — PDF is **not in this git repo**. Rename instruction published: `EM_385-1-1.pdf` → `EM_385-1-1_30Nov2014_DECOY.pdf` in the vault/Drive copy. Cited 2024 file: `EM 385-1-1 _EFFECTIVE 15 March 2024.pdf`.
7. **NAVFAC P-307 / Crane Corner** — 2000/2006 P-307 **dated-held** in the vault (not in git). 2025 PDF URL **HTTP 403**. Crane Corner archive **HTTP 403**. OHC-11 does **not** gate from either. Status pack: `OHC — NAVFAC P-307 and Crane Corner status.md`.

### Still blocked (do not pretend these are gated)

- **EM 385-1-1 (15 Mar 2024) Chapter 16 body** unread for **§16.G.05 / §16.B.06**. OHC-09 items that use those numbers remain marked *2014 text*. **16-8.aa(2)–(7)** already crosswalked.
- **Part 1910 Subpart D** (and Subpart S by name at 1910.179) — unheld. OHC-10 `A.K4` / `A.K5b` OPEN.
- **CSA B167** — cite-by-name until a verified edition is held (Canada pack unchanged).
- **eCFR** — CAPTCHA; OSHA.gov HTML is the held copy.
- **Crane Corner / P-307 2025** — 403, unfetched.
- **Paid ASME volumes** — not reproduced. Cite OSHA IBR sentences only.

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
| `vault-dropin/Crane Standards & Guides/OHC — 1926.1412 and 1413 Citation Pack (verified).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — 1910.184 and 1910.147 Citation Pack (verified).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — NCCCO Overhead Program (public pages).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — B30.2 edition scope.md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — NAVFAC P-307 and Crane Corner status.md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/EM_385-1-1_30Nov2014_DECOY-DO-NOT-CITE.md` | `📚 Resources/Crane Standards & Guides/` (rename instruction; PDF not in git) |
| `vault-dropin/held-cfr/*.txt` | Held OSHA.gov extracts (not eCFR) |

Both carry Obsidian frontmatter and `[[wikilinks]]` matching the existing index convention. After dropping them in, add eight lines to `_Crane Standards — Index.md` so they are reachable from the index.

This is the remote-run delivery path described in the vault's own `CLAUDE.md` — the Microsoft 365 connector available to this session has read access to the vault but not `Files.ReadWrite.All`, so it cannot write directly.
