# OHC ACS — Vestas amendment (Mexico branch · lift planning · tandem load share)

**Client:** Vestas
**Equipment scope:** factory / workshop bridge cranes · port / staging / logistics cranes
**Regulatory spine:** US OSHA + ASME (primary) · **Mexico STPS branch**
**Curriculum:** combined OHC + Stage 2 rigging and lift planning — see `docs/OHC-Vestas-curriculum-map.md`

Append to `OHC-ACS-build-spec.md` census after owner review. Codes are provisional under the same Gate Master rule as the US track and the Canada amendment.

**Scope note.** Nacelle davit cranes and tower internal service hoists are **out of scope** by client decision. Nothing in this amendment addresses turbine-mounted lifting equipment; if that scope returns it needs its own ACS task, not an overlay on these elements.

---

## Gap analysis — what the existing ACS already covers

Written before authoring, so the amendment adds only what is genuinely absent. Three claimed gaps turned out to be two.

| Vestas requirement | Existing ACS coverage | Verdict |
|---|---|---|
| Outdoor port / staging exposure — wind, storm securing, ice | **`OHC.10.B.K1–K5`, `B.R1–R3`, `B.S1–S3`** — outdoor gantry and bridge wind thresholds, storm procedures, temperature, precipitation/ice load change, weather suspension criteria, large-surface-area gust risk | **Already covered. No new elements.** |
| Multi-crane bay traffic, shared runways | **`OHC.08.B`** (5K/3R/3S), `OHC.07.B.K4/K5`, `OHC.07.B.S3` | **Already covered** — but see below, this is *traffic*, not *shared load* |
| Below-the-hook devices (spreader beams, lifting beams, C-hooks) | **`OHC.06.B`** (ASME B30.20 by name), `OHC.04.A.K5`, `OHC.04.B.K4` | Covered for the operator interface role. Depth lives in **Stage 2 M21 (BTH-1)** |
| **Tandem / synchronized shared-load picks** | `OHC.04.C.R3` names *"multiple-hoist picks without engineered load share"* as a **Risk only.** No Knowledge element anywhere teaches how load share is established, verified or executed | **REAL GAP → OHC-07 Task D** |
| **Engineered lift planning / rigging plan** | `OHC.04.B.K5` — one element, *"Standard lift planning discipline (ASME P30.1 by name)"* | **THIN → OHC-04 Task D** |
| **Mexico jurisdiction** | Absent entirely. US + Canada only | **ABSENT → OHC-01 Task E** |

**The load-share distinction is the substantive finding.** `OHC-08 Task B` is about cranes sharing a *runway* — clearance, right-of-way, parking priority, bumper contact. It is not about two cranes sharing a *load*. For Vestas factory and port work — tower sections, nacelle assemblies, blade handling — tandem picks are routine, and the ACS currently gates the risk of doing them badly without ever teaching how to do them correctly. That is the gap this amendment closes.

---

### OHC-01 Task E — Mexican Jurisdictional Framework

**Objective.** Determine that Mexican federal labour law governs the crane, name the applicable NOM spine, and route the operator through DC-3 **plus** employer authorization.

**References:** NOM-006-STPS-2023 (by name) · NOM-004-STPS-1999 (by name) · Ley Federal del Trabajo Arts. 153-A / 153-T / 153-V · RFSST (by name, edition unconfirmed) · supporting NOMs per `docs/OHC-Mexico-jurisdiction-pack.md`

#### Knowledge

- `OHC.01.E.K1` Mexican OH&S is **federal**: Ley Federal del Trabajo + RFSST + STPS Normas Oficiales Mexicanas. There is no state-level OH&S code equivalent to a Canadian province or a US state plan
- `OHC.01.E.K2` **NOM-006-STPS-2023** — *Almacenamiento y manejo de materiales mediante el uso de maquinaria* — as the primary lifting-machinery duty standard; DOF 7 Mar 2024, in force 3 Sep 2024
- `OHC.01.E.K3` **NOM-006-STPS-2014 is derogated.** The 2023 edition narrowed scope to handling *by machinery*; material still citing 2014 is citing a dead standard
- `OHC.01.E.K4` Mexican authorization model: trained and employer-authorized worker, evidenced by **DC-3** (*Constancia de Competencias o de Habilidades Laborales*) under LFT Arts. 153-T / 153-V, authenticated by the *Comisión Mixta* above 50 workers or by the *patrón* at 50 or fewer
- `OHC.01.E.K5` Supporting NOM overlay: NOM-004 (machine safeguarding), NOM-029 (electrical maintenance), NOM-026 (colours and signs), NOM-017 (PPE), NOM-009 (work at height)

#### Risk Management

