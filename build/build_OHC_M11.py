#!/usr/bin/env python3
"""OHC-11 Malfunctions and Emergency Procedures -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M11"
MODLABEL = "Module 11"
TITLE = "Malfunctions and Emergency Procedures"
SUBTITLE = ("Respond correctly to equipment malfunctions, stranded loads, and emergency "
            "events.")

OBJECTIVES = [
    "Respond to loss of power or control with a suspended load, secure the area, and hand the "
    "recovery to the people authorised to perform it.",
    "Recognise overtravel, brake and mechanical malfunctions as stop triggers, and hold the "
    "crane out of service until it has been inspected.",
    "Manage dropped loads, contact events, injuries and fire, preserve the scene, and produce "
    "a factual account.",
]

SECTIONS = [
    ("A", "Power and Control Failures",
     "Respond to loss of power or control with a suspended load."),
    ("B", "Overtravel and Mechanical Malfunctions",
     "Respond to limit failures, brake malfunction, and abnormal mechanical events."),
    ("C", "Emergency Events",
     "Manage dropped loads, contact events, injuries, and fire."),
]

CONTENT = {
    "A": [
        ("Power loss holds the load &#8212; by design",
         "&sect;1910.179(a)(20) defines it: <i>a <b>holding brake</b> is a brake that "
         "<b>automatically prevents motion when power is off</b></i>. And "
         "&sect;1910.179(f)(2)(iii) requires it: <i>holding brakes on hoists shall be "
         "<b>applied automatically when power is removed</b></i>.",
         "So the expected behaviour on a power failure is that the load <b>stops and stays</b>. "
         "The hazard of a power loss is not the drop &#8212; it is everything people do next."),
        ("Two brake systems, and a branch split",
         "&sect;1910.179(f)(1)(i): each independent hoisting unit shall have <b>at least one "
         "self-setting brake</b>, the holding brake, applied directly to the motor shaft or "
         "part of the gear train. <b>(f)(1)(ii)</b> adds a second system &#8212; <b>control "
         "braking means to prevent overspeeding</b>, in addition to the holding brake.",
         "Note the branch line. <b>(f)(1)</b> is in the &sect;1926.1438(b)(2) list, so the "
         "self-setting brake is required on <b>both</b> branches. <b>(f)(2)</b> is <b>not</b> "
         "&#8212; so the *applied automatically when power is removed* wording, and the "
         "torque percentages at (f)(2)(i), are <b>facility branch</b>. The ACS's phrase "
         "<i>&#8220;spring-set&#8221;</i> names a common mechanism; the standard names a "
         "<b>behaviour</b>, and is deliberately mechanism-agnostic."),
        ("A stranded load is a scene, not a problem to solve",
         "The load is held. That is the system working. The correct response is to <b>secure "
         "the area beneath and around it</b>, keep everyone out, and notify. Nothing about a "
         "stranded load requires speed.",
         "What it does not require is <b>improvisation</b>. Recovery of a suspended load on a "
         "failed crane is an engineered operation, and the operator's job ends at securing and "
         "reporting."),
        ("Never release a brake to get a load down",
         "The single most dangerous action available to a person standing next to a stranded "
         "load is manually releasing the holding brake. There is no controlled descent at the "
         "other end of that decision &#8212; there is a free fall with the load's full weight "
         "and no braking system in the path.",
         "&sect;1910.179(l)(3)(i) closes the door on it from the other side: <b>adjustments "
         "and repairs shall be done only by designated personnel</b>. Releasing a brake is an "
         "adjustment."),
        ("The disconnect, and when to use it",
         "&sect;1910.179(g)(5)(i) puts the runway conductor supply on a switch or breaker on a "
         "<b>fixed structure, accessible from the floor, lockable in the open position</b>. "
         "(g)(5)(ii) and (iii) put a second one on the crane, reachable by the operator.",
         "Isolate when the crane is <b>doing something it was not told to do</b>, or when it "
         "must stay stopped while people work near or under it. &sect;1910.179(l)(2)(i)(c) is "
         "the standard's own sequence: the main or emergency switch <b>open and locked in the "
         "open position</b>. That lockout implements the employer's <b>&sect;1910.147</b> "
         "energy-control programme (held). The operator is typically an <b>affected</b> "
         "employee &#8212; isolation is applied by an authorized employee."),
        ("What a control malfunction looks like",
         "Three signatures. <b>Unresponsive</b> &#8212; a motion that will not start. "
         "<b>Sticking</b> &#8212; a controller or button that does not return to off when "
         "released. <b>Self-motion</b> &#8212; the crane moving with no input at all.",
         "The standard treats the second and third as regulated failures. "
         "&sect;1910.179(g)(3)(vi) requires floor-operated controllers to <b>automatically "
         "return to the off position when released</b>; (g)(3)(vii) requires pendant "
         "pushbuttons to <b>return to off when pressure is released</b>; (g)(3)(ix) requires "
         "that on <b>remote-operated</b> cranes, if the control signal <b>becomes ineffective "
         "the crane motion shall stop</b>. A control that holds a motion after release is a "
         "failed safety function, not a quirk."),
        ("Why the E-stop is the answer and the controller is not",
         "&sect;1910.179(a)(59): an <b>emergency stop switch</b> is a switch <b>to cut off "
         "electric power independently of the regular operating controls</b>.",
         "That phrase is the whole reason it exists. If the controller is the thing that has "
         "failed, then working the controller harder is asking the failed component to fix "
         "itself. The E-stop takes a <b>different path</b> to the same result. On a sticking "
         "or self-moving crane it is the first action, not the last resort. "
         "&sect;1910.179(a)(40) names the design principle: <b>fail-safe</b> means a provision "
         "designed to automatically stop or safely control any motion in which a malfunction "
         "occurs."),
        ("Re-energising is a decision, and it is not the operator's",
         "Restoring power to a crane whose failure is not understood can restart the motion "
         "that caused the problem &#8212; now with people nearby who believe the crane is "
         "dead.",
         "The failure is diagnosed before the crane is re-energised, by the people authorised "
         "to diagnose it. The operator's contribution is an accurate account of <b>what the "
         "crane did</b>, which is worth more than a theory about why."),
    ],
    "B": [
        ("A two-block event is a rope event",
         "Two-blocking loads the rope and reeving against a hard stop. The damage is in the "
         "<b>rope, the sheaves and the terminations</b>, and it is frequently invisible from "
         "the floor.",
         "The response is <b>stop, and do not move</b> &#8212; not even to lower the load, "
         "until the rope and reeving have been assessed. The next motion is the one that "
         "finds out whether the rope is still whole."),
        ("A limit switch that fails verification",
         "&sect;1910.179(n)(4)(i) ends with the duty: <i>if the switch <b>does not operate "
         "properly, the appointed person shall be immediately notified</b></i>. Immediately, "
         "and to a named role.",
         "The ACS states this as <i>&#8220;crane out of service.&#8221;</i> That is the right "
         "outcome, and it arrives via <b>&sect;1910.179(l)(3)(i)</b> &#8212; unsafe conditions "
         "disclosed by inspection <b>corrected before operation is resumed</b>. The regulation "
         "names the <b>notification</b>; the out-of-service state follows from it. Teach both "
         "halves, because the notification is the one that gets skipped."),
        ("Brake drift is not a control problem",
         "A load that creeps down with the controller at off is a brake that is no longer "
         "holding. The instinct is to correct it with hoist inputs &#8212; and that hides a "
         "failing brake behind operator effort for as long as the operator keeps doing it.",
         "The correct response is to <b>set the load down</b> at the first safe opportunity "
         "and take the crane out of service. Remember there are two systems: the <b>holding</b> "
         "brake at (f)(1)(i) and the <b>control braking means</b> at (f)(1)(ii). Drift points "
         "at the holding brake."),
        ("Noise, vibration and rope behaviour are stop triggers",
         "A new sound, a new vibration, or rope that is doing something it did not do "
         "yesterday &#8212; jumping a groove, spooling unevenly, slapping &#8212; is "
         "information arriving early. Machines usually announce failures before they complete "
         "them.",
         "The discipline is treating <b>new</b> as the trigger, not <b>loud</b>. A quiet new "
         "noise is a better signal than a loud familiar one."),
        ("Equipment character is a story people tell",
         "Every long-serving crane accumulates a set of noises the crew has agreed to find "
         "normal. Some genuinely are. The problem is that the agreement is never revisited, so "
         "a new sound gets absorbed into the existing story on the day it appears.",
         "The counter is a written baseline and a low threshold for reporting. <i>&#8220;It's "
         "always done that&#8221;</i> is a claim about history, and it needs a date."),
        ("Post-event inspection before return to service",
         "After any two-block, contact or mechanical event, the crane is inspected before it "
         "runs again. &sect;1910.179(l)(3)(i) requires unsafe conditions <b>corrected before "
         "operation is resumed</b>, and <b>(l)(2)(ii)</b> holds the crane until <b>all guards "
         "are reinstalled, safety devices reactivated, and maintenance equipment removed</b>.",
         "Both are in paragraphs (l) &#8212; <b>facility branch</b>. On the construction "
         "branch the inspection authority is &sect;1926.1412 (held in OHC-05): a competent "
         "person begins the shift visual inspection under (d)(1). The operator's duty is "
         "the same either way: the crane does not run until somebody qualified says it may."),
    ],
    "C": [
        ("Dropped load and struck-by, in order",
         "The sequence is fixed and the order matters: <b>aid</b> to anyone injured, "
         "<b>control of the area</b> so nobody becomes the second casualty, then "
         "<b>notification</b> up the line.",
         "Aid comes first, but it does not come recklessly. A dropped load leaves an unstable "
         "scene &#8212; the load itself, the rigging, whatever it struck, and possibly the "
         "crane. Entering an uncontrolled scene to help is how one casualty becomes two."),
        ("Contact events hold two machines, not one",
         "A crane-to-crane or crane-to-structure contact puts <b>both</b> systems in question. "
         "The other crane took the same impact, and the structure may have taken load it was "
         "not designed for.",
         "So the hold is on both. The instinct is to check your own crane, find nothing, and "
         "carry on &#8212; leaving a struck crane in service with an undiscovered defect and "
         "another operator on it. Cross-refs `OHC.08.B.R3`."),
        ("Fire: the cab is a dead end",
         "&sect;1910.179(o)(3) sets the baseline: the employer shall ensure operators are "
         "<b>familiar with the operation and care of the fire extinguishers provided</b>. "
         "Familiar with, before the day it matters.",
         "The extinguisher decision is bounded: fight only a <b>small</b> fire, only with your "
         "<b>egress secured behind you</b>, and only if it is not growing. A cab has one way "
         "out along a walkway and down a ladder. If the fire is between you and that route, "
         "the decision is already made."),
        ("The extinguisher prohibition still in the standard",
         "&sect;1910.179(c)(3) is two words long in substance: <b>carbon tetrachloride "
         "extinguishers shall not be used</b>.",
         "It reads as a historical artefact and it is live regulatory text. Carbon "
         "tetrachloride is acutely toxic and decomposes in heat to phosgene &#8212; in a "
         "cab, the extinguisher would be more dangerous than the fire. Both (c) and (o) are "
         "<b>facility branch</b>; neither is in the &sect;1926.1438(b)(2) list."),
        ("Electrical fire is an isolation problem first",
         "A crane fire is usually electrical, and an energised electrical fire cannot be put "
         "out in any durable way while it is still fed. The first useful action is <b>removing "
         "the supply</b> &#8212; the runway disconnect at &sect;1910.179(g)(5)(i), lockable "
         "and accessible from the floor.",
         "Never water on an energised fire. And a de-energised electrical fire is still hot "
         "and still full of stored energy in capacitors and windings."),
        ("Preserve the scene",
         "The instinct after an incident is to tidy up &#8212; move the load, coil the "
         "slings, get the crane out of the way. Every one of those destroys the record of what "
         "happened.",
         "Nothing moves until the scene has been documented and released, except what must "
         "move to reach an injured person or to remove an active hazard. That exception is "
         "narrow and it is the only one."),
        ("Your account, and what makes it useful",
         "The operator writes what they <b>saw, heard and did</b>, with times, in the order it "
         "happened. That is the highest-value document in any investigation, because it is the "
         "only record of the inside of the cab.",
         "Keep it factual and keep speculation out of it &#8212; not to protect anyone, but "
         "because a guess written down becomes a finding that has to be disproved later. "
         "<i>&#8220;The hoist did not stop when I released the button&#8221;</i> is worth more "
         "than <i>&#8220;I think the contactor stuck.&#8221;</i>"),
    ],
}

PRACTICE = [
    ("OHC.11.A.K1",
     "&sect;1910.179(a)(20) defines a holding brake as one that:",
     ["Slows the load under control", "Automatically prevents motion when power is off",
      "Applies only on command", "Prevents overspeeding in the lowering direction"], 1,
     "The defining behaviour is automatic prevention of motion when power is off. "
     "(f)(2)(iii) then requires it be applied automatically when power is removed."),
    ("OHC.11.A.K2",
     "The correct response to a stranded suspended load is:",
     ["Attempt a controlled manual lowering", "Secure the area, keep everyone clear, and "
      "notify", "Release the brake to lower the load", "Re-energise and try again"], 1,
     "The load is held -- that is the system working. The operator's job ends at securing and "
     "reporting."),
    ("OHC.11.A.K4",
     "A pendant button is released but the hoist keeps running. This is:",
     ["Normal drift", "A failed safety function -- (g)(3)(vii) requires return to off on "
      "release", "A limit switch issue", "Acceptable at low speed"], 1,
     "(g)(3)(vii) requires pendant pushbuttons to return to the off position when pressure is "
     "released. A motion that continues is a failure, not a quirk."),
    ("OHC.11.A.K4b",
     "The E-stop is the correct response to a sticking controller because it:",
     ["Is faster to reach", "Cuts off electric power independently of the regular operating "
      "controls", "Sets the holding brake harder", "Notifies maintenance automatically"], 1,
     "&sect;1910.179(a)(59). If the controller is the failed component, working it harder asks "
     "the failure to fix itself. The E-stop takes a different path."),
    ("OHC.11.B.K2",
     "The upper limit switch fails its shift verification. &sect;1910.179(n)(4)(i) requires "
     "that:",
     ["The crane be tagged at end of shift", "The appointed person be immediately notified",
      "The switch be adjusted by the operator", "A second test be attempted"], 1,
     "Immediate notification to the appointed person. The out-of-service state follows from "
     "(l)(3)(i)."),
    ("OHC.11.B.K3",
     "A load creeps downward with the controller at off. The correct response is:",
     ["Hold it with periodic hoist inputs", "Set the load down at the first safe opportunity "
      "and remove the crane from service", "Continue and report at end of shift",
      "Increase hoist speed"], 1,
     "Drift is a failing holding brake. Correcting it with control inputs hides the failure "
     "behind operator effort."),
    ("OHC.11.C.K2",
     "After a crane-to-crane contact event, the inspection hold applies to:",
     ["Your crane only", "The other crane only", "Both cranes",
      "Neither, if no damage is visible"], 2,
     "Both took the same impact. Checking only your own leaves a struck crane in service with "
     "another operator on it."),
    ("OHC.11.C.K3b",
     "&sect;1910.179(c)(3) prohibits which type of fire extinguisher?",
     ["Dry chemical", "Carbon dioxide", "Carbon tetrachloride", "Foam"], 2,
     "Carbon tetrachloride extinguishers shall not be used. It is acutely toxic and "
     "decomposes in heat to phosgene."),
    ("OHC.11.C.R2",
     "Moving the load and coiling the slings after an incident is harmful because:",
     ["It wastes time", "It destroys the record of what happened",
      "It voids the inspection", "It is the rigger's job"], 1,
     "Nothing moves until the scene is documented and released, except to reach an injured "
     "person or remove an active hazard."),
]

GATE = [
    # ---- Task A
    ("OHC.11.A.K1",
     "&sect;1910.179(f)(2)(iii) requires that holding brakes on hoists be:",
     ["Applied manually by the operator on power loss",
      "Applied automatically when power is removed",
      "Released automatically when power is removed", "Tested weekly"], 1, ""),
    ("OHC.11.A.K1b",
     "Which brake requirement applies on BOTH regulatory branches?",
     ["&sect;1910.179(f)(2)(i) holding brake torque percentages",
      "&sect;1910.179(f)(1)(i) at least one self-setting holding brake per hoisting unit",
      "&sect;1910.179(f)(2)(iii) applied automatically when power is removed",
      "&sect;1910.179(f)(2)(vi) two holding brakes for hot metal"], 1, ""),
    ("OHC.11.A.K2",
     "With a load stranded aloft after a power failure, the operator's role ends at:",
     ["Lowering the load manually", "Securing the area and notifying",
      "Diagnosing the fault", "Re-energising once the area is clear"], 1, ""),
    ("OHC.11.A.K3",
     "The runway conductor disconnect required by &sect;1910.179(g)(5)(i) is:",
     ["Inside the cab only", "On a fixed structure, accessible from the floor, and lockable "
      "in the open position", "On the trolley", "Operated only by maintenance keys"], 1, ""),
    ("OHC.11.A.K3b",
     "When the crane is locked out for servicing, &sect;1910.147 (held) treats the operator "
     "as typically which kind of employee?",
     ["Authorized employee -- the operator applies and removes the locks",
      "Affected employee -- isolation is applied by an authorized employee; the operator "
      "holds until it is verified",
      "Qualified person under &sect;1926.1427",
      "Appointed person under &sect;1910.179(m)(1)"], 1, ""),
    ("OHC.11.A.K4",
     "Which of these is a regulated control failure rather than a nuisance?",
     ["A controller that feels stiff", "A controller that does not return to off when "
      "released", "A slow hoist", "A noisy contactor"], 1, ""),
    ("OHC.11.A.K4b",
     "&sect;1910.179(a)(59) defines the emergency stop switch as cutting off electric power:",
     ["Through the main controller", "Independently of the regular operating controls",
      "After a preset delay", "Only in the hoist circuit"], 1, ""),
    ("OHC.11.A.K5",
     "Recovery of a suspended load from a failed crane is performed by:",
     ["The operator, using the pendant", "The operator with a spotter",
      "Maintenance or engineering-directed personnel",
      "Any qualified crane operator"], 2, ""),
    ("OHC.11.A.R1",
     "The area beneath a stranded load is controlled because:",
     ["It is required for documentation", "The failure mode that stranded the load is not yet "
      "understood, so the hold cannot be assumed permanent",
      "The load may be damaged", "It keeps the aisle clear"], 1, ""),
    ("OHC.11.A.R2",
     "Manually releasing a holding brake to lower a stranded load produces:",
     ["A slow controlled descent", "A free fall with no braking system in the path",
      "A descent at rated lowering speed", "No motion, since the load is balanced"], 1, ""),
    ("OHC.11.A.R3",
     "Re-energising a crane before the failure is understood is hazardous because:",
     ["It may trip the breaker", "It can restart the motion that caused the problem, now with "
      "people nearby who believe the crane is dead",
      "It resets the inspection record", "It drains the control circuit"], 1, ""),
    # ---- Task B
    ("OHC.11.B.K1",
     "Immediately after a two-block event, the correct action is:",
     ["Lower the load to the floor", "Stop, and make no further motion until the rope and "
      "reeving are assessed", "Travel the crane clear of the area",
      "Raise the block off the stop"], 1, ""),
    ("OHC.11.B.K2",
     "&sect;1910.179(n)(4)(i) requires that a limit switch which does not operate properly "
     "results in:",
     ["An entry in the log", "Immediate notification of the appointed person",
      "Adjustment by the operator", "Retesting next shift"], 1, ""),
    ("OHC.11.B.K2b",
     "The crane's out-of-service state after a failed limit verification comes from:",
     ["&sect;1910.179(n)(4)(ii)", "&sect;1910.179(l)(3)(i) -- unsafe conditions corrected "
      "before operation is resumed", "&sect;1910.179(j)(4)",
      "EM 385 16-8.aa(7)"], 1, ""),
    ("OHC.11.B.K3",
     "Brake drift points to a failure in:",
     ["The control braking means at (f)(1)(ii)", "The holding brake at (f)(1)(i)",
      "The limit switch", "The runway conductors"], 1, ""),
    ("OHC.11.B.K4",
     "The threshold that should trigger a stop for noise or vibration is:",
     ["Loud", "New", "Continuous", "Accompanied by a fault code"], 1, ""),
    ("OHC.11.B.K5",
     "&sect;1910.179(l)(2)(ii) holds a crane out of service after repair until:",
     ["The work order is signed", "All guards are reinstalled, safety devices reactivated, "
      "and maintenance equipment removed", "The next periodic inspection",
      "A load test is completed"], 1, ""),
    ("OHC.11.B.R1",
     "Continuing to operate after a two-block event without inspection risks:",
     ["Brake overheating", "Rope failure from damage that is invisible from the floor",
      "Limit switch nuisance trips", "Conductor wear"], 1, ""),
    ("OHC.11.B.R2",
     "Chasing a drifting brake with control inputs is hazardous because:",
     ["It overheats the motor", "It hides a failing brake behind operator effort for as long "
      "as the operator keeps doing it", "It trips the limit switch",
      "It shortens rope life"], 1, ""),
    ("OHC.11.B.R3",
     "The counter to normalising abnormal sounds as equipment character is:",
     ["Longer operator experience", "A written baseline and a low reporting threshold",
      "More frequent periodic inspection", "Sound level monitoring"], 1, ""),
    # ---- Task C
    ("OHC.11.C.K1",
     "The response sequence after a dropped load is:",
     ["Notification, aid, area control", "Aid, area control, notification",
      "Area control, notification, aid", "Documentation, aid, notification"], 1, ""),
    ("OHC.11.C.K2",
     "After a crane-to-structure contact, the structure is also held for assessment because:",
     ["It is required for documentation", "It may have taken load it was not designed for",
      "It belongs to the facility", "The paint may be damaged"], 1, ""),
    ("OHC.11.C.K3",
     "&sect;1910.179(o)(3) requires that operators be:",
     ["Certified in firefighting", "Familiar with the operation and care of the fire "
      "extinguishers provided", "Trained annually in fire suppression",
      "Accompanied by a fire watch"], 1, ""),
    ("OHC.11.C.K3b",
     "&sect;1910.179(c)(3) states that which extinguishers shall not be used?",
     ["Water-type", "Carbon tetrachloride", "Carbon dioxide", "Dry chemical"], 1, ""),
    ("OHC.11.C.K4",
     "The only justification for moving anything at an incident scene before it is documented "
     "is:",
     ["Restoring production", "Reaching an injured person or removing an active hazard",
      "Clearing the aisle", "Protecting the equipment"], 1, ""),
    ("OHC.11.C.K5",
     "The most useful content of an operator's incident account is:",
     ["A theory of the mechanical cause", "What was seen, heard and done, with times, in "
      "order", "An assessment of who was at fault",
      "A list of the equipment involved"], 1, ""),
    ("OHC.11.C.R1",
     "Entering an uncontrolled scene to render aid risks:",
     ["Contaminating evidence", "One casualty becoming two",
      "Delaying notification", "Voiding the inspection"], 1, ""),
    ("OHC.11.C.R2",
     "The first useful action on an energised electrical fire in a crane is:",
     ["Discharge an extinguisher at the source", "Remove the supply at the runway disconnect",
      "Apply water", "Open the enclosure to locate the fault"], 1, ""),
    ("OHC.11.C.R3",
     "Delayed notification escalates consequences chiefly because:",
     ["Reports become less accurate", "The hazard stays live and uncontrolled while nobody "
      "with authority knows about it", "Documentation takes longer",
      "Witnesses leave the site"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.11.A.K1": ("**&sect;1910.179(f)(2)(iii)** &middot; (a)(20) definition", "OK"),
    "OHC.11.A.K1b": ("**&sect;1910.179(f)(1)(i)** vs **(f)(2)** branch split", "OK"),
    "OHC.11.A.K2": ("derived", "OK"),
    "OHC.11.A.K3": ("**&sect;1910.179(g)(5)(i)** &middot; (l)(2)(i)(c)", "OK"),
    "OHC.11.A.K3b": ("**&sect;1910.147(b),(c)(1)** held -- affected employee", "OK"),
    "OHC.11.A.K4": ("**&sect;1910.179(g)(3)(vi), (vii), (ix)**", "OK"),
    "OHC.11.A.K4b": ("**&sect;1910.179(a)(59)** &middot; (a)(40) fail-safe", "OK"),
    "OHC.11.A.K5": ("**&sect;1910.179(l)(3)(i)** designated personnel", "OK"),
    "OHC.11.A.R1": ("derived", "OK"),
    "OHC.11.A.R2": ("&sect;1910.179(l)(3)(i) &middot; derived", "OK"),
    "OHC.11.A.R3": ("derived", "OK"),
    "OHC.11.B.K1": ("derived &middot; `OHC.07.A.K5`", "OK"),
    "OHC.11.B.K2": ("**&sect;1910.179(n)(4)(i)** &#8212; both branches", "OK"),
    "OHC.11.B.K2b": ("**&sect;1910.179(l)(3)(i)** &#8212; facility branch", "ACSFIX"),
    "OHC.11.B.K3": ("**&sect;1910.179(f)(1)(i)** vs **(f)(1)(ii)**", "OK"),
    "OHC.11.B.K4": ("derived", "OK"),
    "OHC.11.B.K5": ("**&sect;1910.179(l)(2)(ii)** &#8212; facility branch", "OK"),
    "OHC.11.B.R1": ("derived", "OK"),
    "OHC.11.B.R2": ("derived", "OK"),
    "OHC.11.B.R3": ("derived &middot; `OHC.05.A.R3`", "OK"),
    "OHC.11.C.K1": ("derived", "OK"),
    "OHC.11.C.K2": ("derived &middot; EM 385 16-8.aa(6)", "OK"),
    "OHC.11.C.K3": ("**&sect;1910.179(o)(3)** &#8212; facility branch", "OK"),
    "OHC.11.C.K3b": ("**&sect;1910.179(c)(3)** &#8212; facility branch", "OK"),
    "OHC.11.C.K4": ("derived", "OK"),
    "OHC.11.C.K5": ("derived", "OK"),
    "OHC.11.C.R1": ("derived", "OK"),
    "OHC.11.C.R2": ("**&sect;1910.179(g)(5)(i)** &middot; derived", "OK"),
    "OHC.11.C.R3": ("derived", "OK"),
}

TRACE_PERF = [
    ("OHC.11.A.S1", "Execute the stranded-load securing sequence"),
    ("OHC.11.A.S2", "Demonstrate E-stop response to a simulated control malfunction"),
    ("OHC.11.A.S3", "Conduct the notification and turnover to maintenance"),
    ("OHC.11.B.S1", "Demonstrate correct response to a simulated limit failure"),
    ("OHC.11.B.S2", "Execute an immediate set-down for brake drift"),
    ("OHC.11.B.S3", "Document a mechanical event for inspection escalation"),
    ("OHC.11.C.S1", "Execute the emergency response sequence for a simulated dropped load"),
    ("OHC.11.C.S2", "Complete post-contact inspection holds on both affected systems"),
    ("OHC.11.C.S3", "Produce a factual incident account for investigation"),
]

TRACE_NOTES = [
    ("&#11088; The E-stop has a regulatory definition, and it is the reason the E-stop is the "
     "answer",
     "**&sect;1910.179(a)(59)**: an emergency stop switch is a switch to cut off electric "
     "power **independently of the regular operating controls**. That clause is the whole "
     "argument for `A.K4b`. If the controller is the component that failed, working it harder "
     "asks the failure to repair itself; the E-stop reaches the same result by a different "
     "path. Pair it with **(a)(40)**, which defines **fail-safe** as a provision designed to "
     "automatically stop or safely control any motion in which a malfunction occurs. The ACS "
     "asserts *immediate E-stop response* without either citation."),
    ("&#9989; Three control failures the standard already regulates",
     "`A.K4` asks for *unresponsive, sticking, or self-motion conditions*. Two of the three "
     "are named safety functions: **(g)(3)(vi)** floor-operated controllers shall "
     "**automatically return to the off position when released**; **(g)(3)(vii)** pendant "
     "pushbuttons shall **return to off when pressure is released**; and **(g)(3)(ix)** on "
     "**remote-operated** cranes, if the control signal **becomes ineffective the crane motion "
     "shall stop**. A motion that continues after release is a **failed safety function**, not "
     "equipment character. **(g)** is in the &sect;1926.1438(b)(2) list &#8212; both branches."),
    ("&#9989; `A.K1b` &#8212; brakes split across the branch line, and the ACS names a "
     "mechanism where the standard names a behaviour",
     "**&sect;1910.179(f)(1)(i)** requires **at least one self-setting brake** per independent "
     "hoisting unit, and **(f)(1)** *is* in the &sect;1926.1438(b)(2) list &#8212; both "
     "branches. **(f)(2)** is **not**, so *applied automatically when power is removed* at "
     "**(f)(2)(iii)** and the torque percentages at **(f)(2)(i)** (125&#37; / 100&#37; / "
     "100&#37; each) are **facility branch**. Separately, the ACS says the load is held by "
     "**spring-set** brakes. Spring-set is the common mechanism; the standard specifies "
     "**self-setting** and **automatic on power removal** &#8212; a behaviour, deliberately "
     "mechanism-agnostic. Practically identical, but a learner who is taught *spring* will not "
     "recognise a compliant brake that works another way."),
    ("&#9989; `B.K2` &#8212; the regulation names a notification, not an out-of-service state",
     "The ACS states `B.K2` as *&#8220;crane out of service.&#8221;* That is the right "
     "outcome, but the regulation gets there in two steps. **&sect;1910.179(n)(4)(i)** ends: "
     "*if the switch does not operate properly, the **appointed person shall be immediately "
     "notified**.* The out-of-service state then follows from **&sect;1910.179(l)(3)(i)** "
     "&#8212; unsafe conditions **corrected before operation is resumed**. `B.K2` gates the "
     "notification and `B.K2b` gates the source of the hold, because the notification is the "
     "half that gets skipped. Note the branch difference too: **(n)** binds on both branches, "
     "**(l)** is facility only."),
    ("&#9989; Two fire provisions, one of them startling",
     "**&sect;1910.179(o)(3)**: the employer shall ensure operators are **familiar with the "
     "operation and care of the fire extinguishers provided** &#8212; `C.K3`. And "
     "**&sect;1910.179(c)(3)**, which is live regulatory text and reads like an artefact: "
     "**carbon tetrachloride extinguishers shall not be used** &#8212; `C.K3b`. Carbon "
     "tetrachloride is acutely toxic and decomposes in heat to phosgene, so in a cab the "
     "extinguisher would be worse than the fire. Both **(c)** and **(o)** are **facility "
     "branch**; neither is in the &sect;1926.1438(b)(2) list."),
    ("&#9432; Elements carrying a second item",
     "`A.K1`, `A.K3`, `A.K4`, `B.K2` and `C.K3` each carry two items. `A.K3b` maps held "
     "**&sect;1910.147** onto mainline disconnect use: the operator is typically an "
     "**affected** employee."),
]


def main():
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)
    A.write_pre_and_manifest(
        MODULE, html, "OHC_M11_MalfunctionsAndEmergencies.pre.html",
        "CQ1:OHC_M11_MalfunctionsAndEmergencies", "OHC_M12", PRACTICE, GATE,
        notes="1910.147 A.K3b; 1412 cross-ref closed")


if __name__ == "__main__":
    main()
