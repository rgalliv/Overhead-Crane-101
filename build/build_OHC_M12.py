#!/usr/bin/env python3
"""OHC-12 Capstone: Qualification Readiness and Documentation -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M12"
MODLABEL = "Module 12"
TITLE = "Capstone: Qualification Readiness and Documentation"
SUBTITLE = ("Demonstrate integrated performance and complete the documentation architecture "
            "for the Designation Gate.")

OBJECTIVES = [
    "Execute complete lift assignments that integrate every prior competency, and detect "
    "injected faults without being prompted.",
    "Produce and maintain the records that evidence competency and equipment status, in the "
    "form the standard actually specifies.",
    "State which gate applies to your work, what your designation covers, and what programme "
    "completion does and does not give you.",
]

SECTIONS = [
    ("A", "Integrated Scenario Performance",
     "Execute complete lift assignments integrating all prior competencies."),
    ("B", "Documentation and Records",
     "Produce and maintain the records that evidence competency and equipment status."),
    ("C", "Designation Gate and Certification Routing",
     "Complete the gate architecture appropriate to the operating branch."),
]

CONTENT = {
    "A": [
        ("The full cycle, in order, every time",
         "Six phases, and none of them is optional: <b>jurisdiction confirmation</b> (which "
         "branch, which rulebook), <b>inspection</b>, <b>planning</b>, <b>communication</b>, "
         "<b>execution</b>, <b>securing</b>. OHC-01 through OHC-08 each taught one piece; the "
         "capstone is the first time you run all six as one thing.",
         "The order matters because each phase produces something the next one needs. "
         "Jurisdiction tells you which inspection regime applies. Inspection tells you whether "
         "there is a crane to plan with. Planning tells the crew what to communicate about."),
        ("Jurisdiction first, because it changes the rules",
         "The single most common structural error in crane training is teaching one rulebook. "
         "The same overhead crane, doing the same lift, is governed differently depending on "
         "whether it is <b>permanently installed</b> (&sect;1926.1438(a) &#8212; all of "
         "&sect;1910.179) or <b>not</b> (&sect;1926.1438(b) &#8212; an enumerated subset plus "
         "Subpart CC).",
         "You have now met both faces of this. Inspection intervals and maintenance rules are "
         "<b>facility branch</b> (OHC-05). The signals regime is <b>construction branch</b> "
         "(OHC-09). Load handling binds on <b>both</b> (OHC-07). Confirming the branch is the "
         "first phase because it silently selects everything after it."),
        ("Scenario variation is the point, not the padding",
         "Assessment runs across the <b>control modes and load types on your assigned "
         "equipment</b> &#8212; pendant, cab, radio; compact and awkward loads; open floor and "
         "congested placement. A single scenario tests one habit. Variation tests "
         "<b>competence</b>.",
         "This is also how mode-specific habit transfer gets caught, which is the failure "
         "OHC-03 warned about: the cab operator's spatial reference, applied from the floor, "
         "puts the load the wrong way."),
        ("Faults are injected, and nobody will point at them",
         "Scenarios carry embedded faults and hazards, and <b>detection is expected without "
         "prompting</b>. An evaluator who has to ask <i>&#8220;did you notice anything about "
         "the hook?&#8221;</i> has already recorded the answer.",
         "This is deliberately harder than a checklist, because the real failure mode is an "
         "operator who completes every checklist item and walks past the defect between them."),
        ("What a critical error is",
         "Performance is graded on <b>tolerances</b>, <b>sequence discipline</b>, and a "
         "<b>zero critical-error requirement</b>. Tolerances and sequence can carry minor "
         "deductions. A critical error cannot.",
         "A critical error is one that would have injured somebody or wrecked equipment if the "
         "scenario had been real &#8212; a load over a person, a defect operated through, a "
         "brake left unproven, a placement into live equipment. There is no partial credit on "
         "those, and that is the same standard the 100&#37; knowledge gate applies."),
        ("Consistency is the actual assessment",
         "`A.K5` is the element that makes this a standard of care rather than an exam: the "
         "standard is demonstrated as <b>consistent behaviour, not test-day behaviour</b>. "
         "Performance is sustained <b>across consecutive scenarios</b>, which is how the "
         "difference shows up.",
         "Anybody can run one clean lift while being watched. The question the capstone asks "
         "is what you do on the fourth one, when the evaluator has stopped writing and the "
         "shortcut is available."),
        ("Time pressure is the test condition, not an excuse",
         "Sequence shortcuts under pressure are the most common capstone failure, and the "
         "reason is that pressure is <b>always</b> present in real work. A sequence that only "
         "survives an unhurried shift is not a sequence you have.",
         "The counter is that the sequence is short and fixed. Slack, load, prove the brake. "
         "Confirm balance. Sound the warning. There is no version of a working day that does "
         "not have room for it."),
    ],
    "B": [
        ("Records are the evidentiary layer",
         "`B.K4` is the framing element and it is worth stating plainly: the standard of care "
         "is a <b>behaviour</b>, but in any audit, investigation or dispute it is only visible "
         "through <b>records</b>. An inspection that happened and was not recorded is, "
         "evidentially, an inspection that did not happen.",
         "That is not a reason to write fiction. It is a reason to record what you actually "
         "did, at the time you did it."),
        ("The record the standard actually specifies",
         "For hooks (j)(2)(iii), chains (j)(2)(iv) and ropes (m)(1), the certification record "
         "is not free-form. It carries three named fields: <b>the date of the inspection</b>, "
         "<b>the signature of the person who performed it</b>, and <b>the serial number or "
         "other identifier of the item inspected</b>.",
         "That third field is the one facility logs most often omit, and it is the one that "
         "makes the record mean anything later. A dated tick with no item identifier proves "
         "somebody looked at something."),
        ("Where the records live",
         "&sect;1910.179(m)(1) requires the rope certification record be <b>kept on file where "
         "readily available to appointed personnel</b>. &sect;1910.179(k)(2) requires rated "
         "load test reports to be <b>on file where readily available to appointed "
         "personnel</b>.",
         "&#8220;Readily available&#8221; is a real requirement, not a formality. A record in "
         "a system nobody can reach on the day of an incident is not on file in any useful "
         "sense. Knowing <b>where</b> is part of the competency."),
        ("Equipment status records",
         "Three documents move a crane through a defect: the <b>deficiency report</b> that "
         "raises it, the <b>removal-from-service tag</b> that controls the equipment, and the "
         "<b>return-to-service verification</b> that releases it.",
         "The standard specifies the middle one in detail &#8212; &sect;1910.179(l)(2)(i) puts "
         "signs on the crane <b>and</b> on the floor beneath or on the hook where visible from "
         "the floor. And it specifies the third: <b>(l)(2)(ii)</b>, guards reinstalled, safety "
         "devices reactivated, maintenance equipment removed; <b>(l)(3)(i)</b>, unsafe "
         "conditions corrected before operation resumes."),
        ("Training and evaluation records",
         "Your personal record package supports somebody else's decision: the "
         "<b>employer's</b> qualification determination. It needs to show what you were "
         "trained on, what you were evaluated on, by whom, when, and on what equipment.",
         "Scope is the part people under-record. <i>&#8220;Overhead crane training&#8221;</i> "
         "is not a scope. <i>&#8220;Pendant and radio, 5-ton and 10-ton single-girder, Bay 3 "
         "and Bay 4&#8221;</i> is."),
        ("Retention and audit readiness",
         "Retention periods come from the facility programme and, for some records, from the "
         "regulation's own filing requirements. Audit readiness is simpler than it sounds: "
         "could you produce the last twelve months of your own records today, without help?",
         "If the answer is no, the records exist but the evidentiary layer does not."),
        ("Records written afterwards",
         "A record completed at the end of the week for four earlier shifts is a reconstruction, "
         "and reconstructions are systematically wrong in a specific direction &#8212; they "
         "record what should have happened.",
         "This is also the failure mode that produces the worst outcome in an investigation, "
         "because a record that is provably retrospective damages the credibility of every "
         "other record beside it."),
    ],
    "C": [
        ("The Designation Gate, and its citation",
         "&sect;1910.179(b)(8): <i><b>&#8220;Only designated personnel shall be permitted to "
         "operate a crane covered by this section.&#8221;</b></i> That single sentence is the "
         "Designation Gate.",
         "Note what it does <b>not</b> say. It does not require a certificate, a card, or a "
         "third party. It requires that the <b>employer designate</b> &#8212; and the employer "
         "therefore remains <b>the qualified person</b> making that determination. The same "
         "term scopes a second role at <b>(l)(3)(i)</b>: adjustments and repairs only by "
         "designated personnel."),
        ("Why there has to be a second gate",
         "&sect;1910.179(b)(8) is <b>not</b> in the &sect;1926.1438(b)(2) enumeration. On the "
         "construction branch it simply does not apply &#8212; so &#8220;designated by the "
         "employer&#8221; has no legal force there.",
         "That absence is the whole reason the architecture has two gates rather than one. It "
         "is not a programme preference; it is what the incorporation list does and does not "
         "carry."),
        ("The Certification Gate, and what is verified about it",
         "On the &sect;1926.1438(b) construction branch, operator qualification comes from "
         "<b>&sect;1926.1427</b> (held from OSHA.gov). That section <b>does</b> apply: the "
         "enumeration at &sect;1926.1438(b)(2)(i) brings in <b>&sect;&sect;1926.1427 through "
         "1434</b>. &sect;1926.1427(d) requires certification by an <b>accredited crane "
         "operator testing organization</b> or a qualifying government licence. OSHA does "
         "<b>not</b> name NCCCO.",
         "NCCCO's public overview confirms a <b>CCO Overhead Crane Operator</b> certification "
         "(written + practical; cab or pendant/remote). CraneQualified routes that programme "
         "path through CCOS. That routing is administrative, not a CFR citation. Exam-item "
         "counts are not OSHA requirements and are not gated here."),
        ("Your designation has edges",
         "A designation is not a licence to operate cranes. It covers named <b>equipment</b>, "
         "named <b>control modes</b>, and named <b>environments</b>. Everything outside those "
         "names is uncovered, and operating there is outside your designation even though it "
         "is the same building and the same skill.",
         "Scope drift is quiet: a second crane arrives, a radio unit replaces a pendant, a "
         "bay is added. Nobody revokes anything &#8212; the work simply moves past the paper."),
        ("What brings you back for re-evaluation",
         "Four triggers, and only one is a calendar: <b>new equipment</b> or a new control "
         "mode, an <b>incident</b>, an <b>observed deficiency</b>, and <b>lapsed activity</b> "
         "&#8212; a long enough gap that currency is in question.",
         "The one most often ignored is the incident trigger, because re-evaluation after an "
         "event reads as blame. It is not. An incident is evidence that the operating picture "
         "changed, and re-evaluation is how the picture gets re-established."),
        ("What this programme gives you, and what it does not",
         "`C.K5` is the most important element in the track. Completing this programme "
         "establishes <b>structured preparation</b> and evidences your <b>standard of care</b>. "
         "It does <b>not</b> confer qualification.",
         "Qualification is a determination, and it belongs to the <b>controlling entity</b> "
         "&#8212; the employer &#8212; who knows the equipment, the site and the work. It is "
         "<b>not delegable to a training vendor</b>, including this one. Anybody who tells you "
         "a course made you qualified has misdescribed both the course and the law."),
        ("Canada routing at the Designation Gate",
         "If the work is Canadian, do <b>not</b> close the file with a US Certification Gate "
         "story. Complete the employer written authorization using the Canada jurisdiction "
         "pack (CSA B167 + federal/provincial overlay) and the EN/FR designation certificate.",
         "A US certification card is not sole evidence of Canadian competency. Keep PES sheets, "
         "gate records, and the signed designation together &#8212; that is the audit file.",
         "01-canada-shop.jpg", "Canadian site &#8212; same capstone evidence, local statute"),
        ("The package the safety director keeps",
         "Minimum record set: 100&#37; module gates, signed PES for skills in scope, jurisdiction "
         "determination (US branch or Canada branch), designation certificate scoped to "
         "equipment and modes, site familiarization, requalification triggers.",
         "Print <code>docs/OHC-buyer-audit-binder.md</code> and tick the checklist into the "
         "operator file."),
    ],
}

PRACTICE = [
    ("OHC.12.A.K1",
     "The full task cycle begins with:",
     ["Pre-operational inspection", "Jurisdiction confirmation", "Load weight determination",
      "The pre-lift briefing"], 1,
     "Jurisdiction selects which inspection regime and which rulebook apply, so it comes "
     "first."),
    ("OHC.12.A.K3",
     "An evaluator has to prompt you before you notice a planted defect. This is recorded as:",
     ["A pass, since you found it", "A minor deduction",
      "A detection failure -- detection is expected without prompting",
      "Not assessed"], 2,
     "The element specifies detection without prompting. The prompt is itself the result."),
    ("OHC.12.A.K4",
     "The critical-error requirement in the capstone is:",
     ["No more than one", "No more than two on non-safety items", "Zero",
      "Scaled to scenario difficulty"], 2,
     "Zero critical errors. A critical error is one that would have injured somebody or "
     "wrecked equipment had the scenario been real."),
    ("OHC.12.B.K2",
     "The certification record for a hook inspection must include:",
     ["Date only", "Date and signature", "Date, signature, and the item's serial number or "
      "other identifier", "Date and a photograph"], 2,
     "Three named fields. The item identifier is the one most often omitted and the one that "
     "makes the record mean anything later."),
    ("OHC.12.B.K5",
     "&sect;1910.179(m)(1) requires the rope certification record to be:",
     ["Retained for three years", "Kept on file where readily available to appointed "
      "personnel", "Submitted to OSHA", "Posted on the crane"], 1,
     "Readily available to appointed personnel. A record nobody can reach on the day of an "
     "incident is not usefully on file."),
    ("OHC.12.B.R2",
     "An inspection log filled in on Friday for Monday through Thursday is unreliable "
     "because a reconstruction records:",
     ["Too little detail", "What should have happened rather than what did",
      "Only the defects found", "The wrong inspector"], 1,
     "Reconstructions err in a consistent direction, and a provably retrospective record "
     "damages the credibility of every record beside it."),
    ("OHC.12.C.K1",
     "The Designation Gate rests on:",
     ["&sect;1926.1427", "&sect;1910.179(b)(8) -- only designated personnel shall be "
      "permitted to operate", "EM 385 16-8.aa(2)", "ASME B30.2 by name"], 1,
     "&sect;1910.179(b)(8). It requires employer designation -- not a certificate, and not a "
     "third party."),
    ("OHC.12.C.K2",
     "On the &sect;1926.1438(b) construction branch, operator qualification comes from:",
     ["&sect;1910.179(b)(8)", "&sect;1926.1427", "&sect;1926.1412", "EM 385 &sect;16.B.06"],
     1,
     "&sect;1926.1427, which applies via the &sect;1926.1438(b)(2)(i) enumeration of "
     "&sect;&sect;1926.1427 through 1434."),
    ("OHC.12.C.K5",
     "Completing this programme confers qualification.",
     ["True", "False"], 1,
     "It establishes structured preparation and evidences the standard of care. Qualification "
     "is the controlling entity's determination and is not delegable to a training vendor."),
]

GATE = [
    # ---- Task A
    ("OHC.12.A.K1",
     "The six phases of the full task cycle are jurisdiction confirmation, inspection, "
     "planning, communication, execution and:",
     ["Documentation", "Securing", "Debriefing", "Handover"], 1, ""),
    ("OHC.12.A.K1b",
     "Jurisdiction confirmation comes first in the cycle because it:",
     ["Is the quickest step", "Silently selects which rulebook and which inspection regime "
      "apply to everything after it", "Is required by the lift plan template",
      "Determines the load weight"], 1, ""),
    ("OHC.12.A.K2",
     "Scenario variation across control modes exists in order to:",
     ["Extend the assessment time", "Test competence rather than a single habit, and expose "
      "mode-specific habit transfer", "Satisfy the record requirement",
      "Cover every crane in the facility"], 1, ""),
    ("OHC.12.A.K3",
     "Embedded faults in capstone scenarios are:",
     ["Pointed out by the evaluator before the run",
      "Expected to be detected without prompting", "Disclosed in the briefing",
      "Assessed only on the final scenario"], 1, ""),
    ("OHC.12.A.K4",
     "Which of these is a critical error rather than a tolerance deduction?",
     ["Placing a load 3 inches outside the marked target",
      "Operating a crane through a known defect", "Taking longer than the target time",
      "Sounding the warning twice"], 1, ""),
    ("OHC.12.A.K5",
     "The standard of care is demonstrated as:",
     ["Test-day performance to a checklist", "Consistent behaviour sustained across "
      "consecutive scenarios", "A single flawless scenario",
      "Completion of all knowledge gates"], 1, ""),
    ("OHC.12.A.R1",
     "An operator completes every checklist item and walks past a defect between them. This "
     "is:",
     ["An acceptable pass", "Checklist performance without hazard recognition",
      "A documentation failure", "A sequence error"], 1, ""),
    ("OHC.12.A.R2",
     "Sequence shortcuts under time pressure are treated seriously because:",
     ["They save little time", "Pressure is always present in real work, so a sequence that "
      "only survives an unhurried shift is not a sequence you have",
      "They are hard to observe", "They affect tolerances"], 1, ""),
    ("OHC.12.A.R3",
     "A cab operator's spatial reference applied while operating from the floor produces:",
     ["Slower travel", "Motion in the wrong direction", "Excessive brake wear",
      "A documentation error"], 1, ""),
    # ---- Task B
    ("OHC.12.B.K1",
     "The personal training and evaluation record package exists to support:",
     ["The training vendor's certificate", "The employer's qualification determination",
      "The OSHA inspection file", "The crane's inspection history"], 1, ""),
    ("OHC.12.B.K2",
     "The three fields a certification record must carry are:",
     ["Date, location, load weight",
      "Date, signature of the person who performed the inspection, and the serial number or "
      "other identifier of the item", "Date, signature, and the next due date",
      "Inspector name, crane number, and shift"], 1, ""),
    ("OHC.12.B.K2b",
     "Which field is most often omitted from facility inspection logs, and most needed later?",
     ["The date", "The signature", "The item's serial number or other identifier",
      "The weather conditions"], 2, ""),
    ("OHC.12.B.K3",
     "The three documents that move a crane through a defect are the deficiency report, the "
     "removal-from-service tag, and:",
     ["The periodic inspection record", "The return-to-service verification",
      "The load test report", "The operator's designation"], 1, ""),
    ("OHC.12.B.K4",
     "Records are described as the evidentiary layer of the standard of care because:",
     ["Records are the standard of care",
      "The standard is a behaviour, but in audit or investigation it is only visible through "
      "records", "Records replace performance evaluation",
      "Records are required by the vendor"], 1, ""),
    ("OHC.12.B.K5",
     "&sect;1910.179(k)(2) requires rated load test reports to be:",
     ["Submitted to the certifying body", "On file where readily available to appointed "
      "personnel", "Posted in the cab", "Retained for five years"], 1, ""),
    ("OHC.12.B.R1",
     "An inspection that was performed thoroughly but never recorded is, evidentially:",
     ["Adequate, since it happened", "An inspection that did not happen",
      "A minor documentation gap", "Covered by the operator's statement"], 1, ""),
    ("OHC.12.B.R2",
     "Records reconstructed at the end of the week are systematically wrong because they "
     "record:",
     ["Too much detail", "What should have happened rather than what did",
      "Only the failures", "The wrong dates only"], 1, ""),
    ("OHC.12.B.R3",
     "A status record that does not travel across shifts results in:",
     ["A retention failure", "The next operator discovering the defect with a load on the "
      "hook", "An audit finding only", "A scope drift"], 1, ""),
    # ---- Task C
    ("OHC.12.C.K1",
     "&sect;1910.179(b)(8) states that only which personnel shall be permitted to operate a "
     "crane covered by the section?",
     ["Certified personnel", "Designated personnel", "Appointed personnel",
      "Qualified personnel"], 1, ""),
    ("OHC.12.C.K1b",
     "The Designation Gate does not reach the construction branch because:",
     ["Employers there cannot designate",
      "&sect;1910.179(b)(8) is not in the &sect;1926.1438(b)(2) enumeration",
      "&sect;1926.1438 prohibits designation", "It applies only to cab-operated cranes"],
     1, ""),
    ("OHC.12.C.K2",
     "&sect;1926.1427 applies to overhead cranes on the construction branch because:",
     ["It applies to all cranes without exception",
      "&sect;1926.1438(b)(2)(i) brings in &sect;&sect;1926.1427 through 1434",
      "&sect;1910.179 incorporates it", "EM 385 requires it"], 1, ""),
    ("OHC.12.C.K3",
     "A designation scope is stated in terms of:",
     ["Years of experience", "Equipment, control modes, and environments",
      "Crane capacity only", "Facility name only"], 1, ""),
    ("OHC.12.C.K4",
     "Which of these is NOT one of the four re-evaluation triggers?",
     ["New equipment or a new control mode", "An incident",
      "An observed deficiency", "A change of supervisor"], 3, ""),
    ("OHC.12.C.K5",
     "Programme completion establishes:",
     ["Qualification to operate", "Structured preparation and evidence of the standard of "
      "care", "A certification recognised by OSHA",
      "An employer designation"], 1, ""),
    ("OHC.12.C.K5b",
     "The qualification determination belongs to:",
     ["The training vendor", "The controlling entity -- the employer",
      "The certifying body", "The operator"], 1, ""),
    ("OHC.12.C.R1",
     "A radio unit replaces the pendant on your assigned crane. Your designation:",
     ["Covers it, since it is the same crane",
      "May not cover the new control mode -- scope must be checked and extended",
      "Automatically extends", "Is unaffected because capacity is unchanged"], 1, ""),
    ("OHC.12.C.R2",
     "An operator designated under &sect;1910.179(b)(8) is assigned to a non-permanently-"
     "installed crane in construction work. The problem is:",
     ["Nothing -- designation is universal", "The construction branch requires certification "
      "under &sect;1926.1427; designation has no force there",
      "The crane needs re-rating", "A second designation is needed from the same employer"],
     1, ""),
    ("OHC.12.C.R3",
     "Re-evaluation after an incident is most often skipped because:",
     ["It is not required", "It reads as blame rather than as re-establishing the operating "
      "picture", "Records are unavailable", "The operator is unavailable"], 1, ""),
    ("OHC.12.C.K6",
     "On a Canadian site, closing the Designation Gate correctly means:",
     ["Filing an NCCCO card with no employer authorization",
      "Employer written authorization aligned to CSA B167 and the applicable OH&amp;S Act, "
      "with PES and gate records attached",
      "Skipping records because hazards are the same as in the US",
      "Using only EM 385 Class I paperwork"], 1, ""),
    ("OHC.12.C.R4",
     "Using a US certification card as the sole evidence of competency on a Canadian "
     "provincial site, with no employer authorization on file, primarily risks:",
     ["Nothing &#8212; cards travel internationally",
      "An indefensible due-diligence file under Canadian OH&amp;S expectations",
      "Automatic CSA B167 exemption", "Faster hoist speeds"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.12.A.K1": ("ACS synthesis &middot; `OHC-01`&#8211;`OHC-08`", "OK"),
    "OHC.12.A.K1b": ("**&sect;1926.1438(a)** vs **(b)** &middot; `OHC.01.B`", "OK"),
    "OHC.12.A.K2": ("derived &middot; `OHC.03.C.R3`", "OK"),
    "OHC.12.A.K3": ("ACS element as written", "OK"),
    "OHC.12.A.K4": ("derived &middot; gate architecture", "OK"),
    "OHC.12.A.K5": ("Gate Master Rev 1.3 standard of care", "OK"),
    "OHC.12.A.R1": ("derived", "OK"),
    "OHC.12.A.R2": ("derived", "OK"),
    "OHC.12.A.R3": ("derived &middot; `OHC.03.C.R3`", "OK"),
    "OHC.12.B.K1": ("**&sect;1910.179(b)(8)** &middot; derived", "OK"),
    "OHC.12.B.K2": ("**&sect;1910.179(j)(2)(iii)&#8211;(iv)** &middot; **(m)(1)**", "OK"),
    "OHC.12.B.K2b": ("**&sect;1910.179(j)(2)(iii)** &middot; derived", "OK"),
    "OHC.12.B.K3": ("**&sect;1910.179(l)(2)(i), (l)(2)(ii), (l)(3)(i)**", "OK"),
    "OHC.12.B.K4": ("Gate Master Rev 1.3 &middot; derived", "OK"),
    "OHC.12.B.K5": ("**&sect;1910.179(k)(2)** &middot; **(m)(1)**", "OK"),
    "OHC.12.B.R1": ("derived", "OK"),
    "OHC.12.B.R2": ("derived", "OK"),
    "OHC.12.B.R3": ("derived &middot; `OHC.05.C.K5`", "OK"),
    "OHC.12.C.K1": ("**&sect;1910.179(b)(8)** &middot; (l)(3)(i)", "OK"),
    "OHC.12.C.K1b": ("**&sect;1926.1438(b)(2)** enumeration", "OK"),
    "OHC.12.C.K2": ("**&sect;1926.1427(a),(d)** held via **&sect;1926.1438(b)(2)(i)**; NCCCO public overview (programme path)", "OK"),
    "OHC.12.C.K3": ("derived", "OK"),
    "OHC.12.C.K4": ("ACS element as written", "OK"),
    "OHC.12.C.K5": ("Gate Master Rev 1.3, amendment A2", "OK"),
    "OHC.12.C.K5b": ("Gate Master Rev 1.3, amendment A2", "OK"),
    "OHC.12.C.R1": ("derived", "OK"),
    "OHC.12.C.R2": ("**&sect;1910.179(b)(8)** &middot; **&sect;1926.1427**", "OK"),
    "OHC.12.C.R3": ("derived", "OK"),
    "OHC.12.C.K6": ("CSA B167 &middot; Canada jurisdiction pack", "OK"),
    "OHC.12.C.R4": ("Canada jurisdiction pack &middot; due diligence", "OK"),
}

TRACE_PERF = [
    ("OHC.12.A.S1", "Complete graded integrated scenarios across assigned control modes"),
    ("OHC.12.A.S2", "Detect and respond to injected faults and hazards"),
    ("OHC.12.A.S3", "Sustain performance standards across consecutive scenarios"),
    ("OHC.12.B.S1", "Assemble a complete personal qualification record package"),
    ("OHC.12.B.S2", "Produce inspection and status documentation for a full task cycle"),
    ("OHC.12.B.S3", "Locate and interpret equipment history for an assigned crane"),
    ("OHC.12.C.S1", "State their designation scope and its boundaries accurately"),
    ("OHC.12.C.S2", "Identify the correct gate requirement for given work scenarios"),
    ("OHC.12.C.S3", "Complete all Designation Gate performance and documentation requirements"),
]

TRACE_NOTES = [
    ("&#11088; The two-gate architecture now has both citations, and they are verified",
     "The ACS asserts both gates without citing either. **Designation Gate &#8594; "
     "&sect;1910.179(b)(8)**: *&#8220;Only designated personnel shall be permitted to operate "
     "a crane covered by this section.&#8221;* It requires **employer designation** &#8212; "
     "not a certificate, not a third party &#8212; which is precisely why the employer remains "
     "the qualified person. **Certification Gate &#8594; &sect;1926.1427**, which **does** "
     "apply to overhead cranes on the construction branch: the enumeration at "
     "**&sect;1926.1438(b)(2)(i)** brings in **&sect;&sect;1926.1427 through 1434**. And the "
     "reason there must be two gates rather than one: **&sect;1910.179(b)(8) is not in that "
     "enumeration**, so employer designation has no force on the construction branch. "
     "`C.K1`, `C.K1b`, `C.K2` and `C.R2` gate the whole structure."),
    ("&#9989; `C.K2` &#8212; paragraph text held; NCCCO confirmed as a public overhead path",
     "`C.K2` gates **&sect;1926.1427** via the (b)(2)(i) enumeration. **(a)** and **(d)** "
     "were fetched from OSHA.gov 2026-08-28: trained, certified/licensed, evaluated; "
     "certification by an accredited crane operator testing organization or qualifying "
     "government licence. OSHA does **not** name NCCCO. NCCCO's public Overhead Crane "
     "Operator overview confirms that a CCO overhead programme exists (written + practical; "
     "cab or pendant/remote). Programme routing through CCOS remains administrative. "
     "Exam-item counts, fees, and handbook domains are **not** gated. Canada `C.K6`/`C.R4` "
     "are unchanged."),
    ("&#11088; `C.K5` is the ethical spine of the track and it is stated without hedging",
     "Programme completion establishes **structured preparation** and evidences the "
     "**standard of care**. It does **not** confer qualification. Qualification is a "
     "determination belonging to the **controlling entity** &#8212; the employer &#8212; and "
     "per **Gate Master Rev 1.3, amendment A2** it is **not delegable to a training vendor**, "
     "including CraneQualified. `C.K5` and `C.K5b` gate both halves separately, because "
     "learners reliably retain the first and forget the second."),
    ("&#9989; `B.K2` closes the loop opened in OHC-05",
     "The ACS describes documentation at `B.K2` as *&#8220;inspection documentation the "
     "operator generates and where it lives.&#8221;* The standard specifies both. The **three "
     "named fields** &#8212; date, signature of the person who performed it, serial number or "
     "other identifier of the item &#8212; come from **(j)(2)(iii)**, **(j)(2)(iv)** and "
     "**(m)(1)**. *Where it lives* comes from **(m)(1)** and **(k)(2)**: **on file where "
     "readily available to appointed personnel**. `B.K2b` gates the item identifier "
     "specifically, because it is the field facility logs most often omit and the only one "
     "that makes a record traceable to a component."),
    ("&#9989; The capstone's branch content is the track's own structure",
     "`A.K1b` gates jurisdiction-first because this track has now demonstrated the "
     "consequence three separate ways: inspection and maintenance are **facility branch** "
     "(OHC-05, with **&sect;&sect;1926.1412/1413** held on the other side); the signals "
     "regime is **construction branch** (OHC-09, **1419&#8211;1422 / 1428** held); load "
     "handling under paragraph **(n)** binds on **both** (OHC-07). No other single decision "
     "changes as much downstream."),
    ("&#9432; Elements carrying a second item",
     "`A.K1`, `B.K2`, `C.K1` and `C.K5` each carry two items &#8212; separating the phase list "
     "from why its order matters, the record's fields from the field that gets dropped, the "
     "gate's citation from why a second gate exists, and what completion gives you from whose "
     "decision qualification actually is."),
    ("&#11088; Canada routing closes the Designation Gate without a false NCCCO story",
     "`C.K6` / `C.R4` require employer written authorization aligned to **CSA B167** and the "
     "applicable federal/provincial OH&amp;S Act, with PES and gate records attached. A US "
     "certification card alone is not Canadian due diligence."),
]


def main():
    # Extend objectives for Canada / audit package
    objs = list(OBJECTIVES) + [
        "Route Canadian work through CSA B167 + employer authorization &#8212; not US "
        "certification paperwork &#8212; and assemble the safety-director audit package.",
    ]
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, objs,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE,
                      hero_image="01-hero-bridge.jpg",
                      extra_before_gate=[A.na_jurisdiction_tree_slide])
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, "out", "OHC_M12_Capstone.pre.html")
    with open(out, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
        f.write(html)
    print("wrote %s (%d bytes, slides %d)" % (out, len(html), A.LAST_TOTAL))

    import json
    answer_key = {}
    for i, q in enumerate(PRACTICE, 1):
        answer_key["%s_q%02d" % (MODULE, i)] = q[3]
    for i, q in enumerate(GATE, 1):
        answer_key["%s_q%02d" % (MODULE, len(PRACTICE) + i)] = q[3]
    gate_ids = ["%s_q%02d" % (MODULE, len(PRACTICE) + i) for i in range(1, len(GATE) + 1)]
    man = {
        "module": MODULE,
        "stage": "OHC",
        "gate_code": "OHC-1",
        "version": "2026.08-CA",
        "salt": "CQ1:OHC_M12_Capstone",
        "total": A.LAST_TOTAL,
        "next": "",
        "gate": gate_ids,
        "review_offset": len(PRACTICE),
        "answer_key": answer_key,
        "course": "OCO301C",
        "notes": "Canada designation routing + visual pack",
    }
    man_path = os.path.join(root, "manifests", "OHC_M12.json")
    with open(man_path, "w", encoding="utf-8") as f:
        json.dump(man, f, indent=2)
        f.write("\n")
    print("wrote %s (gate %d)" % (man_path, len(gate_ids)))


if __name__ == "__main__":
    main()