- `OHC.01.E.R1` Applying US OSHA / NCCCO routing — or Canadian provincial routing — to a Mexican work centre and treating it as compliance
- `OHC.01.E.R2` Searching for a state-level OH&S standard that does not exist, and defaulting to no standard when none is found
- `OHC.01.E.R3` **Treating the DC-3 as an operating authorization.** A DC-3 does not expire, is not equipment-scoped, and carries no requalification trigger. It evidences training completed — not authorization to operate a specific crane

#### Skills

- `OHC.01.E.S1` Select the Mexico branch correctly and name the governing NOM for an assigned crane
- `OHC.01.E.S2` State that NOM-006-STPS-2023 supersedes the 2014 edition and identify a stale citation in a supplied document
- `OHC.01.E.S3` Produce or request **both** the DC-3 and the dated employer authorization naming equipment and control modes

**Census delta (OHC-01):** +5 K · +3 R · +3 S = **+11**

---

### OHC-04 Task D — Engineered Lift Planning and the Rigging Plan

**Objective.** Produce, read and apply a written lift plan, and know when one is mandatory rather than discretionary.

**References:** ASME P30.1 (by name only) · 29 CFR 1910.179 · EM 385-1-1 (15 Mar 2024) para 16-2 · Vestas internal lifting procedure *(not yet supplied — see Open items)*

Expands `OHC.04.B.K5`, which currently carries the entire lift-planning load as a single element.

#### Knowledge

- `OHC.04.D.K1` Lift classification: ordinary / standard versus **critical or engineered**, and the facility triggers that force the higher class — percentage of rated capacity, tandem picks, high-value or long-lead loads, personnel exposure, blind placements
- `OHC.04.D.K2` Required contents of a written lift plan: load weight and source of that weight, centre of gravity, rigging selection and capacity, hook and device weights, crane and configuration, path, exclusion zones, roles, communication method, stop-work authority
- `OHC.04.D.K3` **The rigging plan as a component of the lift plan**, not a separate document — sling type, hitch, angle, tension per leg, D/d, hardware ratings, and below-the-hook device weight all resolve into the total lifted load
- `OHC.04.D.K4` Total lifted load assembled completely: load + rigging + below-the-hook device + any entrained material, verified against **rated capacity at the governing configuration**
- `OHC.04.D.K5` Plan currency and revision: the plan is valid for the configuration it was written for; changed load, rigging, path or crane invalidates it

#### Risk Management

- `OHC.04.D.R1` Load weight taken from a drawing, a nameplate or a memory rather than a verified source, then carried through every downstream calculation
- `OHC.04.D.R2` Rigging plan omitted or assumed, so sling angle and device weight never reach the capacity check
- `OHC.04.D.R3` Executing a plan written for a different configuration, load or crane because "it is the same pick"

#### Skills

- `OHC.04.D.S1` Assemble a total lifted load from load, rigging, and below-the-hook device and check it against rated capacity
- `OHC.04.D.S2` Complete a written lift plan including the rigging plan for an assigned facility lift
- `OHC.04.D.S3` Identify a supplied lift plan as invalid for the presented configuration and state why

**Census delta (OHC-04):** +5 K · +3 R · +3 S = **+11**

---

### OHC-07 Task D — Tandem and Synchronized Multi-Crane Load Handling

**Objective.** Execute a shared-load pick with two or more hoists or cranes under an engineered load share, with defined single-point control.

**References:** ASME P30.1 (by name only) · ASME B30.2 / B30.17 (by name only) · 29 CFR 1910.179 · EM 385-1-1 (15 Mar 2024) para 16-8.aa

Closes the gap `OHC.04.C.R3` currently names as a risk without teaching. **Distinct from `OHC-08 Task B`**, which governs cranes sharing a runway rather than a load.

#### Knowledge

- `OHC.07.D.K1` Tandem lift defined: one load, two or more hoists or cranes, **load share engineered in advance** — never established by feel during the lift
- `OHC.07.D.K2` Load share determination: centre of gravity position sets the proportion each crane carries; share shifts as the load rotates, tilts or is set down unevenly
- `OHC.07.D.K3` **Derating**: each crane's usable capacity is reduced below its rating for tandem service per the facility or engineered plan, because dynamic and share-shift effects load one crane beyond its nominal proportion
- `OHC.07.D.K4` **Single-point control**: one lift director, one signaler, one command stream. Both operators respond to the same voice; either may stop
- `OHC.07.D.K5` Synchronization discipline: matched hoist speed, hoisting only on command, avoiding differential lift that transfers share and induces side pull on the trailing crane
- `OHC.07.D.K6` *(second item on K2 — independently testable)* Share verification at low height before committing to full lift: read load indication or observe rope angle on both cranes, confirm against plan

#### Risk Management

- `OHC.07.D.R1` Load share assumed from geometry alone without verification at low height, so an overloaded crane is discovered at full height
- `OHC.07.D.R2` Two operators taking independent commands from two signalers, or self-directing "to keep it level"
- `OHC.07.D.R3` Differential hoisting transferring share onto one crane and inducing side pull — the failure mode `OHC.07.A.K3` prohibits, arriving through a route the single-crane rule does not cover

