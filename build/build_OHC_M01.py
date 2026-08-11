#!/usr/bin/env python3
"""OHC-01 Equipment Types, Configurations, and Jurisdictional Framework.

US facility / construction / EM 385 branches plus Canada Task D (CSA B167 +
provincial overlays). Visual hero, flip cards, interactive jurisdiction tree.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cq_authoring as A

MODULE = "OHC_M01"
MODLABEL = "Module 1"
TITLE = "Equipment Types, Configurations, and Jurisdictional Framework"
SUBTITLE = ("Determine the equipment class, installation status, and governing "
            "regulatory regime &#8212; United States <b>or</b> Canada &#8212; before operation.")

OBJECTIVES = [
    "Identify overhead and gantry crane types, girder configurations and trolley "
    "arrangements, and name the governing consensus volume for each.",
    "Walk the installation-status decision tree (US) and the federal/provincial "
    "tree (Canada), and state the governing regime.",
    "Explain who qualifies the operator, what a designation covers, and where your "
    "own authority begins and ends &#8212; including the Canadian employer-authorization model.",
]

SECTIONS = [
    ("A", "Equipment Identification and Classification",
     "Identify overhead and gantry crane types and configurations and their operational "
     "characteristics."),
    ("B", "US Jurisdictional Determination",
     "Determine which US federal regime governs a specific crane based on installation "
     "status and work context."),
    ("C", "Roles, Qualification Architecture, and Standard of Care",
     "Explain who qualifies the operator, what the designation covers, and the operator's "
     "standard of care."),
    ("D", "Canadian Jurisdictional Framework",
     "Determine Canadian federal or provincial coverage and apply the CSA B167 spine with "
     "employer written authorization."),
]

CONTENT = {
    "A": [
        ("The equipment family",
         "Overhead and gantry cranes are bridge-and-trolley machines that travel a fixed "
         "runway. The family includes overhead and bridge cranes, gantry and semigantry "
         "cranes, cantilever gantry cranes, wall cranes, storage bridge cranes and "
         "launching gantry cranes.",
         "The family definition is deliberately broad and applies <b>irrespective of "
         "whether the equipment travels on tracks, wheels or other means</b>.",
         "01-hero-bridge.jpg", "Double-girder overhead bridge crane &#8212; fixed runway family"),
        ("Top running and underhung",
         "Two questions settle most configuration calls: does the bridge ride on top of "
         "the runway rails or beneath the runway beam flange, and does the trolley ride "
         "on top of the girder or suspended below it?",
         "Top running bridge with top running trolley is the common heavy configuration. "
         "Underhung equipment rides the lower flange and is generally lighter.",
         "01-top-vs-underhung.jpg", "Configuration drives the consensus volume"),
        ("Girder configuration",
         "Single-girder cranes carry one bridge girder with the trolley usually underhung. "
         "Double-girder cranes carry two, with the trolley running on rails on top.",
         "For a given girder design the relationship between span and capacity is "
         "<b>inverse</b>: a longer span carries less."),
        ("Related classes",
         "Monorail systems, underhung cranes and wall or jib cranes sit alongside the "
         "overhead family. They lift loads overhead but have their own configuration-"
         "specific requirements.",
         "Knowing that a machine is <i>related but not the same</i> stops an operator "
         "applying a bridge-crane rule to a monorail."),
        ("When a standard becomes law",
         "A consensus standard cited <i>by name</i> is guidance. A consensus standard "
         "<b>incorporated by reference</b> into a regulation is <b>law</b> for the named "
         "sections.",
         "29 CFR 1910.6 and 1926.6 are the US mechanisms. In Canada, CSA B167 becomes "
         "binding when adopted by statute, regulation, AHJ, or the employer's documented "
         "programme."),
        ("Which volume governs",
         "Configuration determines the governing consensus volume. Top running, underhung, "
         "monorails and hoists are each addressed by their own volume (ASME by name; "
         "CSA B167 for Canadian overhead travelling cranes).",
         "Confirm the <b>edition</b> in force before relying on any scope statement."),
    ],
    "B": [
        ("Two branches, one question",
         "Every US jurisdictional call starts with: <b>is this crane permanently installed "
         "in a facility?</b>",
         "Answer that wrong and every downstream rule &#8212; inspection, marking, operator "
         "requirement &#8212; comes from the wrong place."),
        ("The facility branch",
         "A permanently installed overhead or gantry crane used in construction is routed "
         "to 29 CFR 1910.179, with paragraph (b)(1) carved out. Subpart CC does not apply.",
         "This is the branch most facility operators work under for their whole career."),
        ("The construction branch",
         "A crane that is <b>not</b> permanently installed, used in construction, falls "
         "under a hybrid: designated Subpart CC sections including operator certification, "
         "plus an enumerated list of 1910.179 paragraphs.",
         "Only the enumerated paragraphs carry across, with definitions except "
         "<i>hoist</i> and <i>load</i>."),
        ("General industry",
         "Where the crane is operated in a facility outside any construction work, "
         "1910.179 is the direct spine.",
         "Same standard, arrived at directly rather than by cross-reference."),
        ("Federal and USACE work",
         "Federal work adds EM 385-1-1 Chapter 16 supplemental requirements on top of "
         "whichever branch already applies.",
         "These apply <b>whether or not the crane is permanently installed</b>."),
        ("One standard, two editions",
         "Both US branches incorporate the overhead crane design standard &#8212; but "
         "<b>not the same edition</b> (ANSI B30.2.0-1967 facility cut-off vs ASME "
         "B30.2-2005 construction cut-off).",
         "The edition follows the branch, and the cut-off date follows the equipment."),
        ("Recognising permanent installation",
         "Indicators are physical: fastened to the building, not readily assembled or "
         "disassembled, an irremovable part of the property.",
         "Time on site is not an indicator."),
    ],
    "C": [
        ("What this training does",
         "This module establishes your <b>standard of care</b> &#8212; what a competent "
         "operator is expected to know and to do.",
         "It does not qualify you. No training vendor can."),
        ("Who qualifies the operator",
         "The determination belongs to the <b>controlling entity</b>. It is not delegable "
         "to a training provider.",
         "Your completion record feeds that determination. It is not the determination."),
        ("The Designation Gate",
         "On the US facility branch: <b>only designated personnel</b> may operate "
         "(&sect;1910.179(b)(8)). <i>Designated</i> means selected or assigned by the "
         "employer as qualified for specific duties.",
         "Scoped in writing to named equipment and control modes."),
        ("The Certification Gate",
         "On the non-permanently-installed US construction branch the operator requirement "
         "is a certified operator under the Subpart CC operator certification section.",
         "Two US branches, two gates. Canada uses employer authorization &#8212; Task D."),
        ("Roles are distinct",
         "Designated personnel operate. An <b>appointed person</b> carries defined "
         "inspection and approval duties. Maintenance qualified persons adjust and repair.",
         "Undocumented roles blur accountability."),
    ],
    "D": [
        ("Canada is not a US overlay",
         "Canadian workplaces are not governed by OSHA 1910.179 or NCCCO routing. Applying "
         "US citations as if they were Canadian compliance is a jurisdictional failure.",
         "Use the Canada tree: federal vs province, then CSA B167 + employer authorization.",
         "01-canada-shop.jpg", "Canadian fabrication shop &#8212; same hazards, different statute"),
        ("CSA B167 &#8212; the consensus spine",
         "<b>CSA B167</b> addresses overhead travelling cranes: design, inspection, testing, "
         "maintenance, and safe operation. Cite it by name beside ASME B30.2 / B30.17 for "
         "configuration practice.",
         "Confirm the edition held at the site before quoting clause numbers. Until verified "
         "in the corpus, teach structure &#8212; not invented clause IDs."),
        ("Federal workplaces",
         "Federally regulated workplaces (banks, rail, interprovincial, federal lands) follow "
         "the <b>Canada Labour Code Part II</b> / COHSR path.",
         "Employer duties still require competent workers and documented authorization."),
        ("Provincial overlays",
         "<b>Ontario</b> &#8212; OHSA + Reg. 851 (industrial) / Reg. 213 (construction).<br>"
         "<b>British Columbia</b> &#8212; WorkSafeBC OHS Regulation Part 14.<br>"
         "<b>Alberta</b> &#8212; OHS Code Part 6.<br>"
         "<b>Quebec</b> &#8212; LSST / CNESST; prefer French designation paperwork.",
         "Other provinces and territories: attach the local OH&amp;S cite page; keep the "
         "same Designation Gate logic."),
        ("Authorization, not a US card",
         "The Canadian analogue of the Designation Gate is <b>employer written authorization</b> "
         "of a competent / qualified worker under the applicable Act.",
         "Do not treat an NCCCO or US certification card as sole evidence of Canadian "
         "competency. Use the EN/FR designation certificate in <code>forms/designation/</code>."),
    ],
}

PRACTICE = [
    ("OHC.01.A.K1", "Which of these is NOT part of the overhead and gantry crane family?",
     ["Semigantry crane", "Cantilever gantry crane",
      "Truck-mounted lattice boom crane", "Storage bridge crane"], 2,
     "A truck-mounted lattice boom crane is a mobile crane."),
    ("OHC.01.A.K2", "On a top-running bridge crane, the bridge end trucks ride:",
     ["On the bottom flange of the runway beam", "On rails mounted on top of the runway beams",
      "On the building floor", "On a suspended monorail track"], 1,
     "Top-running means the end trucks ride rails on top of the runway beams."),
    ("OHC.01.A.K6",
     "The hoist is treated as its own component class with its own consensus standard, "
     "separate from the crane it is mounted on.",
     ["True", "False"], 0, "The hoist is a distinct component class."),
    ("OHC.01.B.K6",
     "A crane bolted to the building structure that cannot be readily assembled or "
     "disassembled is best described as:",
     ["Temporarily erected", "Permanently installed", "A mobile crane",
      "Outside any federal standard"], 1,
     "Physical fastening and immobility are the indicators."),
    ("OHC.01.B.K1",
     "For a permanently installed overhead crane used in construction, the governing "
     "OSHA requirements are:",
     ["Subpart CC in full", "29 CFR 1910.179, except (b)(1)",
      "29 CFR 1926.1427 only", "None &#8212; no federal standard applies"], 1,
     "Subpart CC routes permanently installed overhead cranes to 1910.179."),
    ("OHC.01.B.R3",
     "Once a crane's governing regime has been determined, it never needs re-checking "
     "for the life of the equipment.",
     ["True", "False"], 1, "Jurisdiction follows installation status and work context."),
    ("OHC.01.C.R1", "Completing this course makes you a qualified overhead crane operator.",
     ["True", "False"], 1, "Training establishes standard of care, not qualification."),
    ("OHC.01.C.K1", "The determination that an operator is qualified belongs to:",
     ["The training provider", "The controlling entity",
      "The crane manufacturer", "The operator"], 1,
     "Not delegable to a training vendor."),
    ("OHC.01.C.S3",
     "An operator asked to run a crane type outside the scope of their designation should:",
     ["Proceed if a supervisor approves", "Proceed if they feel confident",
      "Decline until the designation is extended", "Proceed if the crane looks similar"], 2,
     "Outside scope there is no designation."),
    ("OHC.01.D.K1",
     "For Canadian overhead travelling crane programmes, the consensus spine to name "
     "beside ASME configuration volumes is:",
     ["OSHA 1910.179", "CSA B167", "NCCCO Candidate Handbook", "EM 385 Figure 16-4"], 1,
     "CSA B167 is the Canadian overhead travelling crane consensus standard."),
    ("OHC.01.D.R1",
     "Using US OSHA/NCCCO routing as the compliance story for a Canadian provincial "
     "workplace is acceptable if the equipment looks the same.",
     ["True", "False"], 1,
     "Same hazards; different statute. Canada needs its own jurisdiction path."),
    ("OHC.01.D.K4",
     "On a Canadian site, the Designation Gate analogue is best described as:",
     ["Automatic qualification after any online course",
      "Employer written authorization of a competent/qualified worker",
      "A US certification card with no site paperwork",
      "Manufacturer commissioning alone"], 1,
     "Employer authorization under the applicable OH&amp;S Act."),
]

GATE = [
    ("OHC.01.A.K1",
     "The overhead and gantry crane family covers bridge, gantry, semigantry, cantilever "
     "gantry, wall, storage bridge and launching gantry cranes. That coverage applies:",
     ["Only where the crane travels on rails", "Only where the crane travels on wheels",
      "Irrespective of whether it travels on tracks, wheels or other means",
      "Only where the crane is permanently installed"], 2, ""),
    ("OHC.01.A.K2",
     "A crane whose trolley is suspended from the underside of the bridge girder, and "
     "whose bridge rides the lower flange of the runway beams, is:",
     ["Top running bridge, top running trolley", "Underhung bridge with underhung trolley",
      "A gantry crane", "A launching gantry"], 1, ""),
    ("OHC.01.A.K3",
     "For a given girder design, increasing the span of a single-girder bridge crane:",
     ["Increases the rated capacity", "Has no effect on rated capacity",
      "Reduces the rated capacity", "Converts it to a double-girder crane"], 2, ""),
    ("OHC.01.A.K4",
     "Monorail systems, underhung cranes and wall-mounted jib cranes are best described as:",
     ["Identical to top-running bridge cranes in every respect",
      "Related equipment classes with their own configuration-specific requirements",
      "Not lifting equipment", "Always exempt from inspection"], 1, ""),
    ("OHC.01.A.K5",
     "Selecting the governing consensus volume for a crane depends first on:",
     ["The crane's age", "The crane's colour",
      "The crane's configuration &#8212; top running versus underhung",
      "The operator's experience level"], 2, ""),
    ("OHC.01.A.K6",
     "The hoist mounted on an overhead crane is covered by the same consensus volume as "
     "the crane structure itself.",
     ["True", "False"], 1, ""),
    ("OHC.01.A.R1",
     "The direct operational consequence of misclassifying a crane's type or configuration is:",
     ["Nothing &#8212; classification is administrative only",
      "The wrong inspection, marking and operating rule set attaches",
      "The crane loses its capacity rating", "The runway must be replaced"], 1, ""),
    ("OHC.01.A.R2",
     "Which mobile-crane habit does NOT transfer to overhead crane operation?",
     ["Confirming the load weight before lifting",
      "Reading capacity from a load chart by boom radius",
      "Keeping personnel clear of the load", "Checking rigging before the pick"], 1, ""),
    ("OHC.01.A.R3",
     "Before operating an overhead crane configuration you have not run before, "
     "configuration-specific familiarization is required even when the crane is within "
     "your designated class.",
     ["True", "False"], 0, ""),
    ("OHC.01.A.K7",
     "A consensus standard that has been incorporated by reference into an OSHA "
     "regulation is:",
     ["Advisory guidance only", "Enforceable as regulation for the sections named",
      "Superseded by the regulation", "Applicable only to new equipment"], 1, ""),
    ("OHC.01.B.K1",
     "A permanently installed overhead crane in a facility is used for a construction task. "
     "Which applies?",
     ["Subpart CC applies in full", "29 CFR 1910.179 applies, except (b)(1)",
      "Both apply in full simultaneously", "Neither applies"], 1, ""),
    ("OHC.01.B.K2",
     "An overhead crane that is NOT permanently installed, used in construction, falls under:",
     ["1910.179 in its entirety",
      "Designated Subpart CC sections including the operator certification requirement, "
      "plus specified 1910.179 paragraphs",
      "State building code only", "The manufacturer's manual only"], 1, ""),
    ("OHC.01.B.K3",
     "On the non-permanently-installed construction branch, which portion of 1910.179 "
     "carries across?",
     ["All of 1910.179", "None of 1910.179",
      "Only an enumerated list of paragraphs, plus the definitions except hoist and load",
      "Only the appendices"], 2, ""),
    ("OHC.01.B.K4",
     "For an overhead crane operated in a general-industry facility outside any "
     "construction work, 29 CFR 1910.179 is the direct governing standard.",
     ["True", "False"], 0, ""),
    ("OHC.01.B.K5",
     "On federal and USACE work, the supplemental overhead and gantry requirements apply:",
     ["Only to permanently installed cranes", "Only to cranes that are not permanently installed",
      "Whether or not the crane is permanently installed", "Only to cranes over 30 tons"], 2, ""),
    ("OHC.01.B.K6",
     "Which is the strongest indicator that a crane is permanently installed?",
     ["It has been on site more than a year", "It is painted in facility colours",
      "It is physically fastened to the building and is not readily assembled or disassembled",
      "It is operated by facility employees"], 2, ""),
    ("OHC.01.B.R1",
     "Treating a non-permanently-installed construction crane as if it were a facility "
     "crane most seriously risks:",
     ["Over-inspecting the equipment",
      "Missing the operator certification requirement that attaches on that branch",
      "Using the wrong paint specification", "Nothing of consequence"], 1, ""),
    ("OHC.01.B.R2",
     "Because a crane is being used for a construction task, Subpart CC automatically "
     "applies to it regardless of installation status.",
     ["True", "False"], 1, ""),
    ("OHC.01.B.R3",
     "A facility crane is dismantled and re-erected at a temporary work area for a "
     "construction project. The correct action is to:",
     ["Continue under the original determination",
      "Re-evaluate the governing regime, because installation status has changed",
      "Stop using the crane permanently", "Apply whichever regime is less restrictive"], 1, ""),
    ("OHC.01.B.K7",
     "The overhead crane design standard is incorporated by reference on both US branches. "
     "Which statement is correct?",
     ["The same edition is incorporated on both branches",
      "The facility and construction branches incorporate different editions, each with "
      "its own equipment cut-off date",
      "Only the construction branch incorporates any edition",
      "Incorporation by reference applies only to cranes built before 1971"], 1, ""),
    ("OHC.01.C.K1",
     "Training content such as this module establishes:",
     ["The operator's qualification", "The operator's standard of care",
      "The employer's insurance rating", "The crane's rated capacity"], 1, ""),
    ("OHC.01.C.K2",
     "On the facility branch, the governing rule on who may run the crane is that:",
     ["Any trained person may operate", "Only designated personnel may operate",
      "Only the manufacturer may operate", "Anyone with a valid driver's licence may operate"], 1, ""),
    ("OHC.01.C.K3",
     "On the non-permanently-installed construction branch, the operator requirement is:",
     ["An employer-issued designation only",
      "A certified operator under the Subpart CC operator certification section",
      "No requirement", "A state-issued licence only"], 1, ""),
    ("OHC.01.C.K4",
     "On federal work, the Certificate of Compliance submitted for each piece of load "
     "handling equipment brought on site must be signed by:",
     ["The crane operator", "A Competent Person for Crane and Rigging",
      "The equipment supplier", "Any site supervisor"], 1, ""),
    ("OHC.01.C.K5",
     "Which pairing is correct?",
     ["Designated personnel operate; an appointed person carries defined inspection and "
      "approval duties",
      "Designated personnel and appointed persons are the same role",
      "An appointed person operates; designated personnel inspect",
      "Neither term appears in the standard"], 0, ""),
    ("OHC.01.C.R1",
     "A completion certificate from a training programme is sufficient evidence that an "
     "operator is qualified.",
     ["True", "False"], 1, ""),
    ("OHC.01.C.R2",
     "On federal work, load handling equipment shall be operated only by personnel who are:",
     ["Available and willing", "Trained, qualified and designated",
      "Employed by the prime contractor", "Over 21 years of age"], 1, ""),
    ("OHC.01.C.R3",
     "When operator, inspector and maintenance roles are not documented, the primary "
     "exposure is:",
     ["Higher training cost", "Blurred accountability when something goes wrong",
      "Slower crane travel speeds", "Reduced rated capacity"], 1, ""),
    # ---- Canada Task D gates
    ("OHC.01.D.K1",
     "On a Canadian overhead travelling crane programme, the consensus standard that "
     "should be named as the spine for design, inspection, testing, maintenance and safe "
     "operation is:",
     ["ASME P30.1 only", "CSA B167", "29 CFR 1910.179", "CMAA Spec 70 only"], 1, ""),
    ("OHC.01.D.K2",
     "A federally regulated Canadian workplace (for example interprovincial rail) is "
     "governed primarily under:",
     ["OSHA Subpart CC", "Canada Labour Code Part II / COHSR",
      "WorkSafeBC Part 14 exclusively", "Quebec CNESST exclusively"], 1, ""),
    ("OHC.01.D.K3",
     "Which pairing is correct for provincial crane rules?",
     ["Ontario &#8212; WorkSafeBC Part 14", "British Columbia &#8212; OHS Code Part 6",
      "Alberta &#8212; OHS Code Part 6; BC &#8212; WorkSafeBC Part 14",
      "Quebec &#8212; OSHA 1910.179"], 2, ""),
    ("OHC.01.D.K4",
     "The Canadian Designation Gate analogue is:",
     ["NCCCO overhead certification alone",
      "Employer written authorization of a competent/qualified worker under the applicable Act",
      "Any toolbox talk attendance sheet", "Manufacturer warranty registration"], 1, ""),
    ("OHC.01.D.K5",
     "Completing OCO301C on a Canadian site:",
     ["Automatically qualifies the operator under every provincial Act",
      "Establishes structured preparation and standard of care; the employer still authorizes",
      "Replaces CSA B167 inspection duties", "Satisfies USACE EM 385 only"], 1, ""),
    ("OHC.01.D.R1",
     "The most serious jurisdictional error on a Canadian site is:",
     ["Citing CSA B167 by name",
      "Treating US OSHA/NCCCO routing as if it were Canadian compliance",
      "Using French designation forms in Quebec",
      "Keeping PES sheets with the training record"], 1, ""),
    ("OHC.01.D.R2",
     "Ignoring Quebec language-of-work and documentation expectations when the workforce "
     "and AHJ require French materials primarily risks:",
     ["Nothing &#8212; English is always sufficient nationwide",
      "Non-compliant or unusable designation / competency records for that site",
      "Higher hoist speeds", "Automatic CSA B167 exemption"], 1, ""),
    ("OHC.01.D.R3",
     "Treating CSA B167 as optional when the employer's programme or AHJ expects it as "
     "the operating standard means:",
     ["You have selected a stronger standard",
      "You may be operating outside the site's documented standard of care",
      "ASME citations become illegal", "EM 385 applies automatically"], 1, ""),
]

TRACE_SOURCE = {
    "OHC.01.A.K1": ("&sect;1926.1438(b)(1)", "OK"),
    "OHC.01.A.K2": ("ASME B30.2 / B30.17 by name", "OK"),
    "OHC.01.A.K3": ("CMAA 70 by name", "OK"),
    "OHC.01.A.K4": ("ASME B30.11 / B30.17 by name", "OK"),
    "OHC.01.A.K5": ("B30.2 / B30.17", "ED2014"),
    "OHC.01.A.K6": ("ASME B30.16 by name", "OK"),
    "OHC.01.A.R1": ("derived", "OK"),
    "OHC.01.A.R2": ("&sect;1910.179(b)(5)", "OK"),
    "OHC.01.A.R3": ("Tier 0 (owned)", "OK"),
    "OHC.01.A.K7": ("&sect;1910.6 &middot; &sect;1910.179(b)(2),(b)(6)(i)", "OK"),
    "OHC.01.B.K1": ("&sect;1926.1438(a)", "OK"),
    "OHC.01.B.K2": ("&sect;1926.1438(b)", "OK"),
    "OHC.01.B.K3": ("&sect;1926.1438(b)(2)(i)", "OK"),
    "OHC.01.B.K4": ("&sect;1910.179", "OK"),
    "OHC.01.B.K5": ("EM 385 Ch. 16", "OK"),
    "OHC.01.B.K6": ("&sect;1926.1438(a)", "OK"),
    "OHC.01.B.R1": ("derived", "OK"),
    "OHC.01.B.R2": ("&sect;1926.1438(a)", "OK"),
    "OHC.01.B.R3": ("derived", "OK"),
    "OHC.01.B.K7": ("&sect;1910.179(b)(2) &middot; &sect;1926.1438(b)(2)(ii)", "OK"),
    "OHC.01.C.K1": ("Gate Master Rev 1.3 &sect;11.2, A2", "OK"),
    "OHC.01.C.K2": ("**&sect;1910.179(b)(8)**", "OK"),
    "OHC.01.C.K3": ("&sect;1926.1427", "OPEN"),
    "OHC.01.C.K4": ("EM 385 &sect;16.A.02", "OK"),
    "OHC.01.C.K5": ("&sect;1910.179(b)(8), (l)(3)(i), (m)(1)", "OK"),
    "OHC.01.C.R1": ("Gate Master &sect;11.2", "OK"),
    "OHC.01.C.R2": ("EM 385 &sect;16.B.01", "OK"),
    "OHC.01.C.R3": ("derived", "OK"),
    "OHC.01.D.K1": ("CSA B167 by name", "OK"),
    "OHC.01.D.K2": ("Canada Labour Code Part II / COHSR", "OK"),
    "OHC.01.D.K3": ("ON Reg 851/213 &middot; WorkSafeBC Part 14 &middot; AB OHS Code Part 6", "OK"),
    "OHC.01.D.K4": ("Canada jurisdiction pack &middot; employer authorization", "OK"),
    "OHC.01.D.K5": ("Gate Master A2 &middot; Canada pack", "OK"),
    "OHC.01.D.R1": ("Canada jurisdiction pack", "OK"),
    "OHC.01.D.R2": ("Quebec / CNESST documentation", "OK"),
    "OHC.01.D.R3": ("CSA B167 programme alignment", "OK"),
}

TRACE_PERF = [
    ("OHC.01.A.S1", "Identify crane type, girder configuration and trolley arrangement on sight"),
    ("OHC.01.A.S2", "Match a given crane to its governing ASME volume by name"),
    ("OHC.01.A.S3", "Locate and interpret equipment identification and capacity markings"),
    ("OHC.01.B.S1", "Walk the installation-status decision tree and state the governing regime"),
    ("OHC.01.B.S2", "Identify which certification or designation attaches on each branch"),
    ("OHC.01.B.S3", "Classify a crane as EM 385 Class I or Class II"),
    ("OHC.01.C.S1", "State who issued their designation, what it covers, and its limits"),
    ("OHC.01.C.S2", "Produce designation and training records on request"),
    ("OHC.01.C.S3", "Refuse an assignment outside the scope of designation"),
    ("OHC.01.D.S1", "Select the correct Canada branch (federal vs named province) for a given site"),
    ("OHC.01.D.S2", "State that CSA B167 is the consensus spine and where ASME still informs configuration"),
    ("OHC.01.D.S3", "Produce or request the employer written authorization / designation for the assigned crane"),
]

TRACE_NOTES = [
    ("&#11088; Task D adds the Canadian jurisdiction spine without forking the track",
     "**CSA B167** is cited by name as the consensus spine. Provincial overlays (ON/BC/AB/QC) "
     "and the Canada Labour Code Part II path are taught as branches parallel to the US "
     "facility/construction split. Clause-level CSA quotes are held back until a verified "
     "edition is in the corpus."),
    ("&#9989; Designation Gate citation",
     "`C.K2` rests on **&sect;1910.179(b)(8)**. Canada uses employer written authorization as "
     "the analogue &#8212; not NCCCO routing."),
]


def main():
    html = A.assemble(
        MODULE, MODLABEL, TITLE, SUBTITLE, OBJECTIVES,
        len(GATE), SECTIONS, CONTENT, PRACTICE, GATE,
        hero_image="01-hero-bridge.jpg",
        extra_before_gate=[
            lambda sid: A.flip_cards_slide(
                sid, "Quick contrast", "US gates vs Canada authorization",
                [
                    ("US Facility", "Designation Gate",
                     "&sect;1910.179(b)(8)", "Only designated personnel may operate. Employer designates in writing."),
                    ("US Construction", "Certification Gate",
                     "&sect;1926.1427 via &sect;1926.1438(b)", "Certified operator on the non-permanent construction branch."),
                    ("Canada", "Employer authorization",
                     "CSA B167 + OH&amp;S Act", "Competent/qualified worker + written authorization. No NCCCO routing."),
                ],
            ),
            A.na_jurisdiction_tree_slide,
        ],
    )
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pre = os.path.join(root, "out", "OHC_M01_EquipmentAndJurisdiction.pre.html")
    with open(pre, "w", encoding="ascii", errors="xmlcharrefreplace") as f:
        f.write(html)
    print("wrote %s (%d bytes, total slides %d)" % (pre, len(html), A.LAST_TOTAL))

    answer_key = {}
    for i, q in enumerate(PRACTICE, 1):
        answer_key["%s_q%02d" % (MODULE, i)] = q[3]
    for i, q in enumerate(GATE, 1):
        answer_key["%s_q%02d" % (MODULE, len(PRACTICE) + i)] = q[3]
    gate_ids = ["%s_q%02d" % (MODULE, len(PRACTICE) + i) for i in range(1, len(GATE) + 1)]
    man = {
        "module": MODULE,
        "stage": "OHC",
        "gate_code": "OHC-1",
        "version": "2026.08-CA",
        "salt": "CQ1:OHC_M01_EquipmentAndJurisdiction",
        "total": A.LAST_TOTAL,
        "next": "OHC_M02",
        "gate": gate_ids,
        "review_offset": len(PRACTICE),
        "answer_key": answer_key,
        "course": "OCO301C",
        "notes": "Canada Task D + visual pack",
    }
    man_path = os.path.join(root, "manifests", "OHC_M01.json")
    with open(man_path, "w", encoding="utf-8") as f:
        json.dump(man, f, indent=2)
        f.write("\n")
    print("wrote %s (gate %d, keys %d)" % (man_path, len(gate_ids), len(answer_key)))


if __name__ == "__main__":
    main()
