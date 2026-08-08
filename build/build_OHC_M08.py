#!/usr/bin/env python3
"""OHC-08 Operational Rules and Safe Practices -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M08"
MODLABEL = "Module 8"
TITLE = "Operational Rules and Safe Practices"
SUBTITLE = ("Apply the standing rules that govern personnel protection, multi-crane "
            "environments, and securing.")

OBJECTIVES = [
    "Enforce the exclusion and protection rules around a suspended load, and hold attention "
    "on the load for a full task cycle.",
    "Operate safely where cranes share runways, bays or airspace at different elevations, "
    "using explicit communication rather than assumed right-of-way.",
    "Secure the crane correctly at task end, shift end and in adverse conditions, and hand "
    "its status across a shift change.",
]

SECTIONS = [
    ("A", "Personnel Protection Rules",
     "Enforce the exclusion and protection rules around suspended loads."),
    ("B", "Multi-Crane and Shared-Runway Operations",
     "Operate safely where cranes share runways, bays, or airspace at different elevations."),
    ("C", "Securing and Shutdown",
     "Secure the crane correctly at task end, shift end, and adverse conditions."),
]

CONTENT = {
    "A": [
        ("The rule, and what the rule actually says",
         "&sect;1910.179(n)(3)(vi): <i>the employer shall require that the operator <b>avoid "
         "carrying loads over people</b></i>. Note the shape of it &#8212; it is written as "
         "an <b>employer duty</b> to require avoidance, not as an absolute prohibition on the "
         "operator.",
         "Nearly every facility programme converts it into an absolute: <b>no load over "
         "personnel, ever</b>. That is a defensible tightening and it is the rule you will be "
         "held to. Know both &#8212; the regulation's wording, and your programme's."),
        ("Path planning is the control",
         "&#8220;Avoid&#8221; is not a thing you do at the controls. It is a thing you do "
         "before you pick, by choosing a route that does not cross occupied ground. Once the "
         "load is up and travelling, your options have already narrowed.",
         "The path is planned on the floor plan, not on the fly: where are people working, "
         "where are the walkways, where are the doors people come through without looking up."),
        ("Nobody rides anything",
         "&sect;1910.179(n)(3)(v): while any employee is <b>on the load or hook</b>, there "
         "shall be <b>no hoisting, lowering, or traveling</b>. Not slowly, not briefly, not "
         "to reposition someone.",
         "The prohibition extends by facility rule to riding the crane itself &#8212; the "
         "bridge, the walkway, the trolley &#8212; while it is in motion. An overhead crane is "
         "not transport."),
        ("The warning device, and its one exception",
         "<b>EM 385-1-1 16-8.aa(4)</b>: an alarm or other effective warning signal is "
         "required for each crane with a <b>power traveling mechanism</b> &#8212; <b>except "
         "for floor-operated cranes</b>.",
         "&sect;1910.179(n)(3)(xi) then names when it is used: <b>when starting the "
         "bridge</b>, and <b>when the load or hook approaches near or over personnel</b>. Two "
         "triggers, not one."),
        ("A warning is not a clearance",
         "This is the limit the ACS asks you to understand. Sounding the alarm announces the "
         "crane. It does <b>not</b> authorise the movement, it does not clear the path, and it "
         "does not transfer responsibility to the people who heard it.",
         "Using the horn as a substitute for looking is the failure mode. If the warning is "
         "doing the work of the exclusion zone, there is no exclusion zone &#8212; there is a "
         "noise and a hope that everyone interprets it the same way you do."),
        ("Attention is a control, and it is spendable",
         "&sect;1910.179(n)(3)(x): the employer shall ensure the operator <b>does not leave "
         "the position at the controls while the load is suspended</b>. Physically present is "
         "the floor of the requirement, not the ceiling of it.",
         "A suspended load is an active hazard for as long as it hangs. The standard also "
         "polices the station itself &#8212; (o)(2) requires clothing and belongings stored so "
         "as not to interfere with access or operation, and tools kept in the tool box rather "
         "than <b>loose in or about the cab</b>."),
        ("The fall zone drifts inward",
         "On a long operation the exclusion zone quietly shrinks. People who were clear at the "
         "start step closer to see, to help, to talk. Nobody decides to enter the fall zone; "
         "they arrive in it by degrees.",
         "This is why the rule is <b>stop motion</b>, not <b>shout</b>. Re-establishing the "
         "zone costs seconds. Discovering it has closed costs somebody."),
    ],
    "B": [
        ("Three clearance relationships, continuously",
         "<b>EM 385-1-1 16-8.aa(5)</b>: clearance shall be maintained between the crane and "
         "<b>any structure or object</b>, <b>any parallel running cranes</b>, and <b>cranes "
         "operating at different elevations</b>.",
         "&sect;1910.179 backs two of the three: <b>(b)(6)(i)</b> sets the installed "
         "clearance from the building, and <b>(b)(7)</b> requires clearance between parallel "
         "cranes. Both apply on either branch. The elevation case is EM 385's contribution."),
        ("Different elevations is the one that surprises people",
         "A crane on another runway at another height is outside the normal scan. It is not in "
         "your bay, not at your eye level, and its load block may occupy airspace you think of "
         "as empty.",
         "Runway heights differ by design in older buildings and in bays that were extended. "
         "Establish the geometry once, deliberately, rather than discovering it with a load in "
         "the air."),
        ("Contact is permitted, but it is never casual",
         "<b>EM 385-1-1 16-8.aa(6)</b>: contacts with <b>runway stops or other cranes</b> "
         "shall be made <b>with extreme caution</b>, with particular care for persons on or "
         "below the crane, and <b>only after making certain that persons on the other cranes "
         "are aware</b>.",
         "It does not prohibit contact. Reaching a runway stop is a normal end-of-travel "
         "event. What it requires is that contact be slow, intended, and known about by "
         "everyone it could affect &#8212; including anyone on the other crane."),
        ("Right of way is negotiated, not assumed",
         "Two operators who each believe the other will yield are two operators on a "
         "collision course. Shared-bay movement runs on <b>explicit communication</b>: who is "
         "moving, where, and when the other is clear.",
         "For a genuinely shared lift, &sect;1910.179(n)(3)(ix) makes it formal &#8212; when "
         "<b>two or more cranes</b> lift one load, <b>one qualified responsible person shall "
         "be in charge</b>, and shall analyse the operation and instruct everyone on "
         "positioning, rigging and the movements to be made."),
        ("Parking and priority are facility conventions",
         "Where cranes share a runway, the facility sets where each parks, who has priority "
         "through a pinch point, and which end of the bay is whose. These are local rules and "
         "they are not in any standard.",
         "That does not make them optional. An operator who does not know the local parking "
         "convention will eventually park a crane where the next one needs to be, and the "
         "resolution happens under time pressure."),
        ("Interlocks and zone limiting",
         "Where fitted, interlocks and zone-limiting systems prevent two cranes occupying the "
         "same space, or keep a crane out of a defined area. They are engineered controls and "
         "they are more reliable than attention.",
         "They also breed dependence. Know whether your bay has them, what they cover, and "
         "&#8212; critically &#8212; what they do <b>not</b> cover. A zone limiter that "
         "protects one pinch point does not protect the other three."),
        ("The low-tech interlock: rail stops",
         "&sect;1910.179(l)(2)(i) closes its lockout sequence with the step that protects an "
         "idle crane: where other cranes are on the same runway, <b>rail stops or other "
         "suitable means shall be provided to prevent interference with the idle crane</b>.",
         "This is the provision that keeps a working crane from running into one that is under "
         "maintenance with a mechanic on it. It is <b>facility branch</b> &#8212; (l) is not "
         "in the &sect;1926.1438(b)(2) list."),
    ],
    "C": [
        ("The end-of-use sequence",
         "Securing is a sequence, and each step answers a specific question. <b>Hook "
         "empty</b> &#8212; nothing is left hanging. <b>Load block raised clear</b> &#8212; "
         "clear of traffic, walkways and work at floor level. <b>Controls off</b> "
         "&#8212; every controller returned to the off position.",
         "Then <b>disconnect as required</b> by the facility: main switch, disconnect, or "
         "lockout where the programme calls for it. A crane left live with the block at head "
         "height is secured in name only."),
        ("Outdoor cranes: secure them when you leave",
         "<b>EM 385-1-1 16-8.aa(7)</b> is one sentence and it is absolute: <b>operators of "
         "outdoor cranes shall secure them when leaving</b>. Not at shift end &#8212; when "
         "leaving.",
         "Wind does not wait for the end of the shift, and an unsecured outdoor crane is a "
         "wheeled structure on a rail with nothing holding it."),
        ("Wind indicators and rail clamps &#8212; read the scope",
         "&sect;1910.179(b)(4) requires that <b>outdoor storage bridges</b> be provided with "
         "<b>automatic rail clamps</b>, and that a <b>wind-indicating device</b> give a "
         "<b>visible or audible alarm</b> to the bridge operator <b>at a predetermined wind "
         "velocity</b>.",
         "Two precisions. It is scoped to <b>outdoor storage bridges</b>, not to every outdoor "
         "crane. And <b>(b)(4) is not in the &sect;1926.1438(b)(2) list</b> &#8212; the "
         "construction branch gets (b)(5), (6) and (7) only &#8212; so this is a "
         "<b>facility-branch</b> requirement. Elsewhere, the manufacturer's storm provisions "
         "and the facility programme govern."),
        ("Pendant and transmitter",
         "A pendant left hanging within reach, or a radio transmitter left switched on and "
         "unattended, is an unsecured crane regardless of what the main switch is doing. The "
         "control is the access point.",
         "Transmitters are stored and, where the system supports it, keyed off or "
         "de-energised. Pendants are returned to their park position. The question to answer "
         "is: <b>could someone who is not qualified move this crane right now?</b>"),
        ("What actually permits leaving the station",
         "&sect;1910.179(n)(3)(x) forbids leaving the controls <b>while the load is "
         "suspended</b>. So the first condition is unconditional: <b>the load is landed</b>.",
         "Then the rest: hook empty, block clear, controls off, and the crane secured to "
         "whatever level the facility requires for the duration you will be away. A break is "
         "not a special case with a lower bar."),
        ("Loads are not left hanging over breaks",
         "This is the one that gets rationalised. The load is nearly placed, the break is "
         "short, moving it costs five minutes. So it hangs &#8212; unattended, over ground "
         "nobody is now watching, with no operator at the controls.",
         "Every element of the rule is broken at once: (n)(3)(x) attendance, the exclusion "
         "zone, and the securing sequence. Land the load."),
        ("Handing over the crane",
         "The incoming operator inherits the equipment and needs its actual state: what was "
         "run, what was noticed, what is outstanding, and whether anything is restricted or "
         "tagged.",
         "A handoff that says <i>&#8220;it's fine&#8221;</i> transfers the crane without "
         "transferring the information. Where a defect exists, OHC-05 governs &#8212; tag, "
         "log, and say it out loud."),
    ],
}

PRACTICE = [
    ("OHC.08.A.K1",
     "&sect;1910.179(n)(3)(vi) is written as:",
     ["An absolute prohibition on the operator", "An employer duty to require that the "
      "operator avoid carrying loads over people", "A recommendation",
      "A rule applying only to outdoor cranes"], 1,
     "It is an employer duty to require avoidance. Most facility programmes tighten it to an "
     "absolute, and that is the rule you are held to."),
    ("OHC.08.A.K2",
     "An employee is standing on the hook to be repositioned a short distance. Permitted "
     "motions are:",
     ["Travel only, at slow speed", "Hoisting only", "None",
      "Any motion, with a signaler"], 2,
     "(n)(3)(v): while any employee is on the load or hook there shall be no hoisting, "
     "lowering, or traveling."),
    ("OHC.08.A.K3",
     "The EM 385 warning-device requirement for power-traveling cranes excepts:",
     ["Cab-operated cranes", "Floor-operated cranes", "Outdoor cranes",
      "Cranes under 5 tons"], 1,
     "16-8.aa(4) requires a warning signal for each crane with a power traveling mechanism, "
     "except for floor-operated cranes."),
    ("OHC.08.A.K5",
     "The operator may step away from the controls with a load suspended if the area below "
     "is barricaded.",
     ["True", "False"], 1,
     "(n)(3)(x) is unconditional while the load is suspended. Land the load first."),
    ("OHC.08.B.K2",
     "Contact with a runway stop is:",
     ["Prohibited in all cases", "Permitted, but only with extreme caution and after "
      "ensuring persons on other cranes are aware", "Routine and needs no particular care",
      "Permitted only by a designated person"], 1,
     "EM 385 16-8.aa(6) permits it but requires extreme caution, care for persons on or "
     "below, and that persons on other cranes be aware."),
    ("OHC.08.B.K5",
     "Where other cranes share the runway with a crane being worked on, "
     "&sect;1910.179(l)(2)(i) requires:",
     ["A warning sign only", "Rail stops or other suitable means to prevent interference "
      "with the idle crane", "A second operator on watch",
      "The other cranes to be shut down"], 1,
     "Step 5 of the lockout sequence. It is the provision that protects a mechanic on an "
     "idle crane."),
    ("OHC.08.C.K2",
     "The &sect;1910.179(b)(4) automatic rail clamp and wind-indicator requirement is "
     "scoped to:",
     ["All outdoor cranes", "Outdoor storage bridges", "All gantry cranes",
      "Cranes over 20 tons"], 1,
     "The paragraph names outdoor storage bridges specifically. It is also facility-branch "
     "only -- (b)(4) is not in the 1926.1438(b)(2) list."),
    ("OHC.08.C.K3",
     "The main disconnect is open, but the pendant hangs at floor level within reach. The "
     "crane is:",
     ["Fully secured", "Not secured against unauthorised use at the control point",
      "Secured, provided a sign is posted", "Secured for indoor cranes only"], 1,
     "The control is the access point. Securing means asking whether an unqualified person "
     "could move the crane now."),
    ("OHC.08.C.R3",
     "A load is nearly placed and the crew is going on a short break. The correct action is:",
     ["Leave it suspended -- it is only a few minutes", "Leave it suspended and barricade "
      "beneath", "Land the load before leaving", "Lower it to knee height"], 2,
     "Leaving it breaks (n)(3)(x), the exclusion zone, and the securing sequence at once."),
]

GATE = [
    # ---- Task A
    ("OHC.08.A.K1",
     "The primary control for keeping loads off personnel is:",
     ["Sounding the warning device continuously",
      "Planning the load path to avoid occupied areas before the pick",
      "Travelling at reduced speed", "Raising the load above head height"], 1, ""),
    ("OHC.08.A.K2",
     "&sect;1910.179(n)(3)(v) prohibits which motions while an employee is on the load or "
     "hook?",
     ["Traveling only", "Hoisting and lowering only",
      "Hoisting, lowering, and traveling", "None -- it permits slow motion"], 2, ""),
    ("OHC.08.A.K3",
     "EM 385-1-1 16-8.aa(4) requires a warning signal for each crane with a power traveling "
     "mechanism, except for:",
     ["Outdoor cranes", "Floor-operated cranes", "Cab-operated cranes",
      "Radio-controlled cranes"], 1, ""),
    ("OHC.08.A.K3b",
     "The limit of the warning device as a control is that sounding it:",
     ["Reduces the required clearance", "Announces the crane but does not authorise the "
      "movement or clear the path", "Transfers responsibility to personnel who heard it",
      "Satisfies the path-planning requirement"], 1, ""),
    ("OHC.08.A.K4",
     "Operator attention rules while a load is suspended require:",
     ["Attention divided between the load and secondary tasks as workload allows",
      "No distraction tasks -- attention stays on the load and its path",
      "Attention on the destination only", "A spotter to watch the load instead"], 1, ""),
    ("OHC.08.A.K5",
     "&sect;1910.179(n)(3)(x) requires that the operator:",
     ["Sound the warning before leaving the controls",
      "Not leave the position at the controls while the load is suspended",
      "Log any absence from the controls", "Remain in the cab for the entire shift"],
     1, ""),
    ("OHC.08.A.R1",
     "Pedestrian traffic crossing under an active lift path is best controlled by:",
     ["Sounding the warning at each crossing", "Rerouting the lift path or physically "
      "controlling the crossing", "Travelling only when no one is looking up",
      "Raising the load higher"], 1, ""),
    ("OHC.08.A.R2",
     "Over a long operation, crew members drift into the fall zone. The correct response is:",
     ["Shout a warning and continue", "Stop motion and re-establish the exclusion zone",
      "Continue at reduced speed", "Sound the alarm continuously"], 1, ""),
    ("OHC.08.A.R3",
     "Attention capture by a phone or a conversation is hazardous with a load suspended "
     "because:",
     ["It is unprofessional", "The load remains an active hazard for as long as it hangs, "
      "and the operator is its only control", "It slows the work",
      "It violates the inspection record"], 1, ""),
    # ---- Task B
    ("OHC.08.B.K1",
     "EM 385-1-1 16-8.aa(5) requires clearance to be maintained from:",
     ["Structures only", "Structures and parallel running cranes only",
      "Structures or objects, parallel running cranes, and cranes operating at different "
      "elevations", "Other cranes only when they carry a load"], 2, ""),
    ("OHC.08.B.K2",
     "Contact with runway stops or other cranes shall be made:",
     ["Never", "With extreme caution, with care for persons on or below, and only after "
      "ensuring persons on the other cranes are aware",
      "At normal travel speed to seat positively", "Only during periodic inspection"],
     1, ""),
    ("OHC.08.B.K3",
     "When two or more cranes lift a single load, &sect;1910.179(n)(3)(ix) requires:",
     ["Two signalers, one per crane", "One qualified responsible person in charge of the "
      "operation, who analyses it and instructs all personnel",
      "Each operator to work to their own judgement", "A written permit only"], 1, ""),
    ("OHC.08.B.K4",
     "Crane parking and priority conventions in a multi-crane bay are:",
     ["Set by &sect;1910.179", "Set by EM 385-1-1", "Facility rules, and not optional",
      "At each operator's discretion"], 2, ""),
    ("OHC.08.B.K5",
     "The value of an interlock or zone-limiting system is real, but the operator must also "
     "know:",
     ["Its manufacturer", "What it does not cover",
      "Its installation date", "Its power consumption"], 1, ""),
    ("OHC.08.B.K5b",
     "&sect;1910.179(l)(2)(i) protects a crane taken out of service on a shared runway by "
     "requiring:",
     ["An out-of-order sign on the crane only",
      "Rail stops or other suitable means to prevent interference with the idle crane",
      "The runway to be de-energised", "A second operator to stand watch"], 1, ""),
    ("OHC.08.B.R1",
     "Two operators each assume the other will yield at a pinch point. The missing control "
     "is:",
     ["A zone limiter", "Explicit communication about who moves, where, and when the other "
      "is clear", "Slower travel speed", "A written lift plan"], 1, ""),
    ("OHC.08.B.R2",
     "Cranes on runways at different rail heights are a particular hazard because:",
     ["They have different capacities", "The other crane sits outside the normal scan and "
      "its load block may occupy airspace assumed to be empty",
      "They cannot sound warnings", "Their brakes respond differently"], 1, ""),
    ("OHC.08.B.R3",
     "Treating bumper contact as routine is hazardous because:",
     ["It wears the bumpers", "It normalises an event that EM 385 requires to be made with "
      "extreme caution and prior awareness on the other crane",
      "It triggers the limit switch", "It shortens rail life"], 1, ""),
    # ---- Task C
    ("OHC.08.C.K1",
     "The end-of-use securing sequence includes:",
     ["Controls off only", "Hook empty, load block raised clear, controls off, and "
      "disconnect as required", "Lowering the block to floor level for inspection",
      "Leaving the crane centred on the runway with power on"], 1, ""),
    ("OHC.08.C.K2",
     "EM 385-1-1 16-8.aa(7) requires operators of outdoor cranes to secure them:",
     ["At the end of each shift", "When leaving", "Weekly",
      "Only when wind is forecast"], 1, ""),
    ("OHC.08.C.K2b",
     "&sect;1910.179(b)(4) requires automatic rail clamps and a wind-indicating device "
     "giving a visible or audible alarm at a predetermined wind velocity. Its scope is:",
     ["All outdoor cranes, on both regulatory branches",
      "Outdoor storage bridges, and it is facility-branch only",
      "All gantry cranes, on both branches", "Cab-operated cranes only"], 1, ""),
    ("OHC.08.C.K3",
     "Securing a pendant or radio transmitter against unauthorised use addresses:",
     ["Weather damage to the control", "The control being the access point by which an "
      "unqualified person could move the crane", "Battery life",
      "Cable wear at the strain relief"], 1, ""),
    ("OHC.08.C.K4",
     "The unconditional first requirement before an operator may leave the station is:",
     ["The warning has been sounded", "The load is landed",
      "A relief operator is present", "The block is at head height"], 1, ""),
    ("OHC.08.C.K4b",
     "A short break is:",
     ["A recognised exception permitting a load to remain suspended",
      "Not an exception -- the same securing standard applies",
      "Permitted if the area is barricaded", "Permitted for loads under 2,000 lb"], 1, ""),
    ("OHC.08.C.K5",
     "A shift handoff must convey:",
     ["That the crane runs", "What was run, what was noticed, what is outstanding, and "
      "whether anything is restricted or tagged", "The operator's name and hours",
      "The number of lifts completed"], 1, ""),
    ("OHC.08.C.R1",
     "An unsecured outdoor crane in a wind event is hazardous because:",
     ["Its markings may become illegible", "It is a wheeled structure on a rail with nothing "
      "restraining it", "Its brakes will overheat", "Its limit switch may trip"], 1, ""),
    ("OHC.08.C.R2",
     "The control that most directly prevents untrained use of an idle crane is:",
     ["A capacity marking", "Securing the control point -- pendant parked or transmitter "
      "stored and de-energised", "A periodic inspection record",
      "A warning device"], 1, ""),
    ("OHC.08.C.R3",
     "Leaving a load suspended during a break breaks which set of rules?",
     ["The inspection interval only", "Operator attendance under (n)(3)(x), the exclusion "
      "zone, and the securing sequence", "The rated load marking rule",
      "The warning device requirement"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.08.A.K1": ("**&sect;1910.179(n)(3)(vi)** &#8212; both branches", "OK"),
    "OHC.08.A.K2": ("**&sect;1910.179(n)(3)(v)**", "OK"),
    "OHC.08.A.K3": ("**EM 385 16-8.aa(4)**", "OK"),
    "OHC.08.A.K3b": ("derived &middot; &sect;1910.179(n)(3)(xi)", "OK"),
    "OHC.08.A.K4": ("&sect;1910.179(n)(3)(x) &middot; (o)(2) &middot; derived", "OK"),
    "OHC.08.A.K5": ("**&sect;1910.179(n)(3)(x)**", "OK"),
    "OHC.08.A.R1": ("&sect;1910.179(n)(3)(vi) &middot; derived", "OK"),
    "OHC.08.A.R2": ("derived", "OK"),
    "OHC.08.A.R3": ("&sect;1910.179(n)(3)(x) &middot; derived", "OK"),
    "OHC.08.B.K1": ("**EM 385 16-8.aa(5)** &middot; &sect;1910.179(b)(6)(i), (b)(7)", "OK"),
    "OHC.08.B.K2": ("**EM 385 16-8.aa(6)**", "OK"),
    "OHC.08.B.K3": ("**&sect;1910.179(n)(3)(ix)**", "OK"),
    "OHC.08.B.K4": ("facility convention &middot; derived", "OK"),
    "OHC.08.B.K5": ("derived", "OK"),
    "OHC.08.B.K5b": ("**&sect;1910.179(l)(2)(i)** step 5 &#8212; facility branch", "OK"),
    "OHC.08.B.R1": ("derived &middot; &sect;1910.179(n)(3)(ix)", "OK"),
    "OHC.08.B.R2": ("**EM 385 16-8.aa(5)** &middot; derived", "OK"),
    "OHC.08.B.R3": ("**EM 385 16-8.aa(6)** &middot; derived", "OK"),
    "OHC.08.C.K1": ("derived &middot; Tier 0", "OK"),
    "OHC.08.C.K2": ("**EM 385 16-8.aa(7)**", "OK"),
    "OHC.08.C.K2b": ("**&sect;1910.179(b)(4)** &#8212; facility branch, storage bridges",
                     "ACSFIX"),
    "OHC.08.C.K3": ("derived &middot; `OHC.03.B` control security", "OK"),
    "OHC.08.C.K4": ("**&sect;1910.179(n)(3)(x)**", "OK"),
    "OHC.08.C.K4b": ("&sect;1910.179(n)(3)(x) &middot; derived", "OK"),
    "OHC.08.C.K5": ("derived &middot; `OHC.05.C.K5`", "OK"),
    "OHC.08.C.R1": ("&sect;1910.179(b)(4) &middot; derived", "OK"),
    "OHC.08.C.R2": ("derived", "OK"),
    "OHC.08.C.R3": ("**&sect;1910.179(n)(3)(x)** &middot; derived", "OK"),
}

TRACE_PERF = [
    ("OHC.08.A.S1", "Plan and execute a load path avoiding occupied zones"),
    ("OHC.08.A.S2", "Stop motion when personnel enter the exclusion area"),
    ("OHC.08.A.S3", "Demonstrate load-attended discipline for a full task cycle"),
    ("OHC.08.B.S1", "Coordinate a shared-bay operation with explicit communication"),
    ("OHC.08.B.S2", "Demonstrate approach and hold-off at defined clearance from a second crane"),
    ("OHC.08.B.S3", "Apply facility priority rules in a simulated conflict"),
    ("OHC.08.C.S1", "Execute the full securing sequence for the assigned crane"),
    ("OHC.08.C.S2", "Apply outdoor securing provisions including wind devices where fitted"),
    ("OHC.08.C.S3", "Complete a documented status handoff at shift change"),
]

TRACE_NOTES = [
    ("&#9888;&#65039; `C.K2` &#8212; the ACS overstates the scope of the wind provision",
     "The ACS pairs **EM 385 16-8.aa(7)** with *&#8220;wind securing devices and storm "
     "provisions for outdoor <b>gantry</b> cranes.&#8221;* The regulation behind that is "
     "**&sect;1910.179(b)(4)**, and it is narrower on both axes: it is scoped to <b>outdoor "
     "storage bridges</b>, not all outdoor or gantry cranes, and **(b)(4) is not in the "
     "&sect;1926.1438(b)(2) list** &#8212; the construction branch receives **(b)(5), (6) and "
     "(7) only** &#8212; so it is **facility branch**. `C.K2` gates the aa(7) duty, which is "
     "universal; `C.K2b` gates the (b)(4) hardware requirement with both precisions stated. "
     "Elsewhere, the manufacturer's storm provisions and the facility programme govern."),
    ("&#9989; `A.K1` teaches the regulation's actual wording and the programme's tightening",
     "The ACS states `A.K1` as *&#8220;no load carried over personnel.&#8221;* "
     "**&sect;1910.179(n)(3)(vi)** is shaped differently: *the <b>employer</b> shall require "
     "that the operator <b>avoid</b> carrying loads over people.* An employer duty to require "
     "avoidance, not an absolute operator prohibition. Facility programmes almost universally "
     "convert it to an absolute, which is a defensible tightening and is the rule an operator "
     "is held to. The module teaches both, and gates `A.K1` on the control that actually "
     "delivers it &#8212; **path planning before the pick**."),
    ("&#9989; The warning-device exception is gated",
     "**EM 385 16-8.aa(4)** requires an alarm or other effective warning signal for each "
     "crane with a power traveling mechanism **except for floor-operated cranes**. The ACS "
     "cites aa(4) without the exception. `A.K3` gates it, and `A.K3b` gates the *limit as a "
     "control* the ACS element asks for &#8212; a warning announces the crane; it does not "
     "authorise the movement, clear the path, or transfer responsibility to whoever heard it."),
    ("&#9989; `B.K5b` adds the low-tech interlock the ACS omits",
     "`B.K5` covers engineered interlocks and zone limiting *where installed*. "
     "**&sect;1910.179(l)(2)(i)** closes its lockout sequence with the provision that "
     "protects an idle crane on a shared runway: **rail stops or other suitable means shall "
     "be provided to prevent interference**. It is the step that keeps a working crane off a "
     "mechanic, it needs no installed system, and it is **facility branch** &#8212; (l) is "
     "not in the &sect;1926.1438(b)(2) list. Cross-refs `OHC.05.C.K3`."),
    ("&#9989; Task A and most of Task B bind on both branches",
     "Every Task A citation is in **&sect;1910.179(n)**, which is in the "
     "&sect;1926.1438(b)(2) list. `B.K1` is backed by **(b)(6)(i)** and **(b)(7)**, also in "
     "the list. The two facility-branch items in this module are both flagged: `B.K5b` "
     "and `C.K2b`."),
    ("&#9432; Elements carrying a second item",
     "`A.K3`, `B.K5`, `C.K2` and `C.K4` each carry two items &#8212; in each case separating "
     "a cited requirement from the judgement or scope limit that the ACS element also asks "
     "for."),
]


def main():
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "OHC_M08_OperationalRules.pre.html")
    with open(out, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))


if __name__ == "__main__":
    main()
