# Overhead-Crane-101

CraneQualified — **Overhead Crane Operator Track (OHC)**. Twelve modules, ACS format, decomposed to Knowledge / Risk Management / Skills elements under the code pattern `OHC.[module].[task].[category][n]`.

## Contents

| Path | What it is |
|---|---|
| `docs/second-brain-crosscheck.md` | Cross-check of the OHC build spec against the CraneQualified Second Brain corpus — citation verification, corpus gaps, build-pipeline conflicts, and recommended order of work. |

## Status

Track status: **all 12 modules not started.** Module codes OHC-01 … OHC-12 remain **provisional** pending Gate Master assignment. No revision change to the CraneQualified Competency and Gate Master is made by anything in this repo.

The ACS build specification itself should be committed to `docs/OHC-ACS-build-spec.md` from the authoritative copy — it is deliberately not transcribed here, because element codes and paragraph-letter citations are exactly the content a re-keying would corrupt.

## Before building

Read the cross-check first. Four items are blocking or near-blocking:

1. **ASME B30.2 is not in the corpus** — it is cited in 9 of 12 modules and is partly incorporated by reference into 29 CFR §1926.1438(b)(2)(ii).
2. **EM 385-1-1 Chapter 16 citations are unverified**, and a 2014-edition decoy file shares the obvious filename with the cited 2024 edition.
3. **NAVFAC P-307 and the Navy Crane Center Crane Corner archive** have been flagged as blocked-to-automation since 30 July and still need a manual browser pull.
4. **The NCCCO overhead crane certification premise** underpinning the Certification Gate needs confirming before OHC-01 or OHC-12 is authored.

## Standing disciplines

Content establishes the operator's standard of care. It never confers qualification — the determination belongs to the **controlling entity** (Gate Master Rev 1.3, amendment A2) and is not delegable to a training vendor.

## Vault drop-in

`vault-dropin/` mirrors the Obsidian vault (`OneDrive - MSC Safety Solutions/Documents/Obsidian/My Second Brain/`). Files land in the matching folder:

| File | Destination |
|---|---|
| `vault-dropin/Crane Standards & Guides/OHC — 1910.179 Citation Pack (verified).md` | `📚 Resources/Crane Standards & Guides/` |
| `vault-dropin/Crane Standards & Guides/OHC — Tier 0 Deck Map.md` | `📚 Resources/Crane Standards & Guides/` |

Both carry Obsidian frontmatter and `[[wikilinks]]` matching the existing index convention. After dropping them in, add two lines to `_Crane Standards — Index.md` so they are reachable from the index.

This is the remote-run delivery path described in the vault's own `CLAUDE.md` — the Microsoft 365 connector available to this session has read access to the vault but not `Files.ReadWrite.All`, so it cannot write directly.
