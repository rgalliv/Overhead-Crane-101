#!/usr/bin/env python3
"""OHC-06 Rigging Interface and Below-the-Hook Devices -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M06"
MODLABEL = "Module 6"
TITLE = "Rigging Interface and Below-the-Hook Devices"
SUBTITLE = ("Attach loads correctly at the hook, work within device markings, and prove "
            "balance before the load leaves the ground.")

OBJECTIVES = [
    "Verify sling tag, condition and hitch at the hook, and reject deficient rigging with "
    "a stated reason.",
    "Operate with engineered below-the-hook devices inside their markings, accounting for "
    "device weight and power dependency.",
    "Prove the hook is over the centre of gravity with a test lift before committing to the "
    "hoist, and control the load in travel.",
]

SECTIONS = [
    ("A", "Sling Interface",
     "Verify sling selection, condition and hitch configuration at the hook."),
    ("B", "Below-the-Hook Lifting Devices",
     "Operate with engineered lifting devices within their markings and instructions."),
    ("C", "Load Balance and Centre of Gravity",
     "Achieve balanced, controlled loads before movement."),
]

CONTENT = {
    "A": [
        ("Where the operator's role starts and stops",
         "Rigging is a discipline of its own and it does not change because the hook above "
         "it belongs to an overhead crane rather than a mobile one. The governing documents "
         "are the same: <b>ASME B30.9</b> for slings, <b>B30.10</b> for hooks, <b>B30.26</b> "
         "for rigging hardware and <b>B30.20</b> for below-the-hook devices.",
         "This module is the <b>interface</b>, not the rigging course. The operator's duty "
         "is to verify what arrives at the hook and to refuse what is not right &#8212; not "
         "to design the lift. Rigger qualification is a separate track."),
        ("The tag is the capacity",
         "Every sling carries a tag, and the tag &#8212; not the diameter, not the look of "
         "it &#8212; is the capacity. It states type, size, and <b>different rated loads for "
         "vertical, choker and basket</b> hitches.",
         "A worn-off rating cannot be estimated from the sling's dimension. Capacity depends "
         "on type, construction and grade. Two slings of the same diameter can have very "
         "different ratings. <b>No legible tag, no lift.</b>"),
        ("Four hitches, three capacities",
         "<b>Vertical</b> is the rated capacity, and it needs an engineered lift point. "
         "<b>Choker</b> derates &#8212; and derates further if drawn tight: when the angle "
         "of choke falls below <b>120&#176;</b>, the choker rating in the table must be "
         "reduced again.",
         "In controlled destructive tests below 120&#176;, the sling body <b>always failed "
         "at the point of choke</b>. <b>Basket</b> can double the capacity, but only at a "
         "steep angle &#8212; and <b>bridle</b> is where most of the arithmetic errors "
         "live."),
        ("Why a shallow angle multiplies the load",
         "Leg tension is the load divided by the number of legs times the sine of the sling "
         "angle. At <b>60&#176;</b> a leg carries about 87&#37; of what it would at vertical. "
         "At <b>45&#176;</b>, 71&#37;. At <b>30&#176;</b>, 50&#37;.",
         "The 30&#176; case is the one worth memorising: <b>at a 30&#176; sling angle, each "
         "leg of a two-leg bridle carries the entire load weight.</b> Two legs have bought "
         "nothing. A basket hitch at 30&#176; is exactly a vertical hitch."),
        ("Three and four legs are not three and four times",
         "Unless the load is perfectly rigid and the legs are exactly equal, load does not "
         "share evenly. The DOE Hanford manual puts it bluntly: <i>&#8220;unless the load is "
         "flexible, it is wrong to assume that a 3- or 4-leg hitch will safely&#8221;</i> "
         "carry proportionally more.",
         "The working assumption is that <b>two legs carry the load while the others balance "
         "it</b>. The master link is the other trap &#8212; it carries the <b>sum</b> of all "
         "leg loads, not one leg's share."),
        ("At the hook: saddle, latch, no tip",
         "The rated load of a hook <b>applies only when the load is applied in the saddle</b> "
         "&#8212; the bowl. Move the load off centre and capacity falls: roughly 86&#37;, "
         "80&#37;, then 70&#37; as it walks outward, and about <b>40&#37;</b> as a point load "
         "at the tip.",
         "Hooks are provided with a latch to bridge the throat and prevent the load line "
         "escaping. Hook tips should <b>point out and away from the load</b>, so that as "
         "slack comes up the hook does not tip-load itself."),
        ("Softeners are not optional dressing",
         "A sling bent over a sharp corner is a sling being cut. Wire rope is protected with "
         "<b>softeners or blocking</b> at corners and sharp bends; synthetics need it more, "
         "not less.",
         "There is a second reason beyond cutting. The <b>D/d ratio</b> &#8212; the diameter "
         "of the bend against the diameter of the rope &#8212; costs about <b>50&#37; "
         "efficiency</b> when it falls to 1:1. A tight bend derates the sling even if it "
         "never cuts it."),
    ],
    "B": [
        ("What a below-the-hook device is",
         "<b>ASME B30.20</b> covers the engineered hardware that hangs below the hook and "
         "takes the load: spreader and lifting beams, C-hooks, coil and sheet lifters, "
         "vacuum lifters and lifting magnets.",
         "It is engineered equipment, not rigging hardware. It has a design basis, a rated "
         "load, and instructions &#8212; and the instructions are part of the equipment."),
        ("Three markings, all required",
         "A below-the-hook device must carry its <b>rated capacity</b>, its <b>manufacturer "
         "or fabricator identification</b>, and be <b>designed for the load configuration</b> "
         "it is being used in. All three, not any one of them.",
         "The inspection tag is a permanent tag on slings, hooks and below-the-hook devices "
         "carrying the safe working load, the inspection date and the serial number. Check "
         "it before use, not after."),
        ("The device weighs something",
         "A spreader beam is not free. Its weight is part of the load on the hook, and it "
         "comes out of the crane's rated capacity before the payload does.",
         "A 12,000 lb crane with a 900 lb beam and 300 lb of slings has <b>10,800 lb</b> of "
         "payload available. This is the same arithmetic as OHC-04 and it is the one people "
         "skip when the beam is already hanging there from the last job."),
        ("Power-dependent devices fail open",
         "A lifting magnet or a vacuum lifter holds the load because energy is being supplied "
         "to it. Remove the energy and the holding force goes away &#8212; which is a "
         "different failure mode from every other piece of rigging on site.",
         "Check the battery state and the alarm function as part of the pre-use check. Know "
         "what the device does on power loss and whether it has backup provision. Then treat "
         "the zone under it as if the load will drop, because that is the failure mode."),
        ("Engagement before transfer",
         "Full engagement is verified <b>before</b> load is transferred to the device, not "
         "during. On a C-hook or a coil lifter that means seated and captured; on a magnet or "
         "vacuum lifter it means contact area clean, full and confirmed.",
         "The verification itself is a hazard. Nobody stands under, reaches into, or steadies "
         "a device that is about to take load. Verify by eye and by position, from clear."),
        ("Where the crane's own provisions come in",
         "The overhead crane has requirements of its own that bear on these devices &#8212; "
         "hoist control braking and the provisions for lifting magnets sit within the ASME "
         "scope that <b>EM 385-1-1 &sect;16</b> references for this equipment class on "
         "federal work.",
         "Practically: a magnet changes what the hoist brake has to do, and the crane's "
         "electrical provisions have to support the device. It is not simply a lump on the "
         "hook."),
    ],
    "C": [
        ("The hook goes over the centre of gravity",
         "A load hangs level when the hook is directly above its centre of gravity. Not above "
         "the geometric centre &#8212; above the <b>CG</b>. A skid with a motor on one end "
         "has a CG toward the motor, and symmetric lift points will tilt it.",
         "Bridle slings give excellent stability when load is distributed equally among the "
         "legs, the hook is directly over the CG, and the load is raised level. Where legs "
         "must differ, they are adjusted with turnbuckles or lever hoists &#8212; not by "
         "knotting or twisting."),
        ("The rule is in the regulation",
         "&sect;1910.179(n)(3)(i) is short and it is the whole of the test lift: <i>the load "
         "shall be <b>well secured and properly balanced in the sling or lifting device "
         "before it is lifted more than a few inches</b></i>.",
         "This paragraph is in the &sect;1926.1438(b) list, so it applies on <b>both</b> "
         "branches. It is one of the few load-handling rules that does."),
        ("What the few inches are for",
         "Lift a few inches and stop. In that pause you check three things: the brake holds "
         "with <b>no downward drift</b>; the load hangs level; and the rigging and hardware "
         "are taking load the way you expected.",
         "A load that tilts at six inches will tilt at sixty feet. The tilt does not "
         "self-correct as the load rises &#8212; it persists, and the steep leg carries more "
         "than its share for the whole lift."),
        ("Correcting an off-CG condition",
         "Set it back down. Move the rigging points toward the heavy side. Test lift again "
         "and confirm level before proceeding. That is the entire procedure and there is no "
         "shortcut inside it.",
         "Tag lines do not substitute for correct rigging. A tilted load held straight by "
         "people on ropes is still a tilted load with an overloaded leg."),
        ("Tag lines, and the way they injure people",
         "A tag line controls orientation from outside the load's footprint. It is never "
         "<b>wrapped around a hand, wrist or body</b> &#8212; a sudden swing puts the load's "
         "full momentum into the line, and a wrapped line cannot be released.",
         "Loose grip only, always. Near energised lines, fibre rope is non-conductive only "
         "while clean and dry; contaminated or wet rope conducts, and a rated non-conductive "
         "tag line is required."),
        ("A suspended load is a pendulum",
         "The load hangs from a point and behaves like one. Acceleration starts a swing; "
         "deceleration at the far end doubles it. The swing does not stop when the trolley "
         "stops &#8212; it is at its worst then.",
         "&sect;1910.179(n)(3)(vi) is the reason it matters: <b>the operator shall not carry "
         "loads over people</b>. A swinging load's footprint is far larger than the load. "
         "All personnel, the rigger included, stay clear."),
    ],
}

PRACTICE = [
    ("OHC.06.A.K1",
     "A sling with an illegible rated-load tag may be used if its diameter matches a known "
     "sling.",
     ["True", "False"], 1,
     "Capacity depends on type, construction and grade, not dimension. No legible tag, no "
     "lift."),
    ("OHC.06.A.K3",
     "A two-leg bridle lifts a 24,000 lb load at a 45&#176; sling angle. Tension in each leg "
     "is about:",
     ["12,000 lb", "16,970 lb", "24,000 lb", "8,500 lb"], 1,
     "Leg tension = 24,000 / (2 x sin 45&#176;) = 24,000 / 1.414 = 16,970 lb per leg."),
    ("OHC.06.A.K3b",
     "At a 30&#176; sling angle, each leg of a two-leg bridle carries:",
     ["Half the load", "The full load weight", "A quarter of the load",
      "70&#37; of the load"], 1,
     "24,000 / (2 x 0.500) = 24,000 lb per leg. Two legs have bought nothing at 30&#176;."),
    ("OHC.06.A.K4",
     "A hook's rated load applies when the load is applied:",
     ["Anywhere on the hook", "In the saddle of the hook", "At the tip",
      "Against the latch"], 1,
     "The designed safe working load applies only in the saddle. Tip loading falls to "
     "roughly 40&#37;."),
    ("OHC.06.B.K2",
     "A 15,000 lb crane uses a 1,200 lb spreader beam and 400 lb of slings. Available "
     "payload is:",
     ["15,000 lb", "13,800 lb", "13,400 lb", "14,600 lb"], 2,
     "15,000 - 1,200 - 400 = 13,400 lb. Device and rigging weight come off first."),
    ("OHC.06.B.K3",
     "A lifting magnet that loses power will hold the load until it is set down.",
     ["True", "False"], 1,
     "Holding force comes from supplied energy. Power loss releases the load unless a backup "
     "provision exists."),
    ("OHC.06.C.K1",
     "A load hangs level when the hook is directly above:",
     ["The geometric centre of the load", "The centre of gravity of the load",
      "The heaviest lift point", "The longest sling leg"], 1,
     "Level hang means hook over CG. On an asymmetric load the CG is not the geometric "
     "centre."),
    ("OHC.06.C.K2",
     "A load that tilts at a six-inch test lift will straighten as it rises.",
     ["True", "False"], 1,
     "The tilt persists. Set down, move the rigging points toward the heavy side, and "
     "re-test."),
    ("OHC.06.C.K4",
     "Wrapping a tag line around the hand for grip is:",
     ["Good practice on heavy loads", "Acceptable with gloves",
      "Prohibited -- a swing cannot be released from a wrapped line",
      "Required near power lines"], 2,
     "A sudden swing transfers the load's full momentum into the line. Loose grip only."),
]

GATE = [
    # ---- Task A
    ("OHC.06.A.K1",
     "The rated capacity of a sling is established by:",
     ["Its diameter", "Its identification tag, which states different ratings for vertical, "
      "choker and basket", "The crane's capacity", "The rigger's judgement"], 1, ""),
    ("OHC.06.A.K2",
     "A choker hitch drawn tight so the angle of choke falls below 120&#176; must be:",
     ["Used at the table choker rating", "Derated further below the table choker rating",
      "Used at the vertical rating", "Used at the basket rating"], 1, ""),
    ("OHC.06.A.K2b",
     "Under the working assumption used for multi-leg bridles, a four-leg bridle should be "
     "rated on the basis that:",
     ["All four legs share equally", "Three legs share the load",
      "Two legs carry the load while the others balance it",
      "The longest leg governs"], 2, ""),
    ("OHC.06.A.K3",
     "A two-leg bridle lifts a 30,000 lb load at a 45&#176; sling angle. Tension per leg is "
     "about:",
     ["10,600 lb", "15,000 lb", "21,200 lb", "30,000 lb"], 2, ""),
    ("OHC.06.A.K3b",
     "A basket hitch at a 30&#176; sling angle, compared with a vertical hitch using the same "
     "sling, gives:",
     ["Double the capacity", "50&#37; more capacity",
      "The same effective capacity", "Less than a vertical hitch"], 2, ""),
    ("OHC.06.A.K4",
     "The rated load of a hook applies only when the load is applied in the saddle. A point "
     "load at the tip reduces capacity to roughly:",
     ["86&#37;", "70&#37;", "40&#37;", "100&#37; -- the hook is rated for any position"],
     2, ""),
    ("OHC.06.A.K4b",
     "Hook tips should point out and away from the load because:",
     ["It looks tidier", "As slack comes up the hook will not tip-load itself",
      "It makes the latch easier to close", "It reduces sling wear"], 1, ""),
    ("OHC.06.A.K5",
     "Beyond preventing cuts, softeners and blocking at a sharp bend also address:",
     ["Corrosion", "The D/d ratio, which costs about 50&#37; efficiency at 1:1",
      "Temperature rating", "Tag legibility"], 1, ""),
    ("OHC.06.A.R1",
     "A sling arrives at the hook with no legible tag. The operator should:",
     ["Estimate capacity from its diameter", "Use it below 50&#37; of an assumed rating",
      "Refuse the lift and state the reason", "Accept it if the rigger vouches for it"],
     2, ""),
    ("OHC.06.A.R2",
     "Hoisting with the load off-centre of the hook is hazardous because:",
     ["It looks unprofessional", "It side-loads the hook outside its rated condition and can "
      "deform or open it", "It wears the sling tag", "It slows the lift"], 1, ""),
    ("OHC.06.A.R3",
     "A crew improvises a shallower sling angle to clear an obstruction. The consequence is:",
     ["No change -- the load weight is unchanged",
      "Leg tension rises sharply, and may exceed the rated capacity of the legs",
      "The load becomes more stable", "The choker rating applies instead"], 1, ""),
    # ---- Task B
    ("OHC.06.B.K1",
     "Which of these is a below-the-hook lifting device under ASME B30.20?",
     ["A wire rope sling", "A shackle", "A vacuum lifter", "A master link"], 2, ""),
    ("OHC.06.B.K2",
     "A below-the-hook lifting device must carry:",
     ["A rated capacity label only", "Rated capacity, manufacturer or fabricator "
      "identification, and design for the load configuration in use",
      "A proof-load certificate only", "Any marking at the manufacturer's discretion"],
     1, ""),
    ("OHC.06.B.K2b",
     "A 20,000 lb crane is fitted with a 1,500 lb lifting beam and 500 lb of slings. "
     "Available payload is:",
     ["20,000 lb", "18,500 lb", "18,000 lb", "19,500 lb"], 2, ""),
    ("OHC.06.B.K3",
     "The pre-use check specific to a magnet or vacuum lifter, beyond the structural check, "
     "is:",
     ["Throat opening measurement", "Battery state, alarm function, and the device's "
      "behaviour on power loss", "Sling angle measurement", "Choker angle verification"],
     1, ""),
    ("OHC.06.B.K4",
     "A lifting magnet matters to the crane itself because:",
     ["It changes the crane's rated capacity marking",
      "Hoist control braking and lifting-magnet provisions are requirements on the crane, "
      "not just the device", "It requires a longer hook", "It changes the duty class"],
     1, ""),
    ("OHC.06.B.K5",
     "Full engagement of a below-the-hook device is verified:",
     ["During load transfer", "Before load is transferred to the device",
      "Once the load is clear of the ground", "At the destination"], 1, ""),
    ("OHC.06.B.R1",
     "The zone beneath a powered lifting device should be treated as:",
     ["Normal working area once the load is engaged",
      "A drop zone, because power loss releases the load",
      "Safe while the alarm is silent", "Restricted only during engagement"], 1, ""),
    ("OHC.06.B.R2",
     "A spreader beam is used for a load configuration different from the one it was designed "
     "for, but well below its rated capacity. This is:",
     ["Acceptable, since the load is within capacity",
      "Not acceptable -- the device must be designed for the configuration in use",
      "Acceptable if a rigger approves", "Acceptable below 50&#37; of rating"], 1, ""),
    ("OHC.06.B.R3",
     "The correct way to verify engagement on a coil lifter is:",
     ["By hand, steadying the device as it takes load",
      "By eye, from a clear position outside the load's footprint",
      "By listening for the seating sound while under the load",
      "By lifting to head height and looking up"], 1, ""),
    # ---- Task C
    ("OHC.06.C.K1",
     "&sect;1910.179(n)(3)(i) requires that the load be well secured and properly balanced "
     "in the sling or lifting device:",
     ["Before it is lifted more than a few inches", "Before it reaches travel height",
      "Before the trolley is moved", "Before the load is landed"], 0, ""),
    ("OHC.06.C.K2",
     "During the pause at the test lift, the operator confirms the brake holds with:",
     ["A slight, even downward drift", "No downward drift",
      "Drift only under rated load", "Drift within one inch per minute"], 1, ""),
    ("OHC.06.C.K3",
     "The correct response to a load that hangs tilted at the test lift is:",
     ["Continue -- it will straighten with height", "Hoist faster to reduce tilt time",
      "Set down, move the rigging points toward the heavy side, and test lift again",
      "Hold it level with tag lines during travel"], 2, ""),
    ("OHC.06.C.K3b",
     "Where bridle legs must differ in length to level a load, they are adjusted with:",
     ["Knots in the shorter leg", "Twisting the leg to shorten it",
      "Turnbuckles or lever hoists", "Wire rope clips"], 2, ""),
    ("OHC.06.C.K4",
     "A tag line is held:",
     ["Wrapped once around the hand for grip", "Wrapped around the wrist",
      "With a loose grip that allows instant release", "Tied to a fixed point"], 2, ""),
    ("OHC.06.C.K5",
     "A suspended load's swing is generally worst:",
     ["While accelerating", "At constant travel speed",
      "As the trolley or bridge decelerates and stops", "While hoisting"], 2, ""),
    ("OHC.06.C.R1",
     "Hoisting an unbalanced load to full height is hazardous chiefly because:",
     ["The load looks untidy", "The steep leg is overloaded for the whole lift and the load "
      "may shift", "The crane draws more current", "The tag line will be too short"],
     1, ""),
    ("OHC.06.C.R2",
     "Correcting a load's balance by hand while it hangs is:",
     ["Acceptable at low height", "Acceptable with gloves",
      "Prohibited -- all personnel including the rigger stay clear of the load",
      "Acceptable if the load is under 2,000 lb"], 2, ""),
    ("OHC.06.C.R3",
     "Standard fibre tag lines near energised lines are inadequate because:",
     ["They stretch too much", "Fibre rope conducts when wet or contaminated, so a rated "
      "non-conductive line is required", "They are too short",
      "They cannot be gripped loosely"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.06.A.K1": ("**ASME B30.9** tag &middot; Tier 0 S2-M1 / WD-SCN-002", "OK"),
    "OHC.06.A.K2": ("**DOE Hanford TR244C** 120&#176; choke &middot; ASME B30.9", "OK"),
    "OHC.06.A.K2b": ("**DOE Hanford TR244C** &middot; ASME B30.9 multi-leg", "OK"),
    "OHC.06.A.K3": ("Tier 0 WD-SCN-002 leg-tension formula", "CONFLICT"),
    "OHC.06.A.K3b": ("Tier 0 WD-SCN-002 &middot; derived", "OK"),
    "OHC.06.A.K4": ("**DOE Hanford TR244C** hook point-load table", "OK"),
    "OHC.06.A.K4b": ("**DOE Hanford TR244C**", "OK"),
    "OHC.06.A.K5": ("**DOE Hanford TR244C** softeners &middot; D/d ratio", "OK"),
    "OHC.06.A.R1": ("ASME B30.9 &middot; derived", "OK"),
    "OHC.06.A.R2": ("**DOE Hanford TR244C** saddle loading", "OK"),
    "OHC.06.A.R3": ("derived &middot; leg-tension formula", "OK"),
    "OHC.06.B.K1": ("**ASME B30.20** scope (by name)", "OK"),
    "OHC.06.B.K2": ("**ASME B30.20** marking &middot; Hanford inspection tag", "OK"),
    "OHC.06.B.K2b": ("derived &middot; `OHC.04.A.K5`", "OK"),
    "OHC.06.B.K3": ("derived &middot; Tier 0", "OK"),
    "OHC.06.B.K4": ("**EM 385 &sect;16** / ASME scope for this class", "OK"),
    "OHC.06.B.K5": ("**DOE Hanford TR244C** pre-use &middot; derived", "OK"),
    "OHC.06.B.R1": ("derived", "OK"),
    "OHC.06.B.R2": ("**ASME B30.20** design for configuration", "OK"),
    "OHC.06.B.R3": ("**DOE Hanford TR244C** stay clear", "OK"),
    "OHC.06.C.K1": ("**&sect;1910.179(n)(3)(i)** &#8212; both branches", "OK"),
    "OHC.06.C.K2": ("**DOE Hanford TR244C** no downward drift", "OK"),
    "OHC.06.C.K3": ("Tier 0 WD-SCN-002 &middot; derived", "OK"),
    "OHC.06.C.K3b": ("**DOE Hanford TR244C** turnbuckles / lever hoists", "OK"),
    "OHC.06.C.K4": ("Tier 0 WD-SCN-002 tag-line rule", "OK"),
    "OHC.06.C.K5": ("derived", "OK"),
    "OHC.06.C.R1": ("derived", "OK"),
    "OHC.06.C.R2": ("**&sect;1910.179(n)(3)(vi)** &middot; Hanford stay clear", "OK"),
    "OHC.06.C.R3": ("Tier 0 WD-SCN-002 non-conductive tag lines", "OK"),
}

TRACE_PERF = [
    ("OHC.06.A.S1", "Verify sling tag, condition and hitch before hoisting"),
    ("OHC.06.A.S2", "Reject deficient rigging and state the reason"),
    ("OHC.06.A.S3", "Confirm hook engagement and latch closure on every pick"),
    ("OHC.06.B.S1", "Perform device pre-use checks including power and alarm functions"),
    ("OHC.06.B.S2", "Demonstrate engagement verification and a test lift at low height"),
    ("OHC.06.B.S3", "Compute total lifted load with device weight included"),
    ("OHC.06.C.S1", "Execute a test lift and balance verification sequence"),
    ("OHC.06.C.S2", "Direct a rigging correction for an off-CG condition"),
    ("OHC.06.C.S3", "Manage tag line use for an orientation-critical load"),
]

TRACE_NOTES = [
    ("&#9989; Rigging sourced as rigging, not as crane-type content",
     "The ACS References for OHC-06 name **ASME B30.9**, **B30.20** and **P30.1** by name "
     "only. Rigging is governed by the B30 volumes and by practice regardless of what hangs "
     "above the hook, so this module is built from the **Tier 0 rigger corpus** &#8212; "
     "`FG_S2-M1_Rigging_Fundamentals`, `WD-SCN-002 Rigging Fundamentals` &#8212; and from "
     "the **DOE Hanford Hoisting and Rigging manual (TR244C Rev 5)**, which is public "
     "domain and quotable."),
    ("&#9888;&#65039; Two Tier 0 guides disagree; four facts held out of the gate",
     "`FG_S2-M1` and `WD-SCN-002` contradict each other on **roundsling colour-code "
     "capacities**, **choker derate** (75/80&#37; by sling type vs a flat 75&#8211;80&#37; "
     "range), **hook throat limit** (5&#37; vs 15&#37;) and **chain elongation** (5&#37; vs "
     "3&#37;). None of the four is gated in this module. The hook conflict is resolved and "
     "taught in **OHC-05 `A.K4`/`A.K4b`**; the other three need an SME ruling. Roundsling "
     "colour is not standardised by ASME at all &#8212; it is a manufacturer convention, "
     "which is why the two guides can both be internally consistent and mutually wrong."),
    ("&#9888;&#65039; A live arithmetic defect in a shipped Tier 0 guide",
     "`WD-SCN-002`'s leg-tension answer key is **wrong by a factor of two in two places** "
     "&#8212; KC Q5 keys 10,606 lb where the formula gives 21,213 lb, and FKC Q2 keys "
     "14,142 lb where it gives 28,284 lb. Both key entries contain an unresolved "
     "*&#8220;Wait &#8212;&#8221;* editorial note left in the shipped text. The worked "
     "example on Slide 15 and the debrief questions are correct, so it is the keys that are "
     "wrong, not the method. `A.K3` here is keyed to the **correct** value (21,200 lb). "
     "**This needs fixing in the source guide.**"),
    ("&#9989; The test lift is regulation, on both branches",
     "`C.K1` and `C.K2` rest on **&sect;1910.179(n)(3)(i)** &#8212; *the load shall be well "
     "secured and properly balanced in the sling or lifting device before it is lifted more "
     "than a few inches*. Paragraph **(n)** is in the &sect;1926.1438(b)(2) list, so this is "
     "one of the few load-handling rules that binds on **both** the facility and the "
     "construction branch."),
    ("&#9989; Hook point-loading given a number",
     "The ACS states `A.K4` as *no point loading or tip loading* without a magnitude. The "
     "Hanford manual carries the derate table &#8212; **100&#37; / 86&#37; / 80&#37; / "
     "70&#37;** as the load walks off the saddle, and about **40&#37;** as a point load at "
     "the tip &#8212; alongside the rule that *the designed SWL applies only when the load "
     "is applied in the saddle of the hook*."),
    ("&#9432; Elements carrying a second item",
     "`A.K2`, `A.K3`, `A.K4`, `B.K2` and `C.K3` each carry a second item. In every case the "
     "element contains two independently testable facts &#8212; for example `A.K3` covers "
     "both the leg-tension calculation and the 30&#176; equivalence, which learners can get "
     "one of and miss the other."),
]


def main():
    html = A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "OHC_M06_RiggingInterface.pre.html")
    with open(out, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))


if __name__ == "__main__":
    main()
