#!/usr/bin/env python3
"""OHC-03 Controls and Operating Modes -- pre-retrofit DOM.

Question tuples: (element, stem, [options], correct_idx, rationale)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M03"
MODLABEL = "Module 3"
TITLE = "Controls and Operating Modes"
SUBTITLE = ("Operate each assigned control mode with mode-specific hazard management and "
            "positioning discipline.")

OBJECTIVES = [
    "Operate a hard-wired pendant crane from the floor with correct standing position "
    "and travel-path discipline.",
    "Operate a radio-controlled crane with transmitter custody discipline, and treat "
    "positioning freedom as a hazard to be managed rather than a convenience.",
    "Operate a cab-controlled crane with access, egress and blind-zone discipline.",
    "State the federal operator class your assigned equipment falls into, and what that "
    "class requires of you.",
]

SECTIONS = [
    ("A", "Floor and Pendant Operation",
     "Operate a hard-wired pendant crane from the floor with correct positioning."),
    ("B", "Wireless Remote Operation",
     "Operate radio-controlled cranes with transmitter discipline and positioning freedom "
     "managed as a hazard."),
    ("C", "Cab Operation",
     "Operate cab-controlled cranes with access, egress and elevated-station discipline."),
]

CONTENT = {
    "A": [
        ("The pendant station",
         "Pendant controls carry motion legends for hoist, trolley and bridge, and are "
         "either multi-speed (stepped detents) or variable speed (progressive). Push-button "
         "covers must be unsplit, legends legible, and lever-operated controls must "
         "spring-return to neutral.",
         "Voltage at pendant push-buttons is limited to <b>150 V a.c. or 300 V d.c.</b> "
         "&#8212; the pendant is the one energised thing you hold all shift."),
        ("Your federal operator class",
         "On federal work, <b>all hard-wired, pendant-operated</b> overhead, bridge and "
         "gantry cranes are <b>Class II</b>.",
         "Class II training is a minimum of <b>2 hours initial</b> with passed written and "
         "practical examinations, and a minimum <b>1-hour biennial refresher</b>, also with "
         "passed examinations. A 60-day grace period exists but depends on supervisory "
         "approval."),
        ("Planning the walk, not just the lift",
         "A pendant operator walks the job. Before first motion, check the load's path, the "
         "crane's path, <b>and your own walking path</b>: floor obstructions, housekeeping, "
         "slick surfaces, floor openings, pedestrian aisles, doorways and other equipment.",
         "Two paths can be clear while the third is not. The one that puts you on the floor "
         "is the one nobody plans."),
        ("Where your body goes",
         "Never position yourself <b>under the load</b>, and never between the load and a "
         "fixed object. Pinch points on a pendant job are formed by the load, the walls, "
         "the racking and the machinery &#8212; not by the crane.",
         "The crane cannot crush you. The load and the building can, and they do it in the "
         "gap you chose to stand in."),
        ("Stopping the crane",
         "Plugging &#8212; reversing the controller to brake &#8212; is a legitimate means "
         "of stopping, and it is better than letting the crane coast to a stop. But it "
         "induces load swing and drivetrain wear.",
         "The discipline is <b>controlled deceleration where the situation allows</b>, with "
         "plugging as a deliberate tool rather than a habit. Sudden stops swing the load "
         "outward and wear the wheels unevenly."),
        ("Attention is the scarce resource",
         "The pendant operator is simultaneously the operator, the walker and often the "
         "spotter. Attention has to be divided across the load, the travel path, the "
         "walking path and the people in the bay.",
         "When the situation demands more attention than you have, the answer is to "
         "<b>stop</b> &#8212; land the load, reset, and continue. Complacency in repetitive "
         "work is the recognised failure mode."),
    ],
    "B": [
        ("The transmitter",
         "A radio transmitter carries the motion controls, an <b>E-stop</b>, and usually a "
         "motion-enable interlock that must be satisfied before any output. Pre-use checks "
         "are battery state, pairing, and a functional test of every motion.",
         "Verify the E-stop works before you verify anything else. It is the only control "
         "that matters when the others misbehave."),
        ("Your federal operator class",
         "For wireless overhead, bridge, gantry, underhung and monorail cranes the split is "
         "<b>capacity-based at 30 tons</b>. Over 30T is <b>Class I</b>; <b>30T or less</b> "
         "is Class II.",
         "One exemption: operators of <b>continually guided</b> loads over 30T are treated "
         "as Class II &#8212; a gate that is raised and lowered within a slot and stays in "
         "it. If the gate clears the slot and hangs free, a Class I operator is required."),
        ("What Class I costs",
         "The class you fall into is not a label; it is a training burden. <b>Class I</b> "
         "requires a minimum of <b>24 hours initial</b> training with passed written and "
         "practical examinations, and a minimum <b>8-hour biennial refresher</b>, also "
         "examined.",
         "Class II is 2 hours initial and 1 hour biennial. The same crane, operated wireless "
         "at 31 tons instead of 29, moves the operator from a 2-hour to a 24-hour "
         "requirement."),
        ("Positioning freedom is the hazard",
         "Wireless removes the tether, and with it the natural limit on where the operator "
         "stands. You can now stand anywhere &#8212; including inside the fall zone, under "
         "the load, or where the load hides the thing you are about to hit.",
         "Choose vantage points deliberately: full line of sight to the load and the "
         "landing area, outside the fall zone, with a way to move that does not cross the "
         "load path."),
        ("Custody of the transmitter",
         "A live transmitter is a live crane. Custody is explicit: one operator holds it, "
         "transfer is announced and acknowledged, and it is secured against unauthorised "
         "use whenever it is not in use.",
         "Never carry an active transmitter into an unrelated task. A transmitter in a "
         "pocket while you do something else is an unattended crane with a hand on it."),
        ("When the signal drops",
         "Know what your crane does on loss of signal &#8212; and confirm it rather than "
         "assume. Expected behaviour is that motion stops and brakes set.",
         "On multi-crane systems, unverified transmitter-to-crane assignment is the "
         "classic wireless incident: the operator commands one crane and a different one "
         "moves. <b>Verify assignment before first motion, every time.</b>"),
    ],
    "C": [
        ("Getting in and out",
         "Access to the cab or bridge walkway is by a conveniently placed fixed ladder, "
         "stairs or platform <b>requiring no step over any gap exceeding 12 inches</b>. "
         "Fixed ladders comply with Subpart D.",
         "Hands stay free while using ladders; anything too large for a pocket or belt is "
         "raised and lowered <b>by hand line</b>. Know your emergency egress route before "
         "you need it, not during."),
        ("Your federal operator class",
         "<b>Cab-operated</b> overhead, bridge, gantry, underhung and monorail cranes are "
         "<b>Class I</b> &#8212; the highest tier.",
         "That is 24 hours initial training with passed written and practical examinations, "
         "and an 8-hour biennial refresher. Cab operation is not a variation on pendant "
         "operation; federally it is a different qualification."),
        ("The cab itself",
         "The cab is arranged so all operating handles are within convenient reach when "
         "facing the area served by the load hook or the direction of travel, and so the "
         "operator has a <b>full view of the load hook in all positions</b>.",
         "The cab is located to afford a minimum of <b>3 inches clearance</b> from all "
         "fixed structures within its area of possible movement."),
        ("Seeing from elevation",
         "Height buys reach and costs resolution. Blind zones from a cab are created by the "
         "girder, the load itself, the trolley machinery and the angle onto the landing "
         "area &#8212; and they grow as the load gets larger.",
         "Where the placement is obscured, the answer is a signaler and an established "
         "signal link agreed <b>before</b> the lift, not improvised part-way through it."),
        ("Cab pre-use items",
         "A portable fire extinguisher with a minimum rating of <b>10 BC</b> is installed "
         "in the cab. Carbon tetrachloride extinguishers <b>shall not be used</b>. Lighting "
         "must be sufficient for the operator to see clearly enough to work.",
         "Housekeeping is a rule, not a preference: clothing and belongings stored so as not "
         "to interfere with access or operation, and tools, oil cans, waste and spare fuses "
         "in the tool box rather than loose in the cab."),
        ("Moving with people around",
         "From a cab you may not be able to see people on access ways, walkways or adjacent "
         "cranes. Contact with runway stops or other cranes is made only with extreme "
         "caution, with particular care for persons on or below the crane, and only after "
         "<b>making certain persons on the other cranes are aware</b>.",
         "The operator does not leave the controls while a load is suspended, and the "
         "warning signal is sounded when starting the bridge and when the load or hook "
         "approaches near or over personnel."),
    ],
}

PRACTICE = [
    ("OHC.03.A.K2",
     "On federal work, a hard-wired pendant-operated overhead crane makes its operator:",
     ["Class I", "Class II", "Exempt from classification", "A Competent Person"], 1,
     "All hard-wired, pendant-mounted operated overhead, bridge and gantry cranes are "
     "Class II."),
    ("OHC.03.A.K4",
     "While walking a load with a pendant, standing between the load and a fixed rack is "
     "acceptable if the load is moving slowly.",
     ["True", "False"], 1,
     "Never position yourself under the load or between the load and a fixed object, at "
     "any speed."),
    ("OHC.03.A.K5",
     "Allowing the crane to coast to a stop rather than using the braking system or "
     "control reversal is:",
     ["Preferred, because it is gentler on the load", "Not acceptable practice",
      "Required on variable-speed cranes", "Only allowed with the hook empty"], 1,
     "Coasting is not an acceptable stopping method. Use the braking system or control "
     "reversal, and prefer controlled deceleration where the situation allows."),
    ("OHC.03.B.K2",
     "A wireless-operated overhead crane rated at 25 tons places its operator in:",
     ["Class I", "Class II", "Neither class", "Class I only when hoisting personnel"], 1,
     "Wireless overhead cranes of 30 tons capacity or less are Class II. Over 30T is "
     "Class I."),
    ("OHC.03.B.R2",
     "In a bay with several wireless cranes, the first action before any motion is to:",
     ["Sound the warning device", "Verify which crane the transmitter is assigned to",
      "Raise the hook to maximum", "Check the load chart"], 1,
     "Unverified transmitter-to-crane assignment is the classic wireless incident: you "
     "command one crane and a different one moves."),
    ("OHC.03.B.K4",
     "An operator finishing a lift is called to another task and pockets the still-active "
     "transmitter. This is:",
     ["Acceptable if the crane is parked", "Acceptable for short periods",
      "Not acceptable &#8212; the transmitter must be secured against unauthorised use",
      "Acceptable if no one else is qualified"], 2,
     "A live transmitter is a live crane. Secure it whenever it is not in use."),
    ("OHC.03.C.K2",
     "A cab-operated overhead crane places its operator in:",
     ["Class II regardless of capacity", "Class I", "An exempt category",
      "Class II if under 30 tons"], 1,
     "Cab-operated overhead, bridge, gantry, underhung and monorail cranes are Class I."),
    ("OHC.03.C.K1",
     "Access to a crane cab or bridge walkway must require no step over any gap exceeding:",
     ["6 inches", "12 inches", "18 inches", "24 inches"], 1,
     "Access is by a conveniently placed fixed ladder, stairs or platform requiring no step "
     "over any gap exceeding 12 inches."),
    ("OHC.03.C.K5",
     "Which extinguisher type is specifically prohibited in a crane cab?",
     ["Dry chemical", "Carbon dioxide", "Carbon tetrachloride", "Foam"], 2,
     "Carbon tetrachloride extinguishers shall not be used. A portable extinguisher with a "
     "minimum 10 BC rating is installed in the cab."),
]

GATE = [
    # ---- Task A
    ("OHC.03.A.K1",
     "The maximum permitted voltage at pendant push-buttons is:",
     ["600 V a.c. and 600 V d.c.", "150 V a.c. and 300 V d.c.",
      "240 V a.c. and 120 V d.c.", "24 V d.c. only"], 1, ""),
    ("OHC.03.A.K2",
     "Class II initial training on federal work requires a minimum of:",
     ["1 hour", "2 hours with passed written and practical examinations",
      "8 hours", "24 hours"], 1, ""),
    ("OHC.03.A.K3",
     "Before first motion, a pendant operator must survey:",
     ["The load path only", "The load path and the crane path",
      "The load path, the crane path and the operator's own walking path",
      "Only the landing area"], 2, ""),
    ("OHC.03.A.K4",
     "The crushing hazard to a pendant operator is created principally by:",
     ["The bridge girder", "The load and fixed objects such as walls, racking and machinery",
      "The pendant cable", "The runway rail"], 1, ""),
    ("OHC.03.A.K5",
     "Which statement about plugging is correct?",
     ["It is prohibited in all circumstances",
      "It is a legitimate means of stopping but induces load swing and drivetrain wear, so "
      "controlled deceleration is preferred where the situation allows",
      "It is the required method for every stop",
      "It applies only to hoist motion, never travel"], 1, ""),
    ("OHC.03.A.R1",
     "Walking backward while tracking a load is hazardous chiefly because:",
     ["It slows the lift", "The operator cannot see their own walking path",
      "It causes the pendant to whip", "It reduces crane capacity"], 1, ""),
    ("OHC.03.A.R2",
     "Pendant whip and entanglement with the load or rigging is best prevented by:",
     ["Holding the pendant above shoulder height",
      "Maintaining position and separation between the pendant, the load and the rigging",
      "Coiling the pendant cable around the wrist",
      "Operating at maximum speed to reduce exposure time"], 1, ""),
    ("OHC.03.A.R3",
     "When the job demands more attention than the operator can divide across load, path "
     "and personnel, the correct action is to:",
     ["Speed up to finish sooner", "Continue and concentrate harder",
      "Stop, land the load, reset and continue", "Hand the pendant to a bystander"], 2, ""),
    # ---- Task B
    ("OHC.03.B.K1",
     "Which transmitter control should be verified first during pre-use checks?",
     ["The hoist-up button", "The E-stop", "The bridge travel selector",
      "The speed selector"], 1, ""),
    ("OHC.03.B.K2",
     "For wireless overhead, bridge, gantry, underhung and monorail cranes, the Class I / "
     "Class II split is set by:",
     ["Whether the crane is indoors or outdoors", "The operator's years of experience",
      "Rated capacity, at a 30-ton threshold", "The number of hoists on the crane"], 2, ""),
    ("OHC.03.B.K2b",
     "An operator runs a 40-ton wireless crane handling loads that are continually guided "
     "and never leave their slot. That operator is treated as:",
     ["Class I, because the crane exceeds 30 tons", "Class II, under the continually "
      "guided exemption", "Exempt from any class", "Class I only during refresher periods"],
     1, ""),
    ("OHC.03.B.K3",
     "When selecting an operating position for a wireless lift, the governing requirement "
     "is:",
     ["Standing as close to the load as possible",
      "Full line of sight to load and landing area, from outside the fall zone",
      "Standing directly beneath the hook for best alignment",
      "Standing at the crane disconnect"], 1, ""),
    ("OHC.03.B.K5",
     "Expected crane behaviour on loss of radio signal is that:",
     ["The crane continues its last commanded motion", "Motion stops and brakes set",
      "The crane returns automatically to its park position",
      "The hoist lowers the load to the floor"], 1, ""),
    ("OHC.03.B.R1",
     "Operating from a position with obstructed line of sight is unacceptable because:",
     ["It reduces radio range", "The operator cannot see hazards developing in the load "
      "path or landing area", "It drains the transmitter battery",
      "It voids the crane's duty classification"], 1, ""),
    ("OHC.03.B.R2",
     "The characteristic wireless incident on a multi-crane system is:",
     ["Battery failure mid-lift", "Commanding one crane and having a different crane move",
      "Interference from mobile phones", "Loss of the motion-enable interlock"], 1, ""),
    ("OHC.03.B.R3",
     "Carrying an active transmitter into an unrelated task is equivalent to:",
     ["Leaving the crane properly secured", "Leaving an unattended crane with a hand on it",
      "A normal handover", "Performing a pre-use inspection"], 1, ""),
    # ---- Task C
    ("OHC.03.C.K1",
     "Which is required of crane cab access?",
     ["A rope ladder is acceptable", "A conveniently placed fixed ladder, stairs or "
      "platform requiring no step over a gap exceeding 12 inches",
      "Access from the load hook", "Access only when the crane is at the runway centre"],
     1, ""),
    ("OHC.03.C.K2",
     "Class I initial training on federal work requires a minimum of:",
     ["2 hours", "8 hours", "24 hours with passed written and practical examinations",
      "40 hours"], 2, ""),
    ("OHC.03.C.K3",
     "The cab must be arranged so that the operator has:",
     ["A view of the runway only", "A full view of the load hook in all positions",
      "A view of the disconnect", "Access to the trolley machinery"], 1, ""),
    ("OHC.03.C.K3b",
     "The cab must be located to afford a minimum clearance from all fixed structures "
     "within its area of possible movement of:",
     ["1 inch", "2 inches", "3 inches", "6 inches"], 2, ""),
    ("OHC.03.C.K5",
     "Cab housekeeping requires that tools, oil cans, waste and spare fuses be:",
     ["Stowed loose behind the seat", "Kept in the tool box and not permitted to lie loose "
      "in or about the cab", "Left on the cab floor for quick access",
      "Stored on the bridge walkway"], 1, ""),
    ("OHC.03.C.R1",
     "Before moving a cab-operated crane where personnel may be on access ways or adjacent "
     "cranes, the operator must:",
     ["Sound the warning once and proceed immediately",
      "Make certain that persons on the affected cranes are aware, and proceed with extreme "
      "caution", "Move only at maximum speed to clear the area quickly",
      "Rely on the adjacent operators to keep clear"], 1, ""),
    ("OHC.03.C.R2",
     "A placement is obscured from the cab. The correct action is to:",
     ["Estimate the position and lower slowly",
      "Establish a signaler and an agreed signal link before the lift",
      "Ask a bystander to shout when it looks close",
      "Lower to just above the floor and drag the load into position"], 1, ""),
    ("OHC.03.C.R3",
     "Emergency egress from the cab should be:",
     ["Worked out at the time of the emergency", "Known and rehearsed before it is needed",
      "The responsibility of the rescue team only", "Unnecessary on indoor cranes"], 1, ""),
]

# Source map for the generated trace table: element -> (source, status)
TRACE_SOURCE = {
    "OHC.03.A.K1": ("&sect;1910.179(g)(1)(iii) &middot; Tier 0 pendant criteria", "OK"),
    "OHC.03.A.K2": ("**EM 385 &sect;16.C.05.a, &sect;16.C.07** (2024: 16-2.h)", "ED2014"),
    "OHC.03.A.K3": ("Tier 0 worksite hazard list", "OK"),
    "OHC.03.A.K4": ("&sect;1910.179(n)(3)(vi) &middot; derived", "OK"),
    "OHC.03.A.K5": ("Tier 0 slide 93 &middot; &sect;1910.179(n)(3)(iii)(a)", "CONFLICT"),
    "OHC.03.A.R1": ("Tier 0 slide 88", "OK"),
    "OHC.03.A.R2": ("derived", "OK"),
    "OHC.03.A.R3": ("Tier 0 complacency note", "OK"),
    "OHC.03.B.K1": ("derived &middot; Tier 0 unfamiliar-crane routine", "OK"),
    "OHC.03.B.K2": ("**EM 385 &sect;16.C.02.e / &sect;16.C.05.b** (2024: 16-2.g/h)", "ED2014"),
    "OHC.03.B.K2b": ("**EM 385 &sect;16.C.02.e** continually-guided exemption", "ED2014"),
    "OHC.03.B.K3": ("derived", "OK"),
    "OHC.03.B.K5": ("derived", "OK"),
    "OHC.03.B.R1": ("derived", "OK"),
    "OHC.03.B.R2": ("derived", "OK"),
    "OHC.03.B.R3": ("derived", "OK"),
    "OHC.03.C.K1": ("**&sect;1910.179(c)(2)** &middot; Subpart D", "OK"),
    "OHC.03.C.K2": ("**EM 385 &sect;16.C.02.d, &sect;16.C.04** (2024: 16-2.g)", "ED2014"),
    "OHC.03.C.K3": ("**&sect;1910.179(c)(1)(i)**", "OK"),
    "OHC.03.C.K3b": ("**&sect;1910.179(c)(1)(ii)**", "OK"),
    "OHC.03.C.K5": ("&sect;1910.179(c)(3),(4) &middot; **(o)(2)** &middot; Tier 0 10 BC", "OK"),
    "OHC.03.C.R1": ("**EM 385 &sect;16.M.06** (16-8.aa(6))", "OK"),
    "OHC.03.C.R2": ("derived &middot; &sect;1910.179(n)(3)(ii)(c)", "OK"),
    "OHC.03.C.R3": ("&sect;1910.179(c)(2) &middot; derived", "OK"),
}

TRACE_PERF = [
    ("OHC.03.A.S1", "Maintain correct standing position relative to load and travel direction"),
    ("OHC.03.A.S2", "Execute smooth acceleration and deceleration without load swing"),
    ("OHC.03.A.S3", "Stop and reposition before continuing when the travel path degrades"),
    ("OHC.03.B.S1", "Verify transmitter-to-crane assignment before first motion"),
    ("OHC.03.B.S2", "Demonstrate E-stop and recovery procedure"),
    ("OHC.03.B.S3", "Select and justify operating positions for a lift sequence"),
    ("OHC.03.C.S1", "Perform cab access, pre-use checks and egress per facility procedure"),
    ("OHC.03.C.S2", "Complete a lift requiring signaler-directed blind placement"),
    ("OHC.03.C.S3", "Demonstrate emergency egress awareness for the assigned cab crane"),
]

TRACE_NOTES = [
    ("&#9989; EM 385 Class I / II now sourced",
     "`A.K2`, `B.K2`, `B.K2b` and `C.K2` were blocked pending EM 385 Section 16's general "
     "paragraphs. Those were located and read: **&sect;16.C.02** (Class I types), "
     "**&sect;16.C.05** (Class II types), **&sect;16.C.04** and **&sect;16.C.07** (training "
     "hours). The 2014 &rarr; 2024 crosswalk is clean &#8212; 16.C.02 is the spec's "
     "`16-2.g`, 16.C.05 is `16-2.h`."),
    ("&#9888;&#65039; Edition basis",
     "Those four items were read from the **2014** Section 16 extract, which numbers by "
     "letter (&sect;16.C). The **content** is verified; the **2024 paragraph numbers** are "
     "taken on the subject-matter owner's verification. Cite the concept and the class, "
     "not a 2024 paragraph number, until the 2024 numbering is read directly."),
    ("&#9888;&#65039; `A.K5` plugging &mdash; house position needed",
     "The shipped Tier 0 deck states *\"never allow the crane to coast to a stop, use "
     "plugging or the braking system.\"* The ACS frames plugging as a load-swing cause and "
     "contrasts it with controlled deceleration. **The item is written to reconcile both**: "
     "plugging is legitimate and beats coasting, but induces swing and wear, so controlled "
     "deceleration is preferred where the situation allows. This reconciliation needs "
     "sign-off, or the two courses will teach differently."),
    ("&#9432; Two elements carry two items",
     "`OHC.03.B.K2` and `OHC.03.C.K3` each carry a second item (`B.K2b`, `C.K3b`) because "
     "each element contains two independently testable facts &#8212; the 30-ton threshold "
     "and its continually-guided exemption; full view of the hook and the 3-inch cab "
     "clearance. Coverage stays 1:1 by element; the gate is 24 items over 15 K + 9 R."),
]


def build():
    return A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)


if __name__ == "__main__":
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "out",
                                       "OHC_M03_ControlsAndOperatingModes.pre.html"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out):
        os.remove(out)
    html = build()
    with open(out, "w", encoding="ascii") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))
