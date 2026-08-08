#!/usr/bin/env python3
"""OHC-04 Rated Load, Capacity, and Load Weight Determination -- pre-retrofit DOM."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M04"
MODLABEL = "Module 4"
TITLE = "Rated Load, Capacity, and Load Weight Determination"
SUBTITLE = ("Confirm every lift is within rated capacity using marked ratings and verified "
            "load weights.")

OBJECTIVES = [
    "Locate every capacity marking on the assigned crane and state the governing rating "
    "for a given pick.",
    "Establish load weight by documentation, calculation or measurement before hoisting, "
    "and document the basis.",
    "Recognise the overload mechanisms that do not announce themselves, and stop rather "
    "than force a load that will not lift.",
]

SECTIONS = [
    ("A", "Rated Load Marking and Interpretation",
     "Locate and interpret capacity markings for the crane and each hoisting unit."),
    ("B", "Load Weight Determination",
     "Establish load weight by documentation, calculation or measurement before hoisting."),
    ("C", "Overload Prevention",
     "Prevent overload conditions in all operating scenarios."),
]

CONTENT = {
    "A": [
        ("Where the rating is written",
         "The rated load of the crane is plainly marked <b>on each side of the crane</b>. "
         "Where the crane has more than one hoisting unit, <b>each hoist</b> carries its "
         "rated load marked on it or on its load block.",
         "Markings on the bridge, trolley and load block must be <b>legible from the ground "
         "or floor</b>. If you cannot read it from where you stand, it is not doing its job."),
        ("Main and auxiliary",
         "A crane with a main and an auxiliary hoist has two ratings, and they are not "
         "interchangeable. The governing rating for a pick is the rating of <b>the hoisting "
         "unit you are actually using</b> &#8212; never the larger number on the girder.",
         "Where multiple hoists exist, the hoist, block or trolley carries a distinguishing "
         "mark and the operator's controller carries a corresponding mark, so you can tell "
         "which control moves which hoist."),
        ("Rated load, test load, duty class",
         "Three different numbers describe a crane and only one of them is your working "
         "limit. <b>Rated load</b> is what you may lift. <b>Test load</b> is a proof figure "
         "&#8212; not more than <b>125&#37;</b> of rated load unless the manufacturer "
         "recommends otherwise &#8212; applied by designated personnel, not by operators.",
         "<b>Duty class</b> describes service severity, not capacity. A Class F crane is not "
         "a stronger crane; it is a crane built to be worked continuously and severely."),
        ("Capacity does not move",
         "On a mobile crane, capacity falls away as the radius grows, and the operator reads "
         "a load chart to find it. <b>An overhead crane has none of that.</b> Its rated "
         "capacity is fixed and applies anywhere along the bridge.",
         "This is the single most common piece of mobile-crane logic to import by mistake. "
         "There is no chart, no radius and no reason to improvise a margin because the "
         "trolley is near the end of the girder."),
        ("The device counts",
         "Below-the-hook lifting devices are lifted load. A spreader beam, C-hook, coil "
         "lifter, vacuum lifter or magnet consumes capacity before the load does.",
         "Device weight is marked on the device where it exceeds 100 lb, along with rated "
         "load and identification. <b>Available payload = rated load &minus; rigging "
         "&minus; device.</b>"),
        ("When you cannot read it",
         "An illegible or missing capacity marking is not an inconvenience to work around. "
         "It means the governing rating cannot be verified, and an unverifiable rating "
         "cannot be respected.",
         "The correct action is to <b>reject the lift</b> and route the defect for "
         "correction. This is the same logic as unmarked rigging: if the rating cannot be "
         "established, the item comes out of service."),
    ],
    "B": [
        ("Where weight comes from",
         "Acceptable sources, roughly in order of reliability: a <b>data plate or stamp on "
         "the load itself</b>, engineering drawings, shipping documents, and manufacturer "
         "data.",
         "The one source that is never acceptable is your eye. Dense and compact loads read "
         "light; large hollow loads read heavy. Appearance is not a source."),
        ("Calculating from geometry",
         "Where documentation is absent, weight is calculated from <b>material and "
         "geometry</b> &#8212; volume multiplied by the density of the material.",
         "The discipline is to calculate conservatively and then check the answer against "
         "something independent. A calculation you cannot sanity-check is an estimate "
         "wearing a calculator."),
        ("Measuring it",
         "Load-indicating devices and dynamometers measure the actual lifted load where they "
         "are fitted or available. They convert an argument into a reading.",
         "Where a load-indicating device exists, use it &#8212; but read it as "
         "<b>confirmation</b> of a weight you already established, not as permission to "
         "start lifting something of unknown weight."),
        ("Total lifted load",
         "The number that matters is not the weight of the load. It is <b>load + rigging + "
         "below-the-hook device</b>.",
         "Slings, shackles, spreader beams and softeners all hang below the hook and all "
         "count. Operators who track only the load routinely run 5&#8211;15&#37; over what "
         "they think they are lifting."),
        ("The lift plan",
         "On federal work <b>all lifts must be planned</b>, and a written Standard Lift Plan "
         "is prepared for every lift or series of lifts where duty-cycle or routine lifts "
         "are being performed. It is <b>developed, reviewed and accepted by all personnel "
         "involved</b>, and maintained on the equipment.",
         "At minimum it addresses personnel and roles; area preparation and path of travel; "
         "equipment considerations including capacity and configuration; <b>load parameters "
         "&#8212; weight, centre of gravity, configuration</b>; rigging including the need "
         "for softeners; and environmental considerations."),
        ("When the margin gets thin",
         "As calculated weight approaches rated capacity, the cost of being wrong rises "
         "sharply. Industry practice treats a lift exceeding <b>75&#37; of rated capacity</b> "
         "as critical, along with tandem lifts, extended suspension and costly or "
         "irreplaceable items.",
         "The rule is also written into operation: the operator <b>tests the brakes each "
         "time a load approaching the rated load is handled</b>, by raising it a few inches "
         "and applying the brakes."),
    ],
    "C": [
        ("The prohibition",
         "The crane <b>shall not be loaded beyond its rated load</b>, except for test "
         "purposes conducted under the testing provisions.",
         "That is the whole rule and it has no operational exception. There is no "
         "\"just this once\", no allowance for a short lift, and no margin the operator is "
         "entitled to spend."),
        ("Overloads that hide",
         "The dangerous overloads are the ones that do not look like overloads: a load "
         "frozen or adhered to the floor, a load bolted or anchored down, a load snagged on "
         "something out of sight, or a load still attached to the structure.",
         "In every case the crane is not lifting the load's weight &#8212; it is lifting "
         "against an unknown restraint, and the only limit is what the rope or the structure "
         "will take before something lets go."),
        ("Breaking loads free",
         "Using the hoist to break a stuck load free is the classic version of this "
         "failure. The load is not weighed, the restraint is not known, and the release is "
         "sudden.",
         "The correct response to a load that will not lift at expected effort is to "
         "<b>stop</b>, set down, and find out why. Never increase effort against an unknown "
         "restraint."),
        ("Shock loading",
         "Slack rope plus sudden application equals shock load. Rapid acceleration while "
         "lifting, or rapid stopping while lowering, multiplies the force in the rope well "
         "beyond the static weight.",
         "Remove slack gradually, apply load progressively, and avoid sudden acceleration or "
         "deceleration of a moving load. Dynamic loading is why a crane that lifted a load "
         "yesterday can fail on it today."),
        ("Weight that arrives uninvited",
         "Water, ice, snow and accumulated material are capacity thieves. A load left "
         "outdoors overnight can gain enough water or ice to move it from comfortable to "
         "over-capacity without anyone touching it.",
         "The same applies to contents, attachments and anything added since the weight was "
         "established. <b>Re-establish weight when the load has changed</b>, not just when "
         "the load is new."),
        ("Load-limiting devices",
         "Where fitted, load-limiting devices interrupt or prevent hoisting above a set "
         "point. They are a backstop against error.",
         "They are <b>not a planning margin</b>. Planning to the device rather than to the "
         "rating means every lift is planned to fail safely rather than to succeed &#8212; "
         "and the device is the only thing between you and an overload."),
    ],
}

PRACTICE = [
    ("OHC.04.A.K1",
     "On a crane with two hoisting units, the rated load must be marked:",
     ["Once, on the bridge girder only", "On each side of the crane, and on each hoist or "
      "its load block", "On the pendant only", "On the runway beam"], 1,
     "Rated load is marked on each side of the crane, and where there is more than one "
     "hoisting unit each hoist carries its rating on it or its load block."),
    ("OHC.04.A.K4",
     "The rated capacity of an overhead crane decreases as the trolley moves toward the end "
     "of the bridge.",
     ["True", "False"], 1,
     "Capacity is fixed and applies anywhere along the bridge. Radius-based capacity is "
     "mobile-crane logic and does not transfer."),
    ("OHC.04.A.K5",
     "A 12,000 lb crane is fitted with a 900 lb spreader beam and 300 lb of slings. "
     "Available payload is:",
     ["12,000 lb", "11,100 lb", "10,800 lb", "11,700 lb"], 2,
     "Rated load minus rigging minus device: 12,000 - 900 - 300 = 10,800 lb."),
    ("OHC.04.B.K1",
     "The most reliable source for a load's weight is:",
     ["An experienced operator's estimate", "A data plate or stamp on the load itself",
      "The size of the load", "The capacity of the crane"], 1,
     "A manufacturer's data plate or stamp is the most reliable source. Drawings, shipping "
     "documents and load-indicating devices follow. Never estimate."),
    ("OHC.04.B.K4",
     "Total lifted load means:",
     ["The weight of the load only", "The load plus the rigging",
      "The load plus the rigging plus the below-the-hook device",
      "The load plus the weight of the hook block"], 2,
     "Everything hanging below the hook counts against capacity."),
    ("OHC.04.B.K5",
     "On federal work, a written Standard Lift Plan is required:",
     ["Only for critical lifts", "Only for tandem lifts",
      "For every lift, or series of lifts where duty-cycle or routine lifts are performed",
      "Only where the load exceeds 75% of capacity"], 2,
     "All lifts must be planned. The SLP is developed, reviewed and accepted by all "
     "personnel involved and maintained on the equipment."),
    ("OHC.04.C.K1",
     "Loading a crane beyond its rated load is permitted:",
     ["Briefly, if the load is lifted only a few inches",
      "Only for test purposes under the testing provisions",
      "When a supervisor authorises it", "When the load-limiting device permits it"], 1,
     "The crane shall not be loaded beyond its rated load except for test purposes as "
     "provided in the testing paragraph."),
    ("OHC.04.C.R1",
     "A load will not lift at the effort you expected. The correct action is to:",
     ["Increase hoist speed to break it free", "Add a second sling and try again",
      "Stop, set down, and determine why", "Apply the load-limiting device override"], 2,
     "A load that will not lift is lifting against an unknown restraint. Never increase "
     "effort against a restraint you have not identified."),
    ("OHC.04.C.K4",
     "A load stored outdoors overnight in freezing rain should be:",
     ["Lifted using the previously established weight", "Re-weighed or recalculated before "
      "lifting", "Lifted at reduced speed only", "Lifted only with the auxiliary hoist"], 1,
     "Water and ice are capacity thieves. Re-establish weight whenever the load has changed."),
]

GATE = [
    # ---- Task A
    ("OHC.04.A.K1",
     "Capacity markings on the bridge, trolley and load block must be:",
     ["Legible from the bridge walkway", "Legible from the ground or floor",
      "Legible from the cab only", "Recorded in the maintenance log only"], 1, ""),
    ("OHC.04.A.K2",
     "On a crane with a main and an auxiliary hoist, the governing rating for a pick is:",
     ["Always the main hoist rating", "The larger of the two ratings",
      "The rating of the hoisting unit actually being used",
      "The sum of both ratings"], 2, ""),
    ("OHC.04.A.K3",
     "Test load applied during a rated load test shall not be more than:",
     ["100&#37; of rated load", "110&#37; of rated load",
      "125&#37; of rated load unless the manufacturer recommends otherwise",
      "150&#37; of rated load"], 2, ""),
    ("OHC.04.A.K3b",
     "CMAA duty class describes:",
     ["Maximum rated capacity", "Service severity, not capacity",
      "The test load percentage", "The number of hoisting units"], 1, ""),
    ("OHC.04.A.K4",
     "Why does an overhead crane have no load chart of the kind a mobile crane carries?",
     ["Because overhead cranes are always smaller",
      "Because rated capacity is fixed and applies anywhere along the bridge",
      "Because the chart is kept in the maintenance office",
      "Because capacity is set by the rigging instead"], 1, ""),
    ("OHC.04.A.K5",
     "Below-the-hook lifting devices affect available capacity because they:",
     ["Reduce the crane's duty class", "Are lifted load and consume capacity before the "
      "load does", "Increase the rated load", "Change the trolley position"], 1, ""),
    ("OHC.04.A.R1",
     "The specific error the distinguishing marks on hoists, blocks and controllers exist to "
     "prevent is:",
     ["Operating the wrong crane in the bay", "Reading or applying the wrong hoist's rating "
      "on a multi-hoist crane", "Reversing bridge and trolley motion",
      "Confusing rated load with test load"], 1, ""),
    ("OHC.04.A.R2",
     "An operator reduces the load when working near the end of the bridge, reasoning that "
     "capacity must be lower there. This is:",
     ["Correct and required", "Sound conservative practice",
      "An improvised margin based on mobile-crane logic that does not apply",
      "Required only on single-girder cranes"], 2, ""),
    ("OHC.04.A.R3",
     "A crane's capacity marking is corroded and unreadable. The correct action is to:",
     ["Use the rating from a similar crane in the bay", "Estimate from the crane's size",
      "Reject the lift and route the defect for correction",
      "Proceed with loads under half the expected rating"], 2, ""),
    # ---- Task B
    ("OHC.04.B.K1",
     "Which is NOT an acceptable source for establishing load weight?",
     ["A data plate or stamp on the load", "Engineering drawings",
      "The operator's visual estimate", "Shipping documents"], 2, ""),
    ("OHC.04.B.K2",
     "Where no documentation exists, load weight is established by:",
     ["Lifting slowly and feeling the response",
      "Calculation from material and geometry",
      "Assuming the crane's rated capacity", "Asking the rigger's opinion"], 1, ""),
    ("OHC.04.B.K3",
     "A load-indicating device or dynamometer is correctly used to:",
     ["Permit lifting a load of unknown weight",
      "Confirm a weight already established by another means",
      "Replace the need for a lift plan", "Set the rated capacity of the crane"], 1, ""),
    ("OHC.04.B.K4",
     "A 6,000 lb load is lifted with 400 lb of slings and a 1,200 lb lifting beam. The "
     "total lifted load is:",
     ["6,000 lb", "6,400 lb", "7,200 lb", "7,600 lb"], 3, ""),
    ("OHC.04.B.K5",
     "The Standard Lift Plan required on federal work must be:",
     ["Prepared by the operator alone and kept in the office",
      "Developed, reviewed and accepted by all personnel involved in the lift, and "
      "maintained on the equipment",
      "Prepared only after the lift for the record",
      "Signed by the manufacturer"], 1, ""),
    ("OHC.04.B.R1",
     "Estimating weight by appearance is most dangerous with:",
     ["Large hollow loads", "Dense or asymmetric loads that read lighter than they are",
      "Loads under 500 lb", "Loads already rigged"], 1, ""),
    ("OHC.04.B.R2",
     "Which is most likely to make an established load weight wrong by the time it is "
     "lifted?",
     ["A change of operator", "Absorbed water, ice, added attachments or contents",
      "A change of shift", "Moving the crane along the runway"], 1, ""),
    ("OHC.04.B.R3",
     "When a calculated weight approaches rated capacity, the operator must:",
     ["Proceed carefully at reduced speed",
      "Verify the weight independently before proceeding",
      "Use the auxiliary hoist instead", "Reduce the number of sling legs"], 1, ""),
    # ---- Task C
    ("OHC.04.C.K1",
     "The rule on loading a crane beyond its rated load is:",
     ["Permitted with supervisory approval",
      "Prohibited except for test purposes under the testing provisions",
      "Permitted up to 110&#37; for short duration",
      "Governed by the load-limiting device setting"], 1, ""),
    ("OHC.04.C.K2",
     "A load that is bolted down, frozen to the floor or snagged out of sight is dangerous "
     "because the crane is:",
     ["Lifting a heavier load than marked",
      "Lifting against an unknown restraint rather than a known weight",
      "Operating outside its duty class", "Exceeding its test load"], 1, ""),
    ("OHC.04.C.K3",
     "Shock loading is produced principally by:",
     ["Lifting at low speed", "Slack rope with sudden application of load, or rapid "
      "acceleration and deceleration", "Using more parts of line",
      "Operating with the auxiliary hoist"], 1, ""),
    ("OHC.04.C.K4",
     "Water, ice and accumulated material are described as capacity thieves because they:",
     ["Corrode the load block", "Add weight after the load weight was established",
      "Reduce the crane's duty class", "Interfere with the limit switch"], 1, ""),
    ("OHC.04.C.K5",
     "The correct relationship between an operator and a fitted load-limiting device is:",
     ["Plan to the device &#8212; it will stop an overload",
      "Plan to the rated load; the device is a backstop against error, not a planning margin",
      "Disable the device for production lifts",
      "Use the device to determine load weight"], 1, ""),
    ("OHC.04.C.R1",
     "Using the hoist to break a stuck load free is unacceptable because:",
     ["It is slow", "The load is unweighed, the restraint unknown, and the release sudden",
      "It wears the brake", "It requires a second operator"], 1, ""),
    ("OHC.04.C.R2",
     "Relying on the overload device as the planning margin means that:",
     ["Lifts are planned to succeed", "Every lift is planned to fail safely rather than to "
      "succeed, with the device as the only protection",
      "The rated load can be increased", "The lift plan is unnecessary"], 1, ""),
    ("OHC.04.C.R3",
     "Where two or more cranes are used to lift one load, the governing requirement is that:",
     ["Each operator works independently",
      "One qualified responsible person is in charge, analyses the operation and instructs "
      "all personnel involved",
      "The larger crane's operator takes command automatically",
      "The load is split evenly by assumption"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.04.A.K1": ("**&sect;1910.179(b)(5)** &middot; **EM 385 &sect;16.M.03**", "OK"),
    "OHC.04.A.K2": ("&sect;1910.179(b)(5) &middot; Tier 0 multi-hoist marking", "OK"),
    "OHC.04.A.K3": ("**&sect;1910.179(k)(2)**", "OK"),
    "OHC.04.A.K3b": ("CMAA 70 duty classes", "OK"),
    "OHC.04.A.K4": ("&sect;1910.179(b)(5) &middot; derived", "OK"),
    "OHC.04.A.K5": ("ASME B30.20 device marking &middot; Tier 0", "OK"),
    "OHC.04.A.R1": ("Tier 0 multi-hoist distinguishing marks", "OK"),
    "OHC.04.A.R2": ("derived &middot; `OHC.01.A.R2`", "OK"),
    "OHC.04.A.R3": ("&sect;1910.179(b)(5) &middot; derived", "OK"),
    "OHC.04.B.K1": ("Tier 0 weight-source hierarchy", "OK"),
    "OHC.04.B.K2": ("Tier 0 &middot; derived", "OK"),
    "OHC.04.B.K3": ("derived", "OK"),
    "OHC.04.B.K4": ("derived &middot; ASME B30.20 device weight", "OK"),
    "OHC.04.B.K5": ("**EM 385 &sect;16.A.03** Standard Lift Plan", "OK"),
    "OHC.04.B.R1": ("Tier 0 never-estimate rule", "OK"),
    "OHC.04.B.R2": ("derived", "OK"),
    "OHC.04.B.R3": ("**&sect;1910.179(n)(3)(vii)** brake test near rated load", "OK"),
    "OHC.04.C.K1": ("**&sect;1910.179(n)(1)**", "OK"),
    "OHC.04.C.K2": ("derived", "OK"),
    "OHC.04.C.K3": ("&sect;1910.179(n)(3)(iii)(a)", "OK"),
    "OHC.04.C.K4": ("derived &middot; Tier 0", "OK"),
    "OHC.04.C.K5": ("derived", "OK"),
    "OHC.04.C.R1": ("derived", "OK"),
    "OHC.04.C.R2": ("derived", "OK"),
    "OHC.04.C.R3": ("**&sect;1910.179(n)(3)(ix)**", "OK"),
}

TRACE_PERF = [
    ("OHC.04.A.S1", "Locate all capacity markings on the assigned crane and state the governing rating"),
    ("OHC.04.A.S2", "Compute available payload after subtracting rigging and device weights"),
    ("OHC.04.A.S3", "Reject a lift with unverifiable capacity information"),
    ("OHC.04.B.S1", "Document the weight basis for a lift before hoisting"),
    ("OHC.04.B.S2", "Calculate a load weight from geometry and material within acceptable margin"),
    ("OHC.04.B.S3", "Hold the lift when weight cannot be established"),
    ("OHC.04.C.S1", "Demonstrate slack removal and gradual load application"),
    ("OHC.04.C.S2", "Detect and respond to a load that does not lift at expected effort"),
    ("OHC.04.C.S3", "Stop and escalate any suspected overload event"),
]

TRACE_NOTES = [
    ("&#9989; Marking cited to both sources",
     "`A.K1` now leads with **&sect;1910.179(b)(5)**, which applies on **both** branches, "
     "and adds **EM 385 &sect;16.M.03** for federal work. The cross-check found the ACS "
     "sourcing this to EM 385 alone, which made a universal rule look federal-only."),
    ("&#9989; Standard Lift Plan read verbatim",
     "`B.K5` rests on **EM 385 &sect;16.A.03**, read directly: all lifts must be planned; a "
     "written SLP for every lift or series of lifts; developed, reviewed and accepted by "
     "all personnel involved; maintained on the equipment; and addressing personnel, area "
     "preparation, equipment, load parameters, rigging and environmental considerations."),
    ("&#9989; Two-crane lifts corrected",
     "The ACS frames `C.R3` as *\"multiple-hoist picks without engineered load share.\"* "
     "The regulation's actual answer is **&sect;1910.179(n)(3)(ix)**: one qualified "
     "responsible person in charge, who analyses the operation and instructs all personnel "
     "involved. The item is written to the regulation."),
    ("&#9432; Two items on one element",
     "`OHC.04.A.K3` carries a second item (`A.K3b`) because the element contains two "
     "independently testable facts &#8212; the 125&#37; test-load ceiling and the "
     "distinction between duty class and capacity."),
]


def build():
    return A.assemble(MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
                      len(GATE), SECTIONS, CONTENT, PRACTICE, GATE)


if __name__ == "__main__":
    out = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "out",
                                       "OHC_M04_RatedLoadAndWeight.pre.html"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out):
        os.remove(out)
    html = build()
    with open(out, "w", encoding="ascii") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))