#### Skills

- `OHC.07.D.S1` Execute a tandem pick under an engineered plan with a single lift director
- `OHC.07.D.S2` Verify load share at low height against plan and stop if it does not match
- `OHC.07.D.S3` Demonstrate synchronized hoist and travel with a second operator, maintaining level and share

**Census delta (OHC-07):** +5 K · +3 R · +3 S = **+11** (K6 is a second item on the K2 element and does not change the census — same convention as the `*b` items in the US track)

---

### OHC-12 Task C — Mexico routing additions

- `OHC.12.C.K7` *(net-new)* On Mexican work centres, complete the Designation Gate with **both** the DC-3 and a dated, equipment-scoped employer authorization; do not route to §1926.1427 / NCCCO or to a provincial Canadian pack unless the work is actually in that jurisdiction
- `OHC.12.C.R5` *(net-new)* Presenting a non-expiring DC-3 as current competency evidence with no employer authorization and no requalification trigger
- `OHC.12.C.S4` *(net-new)* Assemble a Mexico-branch qualification package: DC-3, employer authorization, PES records, and equipment scope statement

**Census delta (OHC-12):** +1 K · +1 R · +1 S = **+3**

---

## Census

| Layer | Elements |
|---|---:|
| US track | 400 |
| Canada overlay (OHC-01 Task D; OHC-12 `C.K6`/`C.R4`) | 413 |
| **+ OHC-01 Task E** (Mexico) | 424 |
| **+ OHC-04 Task D** (lift planning) | 435 |
| **+ OHC-07 Task D** (tandem load share) | 446 |
| **+ OHC-12 Task C** (DC-3 routing) | **449** |

**Gate items.** New K and R elements are gateable: 8 + 8 + 8 + 2 = **+26**, taking the track from 347 to **373**.
**PES lines.** New S elements: 3 + 3 + 3 + 1 = **+10**, taking S from 111 to **121**.

**Modules requiring rebuild: OHC-01, OHC-04, OHC-07, OHC-12.** OHC-02, -03, -05, -06, -08, -09, -10, -11 are unchanged by this amendment.

---

## Build notes

Per `docs/OHC-build-format-spec.md` and the module-builder contract:

- Author question data into `build/build_OHC_M01.py`, `M04`, `M07`, `M12`; regenerate `.pre.html`; run `build/retrofit.py` for FNV-1a hashes and the gate engine.
- Keep each module's **salt stable** — these are rebuilds, not new modules. Do not regenerate salts in `manifests/OHC_M01.json`, `M04`, `M07`, `M12`.
- Regenerate trace tables with `python3 build/gen_trace.py 01 04 07 12`.
- Re-run behavioural verification and re-audit to 0 gaps before shipping. A rebuild that has not passed `verify_module.cjs` is not done.
- Narration: modules carry versioned narration. **Never restore audio across a script revision** — new elements mean new narration for the affected slides, not reused clips.
- OHC-01 is already the largest module (891 KB) carrying Tasks A–D plus the interactive jurisdiction tree. Adding Task E pushes it further; watch the 15 MB ceiling and consider whether the Mexico branch renders into the existing tree rather than a second tree.

---

## Sourcing discipline

**No clause-numbered Mexican gate items.** NOM full text is not held — `stps.gob.mx`, `dof.gob.mx` and `platiica.economia.gob.mx` are all egress-blocked. Every Task E item above gates on **names, titles, dates, structure and routing logic**, all of which are search-verified, and none on clause numbers. This is the CSA B167 rule from the Canada amendment applied unchanged.

What **is** verified and therefore gateable:
- NOM-006-STPS-2023 title, DOF publication 7 Mar 2024, in force 3 Sep 2024, derogation of the 2014 edition
- DC-3 statutory basis (LFT 153-A / 153-T / 153-V), authentication thresholds (Art. 24 §II, Normative Agreement DOF 14 Jun 2013), contents, and non-expiry
- Titles and currency of the supporting NOMs listed in the jurisdiction pack

## Open items

1. **NOM-006-STPS-2023 clause text** — hold into `vault-dropin/held-nom/` before any clause-numbered item is authored.
2. **RFSST edition** — unverified; cite by name only until confirmed.
3. **Vestas internal lifting procedures** — not supplied. Where a Vestas procedure exceeds NOM or OSHA it governs as the higher duty, and `OHC.04.D` should cite it directly once held.
4. **Tandem derating factor** — `OHC.07.D.K3` teaches derating as a principle. The specific factor is a facility or engineering decision; do not gate a number until Vestas supplies theirs.
5. **Spanish designation certificate** — `forms/designation/` carries EN + FR. ES is required for this branch.
