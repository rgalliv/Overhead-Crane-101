#!/usr/bin/env python3
"""OHC-09 Communication and Signals -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M09"
MODLABEL = "Module 9"
TITLE = "Communication and Signals"
SUBTITLE = ("Direct and receive lift communication using standard signals and disciplined "
            "verbal protocols.")

OBJECTIVES = [
    "Use and respond to the standard overhead crane hand signal set, and know when a signal "
    "person is required and who is permitted to be one.",
    "Conduct lifts on closed-loop verbal and radio direction, with motion vocabulary anchored "
    "to fixed references and a stop-and-hold convention on communication loss.",
    "Integrate spotters, riggers and adjacent trades into the lift communication plan, and "
    "honour stop-work authority from anyone.",
]

SECTIONS = [
    ("A", "Standard Hand Signals",
     "Use and respond to standard overhead crane hand signals."),
    ("B", "Verbal and Radio Protocols",
     "Conduct lifts on verbal direction with closed-loop communication."),
    ("C", "Crew Coordination",
     "Integrate spotters, riggers, and adjacent trades into the lift communication plan."),
]

CONTENT = {
    "A": [
        ("One standard set, and it is not yours to invent",
         "The overhead crane signal set is small and fixed: <b>hoist</b>, <b>lower</b>, "
         "<b>bridge travel</b>, <b>trolley travel</b>, <b>stop</b>, and <b>emergency "
         "stop</b>. <b>EM 385-1-1 &sect;16.G.05.a</b> requires a <b>standard signal "
         "system</b> on all lifting and hoisting equipment &#8212; by hand, voice, audible "
         "or comparable signals.",
         "Where hand signals are used, the <b>Standard Method</b> must be used. The DOE "
         "Hanford manual states the same rule from the other side: <i>the standard overhead "
         "crane and hoist hand signals adopted by ANSI standards are to be used.</i>"),
        ("The hundred-foot boundary",
         "<b>&sect;16.G.05.a(1)</b>: manual hand signals may be used when the distance "
         "between the operator and signal person is <b>not more than 100 ft</b> (30.4 m). "
         "Beyond that, hands stop working as a channel.",
         "<b>&sect;16.G.05.a(2)</b>: radio, telephone, or a visual and audible "
         "electrically-operated system <b>shall</b> be used when the distance is <b>more "
         "than 100 ft</b>, <b>or when the operator and signal person cannot see each "
         "other</b>. Either trigger, not both."),
        ("Three situations that require a signal person",
         "<b>&sect;16.G.05.b</b> names them and they are not judgement calls. A signal "
         "person must be used: when the <b>point of operation, load travel, or the area near "
         "or at load placement is not in full view of the operator</b>; when the equipment "
         "is <b>traveling and the view in the direction of travel is obstructed</b>.",
         "And the third, which is the one that protects everybody: <b>due to site-specific "
         "safety concerns, either the operator or the person handling the load determines "
         "that it is necessary</b>. Either party can call for a signaler. Neither needs "
         "permission."),
        ("Who is permitted to signal",
         "A signal person is a <b>qualified</b> role, not a volunteer. <b>&sect;16.B.06</b> "
         "requires qualification by a third-party Qualified Evaluator or the employer's "
         "Qualified Evaluator, with <b>documentation specifying each type of signaling</b> "
         "&#8212; hand, radio, and so on &#8212; the person is qualified for.",
         "The qualification covers knowing the Standard Method, competence in applying it, "
         "and <b>a basic understanding of crane operation and limitations, including the "
         "dynamics of swinging and stopping loads</b>, demonstrated by <b>written and "
         "practical test</b>. And one clause people miss: an <b>employer's assessment is not "
         "portable</b> &#8212; another employer may not rely on it."),
        ("One signaler at a time",
         "<b>&sect;16.G.05.d</b>, first half: <b>only one person gives signals to the "
         "operator at a time</b>. Two people signalling is not redundancy; it is two "
         "instructions and one crane.",
         "The signaler is agreed before the lift and is identifiable &#8212; by position, by "
         "vest, by name. If the operator cannot tell who the signaler is, the signaler has "
         "not been established."),
        ("Except the one signal anybody can give",
         "<b>&sect;16.G.05.d</b>, second half: the single-signaler rule holds <b>unless an "
         "emergency stop signal is given, which may be given by <i>anyone</i> and must be "
         "obeyed by the operator</b>.",
         "This is the only signal with no authority requirement attached. Anyone who sees "
         "something can stop the crane, and the operator's duty is to comply first and ask "
         "afterwards. A stop that turns out to be unnecessary costs a minute."),
        ("Where the signaler stands",
         "Two requirements at once: <b>visible to the operator</b> for the whole signalling "
         "period, and <b>clear of the load</b> and its fall zone. Losing either one ends the "
         "lift.",
         "These conflict on tight placements, and the resolution is never to compromise the "
         "second. If the only position with a view is inside the fall zone, the answer is a "
         "different channel &#8212; radio, or a second spotter relaying &#8212; not a "
         "signaler standing under the load."),
        ("Charts, and what to do when the standard does not fit",
         "The signal chart is <b>posted</b> where operators and signalers can see it, and the "
         "signals to be used are <b>agreed before the lift</b>, not discovered during it.",
         "Hanford states the exception precisely: <i>if compliance with these hand signals is "
         "impractical for the job being performed, <b>other hand signals shall be agreed on "
         "by the operator and signal person</b></i>, and radio may be substituted by the same "
         "agreement. Non-standard signals are permitted &#8212; <b>invented</b> ones are "
         "not. The difference is the agreement, made in advance."),
        ("Which rulebook you are actually under",
         "This module has the <b>opposite</b> branch profile to OHC-05. On the <b>facility "
         "branch</b> &#8212; permanently installed, &sect;1926.1438(a) &#8212; only "
         "&sect;1910.179 applies, and &sect;1910.179 says <b>almost nothing about "
         "signals</b>: a warning device at (i), and a warning signal at (n)(3)(xi). No signal "
         "chart, no signal person qualification, no voice protocol.",
         "On the <b>construction branch</b> &#8212; not permanently installed, "
         "&sect;1926.1438(b) &#8212; the enumeration at (b)(2)(i) pulls in "
         "<b>&sect;&sect;1926.1417 through 1425</b> and <b>&sect;&sect;1926.1427 through "
         "1434</b>, which is the <b>entire Subpart CC signals regime</b>: 1419 general, 1420 "
         "radio and electronic, 1421 voice, 1422 hand signal chart, and <b>1428 signal person "
         "qualifications</b>. The detailed rules live on the branch the ACS says least about."),
    ],
    "B": [
        ("Closed loop, four steps",
         "Verbal direction is not a stream of instructions. It is a loop that closes each "
         "time: <b>direction</b> given, <b>readback</b> by the receiver, <b>execution</b>, "
         "<b>confirmation</b> that it happened.",
         "The readback is the step people drop, and it is the step that catches the error. "
         "Hearing <i>&#8220;down two feet&#8221;</i> and saying <i>&#8220;down two "
         "feet&#8221;</i> costs a second and catches the difference between two feet and two "
         "inches."),
        ("Radio discipline",
         "A radio channel is shared infrastructure. Discipline means an <b>assigned "
         "channel</b>, <b>identification</b> on each transmission so everyone knows who is "
         "speaking to whom, and for blind work a <b>continuous-communication</b> rule rather "
         "than intermittent check-ins.",
         "<b>&sect;16.G.05.a(2)</b> is what puts you on radio in the first place: it is "
         "required beyond 100 ft, or whenever the operator and signal person cannot see each "
         "other. If you are on radio because of the second trigger, the radio is the only "
         "channel you have."),
        ("Anchor directions to the building, not to your body",
         "&#8220;Left&#8221; and &#8220;right&#8221; depend on which way the speaker is "
         "facing. Two people facing each other have opposite lefts, and the load moves "
         "according to whichever one the operator guessed.",
         "Standardised vocabulary ties motion to <b>fixed references</b>: north, the press "
         "end, column line 4, toward the roll-up door. The reference is chosen in the "
         "pre-lift briefing and it does not move when people turn around."),
        ("Communication lost means stop",
         "<b>&sect;16.G.05.c</b> is the rule and it is unambiguous: during operations "
         "requiring signals, the ability to transmit signals <b>shall be maintained</b>. If "
         "that ability is <b>interrupted at any time</b>, the operator shall <b>safely stop "
         "operations requiring signals until it is re-established and a proper signal is "
         "given and understood</b>.",
         "Three conditions to resume, not one: re-established, <b>proper signal given</b>, "
         "<b>and understood</b>. A radio crackling back to life is not permission to move."),
        ("Silence is not consent",
         "The dangerous reading of a dropout is that no instruction means keep going. On a "
         "blind placement the operator has no other information, and the load continues into "
         "a space nobody is watching.",
         "This is why the stop convention is agreed <b>before</b> the lift. Mid-motion is not "
         "when to negotiate what silence means."),
        ("Mixed-language crews",
         "Where the crew does not share a first language, the requirement is not goodwill; it "
         "is <b>terminology alignment before the lift</b>. Agree the motion words, agree who "
         "interprets, and confirm both directions of the loop work.",
         "The signal set is an asset here &#8212; hand signals are language-independent, and "
         "a crew that agrees on the Standard Method has a channel that does not depend on "
         "vocabulary at all."),
    ],
    "C": [
        ("The pre-lift briefing has six headings",
         "<b>Load</b> &#8212; what it is and what it weighs. <b>Path</b> &#8212; where it "
         "goes and over what. <b>Roles</b> &#8212; who operates, who signals, who spots, who "
         "rigs. <b>Signals</b> &#8212; which set, which channel, which fixed references.",
         "<b>Exclusion zones</b> &#8212; where nobody stands. And <b>stop-work "
         "authority</b> &#8212; stated out loud, so that using it later does not require "
         "courage. A briefing that omits the last two has covered the mechanics and skipped "
         "the protection."),
        ("Spotter is not signaler",
         "The <b>signaler</b> directs the crane. The <b>spotter</b> watches something the "
         "operator and signaler cannot &#8212; path clearance, an adjacent hazard, a pinch "
         "point, traffic. Different job, different attention, and normally a different "
         "person.",
         "EM 385 does describe a signal person acting as a spotter for a specific watch, so "
         "the roles can combine by design. What causes incidents is combining them by "
         "accident &#8212; a spotter who starts giving motion signals, or a signaler who "
         "looks away to check clearance."),
        ("Stop-work authority is universal or it is nothing",
         "<b>&sect;16.G.05.d</b> already grants it in the narrow case: an emergency stop "
         "<b>may be given by anyone and must be obeyed</b>. A functioning site extends that "
         "to any hazard, from any person, at any time.",
         "The hard part is not the authority; it is the <b>without penalty</b>. Authority "
         "that costs the user something is authority nobody uses twice. It has to be honoured "
         "visibly &#8212; thank the caller, check the concern, then resume."),
        ("Production environments have other operators in them",
         "In a live bay the crane shares space with machine operators, line personnel, "
         "forklifts and foot traffic, none of whom are part of the lift and most of whom are "
         "concentrating on something else.",
         "Coordination means telling them before you start, not warning them while you move. "
         "A lift path across a production line is a two-supervisor conversation before it is "
         "a crane movement."),
        ("Crane-to-crane contact is an adjacent-crew event",
         "<b>EM 385-1-1 16-8.aa(6)</b>: contact with runway stops or other cranes is made "
         "with <b>extreme caution</b>, with particular care for persons on or below the "
         "crane, and <b>only after making certain that persons on the other cranes are "
         "aware</b>.",
         "Read that last clause as a communication requirement, because that is what it is. "
         "Before contact, the other crane's crew is <b>told and has acknowledged</b>. Not "
         "signalled at &#8212; aware. Cross-refs `OHC.08.B.K2`."),
        ("Trades who arrive without knowing",
         "The most common uninvited hazard is a competent person doing their own job who has "
         "no idea a lift is underway. They did not ignore the exclusion zone; they never knew "
         "it existed.",
         "Which makes the control physical and informational rather than verbal: barriers and "
         "signage that work on someone who was never at the briefing, plus a spotter watching "
         "the approaches rather than the load."),
    ],
}

PRACTICE = [
    ("OHC.09.A.K1b",
     "Hand signals may be used when the distance between operator and signal person is not "
     "more than:",
     ["50 ft", "75 ft", "100 ft", "150 ft"], 2,
     "EM 385 &sect;16.G.05.a(1) sets 100 ft (30.4 m). Beyond that, or when they cannot see "
     "each other, radio or an electrically-operated system is required."),
    ("OHC.09.A.K2",
     "Which of these does NOT by itself require a signal person under EM 385 "
     "&sect;16.G.05.b?",
     ["Load placement not in full view of the operator",
      "Travel with the view in the direction of travel obstructed",
      "The load exceeding 50&#37; of rated capacity",
      "The operator determining it is necessary for site-specific safety concerns"], 2,
     "The three triggers are view of the operation, obstructed travel view, and either party "
     "judging it necessary. Load percentage is not one of them."),
    ("OHC.09.A.K3",
     "Two crew members are both giving motion signals. This is:",
     ["Acceptable redundancy", "A violation of the one-signaler-at-a-time rule",
      "Required for blind lifts", "Acceptable if they agree"], 1,
     "&sect;16.G.05.d: only one person gives signals to the operator at a time."),
    ("OHC.09.A.K3b",
     "An emergency stop signal may be given by:",
     ["The designated signaler only", "The lift director only", "Anyone",
      "The operator only"], 2,
     "&sect;16.G.05.d: it may be given by anyone and must be obeyed by the operator."),
    ("OHC.09.A.K2b",
     "An employer's Qualified Evaluator assessment of a signal person is portable to other "
     "employers.",
     ["True", "False"], 1,
     "&sect;16.B.06.e: an employer's assessment is not portable. Other employers are not "
     "permitted to use it."),
    ("OHC.09.B.K1",
     "The step most often dropped from the closed-loop protocol is:",
     ["Direction", "Readback", "Execution", "Confirmation"], 1,
     "Readback is the step that catches the error, and it is the one that gets skipped."),
    ("OHC.09.B.K3",
     "Motion vocabulary should be tied to:",
     ["The operator's left and right", "The signaler's left and right",
      "Fixed references agreed in the pre-lift briefing", "Compass bearings only"], 2,
     "Left and right invert depending on which way the speaker faces. Fixed references do not "
     "move when people turn around."),
    ("OHC.09.B.K4",
     "Radio contact is lost mid-motion. Conditions to resume are:",
     ["Communication re-established", "Communication re-established and a proper signal given",
      "Communication re-established, a proper signal given, and understood",
      "Any of the above, at the operator's discretion"], 2,
     "&sect;16.G.05.c requires all three. A radio coming back to life is not permission to "
     "move."),
    ("OHC.09.C.K3",
     "Stop-work authority fails in practice most often because:",
     ["It is not written down", "Using it carries a cost to the person who uses it",
      "Operators cannot hear it", "It is limited to supervisors"], 1,
     "Authority that costs the user something is authority nobody uses twice. It must be "
     "honoured without penalty."),
]

GATE = [
    # ---- Task A
    ("OHC.09.A.K1",
     "The standard overhead crane signal set covers:",
     ["Hoist and lower only", "Hoist, lower, bridge travel, trolley travel, stop, and "
      "emergency stop", "Boom up, boom down, swing, and travel",
      "Whatever the crew agrees on the day"], 1, ""),
    ("OHC.09.A.K1b",
     "EM 385 &sect;16.G.05 requires radio, telephone, or a visual and audible "
     "electrically-operated system when:",
     ["The load exceeds 10 tons",
      "The distance exceeds 100 ft, or the operator and signal person cannot see each other",
      "Only when the distance exceeds 100 ft", "The lift is designated critical"], 1, ""),
    ("OHC.09.A.K2",
     "Under EM 385 &sect;16.G.05.b, a signal person is required when:",
     ["The load exceeds half of rated capacity",
      "The point of operation, load travel, or placement area is not in full view of the "
      "operator", "Two or more riggers are present", "The lift is outdoors"], 1, ""),
    ("OHC.09.A.K2b",
     "Signal person qualification under EM 385 &sect;16.B.06 requires documentation that:",
     ["Names the crane the person was assessed on",
      "Specifies each type of signaling the person is qualified for",
      "Is valid for five years", "Is issued by the crane manufacturer"], 1, ""),
    ("OHC.09.A.K3",
     "The single-signaler rule states that:",
     ["Only a supervisor may signal", "Only one person gives signals to the operator at a "
      "time", "Signals must be given by two people for verification",
      "The rigger always signals"], 1, ""),
    ("OHC.09.A.K3b",
     "The exception to the single-signaler rule is:",
     ["A supervisor may override the signaler",
      "An emergency stop signal, which may be given by anyone and must be obeyed",
      "The rigger may signal during rigging", "There is no exception"], 1, ""),
    ("OHC.09.A.K4",
     "Signaler positioning requires that the signaler be:",
     ["Visible to the operator", "Clear of the load",
      "Both visible to the operator and clear of the load",
      "Within 20 ft of the load"], 2, ""),
    ("OHC.09.A.K5",
     "Where the standard hand signals are impractical for the job, the correct course is:",
     ["The operator improvises signals as needed",
      "Other signals are agreed between the operator and signal person in advance",
      "The lift is prohibited", "The signaler chooses new signals during the lift"], 1, ""),
    ("OHC.09.A.K5b",
     "On the construction branch, &sect;1926.1438(b)(2)(i) brings in the Subpart CC signals "
     "sections, including:",
     ["Nothing on signals -- &sect;1910.179 governs alone",
      "&sect;&sect;1926.1419 through 1422 and &sect;1926.1428 signal person qualifications",
      "&sect;1926.1412 only", "ASME B30.9 only"], 1, ""),
    ("OHC.09.A.R1",
     "Conflicting signals from multiple crew members should be met with:",
     ["Following the most senior person", "Stopping and re-establishing a single signaler",
      "Following the first signal received", "Averaging the instructions"], 1, ""),
    ("OHC.09.A.R2",
     "The only position with a clear view of a tight placement is inside the fall zone. The "
     "correct resolution is:",
     ["Signal from that position briefly", "Signal from there wearing full PPE",
      "Use a different channel -- radio, or a spotter relaying from a safe position",
      "Have the operator proceed without signals"], 2, ""),
    ("OHC.09.A.R3",
     "An operator receives a signal that is unclear. The required action is:",
     ["Execute the most likely interpretation slowly",
      "Do not move -- stop and re-establish communication",
      "Ask the rigger to interpret", "Proceed and watch for a stop signal"], 1, ""),
    # ---- Task B
    ("OHC.09.B.K1",
     "The closed-loop verbal protocol is:",
     ["Direction and execution", "Direction, execution, confirmation",
      "Direction, readback, execution, confirmation", "Readback and confirmation"], 2, ""),
    ("OHC.09.B.K2",
     "Radio discipline for blind work requires:",
     ["Periodic check-ins at agreed intervals",
      "An assigned channel, identification on transmissions, and continuous communication",
      "A single transmission before each motion", "Two radios per person"], 1, ""),
    ("OHC.09.B.K3",
     "Anchoring motion vocabulary to fixed references rather than left and right prevents:",
     ["Radio cross-talk", "Direction reversing depending on which way the speaker faces",
      "Signal person fatigue", "Channel congestion"], 1, ""),
    ("OHC.09.B.K4",
     "EM 385 &sect;16.G.05.c requires that when the ability to transmit signals is "
     "interrupted, the operator:",
     ["Continues at reduced speed until contact returns",
      "Safely stops operations requiring signals until communication is re-established and a "
      "proper signal is given and understood",
      "Completes the current motion, then stops", "Switches to hand signals"], 1, ""),
    ("OHC.09.B.K5",
     "For a crew without a shared first language, the required provision is:",
     ["Hand signals only, in all cases",
      "Terminology alignment and interpretation arranged before the lift",
      "A supervisor translating during the lift", "Written instructions only"], 1, ""),
    ("OHC.09.B.R1",
     "Unanchored left/right language is hazardous because:",
     ["It is slower to say", "Two people facing each other have opposite lefts, so the load "
      "moves the wrong way", "It cannot be transmitted by radio",
      "It is not in the Standard Method"], 1, ""),
    ("OHC.09.B.R2",
     "The dangerous interpretation of a radio dropout mid-motion is:",
     ["That the lift is complete", "That silence means continue",
      "That the signaler has moved", "That the channel is congested"], 1, ""),
    ("OHC.09.B.R3",
     "Cross-talk from adjacent operations on a shared channel is controlled by:",
     ["Speaking louder", "Channel assignment and identification on each transmission",
      "Using hand signals instead at any distance", "Reducing transmission power"], 1, ""),
    # ---- Task C
    ("OHC.09.C.K1",
     "A complete pre-lift briefing covers load, path, roles, signals, and:",
     ["The crane's inspection date", "Exclusion zones and stop-work authority",
      "The rigging manufacturer", "The production schedule"], 1, ""),
    ("OHC.09.C.K2",
     "The spotter's role is distinct from the signaler's in that the spotter:",
     ["Gives motion signals when the signaler is busy",
      "Watches path clearance and adjacent hazards the operator and signaler cannot see",
      "Supervises the rigging", "Operates the pendant"], 1, ""),
    ("OHC.09.C.K3",
     "Stop-work authority must be:",
     ["Limited to the signaler and lift director", "Universal, and honoured without penalty",
      "Exercised only through a supervisor", "Documented before it may be used"], 1, ""),
    ("OHC.09.C.K4",
     "In a live production bay, coordination with machine operators and line personnel "
     "should happen:",
     ["While the load is travelling, using the warning device",
      "Before the lift starts", "Only if the path crosses their station",
      "At the end of the shift"], 1, ""),
    ("OHC.09.C.K5",
     "EM 385-1-1 16-8.aa(6) requires that before contact with another crane, persons on that "
     "crane are:",
     ["Signalled at", "Aware -- told and acknowledged", "Off the crane",
      "Notified afterwards"], 1, ""),
    ("OHC.09.C.R1",
     "Role confusion between signaler and spotter typically shows up as:",
     ["Two people using the same radio channel",
      "A spotter beginning to give motion signals, or a signaler looking away to check "
      "clearance", "The rigger signalling", "The operator signalling to himself"], 1, ""),
    ("OHC.09.C.R2",
     "Stop-work hesitancy under production pressure is best countered by:",
     ["A written policy alone", "Stating the authority in the briefing and honouring its use "
      "visibly", "Assigning it only to supervisors", "Financial incentives"], 1, ""),
    ("OHC.09.C.R3",
     "Uninformed adjacent trades entering the operation are best controlled by:",
     ["Sounding the warning device more often",
      "Physical barriers and signage plus a spotter watching the approaches",
      "A note in the pre-lift briefing", "Radio announcements on the shared channel"],
     1, ""),
]

TRACE_SOURCE = {
    "OHC.09.A.K1": ("**EM 385 &sect;16.G.05.a** &middot; **DOE Hanford TR244C** (ANSI set)",
                    "ED2014"),
    "OHC.09.A.K1b": ("**EM 385 &sect;16.G.05.a(1)&#8211;(2)** 100 ft", "ED2014"),
    "OHC.09.A.K2": ("**EM 385 &sect;16.G.05.b** three situations", "ED2014"),
    "OHC.09.A.K2b": ("**EM 385 &sect;16.B.06.b, .d, .e**", "ED2014"),
    "OHC.09.A.K3": ("**EM 385 &sect;16.G.05.d** first half", "ED2014"),
    "OHC.09.A.K3b": ("**EM 385 &sect;16.G.05.d** second half", "ED2014"),
    "OHC.09.A.K4": ("derived &middot; EM 385 &sect;16.G.05", "OK"),
    "OHC.09.A.K5": ("**DOE Hanford TR244C** impractical-signals rule", "OK"),
    "OHC.09.A.K5b": ("**&sect;1926.1438(b)(2)(i)** enumeration", "OPEN"),
    "OHC.09.A.R1": ("EM 385 &sect;16.G.05.d &middot; derived", "OK"),
    "OHC.09.A.R2": ("derived", "OK"),
    "OHC.09.A.R3": ("**EM 385 &sect;16.G.05.c** &middot; derived", "ED2014"),
    "OHC.09.B.K1": ("Tier 0 closed-loop protocol", "OK"),
    "OHC.09.B.K2": ("**EM 385 &sect;16.G.05.a(2)** &middot; derived", "ED2014"),
    "OHC.09.B.K3": ("Tier 0 &middot; derived", "OK"),
    "OHC.09.B.K4": ("**EM 385 &sect;16.G.05.c**", "ED2014"),
    "OHC.09.B.K5": ("derived", "OK"),
    "OHC.09.B.R1": ("derived", "OK"),
    "OHC.09.B.R2": ("**EM 385 &sect;16.G.05.c** &middot; derived", "ED2014"),
    "OHC.09.B.R3": ("derived", "OK"),
    "OHC.09.C.K1": ("Tier 0 pre-lift briefing &middot; derived", "OK"),
    "OHC.09.C.K2": ("EM 385 &sect;16 spotter watch &middot; derived", "OK"),
    "OHC.09.C.K3": ("**EM 385 &sect;16.G.05.d** &middot; derived", "ED2014"),
    "OHC.09.C.K4": ("derived", "OK"),
    "OHC.09.C.K5": ("**EM 385 16-8.aa(6)**", "OK"),
    "OHC.09.C.R1": ("derived", "OK"),
    "OHC.09.C.R2": ("derived", "OK"),
    "OHC.09.C.R3": ("derived", "OK"),
}

TRACE_PERF = [
    ("OHC.09.A.S1", "Demonstrate the standard signal set as signaler and as operator"),
    ("OHC.09.A.S2", "Execute a lift sequence entirely on hand signals"),
    ("OHC.09.A.S3", "Stop on any unclear signal and re-establish communication"),
    ("OHC.09.B.S1", "Conduct a blind placement on continuous verbal direction"),
    ("OHC.09.B.S2", "Demonstrate stop-and-hold on communication loss"),
    ("OHC.09.B.S3", "Establish a pre-lift terminology agreement with a mixed crew"),
    ("OHC.09.C.S1", "Deliver a complete pre-lift briefing"),
    ("OHC.09.C.S2", "Integrate a spotter into a congested-path lift"),
    ("OHC.09.C.S3", "Demonstrate an unprompted stop-work response to an introduced hazard"),
]

TRACE_NOTES = [
    ("&#11088; The branch profile is the inverse of OHC-05 &#8212; and it is the module's "
     "most important fact",
     "On the **facility branch** (&sect;1926.1438(a)) only &sect;1910.179 applies, and "
     "&sect;1910.179 contains **almost nothing on signals**: a warning device at **(i)** and "
     "a warning signal at **(n)(3)(xi)**. No signal chart, no signal person qualification, "
     "no voice or radio protocol. On the **construction branch**, the enumeration at "
     "**&sect;1926.1438(b)(2)(i)** brings in **&sect;&sect;1926.1417 through 1425** and "
     "**&sect;&sect;1926.1427 through 1434** &#8212; which is the whole Subpart CC signals "
     "regime: **1419** general, **1420** radio and electronic, **1421** voice, **1422** hand "
     "signal chart, and **1428** signal person qualifications. In OHC-05 the facility branch "
     "was rich and construction was the gap. Here it is exactly reversed. `A.K5b` gates the "
     "finding."),
    ("&#9888;&#65039; Section-level verified; paragraph text of the CC signals sections not "
     "held",
     "The applicability above was read from the &sect;1926.1438(b)(2)(i) enumeration and the "
     "section headings. The **paragraph-level text of &sect;&sect;1926.1419&#8211;1422 and "
     "&sect;1926.1428 is not held in usable form** &#8212; the corpus copy is a heavily "
     "OCR-degraded scan, and osha.gov and ecfr.gov are both blocked by this environment's "
     "egress policy. Nothing below section level is gated from those sections. This is the "
     "same shape of gap as **&sect;1926.1412/1413** in OHC-05 (`B.R3`), and it is now the "
     "largest remaining sourcing hole in the track."),
    ("&#9888;&#65039; EM 385 citations here are **2014 numbering**",
     "Every &sect;16.G.05 and &sect;16.B.06 citation was read verbatim from the standalone "
     "Section 16 extract, which is the **2014** edition and numbers Section 16 by letter. "
     "The ACS references the **15 Mar 2024** edition, whose Section 16 paragraph numbers "
     "could not be re-read &#8212; every available reader caps around page 92 of 757. For "
     "**16-8.aa(6)** the 1:1 crosswalk is established (see the EM 385 note) and the ACS "
     "number is used. For **&sect;16.G.05** and **&sect;16.B.06** the ACS cites nothing, so "
     "there is no crosswalk anchor and **the 2024 equivalents are unconfirmed**. Items are "
     "marked *2014 text* accordingly. **Confirm the 2024 numbers before publication.**"),
    ("&#9989; Three ACS elements land on verbatim EM 385 text",
     "`A.K2` &#8594; **&sect;16.G.05.b**, which names the three situations requiring a signal "
     "person, including the one either party can invoke: *due to site-specific safety "
     "concerns, either the operator or the person handling the load determines that it is "
     "necessary.* `A.K3`/`A.K3b` &#8594; **&sect;16.G.05.d**, which carries the "
     "single-signaler rule and its emergency-stop exception in one sentence &#8212; *which "
     "may be given by anyone and must be obeyed by the operator.* `B.K4` &#8594; "
     "**&sect;16.G.05.c**, whose three conditions to resume (re-established, proper signal "
     "given, **and understood**) are tighter than the ACS's *&#8220;stop and hold.&#8221;*"),
    ("&#9989; `A.K1b` adds the 100 ft boundary the ACS omits",
     "**&sect;16.G.05.a(1)&#8211;(2)**: hand signals may be used at **not more than 100 ft** "
     "(30.4 m); radio, telephone, or a visual and audible electrically-operated system is "
     "**required** beyond 100 ft **or when the operator and signal person cannot see each "
     "other**. Two independent triggers. The ACS has no distance criterion anywhere in "
     "OHC-09, which leaves the hand-signal/radio decision to judgement when it is actually a "
     "number."),
    ("&#9989; `A.K2b` adds who may signal, including the non-portability clause",
     "The ACS asks *when* a signaler is required but never *who may be one*. **&sect;16.B.06** "
     "answers it: qualification by a third-party or employer Qualified Evaluator, "
     "documentation specifying **each type of signaling**, competence plus **a basic "
     "understanding of crane dynamics in swinging and stopping loads**, demonstrated by "
     "**written and practical test** &#8212; and **&sect;16.B.06.e**, an employer's "
     "assessment is **not portable** to other employers. That last clause is routinely "
     "assumed the other way."),
    ("&#9989; `A.K5` &#8212; non-standard signals are allowed, invented ones are not",
     "The DOE Hanford manual (public domain) states the exception cleanly: the ANSI-adopted "
     "signals are to be used, but *if compliance with these hand signals is impractical for "
     "the job being performed, other hand signals shall be agreed on by the operator and "
     "signal person*, and radio may be substituted by the same agreement. The distinguishing "
     "feature is **advance agreement**, which is what `A.K5` gates."),
]


def main():
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "OHC_M09_CommunicationAndSignals.pre.html")
    with open(out, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))


if __name__ == "__main__":
    main()
