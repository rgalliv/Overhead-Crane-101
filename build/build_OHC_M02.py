#!/usr/bin/env python3
"""OHC-02 Crane Components and Systems -- pre-retrofit DOM.

Question tuples: (element, stem, [options], correct_idx, rationale)
Rationale is emitted only for practice items; gate items never reveal.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M02"
MODLABEL = "Module 2"
TITLE = "Crane Components and Systems"
SUBTITLE = ("Identify all major structural, mechanical and electrical components and "
            "describe their function and failure significance.")

OBJECTIVES = [
    "Trace the load path from hook to runway and name every structural element it "
    "passes through.",
    "Identify hoist, brake and drive components, and state why the upper limit switch "
    "is a test device rather than an operating control.",
    "Identify power delivery and control components, and execute a controlled stop and "
    "secure on any electrical anomaly.",
]

SECTIONS = [
    ("A", "Structural Systems",
     "Identify structural components and their inspection significance."),
    ("B", "Mechanical Systems",
     "Identify hoist, trolley and drive components and their operating behaviour."),
    ("C", "Electrical and Control Systems",
     "Identify power delivery and control components and safe electrical interfaces."),
]

CONTENT = {
    "A": [
        ("The load path",
         "Every pound in the hook travels the same road: hook and load block, rope or "
         "chain, drum, trolley frame, trolley wheels, bridge girder, end trucks, bridge "
         "wheels, runway rail, runway beam, and finally the building columns and "
         "foundations.",
         "Naming the path in order is not an academic exercise. It is how you work out "
         "what a noise, a vibration or a crack actually threatens."),
        ("Runways and anchorages",
         "Runway beams, rails, rail joints and their alignment carry everything the crane "
         "carries. Foundations, anchorages, runways and rail tracks are constructed or "
         "installed per the manufacturer's recommendations <b>and ANSI/ASME B30.2 or "
         "B30.17 as applicable</b>.",
         "That requirement is explicit in the federal supplemental rules for overhead and "
         "gantry cranes, and it applies whether or not the crane is permanently installed."),
        ("Stops, bumpers and sweeps",
         "Trolley stops are provided at the limits of travel and are fastened to resist "
         "the forces applied when contacted. A stop engaging the tread of the wheel is at "
         "least equal to the radius of the wheel.",
         "Bumpers absorb energy; stops arrest travel; <b>rail sweeps</b> ride ahead of the "
         "truck wheels and extend below the top of the rail, pushing debris off the rail "
         "before a wheel can climb it."),
        ("Deceleration criteria",
         "Bumper performance is specified, not approximate. Bridge bumpers stop the crane "
         "at an average deceleration not exceeding <b>3 ft/s&#178;</b> at 20&#37; of rated "
         "load speed, with energy capacity to stop at 40&#37;. Trolley bumpers do not "
         "exceed <b>4.7 ft/s&#178;</b> at one-third rated load speed.",
         "Bumpers are also mounted so there is <b>no direct shear on bolts</b>, and "
         "designed to minimise parts falling from the crane if they break. Where two "
         "trolleys share a bridge, each is bumpered on its adjacent end."),
        ("Walkways and access",
         "Footwalks, service platforms, ladders and stairways are structure too. Footwalks "
         "are rigid, carry at least <b>50 lb/ft&#178;</b> distributed, have an antislip "
         "surface, and never provide less than <b>48 inches</b> of headroom.",
         "Fixed ladders, toeboards and handrails must comply with <b>Subpart D</b> of "
         "Part 1910 &#8212; the crane standard hands off to it by name three separate times."),
        ("Reading structural distress",
         "Camber is designed-in upward curvature; deflection is what the load takes back. "
         "Loss of camber, growing deflection, cracked or corroded members, loose bolts or "
         "rivets and distorted connections are the periodic inspection's structural list.",
         "An operator is not the inspector, but is the only person who sees the crane "
         "every shift. <b>Report location-specifically</b>: which girder, which end, which "
         "joint &#8212; not \"it looks bad.\""),
    ],
    "B": [
        ("The hoisting train",
         "Drum, rope reeving, sheaves, load block and hook assembly with its safety latch "
         "make up the hoisting train. Sheave grooves are smooth and free from surface "
         "defects that could damage rope, and all running sheaves have a means of "
         "lubrication.",
         "Bottom-block sheaves carry <b>close-fitting guards</b> so the rope cannot foul "
         "when the block is on the ground with the ropes slack. That guard exists because "
         "of a specific, repeated failure."),
        ("Rope and reeving",
         "The relationship is fixed by rule: the rated load divided by the number of parts "
         "of rope <b>shall not exceed 20&#37; of the nominal breaking strength</b> of the "
         "rope &#8212; a 5:1 design factor.",
         "More parts of line means more mechanical advantage and proportionally slower "
         "hook speed. Four-part reeving gives 4:1 at the hook and one quarter of the drum "
         "line speed."),
        ("Two braking systems",
         "Each independent hoisting unit has at least one <b>self-setting holding brake</b> "
         "applied to the motor shaft or gear train. It engages automatically whenever power "
         "is removed &#8212; it is the fail-safe.",
         "Each unit also has a <b>control braking means</b> to prevent overspeeding, with "
         "one exception: worm-geared hoists whose worm angle already prevents the load "
         "accelerating in the lowering direction. That exception is why two systems exist."),
        ("Chain as a hoisting medium",
         "Load chain and chain hoists are an alternate hoisting medium with their own "
         "consensus volume and their own rejection criteria &#8212; wear, twist, distorted "
         "links interfering with function, and stretch beyond the manufacturer's figures.",
         "Chain pockets and sheave flanges are dimensioned so the chain does not catch or "
         "bind during operation. Grade matters: only alloy chain rated for overhead lifting "
         "belongs on a hoist."),
        ("The upper limit switch",
         "The upper limit switch stops hoisting before the block reaches the trolley. Its "
         "trip setting is determined by <b>test, with an empty hook</b>, at increasing "
         "speeds up to maximum.",
         "That is the whole argument in one sentence: it is set by test, so it is a test "
         "device. The rule states it plainly &#8212; the hoist limit switch controlling "
         "upper travel of the load block <b>shall never be used as an operating control</b>."),
        ("Drive train and duty class",
         "Gear cases, couplings, wheels and the drive train move the crane. Wheels are "
         "removed from service at a <b>1/8 inch</b> tread flat spot &#8212; usually "
         "detected first as a thumping during bridge travel.",
         "Duty classification rates a crane to its service severity. Class A is standby or "
         "infrequent service; <b>Class F is continuous severe service</b> &#8212; mills and "
         "hot metal. Duty class is on the data plate and it governs what the crane may be "
         "asked to do."),
    ],
    "C": [
        ("Getting power to a moving crane",
         "Power reaches a travelling crane one of two ways: <b>conductor bars</b> with "
         "sliding collectors, or a <b>festoon</b> cable system running on a track.",
         "Festoon encloses its conductors. Conductor bar has exposed or semi-enclosed rails "
         "carrying lethal voltage along the whole runway. Both require lockout for any work "
         "on the crane; only one of them looks dangerous."),
        ("The disconnect",
         "The mainline disconnect is the operator's isolation point. Before adjustments or "
         "repairs the main or emergency switch is <b>open and locked in the open "
         "position</b>, all controllers are off, and warning or out-of-order signs go on "
         "the crane <i>and</i> on the floor beneath or the hook where they are visible from "
         "the floor.",
         "Where other cranes share the runway, <b>rail stops or equivalent</b> prevent them "
         "interfering with the idle crane. That is the step people skip."),
        ("Control circuits",
         "Wiring and equipment comply with <b>Subpart S</b> of Part 1910. Control circuit "
         "voltage does not exceed <b>600 V</b> a.c. or d.c., and voltage at pendant "
         "push-buttons does not exceed <b>150 V a.c. or 300 V d.c.</b>",
         "Those pendant limits exist because the pendant is the one energised thing an "
         "operator holds in wet hands all shift."),
        ("The warning device",
         "Except for floor-operated cranes, an alarm or other effective warning signal is "
         "provided for each crane equipped with a power travelling mechanism.",
         "Note the exception and note the branch. On the facility branch this is a "
         "&sect;1910.179 requirement; it is <b>not</b> among the paragraphs carried onto "
         "the non-permanently-installed construction branch. On federal work it applies "
         "either way."),
        ("Operator control hardware",
         "Pendants need working strain relief so the cable never carries the pendant's "
         "weight. Enclosures must be intact, push-button covers unsplit, legends legible, "
         "and lever-operated controls must spring-return to neutral.",
         "Wireless transmitters add battery state, pairing and loss-of-signal behaviour to "
         "the same list. A transmitter with an unknown battery is an unknown crane."),
        ("When the electrics misbehave",
         "Intermittent power pickup &#8212; a dirty collector, a worn shoe, a damaged "
         "festoon trolley &#8212; produces motion you did not command or loses motion you "
         "did.",
         "There is one correct response and it does not involve diagnosis: bring the load "
         "down under control if you can, stop, secure the crane, and report it. Operators "
         "do not troubleshoot energised crane electrics."),
    ],
}

PRACTICE = [
    ("OHC.02.A.K1",
     "Which sequence correctly traces the load path upward from the hook?",
     ["Hook, drum, runway rail, bridge girder, end truck",
      "Hook, load block, rope, drum, trolley, bridge girder, end truck, runway rail",
      "Hook, runway beam, trolley, drum, bridge girder",
      "Hook, bridge girder, rope, runway rail, drum"], 1,
     "Load travels hook and block, through the rope to the drum, through the trolley into "
     "the bridge girder, out to the end trucks and down onto the runway."),
    ("OHC.02.A.K3",
     "Rail sweeps are fitted to:",
     ["Lubricate the rail", "Ride ahead of the truck wheels and clear debris from the rail",
      "Absorb impact at the end of travel", "Ground the crane electrically"], 1,
     "Sweeps extend below the top of the rail ahead of the wheels so debris is pushed clear "
     "rather than climbed."),
    ("OHC.02.A.K5",
     "Camber on a bridge girder is:",
     ["Damage from overloading", "Designed-in upward curvature",
      "Side-to-side misalignment", "A type of rail joint"], 1,
     "Camber is built in. Losing it is the signal; having it is normal."),
    ("OHC.02.B.K2",
     "A holding brake on a crane hoist engages:",
     ["Only when the operator presses a brake control",
      "Automatically whenever power to the brake is removed",
      "Only at the upper limit", "Only when the load exceeds rated capacity"], 1,
     "The holding brake is self-setting and fail-safe. Control braking is the separate "
     "system that prevents overspeeding."),
    ("OHC.02.B.K4",
     "The upper limit switch may be used as a routine stop at the top of hoisting travel.",
     ["True", "False"], 1,
     "It is set by test with an empty hook and shall never be used as an operating control."),
    ("OHC.02.B.K1",
     "In a four-part reeving arrangement, the hook sees:",
     ["1:1 mechanical advantage", "2:1 mechanical advantage",
      "4:1 mechanical advantage and one quarter of drum line speed",
      "4:1 mechanical advantage and four times drum line speed"], 2,
     "Four parts share the load, so the trade is speed: four times the advantage, a quarter "
     "of the hook speed."),
    ("OHC.02.C.K1",
     "Compared with conductor bar, a festoon cable system:",
     ["Carries no voltage", "Encloses its conductors",
      "Requires no lockout", "Cannot be used on travelling cranes"], 1,
     "Festoon encloses the conductors; conductor bar leaves them exposed. Both still "
     "require lockout for work on the crane."),
    ("OHC.02.C.K2",
     "Before adjustments or repairs, the main or emergency switch must be:",
     ["Left energised so the crane can be moved", "Open and locked in the open position",
      "Switched to standby", "Tagged only, no lock required"], 1,
     "Open and locked open, controllers off, out-of-order signs visible from the floor, and "
     "rail stops where other cranes share the runway."),
    ("OHC.02.C.R2",
     "An operator notices the bridge stuttering and briefly losing power as it travels. "
     "The correct response is to:",
     ["Continue and report at end of shift", "Increase speed to push through the dead spot",
      "Land the load under control, stop, secure the crane and report",
      "Open the panel and clean the collector"], 2,
     "Intermittent pickup causes uncommanded motion. Operators secure and report; they do "
     "not troubleshoot energised crane electrics."),
]

GATE = [
    # ---- Task A
    ("OHC.02.A.K1",
     "Why does an operator need to be able to name the load path in order?",
     ["It is required on the data plate",
      "It determines what a noise, vibration or crack actually threatens",
      "It sets the crane's duty class", "It establishes the rated capacity"], 1, ""),
    ("OHC.02.A.K2",
     "Foundations, anchorages, runways and rail tracks are constructed or installed in "
     "accordance with:",
     ["The operator's judgement", "Local building code only",
      "The manufacturer's recommendations and the applicable ASME overhead crane volume",
      "Whatever the erector prefers"], 2, ""),
    ("OHC.02.A.K3",
     "A trolley stop that engages the tread of the wheel must be at least:",
     ["Equal to the radius of the wheel", "Equal to the diameter of the wheel",
      "One inch high", "Half the rail head thickness"], 0, ""),
    ("OHC.02.A.K4",
     "Footwalks on an overhead crane must provide a minimum headroom of:",
     ["36 inches", "42 inches", "48 inches", "60 inches"], 2, ""),
    ("OHC.02.A.K5",
     "Loss of camber in a bridge girder most directly indicates:",
     ["Normal thermal movement", "Structural distress requiring inspection escalation",
      "That the crane needs lubrication", "That the duty class should be raised"], 1, ""),
    ("OHC.02.A.R1",
     "An operator finds a loose rail splice and visible misalignment on the runway. The "
     "correct action is to:",
     ["Operate at reduced speed over that section",
      "Remove the crane from service and report the defect",
      "Operate normally &#8212; runway condition is not the operator's concern",
      "Operate only with light loads"], 1, ""),
    ("OHC.02.A.R2",
     "Contact with runway stops or other cranes is permitted only:",
     ["Never, under any circumstances",
      "With extreme caution, with particular care for persons on or below the crane, and "
      "only after making certain persons on the other cranes are aware",
      "At the end of each shift", "When the load is under 50&#37; of capacity"], 1, ""),
    ("OHC.02.A.R3",
     "Treating visible cracking, corrosion or loose fasteners as acceptable because the "
     "crane still runs is a failure of:",
     ["Load calculation", "Structural hazard recognition and reporting duty",
      "Signal communication", "Rigging selection"], 1, ""),
    # ---- Task B
    ("OHC.02.B.K1",
     "Close-fitting guards are required on the sheaves in the bottom block specifically to:",
     ["Keep the block clean", "Prevent ropes fouling when the block is on the ground with "
      "ropes slack", "Reduce noise", "Increase mechanical advantage"], 1, ""),
    ("OHC.02.B.K2",
     "Which statement about crane hoist braking is correct?",
     ["One brake performs both holding and control functions",
      "A self-setting holding brake holds the load; a separate control braking means "
      "prevents overspeeding, except on worm-geared hoists where the worm angle prevents it",
      "Control braking is optional on all hoists",
      "Holding brakes release automatically when power is removed"], 1, ""),
    ("OHC.02.B.K3",
     "Which chain is acceptable as a load chain on an overhead hoist?",
     ["Grade 30 proof coil", "Any chain of sufficient diameter",
      "Alloy chain rated for overhead lifting", "Galvanised utility chain"], 2, ""),
    ("OHC.02.B.K4",
     "The upper limit switch is correctly described as:",
     ["An operating control for the top of travel",
      "A test-set safety device that is never used as an operating control",
      "A load-limiting device", "A brake"], 1, ""),
    ("OHC.02.B.K5",
     "A crane data plate shows CMAA Class F. That means the crane is rated for:",
     ["Standby or infrequent service", "Moderate service",
      "Continuous severe service", "Outdoor service only"], 2, ""),
    ("OHC.02.B.R1",
     "Routinely running the block into the upper limit switch to stop hoisting is hazardous "
     "chiefly because it:",
     ["Wears the rope faster", "Masks the two-block failure path by making the last line "
      "of defence a routine control", "Drains the control transformer",
      "Voids the duty classification"], 1, ""),
    ("OHC.02.B.R2",
     "An operator detects the hoist brake allowing the load to drift downward with the "
     "controller in neutral. The correct action is to:",
     ["Continue but avoid heavy loads", "Set the load down and remove the crane from "
      "service", "Re-hoist and hold position with the controller",
      "Report it at the end of the shift"], 1, ""),
    ("OHC.02.B.R3",
     "Side loading the hoist and dragging loads primarily damages:",
     ["The warning device", "Reeving, drum wraps and the runway",
      "The data plate", "The pendant enclosure"], 1, ""),
    # ---- Task C
    ("OHC.02.C.K1",
     "The two common means of delivering power to a travelling overhead crane are:",
     ["Battery packs and solar panels", "Conductor bars with collectors, and festoon cable "
      "systems", "Trailing extension cords and generators",
      "Hydraulic lines and air lines"], 1, ""),
    ("OHC.02.C.K2",
     "Which is part of the required sequence before adjustments or repairs on a crane?",
     ["Leave one controller energised for testing",
      "Place warning or out-of-order signs on the crane and on the floor beneath or the "
      "hook, visible from the floor",
      "Move the crane to the centre of the runway",
      "Disconnect the warning device"], 1, ""),
    ("OHC.02.C.K3",
     "The maximum permitted voltage at pendant push-buttons is:",
     ["600 V a.c.", "150 V a.c. and 300 V d.c.", "480 V a.c.", "24 V d.c."], 1, ""),
    ("OHC.02.C.K4",
     "The requirement for an alarm or other effective warning signal on a power-travelling "
     "crane excepts:",
     ["Cab-operated cranes", "Floor-operated cranes",
      "Cranes under 5 tons", "Outdoor cranes"], 1, ""),
    ("OHC.02.C.K5",
     "Pendant strain relief exists so that:",
     ["The pendant floats at a fixed height",
      "The electrical cable never carries the mechanical weight of the pendant",
      "The buttons return to neutral", "The enclosure stays watertight"], 1, ""),
    ("OHC.02.C.R1",
     "During elevated access for inspection, the principal electrical hazard is:",
     ["Static discharge from the hook", "Contact with runway conductors or festoon "
      "components that remain energised", "Radio interference",
      "Battery acid from the transmitter"], 1, ""),
    ("OHC.02.C.R2",
     "Intermittent power pickup on the runway conductors is hazardous because it can "
     "produce:",
     ["A slow but predictable loss of capacity", "Unexpected or uncommanded motion",
      "Excess camber", "Increased rated load"], 1, ""),
    ("OHC.02.C.R3",
     "A crane's travel warning device has failed. The correct action is to:",
     ["Continue and shout warnings instead",
      "Remove the crane from service and report the defect",
      "Continue only during daylight hours",
      "Disable the device so it does not distract"], 1, ""),
]


def build():
    return A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)


if __name__ == "__main__":
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "out",
                                       "OHC_M02_ComponentsAndSystems.pre.html"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out):
        os.remove(out)
    html = build()
    with open(out, "w", encoding="ascii") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))


# Source map for the generated trace table: element -> (source, status)
TRACE_SOURCE = {
    "OHC.02.A.K1": ("derived from load-path analysis", "OK"),
    "OHC.02.A.K2": ("EM 385 &sect;16.M.02 &middot; ASME B30.2 / B30.17", "OK"),
    "OHC.02.A.K3": ("&sect;1910.179(e)(1),(2),(3),(4)", "OK"),
    "OHC.02.A.K4": ("&sect;1910.179(d) &middot; **Subpart D**", "OK"),
    "OHC.02.A.K5": ("&sect;1910.179(j)(3)(i),(ii)", "OK"),
    "OHC.02.A.R1": ("&sect;1910.179(j)(3) &middot; derived", "OK"),
    "OHC.02.A.R2": ("EM 385 &sect;16.M.06", "OK"),
    "OHC.02.A.R3": ("&sect;1910.179(j)(3)(i),(ii)", "OK"),
    "OHC.02.B.K1": ("&sect;1910.179(h)(1),(h)(2)(i)", "OK"),
    "OHC.02.B.K2": ("&sect;1910.179(f)(1)(i),(ii)", "OK"),
    "OHC.02.B.K3": ("ASME B30.16 &middot; &sect;1910.179(j)(2)(iv)", "OK"),
    "OHC.02.B.K4": ("**&sect;1910.179(n)(4)(ii)** + (k)(1)(ii)", "OK"),
    "OHC.02.B.K5": ("CMAA 70 duty classes", "CMAA74"),
    "OHC.02.B.R1": ("&sect;1910.179(n)(4)(ii) &middot; derived", "OK"),
    "OHC.02.B.R2": ("Tier 0 brake drift test &middot; &sect;1910.179(j)(3)(v)", "OK"),
    "OHC.02.B.R3": ("&sect;1910.179(n)(3)(iv)", "OK"),
    "OHC.02.C.K1": ("&sect;1910.179(e)(5)(ii) &middot; Tier 0", "OK"),
    "OHC.02.C.K2": ("**&sect;1910.179(l)(2)(i)(a)-(e)**", "OK"),
    "OHC.02.C.K3": ("&sect;1910.179(g)(1) &middot; **Subpart S**", "OK"),
    "OHC.02.C.K4": ("&sect;1910.179(i) &middot; EM 385 &sect;16.M.04", "BRANCH"),
    "OHC.02.C.K5": ("Tier 0 pendant criteria", "OK"),
    "OHC.02.C.R1": ("&sect;1910.179(e)(5)(ii) &middot; derived", "OK"),
    "OHC.02.C.R2": ("derived", "OK"),
    "OHC.02.C.R3": ("&sect;1910.179(i) &middot; derived", "OK"),
}

TRACE_PERF = [
    ("OHC.02.A.S1", "Trace the load path from hook to runway on the assigned crane"),
    ("OHC.02.A.S2", "Identify stops, bumpers and sweeps and confirm presence during inspection"),
    ("OHC.02.A.S3", "Report structural anomalies with location-specific descriptions"),
    ("OHC.02.B.S1", "Demonstrate limit switch verification without a load per the pre-use routine"),
    ("OHC.02.B.S2", "Verify brake holding on a test lift before full hoisting"),
    ("OHC.02.B.S3", "Identify rope, sheave and hook conditions requiring removal from service"),
    ("OHC.02.C.S1", "Locate and operate the crane disconnect for the assigned equipment"),
    ("OHC.02.C.S2", "Recognise conductor and festoon defects during pre-use inspection"),
    ("OHC.02.C.S3", "Execute a controlled stop and secure the crane on any electrical anomaly"),
]

TRACE_NOTES = [
    ("&#9888;&#65039; CMAA 74 not held",
     "`OHC.02.B.K5` duty classification is authored from **CMAA 70**, which is in the "
     "corpus. The ACS reference block cites *CMAA Spec 70 / 74*; **74 is not held**. "
     "Duty-class concepts are common to both, so the item stands &#8212; but any "
     "single-girder-specific claim needs 74 before it is made."),
    ("&#9888;&#65039; Branch-dependent content",
     "`OHC.02.C.K4` (warning device) rests on &sect;1910.179(i), which is **not** among "
     "the paragraphs carried onto the &sect;1926.1438(b) construction branch. EM 385 "
     "&sect;16.M.04 restores it on federal work regardless of installation status. The "
     "item is written to the facility branch; the branch split itself is taught in OHC-01."),
    ("&#9888;&#65039; Also facility-branch only",
     "`OHC.02.A.K3` draws on &sect;1910.179(e)(2) bridge bumpers and (e)(4) rail sweeps, "
     "neither of which is in the &sect;1926.1438(b)(2) list. (e)(1) trolley stops and "
     "(e)(3) trolley bumpers do carry across."),
    ("&#9989; Part 1910 handoffs honoured",
     "`OHC.02.A.K4` cites **Subpart D** and `OHC.02.C.K3` cites **Subpart S**, the two "
     "handoffs &sect;1910.179 makes by name. This closes the OHC-02 half of the Part 1910 map."),
]
