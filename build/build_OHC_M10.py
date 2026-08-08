#!/usr/bin/env python3
"""OHC-10 Environmental and Site Hazards -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M10"
MODLABEL = "Module 10"
TITLE = "Environmental and Site Hazards"
SUBTITLE = ("Recognise and control the facility, environmental and energy hazards that act "
            "on an overhead crane operation.")

OBJECTIVES = [
    "Survey and clear a lift path through the building, storage and traffic environment, and "
    "suspend operations for inadequate visibility.",
    "Apply environmental limits for outdoor and special-service cranes, including wind, ice "
    "and hot-metal provisions, and know which wind numbers actually apply.",
    "Identify electrical and process energy along a lift path, hold a placement pending "
    "isolation, and route around energised equipment.",
]

SECTIONS = [
    ("A", "Facility and Layout Hazards",
     "Manage hazards created by the building, storage, and traffic environment."),
    ("B", "Environmental Conditions",
     "Apply environmental limits for outdoor and special-service cranes."),
    ("C", "Energy and Process Hazards",
     "Control electrical and process energy exposure during operations."),
]

CONTENT = {
    "A": [
        ("Obstruction is a regulated condition, not just untidiness",
         "&sect;1910.179(b)(6)(ii): <i>where passageways or walkways are provided, "
         "<b>obstructions shall not be placed so that safety of personnel will be jeopardized "
         "by movements of the crane</b></i>.",
         "Read the test in that sentence &#8212; it is not <i>&#8220;is the aisle "
         "tidy&#8221;</i>, it is <b>could the crane's movement make this stack dangerous to "
         "somebody</b>. (b)(6) is in the &sect;1926.1438(b)(2) list, so it binds on both "
         "branches."),
        ("The clearance envelope belongs to the crane, permanently",
         "A runway has a swept volume that is the crane's at all times, whether or not the "
         "crane is in it. Material staged inside that envelope is not <i>&#8220;in the way "
         "today&#8221;</i>; it is inside a space that was never available.",
         "Storage creep is gradual and it is nobody's decision. A pallet goes down for an "
         "hour, a rack is extended by one bay, a delivery is staged where there was room. The "
         "envelope does not move to accommodate any of it."),
        ("Traffic that is not part of the lift",
         "Pedestrians and vehicles cross load paths, and neither is watching the ceiling. A "
         "forklift driver is looking at their forks and their mirrors; a pedestrian is looking "
         "at where they are walking.",
         "Two different controls. Pedestrians need <b>barriers and signage</b> that work on "
         "somebody who never attended a briefing. Vehicles need <b>coordination with the "
         "driver or their supervisor</b>, because a forklift cannot stop or steer like a "
         "person."),
        ("What is between the crane and the ceiling",
         "Piping, lighting, ductwork, conduit, sprinkler mains, cable tray and adjacent "
         "equipment all occupy the space between the load's travel height and the structure. "
         "Most of it is fragile, some of it is energised, and some of it is both.",
         "The load's <b>highest point</b> is what clears these, not the hook. A load rigged "
         "with tall lifting lugs or a spreader beam has a different profile from the same load "
         "in slings."),
        ("Floors matter more for pendant operators",
         "A pendant or floor-operated crane makes the operator a pedestrian who is walking "
         "backwards while watching a load. Housekeeping, floor openings, hoses, spills and "
         "slick surfaces stop being background conditions and become the primary trip and "
         "fall risk.",
         "The path the <b>operator</b> walks is part of the lift plan, not just the path the "
         "load takes. Walk it before you load it."),
        ("Lighting &#8212; and what the standard actually covers",
         "&sect;1910.179(c)(4) is one sentence: <i><b>light in the cab</b> shall be sufficient "
         "to enable the operator to see clearly enough to perform his work.</i> That is the "
         "whole of the lighting requirement in the standard.",
         "Note the scope. It is the <b>cab</b> &#8212; not the load path, not the placement "
         "point, and not floor-operated cranes at all. (c) is also <b>not</b> in the "
         "&sect;1926.1438(b)(2) list, so it is facility-branch. Load-path and placement "
         "lighting is governed by <b>Part 1910 Subpart D</b> and the facility programme, and "
         "the ACS's broader reading of `A.K5` is the correct working rule &#8212; it just is "
         "not what (c)(4) says."),
        ("The path you surveyed is not the path you fly",
         "A path cleared at the start of a shift is a snapshot. Storage moves, staging "
         "arrives, a machine is opened for maintenance. The survey has a shelf life measured "
         "in hours, and the assumption that it does not is what puts a load into something.",
         "Re-survey when anything about the environment changed, and treat <i>&#8220;I ran "
         "this yesterday&#8221;</i> as information about yesterday."),
    ],
    "B": [
        ("Wind on an outdoor crane",
         "Wind acts on two things: the <b>load</b>, where it becomes a horizontal force "
         "proportional to sail area, and the <b>crane</b>, which is a large structure on "
         "wheels on a rail.",
         "<b>EM 385-1-1 16-8.aa(7)</b> gives the operator duty: <b>operators of outdoor "
         "cranes shall secure them when leaving</b>. &sect;1910.179(b)(4) gives the hardware "
         "for <b>outdoor storage bridges</b> &#8212; <b>automatic rail clamps</b> and a "
         "<b>wind-indicating device</b> with a visible or audible alarm at a <b>predetermined "
         "wind velocity</b>."),
        ("There is no published wind number for overhead cranes &#8212; and that matters",
         "&sect;1910.179(b)(4) requires the alarm at a <b>predetermined</b> velocity. It does "
         "not say what that velocity is. The number is set by the <b>manufacturer or the "
         "facility</b>, and it is the number you must know for your own crane.",
         "Two numbers get imported wrongly. The DOE Hanford manual's <b>25 mph</b> is a "
         "trigger for <b>evaluation by a qualified person</b>, not an operating limit. EM "
         "385's <b>20 mph</b> figure governs <b>tower crane climbing</b> &#8212; a different "
         "class, a different operation. Neither is an overhead crane's wind limit. <b>Get "
         "your own crane's number.</b>"),
        ("Cold changes the machine; heat changes the operator",
         "In cold, brake friction materials behave differently, lubricants stiffen, wire rope "
         "loses flexibility, and steel loses toughness &#8212; the structural concern is "
         "brittleness, not strength. Condensation that froze overnight can lock a brake or "
         "bond a clamp.",
         "In heat, the crane is largely unbothered and the <b>operator</b> degrades: "
         "concentration, reaction time and judgement all fall before anybody notices. In a "
         "cab without air conditioning this is the dominant hazard of a hot day."),
        ("Precipitation and ice do three separate things",
         "They <b>add weight</b> &#8212; accumulated water, snow or ice on a load is real "
         "mass that appears in nobody's calculation. They <b>reduce rail traction</b>, so "
         "wheels slip and braking distances stretch. And they <b>cut visibility</b> for "
         "operator, signaler and spotter at once.",
         "Ice adds a fourth: it bonds things together. A load frozen to the ground becomes a "
         "side pull the moment you take up slack, and the load breaks free with no warning "
         "and full stored energy."),
        ("Special service: hot metal",
         "&sect;1910.179(a) defines a <b>hot metal handling crane</b> as one used for "
         "transporting or pouring <b>molten material</b>, and the standard then treats it as "
         "its own class.",
         "<b>&sect;1910.179(g)(4)(iii)</b>: provision shall be made to <b>prevent broken parts "
         "or molten metal falling upon the operator or from the crane</b>. "
         "<b>&sect;1910.179(f)(2)(vi)</b>: each independent hoisting unit of a crane handling "
         "hot metal with power control braking shall have <b>at least two holding brakes</b>. "
         "Note the branch split &#8212; **(g)** is in the &sect;1926.1438(b)(2) list, "
         "**(f)(2)** is not."),
        ("Corrosive and washdown service",
         "Corrosive atmospheres and washdown areas attack the things inspection depends on: "
         "rope interior, electrical enclosures, brake surfaces and the legibility of markings "
         "and tags.",
         "The equipment provisions are a design matter &#8212; enclosure ratings, materials, "
         "sealed bearings. The <b>operator's</b> interest is narrower and constant: corrosion "
         "hides internally, so a rope in corrosive service is inspected on a shorter cycle "
         "than its appearance suggests. Cross-refs `OHC.05.C.K2`."),
        ("Who is watching the weather",
         "Weather monitoring is an assigned responsibility with a named owner and a stated "
         "suspension criterion. Unassigned, it defaults to whoever notices &#8212; which in "
         "practice is nobody, because everyone is doing their job.",
         "<b>EM 385 &sect;16.A</b> puts environmental considerations into the lift plan "
         "itself: <b>wind, storms, precipitation, and power lines in the area of travel or "
         "load swing</b>. The criterion is written down before the lift, so that suspending "
         "is a decision already made rather than an argument to be had."),
    ],
    "C": [
        ("Runway conductors are live and they are at working height",
         "&sect;1910.179(g)(6): open-type conductors mounted on runway beams or overhead "
         "<b>shall be so located or so guarded that persons entering or leaving the cab or "
         "crane footwalk normally could not come into contact with them</b>.",
         "Read <b>&#8220;normally&#8221;</b>. The guarding is designed against ordinary "
         "access, not against someone reaching, leaning or working in an unusual position. "
         "Any elevated access near a runway is an electrical job before it is a climbing job. "
         "(g) is in the &sect;1926.1438(b)(2) list &#8212; both branches."),
        ("The other conductor guard, on the crane itself",
         "&sect;1910.179(e)(5)(ii): a guard <b>shall be provided to prevent contact between "
         "bridge conductors and hoisting ropes</b> if they could come into contact.",
         "That guard is a component whose absence or damage is an inspection finding, and it "
         "is protecting against a rope energising. (e)(5) is also in the &sect;1926.1438(b)(2) "
         "list. Cross-refs `OHC.02` and `OHC.05.B.K1`."),
        ("Facility electrical along the path",
         "Bus ducts, panels, disconnects, transformers and open equipment cabinets sit at "
         "load-path height throughout a working building. A load does not have to touch them "
         "&#8212; a sling, a tag line or a swinging corner will do.",
         "The clearance you plan is not to the equipment; it is to the <b>swept volume of the "
         "load plus its rigging plus its swing</b>. That is a much larger shape than the load."),
        ("Process energy is quieter than electrical",
         "Steam lines, hydraulic runs, pneumatic mains and pressurised process piping are "
         "unmarked as often as not, look like structure, and fail with stored energy rather "
         "than a flash.",
         "A struck steam line is a burn hazard over a wide area with no visible source. A "
         "struck hydraulic line at pressure injects. Neither announces itself the way a "
         "conductor does, which is why they are identified in the survey rather than "
         "recognised on the way past."),
        ("Placing into equipment that is still in service",
         "Placement into a machine, fixture or line that has not been isolated is the highest "
         "consequence item in this module. The receiving equipment can move, cycle, energise, "
         "or hold pressure while a load is being introduced into it and people are working at "
         "the interface.",
         "The rule is simple and it is a hold, not a judgement: <b>no placement into "
         "in-service equipment</b>. The crane waits for isolation. This is the placement "
         "where the operator's stop-work authority is most likely to be needed and most "
         "likely to be unpopular."),
        ("The operator's interface with energy control",
         "The operator is not the authorised employee under the facility's energy control "
         "programme, and does not apply or remove isolations. The interface is narrower: "
         "<b>know that isolation is required, know who verifies it, and hold the placement "
         "until it is verified.</b>",
         "&sect;1910.147 governs the programme itself and is a facility-branch general "
         "industry standard the operator works alongside, not under. What the operator owes "
         "it is the hold."),
        ("The crane's own disconnects, and where they are",
         "&sect;1910.179(g)(5)(i): the power supply to the runway conductors shall be "
         "controlled by a switch or circuit breaker <b>located on a fixed structure, "
         "accessible from the floor, and arranged to be locked in the open position</b>.",
         "And on the crane: <b>(g)(5)(ii)</b> cab-operated cranes get an enclosed lockable "
         "switch in the leads from the runway conductors, openable <b>within easy reach of the "
         "operator</b>. <b>(g)(5)(iii)</b> floor-operated cranes get one mounted on the bridge "
         "or footwalk near the runway collectors, plus one of three floor-reachable means: a "
         "<b>nonconductive rope</b> to the main disconnect, an <b>undervoltage trip</b> "
         "operated by the pendant emergency stop, or a <b>main line contactor</b> operated "
         "from the pendant."),
    ],
}

PRACTICE = [
    ("OHC.10.A.K1",
     "&sect;1910.179(b)(6)(ii) sets the test for obstructions in passageways as:",
     ["Whether the aisle meets a minimum width",
      "Whether safety of personnel would be jeopardized by movements of the crane",
      "Whether the obstruction is permanent", "Whether the obstruction is marked"], 1,
     "The test is the crane's movement making the obstruction dangerous to people, not aisle "
     "tidiness or width."),
    ("OHC.10.A.K5",
     "The lighting requirement in &sect;1910.179(c)(4) covers:",
     ["The load path", "The placement point", "Light in the cab",
      "The whole bay"], 2,
     "It covers light in the cab only, and (c) is facility-branch. Load-path lighting comes "
     "from Subpart D and the facility programme."),
    ("OHC.10.B.K1b",
     "The correct wind limit for an outdoor overhead crane is:",
     ["25 mph, per the DOE Hanford manual", "20 mph, per EM 385",
      "The predetermined velocity set by the manufacturer or facility for that crane",
      "40 mph"], 2,
     "&sect;1910.179(b)(4) requires an alarm at a predetermined velocity but does not set "
     "one. Hanford's 25 mph is an evaluation trigger; EM 385's 20 mph governs tower crane "
     "climbing."),
    ("OHC.10.B.K3",
     "A load frozen to the ground is hazardous on lift-off because:",
     ["The rope will be cold", "It becomes a side pull that breaks free with stored energy",
      "The load weight is unchanged", "The brake will slip"], 1,
     "Ice bonds the load down. Taking up slack creates a side pull, and it releases without "
     "warning."),
    ("OHC.10.B.K4",
     "&sect;1910.179(f)(2)(vi) requires each independent hoisting unit of a hot metal crane "
     "with power control braking to have:",
     ["One holding brake", "At least two holding brakes", "A mechanical load brake only",
      "An emergency brake only"], 1,
     "At least two holding brakes. Note (f)(2) is facility-branch -- it is not in the "
     "&sect;1926.1438(b)(2) list."),
    ("OHC.10.C.K1",
     "&sect;1910.179(g)(6) requires open-type runway conductors to be located or guarded so "
     "that persons entering or leaving the cab or footwalk:",
     ["Are warned by signage", "Normally could not come into contact with them",
      "Wear insulating gloves", "Are accompanied by a second person"], 1,
     "The word is 'normally' -- the guarding is designed against ordinary access, not against "
     "reaching or working in unusual positions."),
    ("OHC.10.C.K5",
     "The operator's role in the facility energy control programme is to:",
     ["Apply and remove locks as needed", "Know isolation is required, know who verifies it, "
      "and hold the placement until verified", "Supervise the authorised employee",
      "Document the isolation"], 1,
     "The operator is not the authorised employee. What the operator owes the programme is "
     "the hold."),
    ("OHC.10.C.K5b",
     "Which is NOT one of the three floor-operated disconnect means in "
     "&sect;1910.179(g)(5)(iii)?",
     ["A nonconductive rope attached to the main disconnect switch",
      "An undervoltage trip operated by the pendant emergency stop button",
      "A main line contactor operated from the pendant",
      "A key-operated switch mounted in the cab"], 3,
     "The three named means are the nonconductive rope, the undervoltage trip, and the main "
     "line contactor. A cab switch is (g)(5)(ii), a different provision."),
    ("OHC.10.C.R2",
     "A load must be placed into a machine that has not been isolated. The correct action is:",
     ["Place it slowly with a spotter", "Place it and notify maintenance afterwards",
      "Hold the placement until isolation is verified", "Place it if the machine is idle"],
     2,
     "No placement into in-service equipment. The crane waits for isolation."),
]

GATE = [
    # ---- Task A
    ("OHC.10.A.K1",
     "Material staged inside a runway's clearance envelope is a problem because:",
     ["It looks untidy", "The envelope is the crane's swept volume at all times, whether or "
      "not the crane is currently in it", "It blocks the inspection route",
      "It may be damaged by dust"], 1, ""),
    ("OHC.10.A.K2",
     "Pedestrian and vehicle traffic require different controls because:",
     ["Vehicles move faster", "Pedestrians respond to barriers and signage, while vehicles "
      "need coordination with the driver or supervisor",
      "Pedestrians are always briefed", "Vehicles are easier to see"], 1, ""),
    ("OHC.10.A.K3",
     "When clearing overhead obstructions such as piping and ductwork, the governing "
     "dimension is:",
     ["The hook height", "The highest point of the load and its rigging",
      "The bridge height", "The trolley height"], 1, ""),
    ("OHC.10.A.K4",
     "Floor conditions matter most for a pendant operator because:",
     ["The pendant cable drags on the floor",
      "The operator walks -- often backwards -- while watching the load, making trips and "
      "slips the primary risk", "The floor carries the crane load",
      "Housekeeping is inspected"], 1, ""),
    ("OHC.10.A.K5",
     "&sect;1910.179(c)(4) requires that light be sufficient:",
     ["Along the entire load path", "In the cab, for the operator to perform his work",
      "At the placement point", "In the runway"], 1, ""),
    ("OHC.10.A.K5b",
     "Adequate lighting for the load path and placement point is governed by:",
     ["&sect;1910.179(c)(4)", "Part 1910 Subpart D and the facility programme",
      "EM 385 16-8.aa(4)", "Nothing -- it is discretionary"], 1, ""),
    ("OHC.10.A.R1",
     "A lift path surveyed at the start of the shift should be re-surveyed:",
     ["Weekly", "When anything about the storage, staging or environment has changed",
      "Only after an incident", "At the end of the shift"], 1, ""),
    ("OHC.10.A.R2",
     "Forklift and crane path conflicts are most dangerous because:",
     ["Forklifts are heavier", "The forklift driver is watching forks and mirrors, not the "
      "ceiling, and cannot stop or steer like a person",
      "Forklifts cannot hear the warning device", "Forklifts damage the floor"], 1, ""),
    ("OHC.10.A.R3",
     "A placement must be made in low light and illumination is inadequate. The correct "
     "action is:",
     ["Proceed slowly", "Proceed using the crane's own lighting",
      "Suspend operations until illumination is adequate", "Proceed with a second spotter"],
     2, ""),
    # ---- Task B
    ("OHC.10.B.K1",
     "EM 385-1-1 16-8.aa(7) requires operators of outdoor cranes to:",
     ["Monitor wind continuously", "Secure them when leaving",
      "Suspend work above 25 mph", "Install rail clamps"], 1, ""),
    ("OHC.10.B.K1b",
     "&sect;1910.179(b)(4) requires the wind-indicating alarm to trigger at:",
     ["25 mph", "20 mph", "A predetermined wind velocity, which the paragraph does not set",
      "40 mph"], 2, ""),
    ("OHC.10.B.K2",
     "The dominant temperature hazard on a hot day in an un-airconditioned cab is:",
     ["Brake fade", "Rope elongation", "Operator degradation -- concentration, reaction "
      "time and judgement", "Structural expansion"], 2, ""),
    ("OHC.10.B.K3",
     "Accumulated ice on a load matters chiefly because:",
     ["It reduces sling grip", "It is added weight that appears in nobody's calculation",
      "It makes the load easier to see", "It lubricates the rails"], 1, ""),
    ("OHC.10.B.K4",
     "&sect;1910.179(g)(4)(iii) requires that provision be made to prevent:",
     ["Wind loading on the bridge", "Broken parts or molten metal falling upon the operator "
      "or from the crane", "Rope corrosion", "Conductor contact"], 1, ""),
    ("OHC.10.B.K4b",
     "Of the two hot-metal provisions, which applies on BOTH regulatory branches?",
     ["&sect;1910.179(f)(2)(vi) two holding brakes",
      "&sect;1910.179(g)(4)(iii) protection from falling parts or molten metal",
      "Both apply on both branches", "Neither applies on the construction branch"], 1, ""),
    ("OHC.10.B.K5",
     "EM 385 &sect;16.A places which environmental items into the lift plan?",
     ["Temperature only", "Wind, storms, precipitation, and power lines in the area of travel "
      "or load swing", "Wind only", "Precipitation and lighting"], 1, ""),
    ("OHC.10.B.R1",
     "A wind gust is most hazardous with:",
     ["A dense, compact load", "A load with large surface area relative to its weight",
      "A load below 25&#37; of rated capacity", "A load in a basket hitch"], 1, ""),
    ("OHC.10.B.R2",
     "Ice-added weight is a hazard specifically because:",
     ["It corrodes the rigging", "It is not reflected in the documented load weight the lift "
      "was planned against", "It changes the centre of gravity only",
      "It reduces rope flexibility"], 1, ""),
    ("OHC.10.B.R3",
     "Continuing outdoor operation into deteriorating weather is best prevented by:",
     ["Operator judgement at the time", "A named weather-monitoring owner and a suspension "
      "criterion written down before the lift", "A wind alarm alone",
      "Checking the forecast at shift start"], 1, ""),
    # ---- Task C
    ("OHC.10.C.K1",
     "The significant word in &sect;1910.179(g)(6)'s conductor guarding requirement is:",
     ["\"overhead\" -- it applies only to overhead conductors",
      "\"normally\" -- guarding is designed against ordinary access, not reaching or working "
      "in unusual positions", "\"open\" -- enclosed conductors need no guarding",
      "\"runway\" -- bridge conductors are excluded"], 1, ""),
    ("OHC.10.C.K1b",
     "&sect;1910.179(e)(5)(ii) requires a guard to prevent contact between:",
     ["The load block and the trolley", "Bridge conductors and hoisting ropes",
      "The bumper and the runway stop", "The pendant cable and the bridge"], 1, ""),
    ("OHC.10.C.K2",
     "When planning clearance from a bus duct or open panel, the shape to clear is:",
     ["The load's footprint", "The swept volume of the load plus its rigging plus its swing",
      "The hook path", "The trolley path"], 1, ""),
    ("OHC.10.C.K3",
     "Steam and pressurised process lines are harder to manage than electrical hazards "
     "because:",
     ["They carry more energy", "They are often unmarked, look like structure, and fail with "
      "stored energy rather than a visible flash", "They are always at floor level",
      "They are outside the lift path"], 1, ""),
    ("OHC.10.C.K4",
     "Placement into equipment that has not been isolated is:",
     ["Permitted at reduced speed", "Permitted with a spotter",
      "Held until isolation is verified", "Permitted if the equipment is idle"], 2, ""),
    ("OHC.10.C.K5",
     "The operator's interface with the facility energy control programme is to:",
     ["Apply the isolation", "Verify the isolation personally",
      "Know isolation is required, know who verifies it, and hold the placement",
      "Document the isolation in the crane log"], 2, ""),
    ("OHC.10.C.K5b",
     "&sect;1910.179(g)(5)(i) requires the runway conductor power supply switch to be:",
     ["Mounted on the bridge", "On a fixed structure, accessible from the floor, and "
      "arranged to be locked in the open position", "Inside the cab only",
      "Operated by the pendant"], 1, ""),
    ("OHC.10.C.R1",
     "Contact between a load or its rigging and energised equipment is most often caused by:",
     ["Overloading", "Swing and rigging extending beyond the load's own footprint",
      "Brake failure", "Limit switch failure"], 1, ""),
    ("OHC.10.C.R2",
     "The reason placement onto in-service machinery is a hold rather than a judgement call "
     "is:",
     ["It takes longer", "The receiving equipment can move, cycle, energise or hold pressure "
      "while people work at the interface", "It requires a permit",
      "It voids the machine warranty"], 1, ""),
    ("OHC.10.C.R3",
     "Elevated access near runway conductors should be treated as:",
     ["A climbing task with fall protection", "An electrical task first, then a climbing task",
      "Routine maintenance access", "A task for the operator alone"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.10.A.K1": ("**&sect;1910.179(b)(6)(ii)** &#8212; both branches", "OK"),
    "OHC.10.A.K2": ("derived", "OK"),
    "OHC.10.A.K3": ("derived &middot; &sect;1910.179(b)(6)(i)", "OK"),
    "OHC.10.A.K4": ("derived &middot; **Subpart D** routing at &sect;1910.179(c)(2)", "OPEN"),
    "OHC.10.A.K5": ("**&sect;1910.179(c)(4)** &#8212; facility branch, cab only", "ACSFIX"),
    "OHC.10.A.K5b": ("**Part 1910 Subpart D** &middot; facility programme", "OPEN"),
    "OHC.10.A.R1": ("derived", "OK"),
    "OHC.10.A.R2": ("derived", "OK"),
    "OHC.10.A.R3": ("derived &middot; &sect;1910.179(c)(4)", "OK"),
    "OHC.10.B.K1": ("**EM 385 16-8.aa(7)**", "OK"),
    "OHC.10.B.K1b": ("**&sect;1910.179(b)(4)** &middot; Hanford 25 mph &middot; EM 385 20 mph "
                     "(tower)", "ACSFIX"),
    "OHC.10.B.K2": ("derived", "OK"),
    "OHC.10.B.K3": ("derived", "OK"),
    "OHC.10.B.K4": ("**&sect;1910.179(g)(4)(iii)** &middot; (a) definition", "OK"),
    "OHC.10.B.K4b": ("**&sect;1910.179(f)(2)(vi)** vs **(g)(4)(iii)** branch split", "OK"),
    "OHC.10.B.K5": ("**EM 385 &sect;16.A** lift-plan environmental items", "ED2014"),
    "OHC.10.B.R1": ("derived", "OK"),
    "OHC.10.B.R2": ("derived &middot; `OHC.04.B`", "OK"),
    "OHC.10.B.R3": ("derived &middot; EM 385 &sect;16.A", "OK"),
    "OHC.10.C.K1": ("**&sect;1910.179(g)(6)** &#8212; both branches", "OK"),
    "OHC.10.C.K1b": ("**&sect;1910.179(e)(5)(ii)** &#8212; both branches", "OK"),
    "OHC.10.C.K2": ("derived", "OK"),
    "OHC.10.C.K3": ("derived", "OK"),
    "OHC.10.C.K4": ("derived", "OK"),
    "OHC.10.C.K5": ("**&sect;1910.147** interface &middot; derived", "OPEN"),
    "OHC.10.C.K5b": ("**&sect;1910.179(g)(5)(i)**", "OK"),
    "OHC.10.C.R1": ("derived", "OK"),
    "OHC.10.C.R2": ("derived", "OK"),
    "OHC.10.C.R3": ("**&sect;1910.179(g)(6)** &middot; derived", "OK"),
}

TRACE_PERF = [
    ("OHC.10.A.S1", "Survey and clear a lift path before operation"),
    ("OHC.10.A.S2", "Coordinate crane and vehicle traffic in a shared aisle"),
    ("OHC.10.A.S3", "Suspend operations for inadequate visibility"),
    ("OHC.10.B.S1", "Apply the facility wind and weather suspension criteria"),
    ("OHC.10.B.S2", "Adjust load weight determination for environmental additions"),
    ("OHC.10.B.S3", "Execute storm securing for an outdoor crane"),
    ("OHC.10.C.S1", "Identify energy hazards along a proposed lift path"),
    ("OHC.10.C.S2", "Hold a placement pending isolation verification"),
    ("OHC.10.C.S3", "Route a load path to maintain clearance from identified energy sources"),
]

TRACE_NOTES = [
    ("&#11088; `B.K1b` &#8212; three wind numbers are in circulation and none of them is "
     "your limit",
     "**&sect;1910.179(b)(4)** requires the wind alarm at a **predetermined wind velocity** "
     "and **does not set one**. The number belongs to the manufacturer or the facility. Two "
     "figures get imported by mistake: the DOE Hanford manual's **25 mph**, which is a "
     "trigger for **evaluation by a qualified person** rather than an operating limit; and EM "
     "385's **20 mph**, which governs **tower crane climbing** &#8212; a different equipment "
     "class and a different operation. The ACS asks for *securing thresholds* without saying "
     "where the threshold comes from. `B.K1b` gates the correct answer: **get your own "
     "crane's number.**"),
    ("&#9888;&#65039; `A.K5` &#8212; the ACS reads lighting far wider than the standard does",
     "The ACS asks for *lighting adequacy for load path and placement visibility*. "
     "**&sect;1910.179(c)(4)** is one sentence and covers **light in the cab** only. It says "
     "nothing about the load path, nothing about the placement point, and nothing about "
     "floor-operated cranes &#8212; and **(c) is not in the &sect;1926.1438(b)(2) list**, so "
     "it is facility-branch. The ACS's broader reading is the correct **working** rule; it is "
     "just not what (c)(4) says. `A.K5` gates the paragraph as written and `A.K5b` gates "
     "where the wider duty actually comes from: **Part 1910 Subpart D** and the facility "
     "programme."),
    ("&#9989; Hot metal is a defined class with two provisions on opposite branches",
     "**&sect;1910.179(a)** defines a *hot metal handling crane* as one used for transporting "
     "or pouring **molten material**. **&sect;1910.179(g)(4)(iii)** requires provision to "
     "prevent **broken parts or molten metal falling upon the operator or from the crane** "
     "&#8212; **(g)** is in the &sect;1926.1438(b)(2) list, so **both branches**. "
     "**&sect;1910.179(f)(2)(vi)** requires **at least two holding brakes** on each "
     "independent hoisting unit with power control braking &#8212; **(f)(2) is not** in the "
     "list, so **facility only**. `B.K4b` gates the split, which is the kind of distinction "
     "that decides an audit finding."),
    ("&#9989; Two conductor provisions, both on both branches",
     "**&sect;1910.179(g)(6)**: open-type runway conductors shall be located or guarded so "
     "that persons entering or leaving the cab or footwalk **normally could not come into "
     "contact** with them &#8212; `C.K1` gates the word *normally*, because the guarding is "
     "designed against ordinary access and not against reaching or working in an unusual "
     "position. **&sect;1910.179(e)(5)(ii)**: a guard shall prevent contact between **bridge "
     "conductors and hoisting ropes** &#8212; `C.K1b`. Both **(e)(5)** and **(g)** are in the "
     "&sect;1926.1438(b)(2) list."),
    ("&#9989; `C.K5b` &#8212; the crane's disconnects are specified in detail",
     "**&sect;1910.179(g)(5)** is more prescriptive than the ACS suggests. **(g)(5)(i)**: "
     "runway conductor supply controlled by a switch or breaker on a **fixed structure, "
     "accessible from the floor, lockable in the open position**. **(g)(5)(ii)**: "
     "cab-operated cranes get an enclosed lockable switch in the leads from the runway "
     "conductors, openable **within easy reach of the operator**. **(g)(5)(iii)**: "
     "floor-operated cranes get one on the bridge or footwalk near the runway collectors, "
     "plus **one of three** named means &#8212; a **nonconductive rope** to the main "
     "disconnect, an **undervoltage trip** operated by the pendant emergency stop, or a "
     "**main line contactor** operated from the pendant."),
    ("&#128295; Correction carried back to OHC-06",
     "`OHC.06.B.K4` was sourced to *&#8220;EM 385 &sect;16 / ASME scope for this class&#8221;* "
     "&#8212; a vague attribution. The actual anchor is **&sect;1910.179(g)(5)(v)**: all "
     "cranes using a **lifting magnet** shall have a magnet circuit switch of the **enclosed "
     "type with provision for locking in the open position**, and **means for discharging the "
     "inductive load of the magnet** shall be provided. OHC-06's trace source is corrected "
     "and the module rebuilt."),
    ("&#9888;&#65039; Two open items in this module",
     "`A.K4` and `A.K5b` route to **Part 1910 Subpart D** (walking-working surfaces, fixed "
     "ladders &#8212; reached from &sect;1910.179(c)(2)) and `C.K5` routes to "
     "**&sect;1910.147** (energy control). **Neither is held as primary text in the corpus** "
     "&#8212; this is cross-check blocking item 6. The items are gated at the level the "
     "operator actually needs (walk the path; hold the placement; know who verifies), not "
     "from paragraph text this repo does not have."),
]


def main():
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "OHC_M10_EnvironmentalHazards.pre.html")
    with open(out, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))


if __name__ == "__main__":
    main()
