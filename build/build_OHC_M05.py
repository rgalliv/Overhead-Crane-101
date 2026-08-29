#!/usr/bin/env python3
"""OHC-05 Inspection Regime -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M05"
MODLABEL = "Module 5"
TITLE = "Inspection Regime"
SUBTITLE = ("Execute the operator-level inspection, recognise removal-from-service "
            "conditions, and feed the periodic programme.")

OBJECTIVES = [
    "Perform and document the daily and frequent inspection scope for the assigned crane, "
    "including the correct limit-switch verification technique.",
    "State what the periodic inspection covers, who performs it, and what the operator owes "
    "it -- including idle, standby and post-repair return to service.",
    "Remove a defective crane from service, control it against use, and hand its status "
    "across a shift without information loss.",
]

SECTIONS = [
    ("A", "Pre-Operational and Frequent Inspection",
     "Perform the daily and frequent inspection scope for the assigned crane."),
    ("B", "Periodic Inspection Interface",
     "Describe the periodic inspection programme and the operator's interface with it."),
    ("C", "Deficiency Response and Removal from Service",
     "Remove defective equipment from service and control it against use."),
]

CONTENT = {
    "A": [
        ("Two regimes, two clocks",
         "&sect;1910.179(j)(1)(ii) splits inspection into two intervals and names them. "
         "<b>Frequent</b> is daily to monthly. <b>Periodic</b> is one to twelve months. "
         "Everything in this module sits in one of those two boxes.",
         "The operator owns the frequent end. The periodic end belongs to a designated "
         "person &#8212; but it runs on what the operator reports."),
        ("The daily scope",
         "Four things are inspected <b>daily</b> under (j)(2): all functional operating "
         "mechanisms for maladjustment interfering with proper operation; deterioration or "
         "leakage in air or hydraulic systems; <b>hooks</b> for deformation or cracks; and "
         "<b>hoist chains</b> for wear, twisted links, distorted links and stretch.",
         "Hooks and chains carry a second obligation: a <b>monthly inspection with a "
         "certification record</b>. Daily is visual. Monthly is documented."),
        ("The certification record has three fields",
         "For hooks (j)(2)(iii), chains (j)(2)(iv) and ropes (m)(1), the record is not "
         "free-form. It must carry <b>the date of the inspection, the signature of the "
         "person who performed it, and the serial number or other identifier of the item "
         "inspected</b>.",
         "An inspection log with a date and a tick, and no identifier for the hook, does not "
         "satisfy the standard. The item has to be identifiable later."),
        ("Function checks: every motion, every brake",
         "Run each motion &#8212; hoist, trolley, bridge &#8212; in both directions. Prove "
         "each brake holds. Prove the warning device sounds. Prove the emergency stop stops. "
         "A crane that moves is not a crane that has been checked.",
         "&sect;1910.179(n)(3)(vii) requires the brakes to be tested by lifting the load a "
         "few inches and applying the brakes whenever the load approaches rated capacity."),
        ("The limit switch is a test device, not a control",
         "&sect;1910.179(n)(4)(i) requires the upper limit switch of each hoist to be tried "
         "out <b>at the beginning of each shift, under no load</b>. Take it up slowly, or "
         "inch it at slow speed into the limit.",
         "(n)(4)(ii) then says it plainly: the limit switch <b>shall not be used as an "
         "operating control</b>. Something that stops the hoist every shift by design is a "
         "device that is wearing out on purpose."),
        ("Hooks: two figures, one rule for choosing",
         "OSHA (j)(2)(iii) removes a hook at <b>more than 15&#37; in excess of normal throat "
         "opening</b>, more than <b>10&#176; twist</b> from the plane of the unbent hook, or "
         "any crack. <b>ASME B30.10 is stricter</b> &#8212; 5&#37;, not to exceed &#188; in, "
         "plus any visible bend or twist.",
         "The rule for choosing, from the DOE Hanford manual's <i>Inconsistent Standards</i> "
         "discussion: <b>follow ASME on the criteria, follow OSHA on the records.</b> ASME "
         "sets the tighter number; OSHA is what requires the monthly documented inspection."),
    ],
    "B": [
        ("Whose inspection it is",
         "The periodic inspection is a <b>designated person</b> function. It is not "
         "something an operator performs, signs, or substitutes for. What the operator owes "
         "it is observations &#8212; the things noticed at the frequent interval that a "
         "quarterly walk-down would never see.",
         "&sect;1910.179 also uses a second term the ACS does not: <b>appointed person</b>, "
         "at (j)(4), (k)(2), (m)(1), (m)(2) and (n)(4)(i). Designated operates. Appointed "
         "approves and receives records."),
        ("What periodic actually covers",
         "(j)(3) names the scope: deformed, cracked or corroded members; loose bolts or "
         "rivets; cracked or worn sheaves and drums; worn, cracked or distorted pins, "
         "bearings, shafts, gears, rollers, locking and clamping devices; excessive wear on "
         "brake parts, linings, pawls and ratchets.",
         "It also covers load, wind and other indicators <b>over their full range</b>, "
         "powerplants, chain drive sprockets and chain stretch, and <b>electrical apparatus "
         "for pitting or deterioration of controller contactors, limit switches and "
         "pushbutton stations</b>."),
        ("Idle and standby cranes",
         "(j)(4) sets three cases. A crane <b>idle one to six months</b> gets the frequent "
         "(j)(2) inspection plus the (m)(2) rope inspection before return to service. A "
         "crane <b>idle over six months</b> gets a complete (j)(2) <i>and</i> (j)(3) "
         "inspection, plus (m)(2).",
         "<b>Standby</b> cranes &#8212; not idle, just not in regular use &#8212; get (j)(2) "
         "and (m)(2) <b>at least semi-annually</b>."),
        ("Rope has its own clock",
         "(m)(1) requires <b>a thorough inspection of all running ropes at least once a "
         "month</b>, with a certification record kept on file where readily available to "
         "appointed personnel.",
         "(m)(2): a rope that has been idle a month or more gets a thorough inspection "
         "<b>before use, by an appointed person whose approval is required</b>."),
        ("After a repair, before use",
         "(l)(2)(ii) is the return-to-service rule and it is three conditions, all of them: "
         "the crane is not operated until <b>all guards are reinstalled</b>, <b>safety "
         "devices are reactivated</b>, and <b>maintenance equipment is removed</b>.",
         "A reactivated crane with a bypassed limit switch and a jumper still fitted is the "
         "classic post-maintenance incident. Two of the three conditions were met."),
        ("The construction branch is a different authority",
         "&sect;1910.179(j), (l) and (m) are <b>not</b> in the &sect;1926.1438(b)(2) list. "
         "On a crane that is not permanently installed and is used in construction, the "
         "inspection duty comes from <b>&sect;1926.1412</b> and wire rope from "
         "<b>&sect;1926.1413</b> (both held from OSHA.gov).",
         "<b>&sect;1926.1412(d)(1)</b>: a competent person must <b>begin a visual inspection "
         "prior to each shift</b> the equipment will be used. <b>(e)(1)</b> monthly repeats "
         "the shift scope. <b>(f)(2)</b> at least every 12 months, a qualified person. "
         "<b>&sect;1926.1413(a)(1)</b>: a competent person begins a visual inspection of "
         "wire ropes prior to each shift. Do not mix Category I/II/III rope removal into "
         "this module's C.K2 &#8212; that list stays on facility &sect;1910.179(m).")
    ],
    "C": [
        ("Stop-work is not a request",
         "(l)(3)(i) is the operator's authority in one line: unsafe conditions disclosed by "
         "the (j) inspection <b>shall be corrected before operation is resumed</b>. Not "
         "logged for later, not worked around, not deferred to the next shift.",
         "The same paragraph closes the other half: <b>adjustments and repairs shall be done "
         "only by designated personnel</b>. The operator stops the crane. The operator does "
         "not fix the crane."),
        ("Six ways a rope loses strength",
         "(m) names the conditions: reduction of rope diameter below nominal, from loss of "
         "core support, internal or external corrosion, or wear of outside wires; the number "
         "of broken outside wires <b>and the degree of distribution or concentration</b> of "
         "them; worn outside wires.",
         "And three more that get forgotten: corroded or broken wires <b>at end "
         "connections</b>; corroded, cracked, bent, worn or <b>improperly applied end "
         "connections</b>; severe kinking, crushing, cutting or unstranding."),
        ("Distribution, not just a count",
         "Six broken wires spread over a long length of rope and six broken wires in one "
         "strand in one lay are not the same finding. The standard asks for the number "
         "<b>and</b> the degree of distribution or concentration.",
         "This is what separates reading a rope from counting one. Concentration is the "
         "signal &#8212; it says the damage has a cause and a location."),
        ("Locking the crane out is five steps",
         "(l)(2)(i), in order: run the crane to a location causing <b>least interference</b> "
         "with other cranes and operations; put all controllers in the <b>off</b> position; "
         "open <b>and lock open</b> the main or emergency switch; hang warning or "
         "<b>out-of-order signs</b> on the crane <i>and</i> on the floor beneath or on the "
         "hook where visible from the floor.",
         "Step five is the one that gets a mechanic hit: where other cranes share the "
         "runway, <b>rail stops or other suitable means</b> shall be provided to prevent "
         "interference with the idle crane. That crane-specific sequence is the isolate "
         "path. The energy-control programme behind lockout is <b>&sect;1910.147</b> "
         "(held). On the construction B30.2-2005 path, &sect;1926.1438(b)(2)(iii) states "
         "that <b>29 CFR 1910.147 shall be substituted for ANSI Z244.1</b>."),
        ("Hooks are discarded, not repaired",
         "(l)(3)(iii)(a): hooks with the (j)(2)(iii) defects <b>shall be discarded</b>. The "
         "standard's own words on the alternative &#8212; <i>&#8220;repairs by welding or "
         "reshaping are not generally recommended.&#8221;</i>",
         "If a repair is attempted at all, it is only under competent supervision, and the "
         "hook must be <b>load tested per (k)(2)</b> before it goes back into service."),
        ("Handing over a defect",
         "A defect that lives only in the finder's head is a defect the next shift will "
         "discover with a load on the hook. The tag on the crane, the entry in the log and "
         "the spoken handover are three channels and all three are cheap.",
         "Where the crane has been taken out of service, the incoming operator needs to know "
         "<b>what is wrong, who was told, and what has to happen before it runs again</b>."),
    ],
}

PRACTICE = [
    ("OHC.05.A.K1",
     "Under &sect;1910.179(j)(1)(ii), the frequent inspection interval is:",
     ["Daily to monthly", "Weekly to quarterly", "Monthly to annually",
      "Whatever the facility programme sets"], 0,
     "Frequent is daily to monthly; periodic is one to twelve months. Both intervals are "
     "in the standard, not left to the programme."),
    ("OHC.05.A.K3",
     "The upper limit switch is tried out at the start of each shift under no load.",
     ["True", "False"], 0,
     "(n)(4)(i) requires it at the beginning of each shift, under no load, taken up slowly "
     "or inched at slow speed into the limit."),
    ("OHC.05.A.K4",
     "OSHA and ASME give different hook throat-opening limits. The rule for choosing is:",
     ["Always use the OSHA figure because it is regulation",
      "Follow ASME on the criteria and OSHA on the records",
      "Use whichever the employer prefers", "Average the two figures"], 1,
     "The DOE Hanford manual resolves this under Inconsistent Standards: ASME sets the "
     "tighter criteria, OSHA is what requires the monthly documented inspection."),
    ("OHC.05.B.K1",
     "The periodic inspection is performed by the operator at the start of each shift.",
     ["True", "False"], 1,
     "Periodic is a designated-person function on a one-to-twelve-month interval. The "
     "operator's shift-start inspection is the frequent regime."),
    ("OHC.05.B.K4",
     "A crane idle for eight months requires, before return to service:",
     ["The frequent inspection only", "A complete frequent AND periodic inspection, plus "
      "the idle-rope inspection", "Nothing, if it was serviceable when parked",
      "A rated load test"], 1,
     "(j)(4): idle over six months gets a complete (j)(2) and (j)(3) inspection plus the "
     "(m)(2) rope inspection."),
    ("OHC.05.C.K1",
     "An unsafe condition disclosed by inspection must be corrected before operation "
     "resumes.",
     ["True", "False"], 0,
     "(l)(3)(i). Not logged for later and not worked around."),
    ("OHC.05.C.K2",
     "When assessing broken wires in a rope, the standard asks for:",
     ["The total count only", "The count and the degree of distribution or concentration",
      "The rope diameter only", "The date of last lubrication"], 1,
     "(m) names the number of broken outside wires AND the degree of distribution or "
     "concentration of them. Concentration is the signal."),
    ("OHC.05.C.K3",
     "Out-of-order signs go on the crane and:",
     ["Nowhere else", "On the floor beneath, or on the hook where visible from the floor",
      "In the maintenance office only", "On the runway rail"], 1,
     "(l)(2)(i) step 4 requires signs on the crane and on the floor beneath or on the hook "
     "where visible from the floor."),
    ("OHC.05.C.K4",
     "A hook found with a crack should be:",
     ["Welded and returned to service", "Reshaped by the operator", "Discarded",
      "Derated by 50&#37; and monitored"], 2,
     "(l)(3)(iii)(a): hooks with (j)(2)(iii) defects shall be discarded. Repairs by welding "
     "or reshaping are not generally recommended."),
]

GATE = [
    # ---- Task A
    ("OHC.05.A.K1",
     "Which of these is inspected <b>daily</b> under &sect;1910.179(j)(2)?",
     ["Chain drive sprockets", "Deterioration or leakage in air or hydraulic systems",
      "Controller contactors for pitting", "Brake linings for excessive wear"], 1, ""),
    ("OHC.05.A.K1b",
     "Hooks and hoist chains carry an obligation beyond the daily visual check:",
     ["An annual load test", "A monthly inspection with a certification record",
      "A weekly dye-penetrant test", "No further obligation"], 1, ""),
    ("OHC.05.A.K2",
     "A complete functional check before operation proves:",
     ["That the crane moves in at least one direction",
      "Each motion, each brake, the warning device and the emergency stop",
      "Only the hoist, since it carries the load", "Only the motions used on that shift"],
     1, ""),
    ("OHC.05.A.K3",
     "The upper limit switch is verified at the beginning of each shift:",
     ["Under no load, taking it up slowly or inching at slow speed",
      "With a test load at full speed", "Under rated load at slow speed",
      "Only after maintenance work"], 0, ""),
    ("OHC.05.A.K3b",
     "&sect;1910.179(n)(4)(ii) states that the limit switch:",
     ["May be used to stop the hoist at the top of routine travel",
      "Shall not be used as an operating control",
      "Should be bypassed once verified", "Is optional on cab-operated cranes"], 1, ""),
    ("OHC.05.A.K4",
     "The OSHA hook removal criteria at (j)(2)(iii) are cracks, throat opening more than:",
     ["5&#37; in excess of normal, and 5&#176; twist",
      "10&#37; in excess of normal, and 15&#176; twist",
      "15&#37; in excess of normal, and 10&#176; twist",
      "25&#37; in excess of normal, and any twist"], 2, ""),
    ("OHC.05.A.K4b",
     "ASME B30.10 sets a throat-opening limit of 5&#37;, not to exceed &#188; in. Where the "
     "two documents differ, the working rule is:",
     ["Follow ASME on the criteria and OSHA on the records",
      "Follow OSHA on everything, as the regulation",
      "Follow whichever is more convenient for the shift",
      "Neither applies unless the manufacturer agrees"], 0, ""),
    ("OHC.05.A.K5",
     "A certification record for a monthly hook inspection must carry:",
     ["The date only", "The date and the inspector's signature",
      "The date, the inspector's signature, and the serial number or other identifier of "
      "the item", "A photograph of the hook"], 2, ""),
    ("OHC.05.A.R1",
     "Function checks are most often skipped:",
     ["On the first pick of a new crane", "After maintenance work and at shift change",
      "During periodic inspection", "When the crane is under load"], 1, ""),
    ("OHC.05.A.R2",
     "Testing the upper limit switch under load, or at speed, is hazardous because:",
     ["It wastes shift time", "The stopping distance and the momentum of the load can carry "
      "the block into the trolley before the switch can act",
      "It voids the manufacturer's warranty", "It requires two operators"], 1, ""),
    ("OHC.05.A.R3",
     "A defect that has been present and reported for several shifts, with the crane still "
     "running, is best described as:",
     ["Acceptable, since it has been reported",
      "A normalised deviation -- the reporting has replaced the correction",
      "A periodic inspection item", "The next shift's problem"], 1, ""),
    # ---- Task B
    ("OHC.05.B.K1",
     "The periodic inspection is:",
     ["An operator function at shift start",
      "A designated-person function at one-to-twelve-month intervals",
      "An annual manufacturer visit", "A records audit only"], 1, ""),
    ("OHC.05.B.K2",
     "The operator's primary contribution to the periodic programme is:",
     ["Performing the periodic inspection when the designated person is unavailable",
      "Reporting observations that trigger inspection escalation",
      "Signing the periodic inspection record", "Setting the inspection interval"], 1, ""),
    ("OHC.05.B.K3",
     "Before first use of an unfamiliar crane, the operator should establish:",
     ["Only that the crane runs", "Where inspection status is documented and whether it is "
      "current", "The name of the manufacturer", "The date of installation"], 1, ""),
    ("OHC.05.B.K4",
     "A crane idle for three months requires, before return to service:",
     ["Nothing further", "The frequent (j)(2) inspection plus the (m)(2) rope inspection",
      "A complete periodic inspection", "A rated load test at 125&#37;"], 1, ""),
    ("OHC.05.B.K4b",
     "A <b>standby</b> crane is inspected to the frequent and rope scope:",
     ["Monthly", "At least semi-annually", "Annually", "Only before use"], 1, ""),
    ("OHC.05.B.K5",
     "After repairs, &sect;1910.179(l)(2)(ii) requires that the crane not be operated until:",
     ["The work order is closed",
      "All guards are reinstalled, safety devices reactivated, and maintenance equipment "
      "removed", "The next shift begins", "A load test is performed"], 1, ""),
    ("OHC.05.B.R1",
     "Operating a crane whose periodic inspection has lapsed is a problem because:",
     ["It is an administrative oversight only",
      "The deep structural, mechanical and electrical scope that only periodic covers has "
      "gone unexamined for an unknown period", "The warranty lapses",
      "The crane will not start"], 1, ""),
    ("OHC.05.B.R2",
     "An operator notices a new noise in the bridge drive and assumes maintenance already "
     "knows. The failure mode is:",
     ["Acceptable if the noise is minor", "The observation never enters the programme, so "
      "nothing escalates", "A periodic inspection defect", "A documentation error only"],
     1, ""),
    ("OHC.05.B.R3",
     "&sect;1926.1412(d)(1) (held) requires a competent person to begin a visual inspection "
     "prior to each shift the equipment will be used. Until that inspection is begun, the "
     "operator:",
     ["May operate if last month's inspection is current",
      "Does not operate -- the shift visual inspection must be begun first",
      "Applies the 1910.179 frequent interval as a substitute",
      "Completes the inspection during the first lift"], 1, ""),
    # ---- Task C
    ("OHC.05.C.K1",
     "&sect;1910.179(l)(3)(i) requires that unsafe conditions disclosed by inspection be:",
     ["Logged for the next periodic inspection", "Corrected before operation is resumed",
      "Reported to the manufacturer", "Monitored over the following week"], 1, ""),
    ("OHC.05.C.K2",
     "Which pair of rope conditions is most often missed by an operator who is only counting "
     "broken wires?",
     ["Kinking and crushing", "Corroded or broken wires at end connections, and improperly "
      "applied end connections", "Diameter reduction and corrosion",
      "Worn outside wires and unstranding"], 1, ""),
    ("OHC.05.C.K3",
     "In the &sect;1910.179(l)(2)(i) lockout sequence, the step most often omitted is:",
     ["Placing controllers in the off position", "Locking the main switch open",
      "Providing rail stops or other means to prevent an adjacent crane interfering with "
      "the idle crane", "Hanging a warning sign"], 2, ""),
    ("OHC.05.C.K3b",
     "&sect;1926.1438(b)(2)(iii) (held) lists construction overhead-crane sections from "
     "ASME B30.2-2005 and states that '29 CFR 1910.147 shall be substituted for ANSI "
     "Z244.1.' At lockout that means:",
     ["ANSI Z244.1 remains the OSHA-mandated lockout standard for construction overhead "
      "cranes",
      "The construction energy-control interface is OSHA &sect;1910.147, not ANSI Z244.1",
      "&sect;1910.147 applies only to facility-branch cranes",
      "Lockout is optional on construction overhead cranes"], 1, ""),
    ("OHC.05.C.K4",
     "An operator finds a controller that sticks between points. The correct action is:",
     ["Adjust the controller and continue", "Remove the crane from service and refer it to "
      "designated personnel", "Operate using the other motions only",
      "Report it at the end of the shift"], 1, ""),
    ("OHC.05.C.K5",
     "The disposition of a reported deficiency must record:",
     ["That it was reported", "What was wrong, who was notified, and what must happen before "
      "the crane runs again", "The operator's name only", "The date only"], 1, ""),
    ("OHC.05.C.R1",
     "A crane with a brake that holds but drifts slightly is:",
     ["Serviceable, because it holds", "A degraded condition that must be corrected before "
      "operation resumes", "An item for the next periodic inspection",
      "Acceptable below 50&#37; of rated load"], 1, ""),
    ("OHC.05.C.R2",
     "The most reliable defect handover uses:",
     ["A verbal mention", "The tag on the crane, the entry in the log, and the spoken "
      "handover together", "The maintenance work order alone",
      "An email to the supervisor"], 1, ""),
    ("OHC.05.C.R3",
     "An operator who corrects a maintenance-level defect personally has:",
     ["Saved downtime appropriately", "Acted outside &sect;1910.179(l)(3)(i), which reserves "
      "adjustments and repairs to designated personnel", "Performed a frequent inspection",
      "Satisfied the return-to-service requirement"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.05.A.K1": ("**&sect;1910.179(j)(2)** daily scope", "OK"),
    "OHC.05.A.K1b": ("**&sect;1910.179(j)(2)(iii)&#8211;(iv)**", "OK"),
    "OHC.05.A.K2": ("&sect;1910.179(n)(3)(vii) &middot; derived", "OK"),
    "OHC.05.A.K3": ("**&sect;1910.179(n)(4)(i)**", "OK"),
    "OHC.05.A.K3b": ("**&sect;1910.179(n)(4)(ii)**", "OK"),
    "OHC.05.A.K4": ("**&sect;1910.179(j)(2)(iii)**", "CONFLICT"),
    "OHC.05.A.K4b": ("ASME B30.10 &middot; **DOE Hanford TR244C** *Inconsistent Standards*",
                     "CONFLICT"),
    "OHC.05.A.K5": ("**&sect;1910.179(j)(2)(iii)** certification record", "OK"),
    "OHC.05.A.R1": ("derived", "OK"),
    "OHC.05.A.R2": ("&sect;1910.179(k)(1)(ii) &middot; derived", "OK"),
    "OHC.05.A.R3": ("derived", "OK"),
    "OHC.05.B.K1": ("**&sect;1910.179(j)(1)(ii)** &middot; (j)(3)", "OK"),
    "OHC.05.B.K2": ("derived", "OK"),
    "OHC.05.B.K3": ("derived &middot; (m)(1) records", "OK"),
    "OHC.05.B.K4": ("**&sect;1910.179(j)(4)**", "OK"),
    "OHC.05.B.K4b": ("**&sect;1910.179(j)(4)** standby", "OK"),
    "OHC.05.B.K5": ("**&sect;1910.179(l)(2)(ii)**", "OK"),
    "OHC.05.B.R1": ("derived", "OK"),
    "OHC.05.B.R2": ("derived", "OK"),
    "OHC.05.B.R3": ("**&sect;1926.1412(d)(1)** held; (e)(1)/(f)(2) and &sect;1926.1413(a)(1) taught", "OK"),
    "OHC.05.C.K1": ("**&sect;1910.179(l)(3)(i)**", "OK"),
    "OHC.05.C.K2": ("**&sect;1910.179(m)** six conditions", "OK"),
    "OHC.05.C.K3": ("**&sect;1910.179(l)(2)(i)** step 5", "OK"),
    "OHC.05.C.K3b": ("**&sect;1926.1438(b)(2)(iii)** 1910.147 for Z244.1 &middot; **&sect;1910.147** held", "OK"),
    "OHC.05.C.K4": ("**&sect;1910.179(l)(3)(i)** &middot; (l)(3)(iii)(a)", "OK"),
    "OHC.05.C.K5": ("derived", "OK"),
    "OHC.05.C.R1": ("&sect;1910.179(l)(3)(i) &middot; derived", "OK"),
    "OHC.05.C.R2": ("derived", "OK"),
    "OHC.05.C.R3": ("**&sect;1910.179(l)(3)(i)**", "OK"),
}

TRACE_PERF = [
    ("OHC.05.A.S1", "Complete a full pre-operational inspection with documentation"),
    ("OHC.05.A.S2", "Demonstrate correct upper-limit-switch verification technique"),
    ("OHC.05.A.S3", "Identify planted defects in a practical inspection exercise"),
    ("OHC.05.B.S1", "Verify inspection status before first use of an unfamiliar crane"),
    ("OHC.05.B.S2", "Route an observation into the facility inspection programme"),
    ("OHC.05.B.S3", "Confirm return-to-service documentation after a known repair"),
    ("OHC.05.C.S1", "Execute a removal from service with tagging and notification"),
    ("OHC.05.C.S2", "Classify sample defects as operate, restrict, or remove"),
    ("OHC.05.C.S3", "Hand off crane status across a shift change without information loss"),
]

TRACE_NOTES = [
    ("&#9888;&#65039; The hook criteria conflict, taught rather than hidden",
     "OSHA **&sect;1910.179(j)(2)(iii)** removes a hook at **15&#37;** throat opening and "
     "**10&#176;** twist. **ASME B30.10** is stricter &#8212; **5&#37;, not to exceed "
     "&#188; in**, plus any visible bend or twist. Two Tier 0 rigging guides in the corpus "
     "teach one figure each and neither states the rule for choosing. The **DOE Hanford "
     "manual (TR244C Rev 5)** resolves it under a heading called *Inconsistent Standards*: "
     "**follow ASME on the criteria, follow OSHA on the records.** `A.K4` and `A.K4b` teach "
     "both figures and the rule."),
    ("&#9989; The intervals the ACS never states",
     "`OHC.05.A` and `OHC.05.B` describe the frequent and periodic regimes without giving "
     "either interval. **&sect;1910.179(j)(1)(ii)** has them: frequent is **daily to "
     "monthly**, periodic is **one to twelve months**. Both are now taught and gated."),
    ("&#9989; The certification record is three named fields",
     "The ACS says `A.K5` is *documentation per facility programme*. The standard is more "
     "specific: for hooks, chains and ropes the record carries **the date, the signature of "
     "the person who performed the inspection, and the serial number or other identifier of "
     "the item**. `A.K5` is written to the standard."),
    ("&#9989; Idle and standby closed from *concepts* to numbers",
     "`B.K4` reads *idle and standby crane inspection concepts* in the ACS. "
     "**&sect;1910.179(j)(4)** gives three cases: idle **1&#8211;6 months** &#8594; (j)(2) "
     "+ (m)(2); idle **over 6 months** &#8594; (j)(2) + (j)(3) + (m)(2); **standby** "
     "&#8594; (j)(2) + (m)(2) **at least semi-annually**."),
    ("&#9989; Construction-branch inspection paragraphs are held",
     "Cross-check finding **F4**: &sect;1910.179 **(j)**, **(l)** and **(m)** are *not* in "
     "the &sect;1926.1438(b)(2) list. Fetched 2026-08-28 from OSHA.gov. `B.R3` gates "
     "**&sect;1926.1412(d)(1)**: a competent person must begin a visual inspection prior "
     "to each shift. Monthly **(e)(1)** and annual **(f)(2)** and wire-rope "
     "**&sect;1926.1413(a)(1)** are taught from the citation pack. Category I/II/III "
     "rope-removal lists stay out of `C.K2`, which remains on facility **&sect;1910.179(m)**. "
     "`C.K3b` gates the **&sect;1926.1438(b)(2)(iii)** substitution of **&sect;1910.147** "
     "for ANSI Z244.1 on the construction B30.2-2005 path. ACS `B.R3` remains *returning "
     "a repaired crane without verification* (already gated at `B.K5`); the construction "
     "shift-inspection overlay occupies the `B.R3` second-fact slot because that is where "
     "the branch hole was taught."),
    ("&#9989; Distribution, not just a wire count",
     "`C.K2` in the ACS lists *broken wires, kinking, crushing, corrosion, stretch, and "
     "gauge wear*. **&sect;1910.179(m)** names six conditions and two of them concern **end "
     "connections**, which the ACS omits entirely. It also asks for the number of broken "
     "wires **and the degree of distribution or concentration** &#8212; the part that "
     "separates reading a rope from counting one."),
]


def main():
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)
    A.write_pre_and_manifest(
        MODULE, html, "OHC_M05_InspectionRegime.pre.html",
        "CQ1:OHC_M05_InspectionRegime", "OHC_M06", PRACTICE, GATE,
        notes="1412/1413 and 1910.147 held 2026-08-28")


if __name__ == "__main__":
    main()
