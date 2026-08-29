---
title: EM 385-1-1 30 Nov 2014 — DECOY filename warning
type: corpus-hygiene
status: rename-instruction
created: 2026-08-28
---

# DECOY — do not cite this edition as 16-2 / 16-8.aa

The ACS and all twelve OHC modules cite **EM 385-1-1 (15 Mar 2024)**.

In the crane library, a **30 November 2014** file is stored under the obvious name `EM_385-1-1.pdf` (present in both crane folders). That edition numbers Chapter 16 as **letter** subsections (16.A–16.S; **M** Overhead and Gantry). The citations **16-2** and **16-8.aa(2)–(7) do not exist in it**.

The cited 2024 file lives separately as `EM 385-1-1 _EFFECTIVE 15 March 2024.pdf`.

## Rename (vault / Drive — this git repo does not hold the PDF)

Rename the 2014 file **immediately** so a builder cannot grab it by the generic name:

```
EM_385-1-1.pdf
  →  EM_385-1-1_30Nov2014_DECOY.pdf
```

Leave the 2024 file's name unchanged. After rename, the only file a search for `EM_385-1-1.pdf` can hit is a miss — the builder must pick the 2024 filename explicitly.

OHC-09 still cites some **2014** §16.G.05 / §16.B.06 numbers because those paragraphs were read from a 2014 extract and the 2024 Chapter 16 body has not been re-read. Those items are marked *2014 text* in the trace table. They are **not** a reason to keep the decoy filename.
