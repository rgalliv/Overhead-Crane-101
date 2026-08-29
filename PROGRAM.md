# OCO301C — In-house corporate training program

CraneQualified / CCOS content, delivered as **instructor-led in-house training** for a manufacturing plant. This is not a self-paced self-enroll course.

**This repo is training + the knowledge test.** Roster, attendance, practical evaluation, designation certificates, and audit binders live in **the company's tracking system** (built separately). Do not look for them here.

---

## Delivery model

| | How it runs |
|---|---|
| Who presents | A plant instructor (leadman, safety trainer, or designated evaluator). |
| Who takes the test | Each operator. Completing slides is not enough. |
| Knowledge test | The existing **100% gate** at the end of each module (`OHC-1`). Instructor presents, then operators take the Final Knowledge Check. Missed gate items do not reveal the answer. |
| Pace | Instructor-controlled. Run **OHC-01 → OHC-12** in order. Do not send operators ahead as if this were a MOOC. The module handshake is unchanged; the instructor decides when the next module starts. |
| Practical / designation | Out of scope here. Skills (S-elements) and employer designation stay in the company's system. |

White-label: any manufacturing company. Do not hard-code a plant name. CraneQualified / CCOS remains the content author in the footer.

---

## Plant default vs other customer

**Facility path is first-class** for this in-house program:

- 29 CFR **1910.179** (overhead and gantry cranes)
- **ANSI B30.2.0-1967** as incorporated at §1910.179(b)(2) (facility IBR — not B30.2-2016)
- 29 CFR **1910.184** (slings)
- 29 CFR **1910.147** (control of hazardous energy / LOTO)
- Designated operator: §1910.179(b)(8)

**Still in the ACS, labeled as the other customer — not this plant's default:**

- Construction branch **§1926.1438** and Certification Gate **§1926.1427**
- Federal / USACE **EM 385-1-1 Chapter 16**

**Canada** (CSA B167 + provincial OH&S) is an **overlay** on OHC-01 Task D and OHC-12 routing, not a fork. Skip or skim the overlay if the cohort is US-facility only.

Do not fabricate OSHA or ASME numbers. Do not scrape NCCCO exam items.

---

## How to run a first in-house session

1. Open `index.html` (program hub) and `instructor/index.html` (run-of-show).
2. Start at **OHC-01**. Open the instructor script, then the gated module.
3. Present the talk track. Use practice questions as teaching checks.
4. Run the **knowledge gate**. 100% required. Retest on misses without reading answers.
5. Instructor releases **OHC-02**. Repeat through **OHC-12**.
6. **OHC-07 (load handling)** is the session that must not be waved through — full talk track, then the gate. Side pulls are conditional under §1910.179(n)(3)(iv), not a flat ban.
7. Record who passed in the company's system. This program does not store people.

Suggested classroom times are on each script. They are **plant pacing**, not regulatory durations.

Rebuild scripts after a module rebuild: `python3 build/gen_instructor.py`

---

## What stayed the same

- Twelve gated HTML modules in `out/`
- `OHC_M01 → … → OHC_M12` completion handshake
- Manifests, salts, FNV gate engine
- Canada overlay files (not a second track)
