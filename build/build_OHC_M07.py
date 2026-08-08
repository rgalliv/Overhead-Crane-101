#!/usr/bin/env python3
"""OHC-07 Load Handling and Movement Control -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M07"
MODLABEL = "Module 7"
TITLE = "Load Handling and Movement Control"
SUBTITLE = ("Hoist, travel and place loads with the smoothness and path discipline that "
            "fixed-path equipment demands.")

OBJECTIVES = [
    "Execute vertical load handling from slack rope to suspended load, centred over the "
    "load, with the brake proved at low height.",
    "Control bridge and trolley travel, arrest load swing by following it, and hold "
    "clearance from structures, parallel cranes and cranes at other elevations.",
    "Place loads within tolerance without contact or shock, and verify load transfer "
    "before any rigging is slacked.",
]

SECTIONS = [
    ("A", "Hoisting Fundamentals",
     "Execute vertical load handling correctly from slack rope to suspended load."),
    ("B", "Travel and Drift Control",
     "Control bridge and trolley travel and arrest load swing."),
    ("C", "Precision Placement",
     "Place loads at target within tolerance without contact or shock."),
]

CONTENT = {
    "A": [
        ("Plumb before power",
         "The hook goes over the load before the load comes off the ground. "
         "&sect;1910.179(n)(3)(ii)(c) puts it as a pre-hoist condition: the hook shall be "
         "brought over the load <b>in such a manner as to prevent swinging</b>.",
         "A load lifted from off-plumb does not stay where it was. It swings to plumb the "
         "instant it breaks free, and it arrives at the plumb point with speed. The further "
         "off you started, the harder it arrives."),
        ("Slack, then load, then prove the brake",
         "Take the slack out slowly. Apply load gradually. Then stop a few inches up and "
         "<b>prove the brake before you commit</b>. &sect;1910.179(n)(3)(vii): the operator "
         "shall test the brakes <b>each time a load approaching the rated load is "
         "handled</b>, by raising the load a few inches and applying the brakes.",
         "There shall be <b>no downward drift</b> during that stop. This is the same pause "
         "that OHC-06 uses to check balance &#8212; one stop, three questions: does it hold, "
         "does it hang level, is the rigging taking load as expected."),
        ("Side pulls: not banned, but gated",
         "&sect;1910.179(n)(3)(iv) does <b>not</b> flatly prohibit side pulls. It permits "
         "them <i>&#8220;except when specifically authorized by a <b>responsible person</b> "
         "who has determined that the <b>stability of the crane is not thereby endangered</b> "
         "and that <b>various parts of the crane will not be overstressed</b>.&#8221;</i>",
         "Two determinations, one named role, before the pick. What is prohibited is the "
         "<b>unauthorised</b> side pull &#8212; which is every side pull an operator decides "
         "on alone, at the controls, because the load is nearly under the hook."),
        ("What a side pull actually damages",
         "The rope leaves the sheave groove and can jump the sheave entirely, cutting itself "
         "on the flange. Drum spooling goes irregular, so the next layer beds badly. The "
         "trolley takes side thrust its wheels and rails were never designed for.",
         "And the bridge girder takes a <b>lateral load</b> it was not designed for &#8212; "
         "an overhead crane is engineered for vertical load and horizontal travel, not for "
         "dragging. This is why the damage shows up in the runway, the trolley and the "
         "reeving, not in the hook."),
        ("Only as high as the job needs",
         "Travel height is a hazard setting, not a convenience. The rule is the <b>minimum "
         "practical height</b> that clears the path &#8212; the DOE Hanford manual states it "
         "as <i>&#8220;never raise the load higher than necessary.&#8221;</i>",
         "Height buys nothing and costs everything: a longer pendulum, a wider swing "
         "footprint, more energy in a drop, and a longer time to react. "
         "&sect;1910.179(n)(3)(vi) then adds the hard one &#8212; the employer shall require "
         "that the operator <b>avoid carrying loads over people</b>."),
        ("Two-blocking, and why the limit switch is not the answer",
         "<b>Two-blocking</b> is contact between the load block and the upper block, trolley "
         "or drum. Keep hoisting into it and something parts &#8212; usually the rope, with "
         "the load underneath.",
         "The upper limit switch exists to catch it. But &sect;1910.179(n)(4)(ii) says the "
         "switch <b>shall never be used as an operating control</b>, and (k)(1)(ii) explains "
         "why: its trip point is set by <b>test, with an empty hook</b>. It was never "
         "calibrated for a loaded block at speed. Prevention is yours: know your headroom, "
         "watch the block, slow the approach."),
        ("The other end of the drum",
         "The upper limit gets all the attention. The lower one is a number and it is "
         "absolute: &sect;1910.179(n)(3)(viii) &#8212; the load shall <b>not be lowered "
         "below the point where less than two full wraps of rope remain on the hoisting "
         "drum</b>.",
         "Those two wraps are what holds the rope's dead-end anchorage from taking the whole "
         "load. Deep pits, low floors and below-grade placements are where operators run out "
         "of drum, and a lower limit switch is not always fitted to stop them."),
    ],
    "B": [
        ("Two axes make one path",
         "Bridge and trolley are independent motions at right angles. Run them one at a time "
         "and the load walks an L. Run them <b>together</b> and the resultant is a diagonal "
         "&#8212; which is usually the shorter, smoother path and the one with fewer "
         "start-stop swing events.",
         "Diagonal travel is a skill, not a shortcut. The two motions have different speeds "
         "and different inertias, so holding a straight resultant means modulating both, not "
         "pinning both buttons and hoping."),
        ("Every swing has a cause and you supplied it",
         "A suspended load only swings if something accelerated it. The three causes: "
         "<b>acceleration</b> at the start, <b>deceleration</b> at the stop, and "
         "<b>plugging</b> &#8212; reversing the direction control while still moving, to brake.",
         "&sect;1910.179(n)(3)(iii)(a) is the rule underneath all three: during hoisting, "
         "care shall be taken that there is <b>no sudden acceleration or deceleration</b> of "
         "the moving load. Plugging is the most violent of the three and the most avoidable."),
        ("Arrest the swing by following it",
         "You cannot stop a pendulum by holding the pivot still. You stop it by <b>moving the "
         "pivot under the load</b> &#8212; drive the trolley or bridge in the direction the "
         "load is swinging, then ease off as the load comes back to plumb beneath the hook.",
         "Fighting the swing feeds it. Following it kills it in one or two cycles. The "
         "technique is the same at every scale; only the timing changes with rope length."),
        ("Inching and float",
         "<b>Inching</b> is momentary control taps &#8212; short pulses that move the crane a "
         "fraction and let it settle, used for the last few inches of approach. On a "
         "variable-frequency drive it is the lowest speed step; on a two-speed contactor "
         "crane it is discipline with the first notch.",
         "<b>Float</b> is holding the load just clear of the surface while alignment is "
         "confirmed. Both trade speed for control, and both are the difference between "
         "placing a load and landing one."),
        ("Clearance is a duty, continuously",
         "<b>EM 385-1-1 16-8.aa(5)</b> is the operating rule: clearance shall be maintained "
         "between the crane and <b>any structure or object</b>, <b>any parallel running "
         "cranes</b>, and <b>cranes operating at different elevations</b>.",
         "All three, all the time. The one operators lose is the third &#8212; a crane on a "
         "different runway at a different height is outside the normal scan and is the one "
         "that surprises people."),
        ("The 3 and 2 are design numbers, not your margin",
         "&sect;1910.179(b)(6)(i) sets a <b>minimum 3 in overhead and 2 in lateral</b> "
         "clearance, in conformity with <b>CMAA Specification No. 61</b>, incorporated by "
         "reference through &sect;1910.6. (b)(7) adds clearance between parallel cranes.",
         "Read what that is: it is the clearance the <b>installed crane structure</b> has "
         "from the building. It is not an operating tolerance for a swinging load, and "
         "quoting it as one is a category error. Your working clearance is set by the load, "
         "the swing and the path &#8212; and it is a great deal more than two inches."),
        ("Approaching stops and other cranes",
         "<b>EM 385-1-1 16-8.aa(6)</b>: contacts with <b>runway stops or other cranes</b> "
         "shall be made with <b>extreme caution</b>, with particular care for persons on or "
         "below the crane, and <b>only after making certain that persons on the other cranes "
         "are aware</b>.",
         "Note what it does not say. It does not prohibit contact &#8212; bumping a stop is a "
         "normal end-of-runway event. It requires that it be deliberate, slow, and known "
         "about by everyone it could affect."),
        ("Sound the warning",
         "&sect;1910.179(n)(3)(xi) names two triggers: <b>when starting the bridge</b>, and "
         "<b>when the load or hook approaches near or over personnel</b>. The warning signal "
         "shall be sounded.",
         "It is a habit that decays fastest in familiar bays, where the operator knows who is "
         "where &#8212; which is precisely where the person who moved is not accounted for."),
    ],
    "C": [
        ("Take the axes off one at a time",
         "A precision placement is not one manoeuvre, it is a controlled reduction. Bring the "
         "load close on all axes, then <b>settle one axis at a time</b> &#8212; stop the "
         "bridge, let it settle, correct the trolley, let it settle, then lower.",
         "Compounding motions on final approach is how a placement becomes a collision. Every "
         "motion you still have running is a variable you are managing while the load is "
         "inches from something hard."),
        ("Set-down is a transfer, not a drop",
         "Lower until the <b>load takes its own weight</b> and the rope begins to slack. Stop "
         "there. That is the transfer point, and it is where you confirm the load is seated, "
         "stable and bearing where it is meant to bear.",
         "Watch the rope, not the load. Rope going slack unevenly means the load is seating on "
         "one corner &#8212; it will tip or slide when you continue. Take it back up and "
         "reset."),
        ("Fixtures, machines and racks",
         "Placing into something is harder than placing onto something. Fixtures and racks add "
         "close-tolerance contact hazards on three or four sides at once, and the load blocks "
         "the operator's view of exactly the surfaces that matter.",
         "Machines add a second problem: the thing you are placing into may be capable of "
         "moving, powered, or holding stored energy. Placement into a machine is an energy "
         "control question before it is a crane question."),
        ("Blind placements belong to the signaler",
         "When the operator cannot see the landing point, the placement is executed on "
         "signals. The operator's judgement does not fill the gap &#8212; it substitutes a "
         "guess for information.",
         "The discipline that makes it safe: one signaler, agreed before the lift, "
         "continuously visible. <b>Signal lost, motion stops.</b> Signalling is developed in "
         "OHC-09; here the point is narrower &#8212; a blind placement without a signaler is "
         "not a placement, it is a hope."),
        ("Verify transfer before slacking anything",
         "The load is fully transferred when it is <b>stable, supported and bearing as "
         "intended</b>. Until all three are confirmed, the rigging stays under tension and "
         "the crane stays engaged.",
         "&sect;1910.179(n)(3)(x): the operator <b>does not leave the position at the "
         "controls while the load is suspended</b>. A load resting but not yet verified is "
         "still the crane's load."),
        ("The moment that crushes people",
         "Set-down is where hands go in. The load is low, it looks placed, the job is nearly "
         "done, and someone reaches to guide a corner or free a sling. The load is still "
         "moving, still capable of shifting, and it weighs what it always weighed.",
         "&sect;1910.179(n)(3)(v) covers the extreme case: while any employee is <b>on the "
         "load or hook</b>, there shall be <b>no hoisting, lowering, or traveling</b>. The "
         "working rule is broader &#8212; hands stay out until the load is verified down."),
    ],
}

PRACTICE = [
    ("OHC.07.A.K1",
     "Bringing the hook plumb over the load before hoisting is required because:",
     ["It looks more professional", "A load lifted off-plumb swings to plumb the instant it "
      "breaks free", "It reduces motor current", "It is only needed for heavy loads"], 1,
     "&sect;1910.179(n)(3)(ii)(c) requires the hook be brought over the load so as to prevent "
     "swinging. The load will find plumb whether you planned for it or not."),
    ("OHC.07.A.K3",
     "Side pulls with an overhead crane are:",
     ["Always prohibited", "Permitted only when specifically authorised by a responsible "
      "person who has made two determinations", "Permitted at the operator's discretion "
      "below 50&#37; of rated load", "Permitted with a spotter"], 1,
     "&sect;1910.179(n)(3)(iv) is conditional: stability not endangered, and parts not "
     "overstressed, determined by a responsible person."),
    ("OHC.07.A.K5",
     "The upper limit switch is adequate protection against two-blocking during a high "
     "placement.",
     ["True", "False"], 1,
     "(n)(4)(ii) forbids using it as an operating control; (k)(1)(ii) sets its trip point by "
     "test with an empty hook, not a loaded block at speed."),
    ("OHC.07.B.K2",
     "Reversing the direction control to brake a moving crane is called:",
     ["Inching", "Floating", "Plugging", "Following"], 2,
     "Plugging. It is the most violent of the three swing causes and the most avoidable."),
    ("OHC.07.B.K2b",
     "A load is swinging. The correct correction is to:",
     ["Hold the bridge and trolley still until it settles",
      "Drive in the direction of the swing, then ease off as the load comes plumb",
      "Drive against the swing to oppose it", "Lower the load quickly to shorten the rope"],
     1,
     "Follow technique. You stop a pendulum by moving the pivot under the load, not by "
     "holding the pivot still."),
    ("OHC.07.B.K4",
     "The 3 in overhead and 2 in lateral figures in &sect;1910.179(b)(6)(i) are:",
     ["The operating clearance an operator must keep around a load",
      "Design clearances for the installed crane structure from the building",
      "The maximum permitted clearance", "Applicable only to gantry cranes"], 1,
     "They are installation clearances per CMAA Spec No. 61. Working clearance for a moving "
     "load is a great deal more."),
    ("OHC.07.C.K2",
     "During set-down, the rope begins to slack unevenly. This means:",
     ["The load is fully seated", "The load is seating on one corner and may tip or slide",
      "The brake is failing", "The hoist is overloaded"], 1,
     "Uneven slack means uneven seating. Take it back up and reset."),
    ("OHC.07.C.K5",
     "Rigging may be slacked once the load is resting on the surface.",
     ["True", "False"], 1,
     "Resting is not verified. The load must be stable, supported and bearing as intended "
     "before tension comes off."),
    ("OHC.07.C.R1",
     "The highest-exposure moment for crushing injury in a placement is:",
     ["During the initial hoist", "During travel at height", "At set-down",
      "During the pre-lift inspection"], 2,
     "Set-down is where hands go in while the load is still capable of shifting."),
]

GATE = [
    # ---- Task A
    ("OHC.07.A.K1",
     "Before hoisting, the hook must be brought over the load in a manner that:",
     ["Minimises rope wear", "Prevents swinging", "Speeds up the pick",
      "Keeps the load block visible"], 1, ""),
    ("OHC.07.A.K2",
     "&sect;1910.179(n)(3)(vii) requires the operator to test the brakes:",
     ["Once per shift", "Each time a load approaching the rated load is handled, by raising "
      "it a few inches and applying the brakes", "Only after maintenance",
      "Only on the main hoist"], 1, ""),
    ("OHC.07.A.K3",
     "Under &sect;1910.179(n)(3)(iv), a side pull is permitted when:",
     ["The operator judges the load light enough",
      "A responsible person has specifically authorised it, having determined that crane "
      "stability is not endangered and that parts will not be overstressed",
      "Never, under any circumstances", "A signaler is present"], 1, ""),
    ("OHC.07.A.K3b",
     "The damage caused by side pulling shows up chiefly in the:",
     ["Hook and latch", "Runway, trolley and reeving", "Pendant and controls",
      "Load block casting"], 1, ""),
    ("OHC.07.A.K4",
     "The correct travel height for a load is:",
     ["As high as the crane will lift, for maximum clearance",
      "The minimum practical height that clears the path",
      "Half the available hook height", "Whatever the signaler prefers"], 1, ""),
    ("OHC.07.A.K4b",
     "&sect;1910.179(n)(3)(vi) requires the employer to ensure the operator:",
     ["Sounds the warning at every start", "Avoids carrying loads over people",
      "Keeps the load below 10 ft", "Uses two tag lines"], 1, ""),
    ("OHC.07.A.K5",
     "Two-blocking is:",
     ["Lifting two loads at once", "Contact between the load block and the upper block, "
      "trolley or drum", "Using two hoists on one load",
      "Blocking the runway with two cranes"], 1, ""),
    ("OHC.07.A.K5b",
     "&sect;1910.179(n)(3)(viii) sets a lower-travel limit: the load shall not be lowered "
     "below the point where less than:",
     ["One full wrap of rope remains on the drum",
      "Two full wraps of rope remain on the drum",
      "Three full wraps of rope remain on the drum",
      "The drum is half empty"], 1, ""),
    ("OHC.07.A.R1",
     "A side pull disguised as a convenience move is dangerous chiefly because:",
     ["It is slower than repositioning", "It bypasses the responsible-person determination "
      "that the crane will not be overstressed", "It wears the hoist motor",
      "It requires a second operator"], 1, ""),
    ("OHC.07.A.R2",
     "A load must cross an occupied work area. The correct action is:",
     ["Travel faster to reduce exposure time", "Raise the load higher and proceed",
      "Clear the area or reroute the path", "Sound the warning and proceed"], 2, ""),
    ("OHC.07.A.R3",
     "Riding the upper limit switch to gain height on a placement is hazardous because:",
     ["It wastes time", "The switch's trip point was set by test with an empty hook and is "
      "not a control", "It drains the battery", "It voids the inspection record"], 1, ""),
    # ---- Task B
    ("OHC.07.B.K1",
     "A diagonal load path is best achieved by:",
     ["Running the bridge, then the trolley", "Running the trolley, then the bridge",
      "Running bridge and trolley simultaneously and modulating both",
      "Swinging the load into position"], 2, ""),
    ("OHC.07.B.K2",
     "The three operator-supplied causes of load swing are:",
     ["Wind, vibration and rope stretch",
      "Acceleration, deceleration and plugging",
      "Overload, side pull and two-blocking",
      "Inching, floating and following"], 1, ""),
    ("OHC.07.B.K2b",
     "Drift arrest by follow technique means:",
     ["Holding all motion still until the swing decays",
      "Moving the bridge or trolley in the direction of the swing, then easing off as the "
      "load comes plumb", "Driving against the swing to oppose it",
      "Plugging the motion to absorb the energy"], 1, ""),
    ("OHC.07.B.K3",
     "Inching is used to:",
     ["Travel long distances efficiently", "Move a fraction at a time on final approach and "
      "let the load settle", "Test the brakes", "Arrest a swing"], 1, ""),
    ("OHC.07.B.K4",
     "EM 385-1-1 16-8.aa(5) requires clearance to be maintained from:",
     ["Structures only", "Structures and parallel running cranes only",
      "Structures or objects, parallel running cranes, and cranes operating at different "
      "elevations", "Other cranes only when they are loaded"], 2, ""),
    ("OHC.07.B.K4b",
     "The 3 in overhead / 2 in lateral clearance of &sect;1910.179(b)(6)(i), per CMAA "
     "Specification No. 61, is:",
     ["The operating clearance to keep around a travelling load",
      "A design clearance for the installed crane structure",
      "The tolerance for precision placement", "A rigging clearance"], 1, ""),
    ("OHC.07.B.K5",
     "EM 385-1-1 16-8.aa(6) requires that contacts with runway stops or other cranes be made:",
     ["Never -- contact is prohibited",
      "With extreme caution, with care for persons on or below, and only after making "
      "certain persons on the other cranes are aware",
      "At full speed to ensure positive seating", "Only by a designated person"], 1, ""),
    ("OHC.07.B.K5b",
     "&sect;1910.179(n)(3)(xi) requires the warning signal to be sounded:",
     ["Only at the start of the shift",
      "When starting the bridge, and when the load or hook approaches near or over personnel",
      "Only when the load is over rated capacity", "Continuously during travel"], 1, ""),
    ("OHC.07.B.R1",
     "An uncontrolled swing is more dangerous than its load weight suggests because:",
     ["It increases motor current", "The load's footprint becomes far larger than the load, "
      "reaching into areas judged clear", "It shortens rope life",
      "It triggers the limit switch"], 1, ""),
    ("OHC.07.B.R2",
     "Two cranes share a runway and both operators are working independently. The missing "
     "control is:",
     ["A second signaler", "Communication, and for a shared lift one qualified responsible "
      "person in charge", "Higher travel speed", "A written lift plan for each crane"],
     1, ""),
    ("OHC.07.B.R3",
     "Travelling with attention on the destination rather than the path leads to:",
     ["Slower cycle times", "Contact with obstructions and personnel that were in the path "
      "but outside the operator's focus", "Excessive brake wear",
      "Limit switch nuisance trips"], 1, ""),
    # ---- Task C
    ("OHC.07.C.K1",
     "Final approach to a placement is best executed by:",
     ["Running all motions together until the load arrives",
      "Settling one axis at a time, letting the load settle between corrections",
      "Lowering first, then positioning", "Swinging the load onto target"], 1, ""),
    ("OHC.07.C.K2",
     "The set-down transfer point is reached when:",
     ["The load touches the surface", "The load takes its own weight and the rope begins to "
      "slack", "The rigging goes fully slack", "The hoist brake sets"], 1, ""),
    ("OHC.07.C.K3",
     "Placement into a powered machine raises a hazard beyond contact damage:",
     ["Increased load weight", "Stored or hazardous energy in the receiving equipment",
      "Reduced hook clearance", "Longer rope length"], 1, ""),
    ("OHC.07.C.K4",
     "On a blind placement, if the signaler is lost from view the operator shall:",
     ["Continue at reduced speed", "Complete the placement using judgement",
      "Stop all motion", "Sound the warning and continue"], 2, ""),
    ("OHC.07.C.K5",
     "Load transfer is verified when the load is:",
     ["Touching the surface", "Stable, supported, and bearing as intended",
      "Below the hook", "Released by the rigger"], 1, ""),
    ("OHC.07.C.K5b",
     "&sect;1910.179(n)(3)(x) requires that the operator:",
     ["Sound the warning before lowering",
      "Not leave the position at the controls while the load is suspended",
      "Log every placement", "Remain in the cab for the whole shift"], 1, ""),
    ("OHC.07.C.R1",
     "Hands and body parts are most exposed to crushing:",
     ["During the pre-lift inspection", "At set-down, while the load is low and still "
      "capable of shifting", "During travel at height", "While rigging the load"], 1, ""),
    ("OHC.07.C.R2",
     "Slacking the rigging before the load is verified stable risks:",
     ["Rope damage only", "The load tipping or sliding with no crane restraint left",
      "A limit switch trip", "Brake overheating"], 1, ""),
    ("OHC.07.C.R3",
     "Contact damage during placement is best prevented by:",
     ["Faster approach to reduce exposure", "Axis-by-axis motion reduction and float before "
      "committing to the set-down", "Raising the load higher before descending",
      "Using a second hoist"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.07.A.K1": ("**&sect;1910.179(n)(3)(ii)(c)** &#8212; both branches", "OK"),
    "OHC.07.A.K2": ("**&sect;1910.179(n)(3)(vii)**", "OK"),
    "OHC.07.A.K3": ("**&sect;1910.179(n)(3)(iv)**", "ACSFIX"),
    "OHC.07.A.K3b": ("derived &middot; Tier 0", "OK"),
    "OHC.07.A.K4": ("**DOE Hanford TR244C** &middot; derived", "OK"),
    "OHC.07.A.K4b": ("**&sect;1910.179(n)(3)(vi)**", "OK"),
    "OHC.07.A.K5": ("**&sect;1910.179(n)(4)(ii)** &middot; (k)(1)(ii)", "OK"),
    "OHC.07.A.K5b": ("**&sect;1910.179(n)(3)(viii)**", "GAP"),
    "OHC.07.A.R1": ("&sect;1910.179(n)(3)(iv) &middot; derived", "OK"),
    "OHC.07.A.R2": ("&sect;1910.179(n)(3)(vi) &middot; derived", "OK"),
    "OHC.07.A.R3": ("**&sect;1910.179(k)(1)(ii)** &middot; (n)(4)(ii)", "OK"),
    "OHC.07.B.K1": ("Tier 0 `Overhead Crane Training Rev 2` Slide 91", "OK"),
    "OHC.07.B.K2": ("**&sect;1910.179(n)(3)(iii)(a)** &middot; Tier 0", "OK"),
    "OHC.07.B.K2b": ("Tier 0 &middot; derived", "OK"),
    "OHC.07.B.K3": ("Tier 0 &middot; derived", "OK"),
    "OHC.07.B.K4": ("**EM 385 16-8.aa(5)**", "OK"),
    "OHC.07.B.K4b": ("**&sect;1910.179(b)(6)(i)** &middot; **CMAA 61** via &sect;1910.6",
                     "OK"),
    "OHC.07.B.K5": ("**EM 385 16-8.aa(6)**", "OK"),
    "OHC.07.B.K5b": ("**&sect;1910.179(n)(3)(xi)**", "OK"),
    "OHC.07.B.R1": ("derived &middot; `OHC.06.C.K5`", "OK"),
    "OHC.07.B.R2": ("**&sect;1910.179(n)(3)(ix)**", "OK"),
    "OHC.07.B.R3": ("derived", "OK"),
    "OHC.07.C.K1": ("derived &middot; Tier 0", "OK"),
    "OHC.07.C.K2": ("derived &middot; **DOE Hanford TR244C**", "OK"),
    "OHC.07.C.K3": ("derived &middot; &sect;1910.147 cross-ref", "OK"),
    "OHC.07.C.K4": ("derived &middot; `OHC-09` signalling", "OK"),
    "OHC.07.C.K5": ("derived", "OK"),
    "OHC.07.C.K5b": ("**&sect;1910.179(n)(3)(x)**", "OK"),
    "OHC.07.C.R1": ("**&sect;1910.179(n)(3)(v)** &middot; derived", "OK"),
    "OHC.07.C.R2": ("derived", "OK"),
    "OHC.07.C.R3": ("derived", "OK"),
}

TRACE_PERF = [
    ("OHC.07.A.S1", "Center the trolley and bridge over a load without a plumb reference"),
    ("OHC.07.A.S2", "Execute lift-off with brake check and controlled acceleration"),
    ("OHC.07.A.S3", "Complete a high placement with margin below the upper limit"),
    ("OHC.07.B.S1", "Demonstrate swing arrest using motion-follow technique"),
    ("OHC.07.B.S2", "Navigate a defined obstacle path within clearance tolerances"),
    ("OHC.07.B.S3", "Coordinate shared-runway movement with a second crane operator"),
    ("OHC.07.C.S1", "Complete a precision placement within stated tolerance"),
    ("OHC.07.C.S2", "Execute a signaler-directed blind placement"),
    ("OHC.07.C.S3", "Demonstrate controlled set-down and safe rigging release"),
]

TRACE_NOTES = [
    ("&#9888;&#65039; `A.K3` corrects the ACS &#8212; side pulls are conditional, not banned",
     "The ACS states `A.K3` as *&#8220;prohibition on side pulling.&#8221;* "
     "**&sect;1910.179(n)(3)(iv)** does not prohibit it: cranes shall not be used for side "
     "pulls *&#8220;except when specifically authorized by a responsible person who has "
     "determined that the stability of the crane is not thereby endangered and that various "
     "parts of the crane will not be overstressed.&#8221;* Two determinations, one named "
     "role. `A.K3` is written to the standard and teaches the authorisation test; `A.K3b` "
     "keeps the ACS's damage-mechanism content. Teaching a flat ban is both wrong and "
     "fragile &#8212; any experienced operator in the room will contradict it, and the "
     "instructor loses the rest of the session."),
    ("&#9888;&#65039; `A.K5b` fills an ACS gap &#8212; two full wraps",
     "`A.K5` covers **two-blocking**, which is the *upper* end of hoist travel. The ACS has "
     "nothing for the lower end. **&sect;1910.179(n)(3)(viii)** &#8212; *the load shall not "
     "be lowered below the point where less than two full wraps of rope remain on the "
     "hoisting drum* &#8212; is a hard numeric operator-owned limit, and a lower limit "
     "switch is not always fitted to enforce it. Deep pits and below-grade placements are "
     "where operators run out of drum. **Recommend adding this to the ACS as a K element in "
     "Task A.**"),
    ("&#9989; `B.K4b` separates a design clearance from an operating one",
     "`B.K4` is sourced by the ACS to **EM 385 16-8.aa(5)**, which is the correct operating "
     "duty. `B.K4b` adds **&sect;1910.179(b)(6)(i)** &#8212; *minimum 3 in overhead, 2 in "
     "lateral*, per **CMAA Specification No. 61**, incorporated via **&sect;1910.6** "
     "&#8212; and teaches explicitly that these are **installation clearances for the crane "
     "structure**, not an operating tolerance for a moving load. Quoting the 2 in figure as "
     "a working margin is a category error worth pre-empting."),
    ("&#9989; Paragraph (n) binds on both branches",
     "Unlike OHC-05, this module needs no branch caveat. **&sect;1910.179(n)** is in the "
     "**&sect;1926.1438(b)(2)** incorporation list, so every (n) citation here applies "
     "whether the crane is permanently installed or not. Eleven of the twenty-nine gate "
     "items rest on (n)."),
    ("&#9989; Three (n) provisions the ACS does not reach, now gated",
     "**(n)(3)(xi)** warning signal on starting the bridge and on approach to personnel "
     "&#8594; `B.K5b`. **(n)(3)(x)** operator shall not leave the controls while the load is "
     "suspended &#8594; `C.K5b`. **(n)(3)(v)** no hoisting, lowering or traveling while any "
     "employee is on the load or hook &#8594; `C.R1`. All three are operator-conduct rules "
     "with no ACS element of their own."),
    ("&#9432; Elements carrying a second item",
     "`A.K3`, `A.K4`, `A.K5`, `B.K2`, `B.K4`, `B.K5` and `C.K5` each carry two items. In "
     "`A.K3` and `A.K5` the split separates the corrected regulatory rule from the ACS's "
     "original content; elsewhere it separates two independently testable facts."),
]


def main():
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "OHC_M07_LoadHandling.pre.html")
    with open(out, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))


if __name__ == "__main__":
    main()
