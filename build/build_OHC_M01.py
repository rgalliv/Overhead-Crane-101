#!/usr/bin/env python3
"""Emit the pre-retrofit DOM for OHC-01.

Authors the module to the Stage-2 contract expected by cq_module_kit.py, then
lets `retrofit` inject the kit's own validated gate engine. No hand-rolled
crypto: plaintext keys are emitted here and stripped by the retrofit, which
replaces them with FNV-1a hashes.

ASCII-only source. Non-ASCII reaches the HTML as entities.
"""
import os

MODULE = "OHC_M01"
SECT = "&#167;"          # section sign
MD = "&#8212;"           # em dash
DEG = "&#176;"           # degree

# ---------------------------------------------------------------- questions
# (qid_num, kind, element, stem, [options], correct_idx, rationale)
# kind: "practice" (unscored, reveals answer) | "gate" (scored, never reveals)

PRACTICE = [
    (1, "OHC.01.A.K1", "Which of these is NOT part of the overhead and gantry crane family?",
     ["Semigantry crane", "Cantilever gantry crane",
      "Truck-mounted lattice boom crane", "Storage bridge crane"], 2,
     "A truck-mounted lattice boom crane is a mobile crane. The overhead and gantry "
     "family is bridge-and-trolley equipment travelling a fixed runway."),
    (2, "OHC.01.A.K2", "On a top-running bridge crane, the bridge end trucks ride:",
     ["On the bottom flange of the runway beam", "On rails mounted on top of the runway beams",
      "On the building floor", "On a suspended monorail track"], 1,
     "Top-running means the end trucks ride rails on top of the runway beams. "
     "Underhung equipment rides the bottom flange."),
    (3, "OHC.01.A.K6",
     "The hoist is treated as its own component class with its own consensus standard, "
     "separate from the crane it is mounted on.",
     ["True", "False"], 0,
     "The hoist is a distinct component class and is covered by its own volume."),
    (4, "OHC.01.B.K6",
     "A crane bolted to the building structure that cannot be readily assembled or "
     "disassembled is best described as:",
     ["Temporarily erected", "Permanently installed",
      "A mobile crane", "Outside any federal standard"], 1,
     "Fastened to the building, not readily assembled or disassembled, and an "
     "irremovable part of the property are the indicators of permanent installation."),
    (5, "OHC.01.B.K1",
     "For a permanently installed overhead crane used in construction, the governing "
     "OSHA requirements are:",
     ["Subpart CC in full", "29 CFR 1910.179, except (b)(1)",
      "29 CFR 1926.1427 only", "None &#8212; no federal standard applies"], 1,
     "Subpart CC routes permanently installed overhead and gantry cranes to "
     "1910.179, carving out (b)(1)."),
    (6, "OHC.01.B.R3",
     "Once a crane's governing regime has been determined, it never needs re-checking "
     "for the life of the equipment.",
     ["True", "False"], 1,
     "Jurisdiction follows installation status and work context. Both can change."),
    (7, "OHC.01.C.R1", "Completing this course makes you a qualified overhead crane operator.",
     ["True", "False"], 1,
     "Training establishes your standard of care. It does not confer qualification."),
    (8, "OHC.01.C.K1", "The determination that an operator is qualified belongs to:",
     ["The training provider", "The controlling entity",
      "The crane manufacturer", "The operator"], 1,
     "The determination belongs to the controlling entity and is not delegable to a "
     "training vendor."),
    (9, "OHC.01.C.S3",
     "An operator asked to run a crane type outside the scope of their designation should:",
     ["Proceed if a supervisor approves", "Proceed if they feel confident",
      "Decline until the designation is extended", "Proceed if the crane looks similar"], 2,
     "Designation is scoped to named equipment and control modes. Outside that scope "
     "there is no designation."),
]

GATE = [
    # ---- Task A
    (10, "OHC.01.A.K1",
     "The overhead and gantry crane family covers bridge, gantry, semigantry, cantilever "
     "gantry, wall, storage bridge and launching gantry cranes. That coverage applies:",
     ["Only where the crane travels on rails", "Only where the crane travels on wheels",
      "Irrespective of whether it travels on tracks, wheels or other means",
      "Only where the crane is permanently installed"], 2,
     ""),
    (11, "OHC.01.A.K2",
     "A crane whose trolley is suspended from the underside of the bridge girder, and "
     "whose bridge rides the lower flange of the runway beams, is:",
     ["Top running bridge, top running trolley", "Underhung bridge with underhung trolley",
      "A gantry crane", "A launching gantry"], 1,
     ""),
    (12, "OHC.01.A.K3",
     "For a given girder design, increasing the span of a single-girder bridge crane:",
     ["Increases the rated capacity", "Has no effect on rated capacity",
      "Reduces the rated capacity", "Converts it to a double-girder crane"], 2,
     ""),
    (13, "OHC.01.A.K4",
     "Monorail systems, underhung cranes and wall-mounted jib cranes are best described as:",
     ["Identical to top-running bridge cranes in every respect",
      "Related equipment classes with their own configuration-specific requirements",
      "Not lifting equipment", "Always exempt from inspection"], 1,
     ""),
    (14, "OHC.01.A.K5",
     "Selecting the governing consensus volume for a crane depends first on:",
     ["The crane's age", "The crane's colour",
      "The crane's configuration &#8212; top running versus underhung",
      "The operator's experience level"], 2,
     ""),
    (15, "OHC.01.A.K6",
     "The hoist mounted on an overhead crane is covered by the same consensus volume as "
     "the crane structure itself.",
     ["True", "False"], 1,
     ""),
    (16, "OHC.01.A.R1",
     "The direct operational consequence of misclassifying a crane's type or configuration is:",
     ["Nothing &#8212; classification is administrative only",
      "The wrong inspection, marking and operating rule set attaches",
      "The crane loses its capacity rating", "The runway must be replaced"], 1,
     ""),
    (17, "OHC.01.A.R2",
     "Which mobile-crane habit does NOT transfer to overhead crane operation?",
     ["Confirming the load weight before lifting",
      "Reading capacity from a load chart by boom radius",
      "Keeping personnel clear of the load", "Checking rigging before the pick"], 1,
     ""),
    (18, "OHC.01.A.R3",
     "Before operating an overhead crane configuration you have not run before, "
     "configuration-specific familiarization is required even when the crane is within "
     "your designated class.",
     ["True", "False"], 0,
     ""),
    (0, "OHC.01.A.K7",
     "A consensus standard that has been incorporated by reference into an OSHA "
     "regulation is:",
     ["Advisory guidance only", "Enforceable as regulation for the sections named",
      "Superseded by the regulation", "Applicable only to new equipment"], 1,
     ""),
    # ---- Task B
    (0, "OHC.01.B.K1",
     "A permanently installed overhead crane in a facility is used for a construction task. "
     "Which applies?",
     ["Subpart CC applies in full", "29 CFR 1910.179 applies, except (b)(1)",
      "Both apply in full simultaneously", "Neither applies"], 1,
     ""),
    (20, "OHC.01.B.K2",
     "An overhead crane that is NOT permanently installed, used in construction, falls under:",
     ["1910.179 in its entirety",
      "Designated Subpart CC sections including the operator certification requirement, "
      "plus specified 1910.179 paragraphs",
      "State building code only", "The manufacturer's manual only"], 1,
     ""),
    (21, "OHC.01.B.K3",
     "On the non-permanently-installed construction branch, which portion of 1910.179 "
     "carries across?",
     ["All of 1910.179", "None of 1910.179",
      "Only an enumerated list of paragraphs, plus the definitions except hoist and load",
      "Only the appendices"], 2,
     ""),
    (22, "OHC.01.B.K4",
     "For an overhead crane operated in a general-industry facility outside any "
     "construction work, 29 CFR 1910.179 is the direct governing standard.",
     ["True", "False"], 0,
     ""),
    (23, "OHC.01.B.K5",
     "On federal and USACE work, the supplemental overhead and gantry requirements apply:",
     ["Only to permanently installed cranes", "Only to cranes that are not permanently installed",
      "Whether or not the crane is permanently installed", "Only to cranes over 30 tons"], 2,
     ""),
    (24, "OHC.01.B.K6",
     "Which is the strongest indicator that a crane is permanently installed?",
     ["It has been on site more than a year", "It is painted in facility colours",
      "It is physically fastened to the building and is not readily assembled or disassembled",
      "It is operated by facility employees"], 2,
     ""),
    (25, "OHC.01.B.R1",
     "Treating a non-permanently-installed construction crane as if it were a facility "
     "crane most seriously risks:",
     ["Over-inspecting the equipment", "Missing the operator certification requirement "
      "that attaches on that branch",
      "Using the wrong paint specification", "Nothing of consequence"], 1,
     ""),
    (26, "OHC.01.B.R2",
     "Because a crane is being used for a construction task, Subpart CC automatically "
     "applies to it regardless of installation status.",
     ["True", "False"], 1,
     ""),
    (27, "OHC.01.B.R3",
     "A facility crane is dismantled and re-erected at a temporary work area for a "
     "construction project. The correct action is to:",
     ["Continue under the original determination",
      "Re-evaluate the governing regime, because installation status has changed",
      "Stop using the crane permanently", "Apply whichever regime is less restrictive"], 1,
     ""),
    (0, "OHC.01.B.K7",
     "The overhead crane design standard is incorporated by reference on both branches. "
     "Which statement is correct?",
     ["The same edition is incorporated on both branches",
      "The facility and construction branches incorporate different editions, each with "
      "its own equipment cut-off date",
      "Only the construction branch incorporates any edition",
      "Incorporation by reference applies only to cranes built before 1971"], 1,
     ""),
    # ---- Task C
    (0, "OHC.01.C.K1",
     "Training content such as this module establishes:",
     ["The operator's qualification", "The operator's standard of care",
      "The employer's insurance rating", "The crane's rated capacity"], 1,
     ""),
    (29, "OHC.01.C.K2",
     "On the facility branch, the governing rule on who may run the crane is that:",
     ["Any trained person may operate", "Only designated personnel may operate",
      "Only the manufacturer may operate", "Anyone with a valid driver's licence may operate"], 1,
     ""),
    (30, "OHC.01.C.K3",
     "On the non-permanently-installed construction branch, the operator requirement is:",
     ["An employer-issued designation only", "A certified operator under the Subpart CC "
      "operator certification section",
      "No requirement", "A state-issued licence only"], 1,
     ""),
    (0, "OHC.01.C.K4",
     "On federal work, the Certificate of Compliance submitted for each piece of load "
     "handling equipment brought on site must be signed by:",
     ["The crane operator", "A Competent Person for Crane and Rigging",
      "The equipment supplier", "Any site supervisor"], 1,
     ""),
    (31, "OHC.01.C.K5",
     "Which pairing is correct?",
     ["Designated personnel operate; an appointed person carries defined inspection and "
      "approval duties",
      "Designated personnel and appointed persons are the same role",
      "An appointed person operates; designated personnel inspect",
      "Neither term appears in the standard"], 0,
     ""),
    (32, "OHC.01.C.R1",
     "A completion certificate from a training programme is sufficient evidence that an "
     "operator is qualified.",
     ["True", "False"], 1,
     ""),
    (0, "OHC.01.C.R2",
     "On federal work, load handling equipment shall be operated only by personnel who are:",
     ["Available and willing", "Trained, qualified and designated",
      "Employed by the prime contractor", "Over 21 years of age"], 1,
     ""),
    (33, "OHC.01.C.R3",
     "When operator, inspector and maintenance roles are not documented, the primary "
     "exposure is:",
     ["Higher training cost", "Blurred accountability when something goes wrong",
      "Slower crane travel speeds", "Reduced rated capacity"], 1,
     ""),
]

# --------------------------------------------------------------------- slides
CONTENT = {
    "A": [
        ("The equipment family",
         "Overhead and gantry cranes are bridge-and-trolley machines that travel a fixed "
         "runway. The family includes overhead and bridge cranes, gantry and semigantry "
         "cranes, cantilever gantry cranes, wall cranes, storage bridge cranes and "
         "launching gantry cranes.",
         "The family definition is deliberately broad and applies <b>irrespective of "
         "whether the equipment travels on tracks, wheels or other means</b>. Do not use "
         "the travel arrangement to argue a crane out of the family."),
        ("Top running and underhung",
         "Two questions settle most configuration calls: does the bridge ride on top of "
         "the runway rails or beneath the runway beam flange, and does the trolley ride "
         "on top of the girder or suspended below it?",
         "Top running bridge with top running trolley is the common heavy configuration. "
         "Underhung equipment rides the lower flange and is generally lighter, with "
         "different structural and inspection consequences."),
        ("Girder configuration",
         "Single-girder cranes carry one bridge girder with the trolley usually underhung. "
         "Double-girder cranes carry two, with the trolley running on rails on top.",
         "For a given girder design the relationship between span and capacity is "
         "<b>inverse</b>: a longer span carries less, because the girder must carry more "
         "of its own weight over the distance."),
        ("Related classes",
         "Monorail systems, underhung cranes and wall or jib cranes sit alongside the "
         "overhead family. They lift loads overhead but have their own configuration-"
         "specific requirements.",
         "Knowing that a machine is <i>related but not the same</i> is what stops an "
         "operator applying a bridge-crane rule to a monorail."),
        ("When a standard becomes law",
         "A consensus standard cited <i>by name</i> is guidance. A consensus standard "
         "<b>incorporated by reference</b> into a regulation is <b>law</b> &#8212; the named "
         "sections are enforceable exactly as the regulation is.",
         "29 CFR 1910.6 and 1926.6 are the mechanisms that do this. Two examples sit "
         "inside the overhead crane rules themselves: the design specification at "
         "1910.179(b)(2), and the clearance specification at 1910.179(b)(6)(i)."),
        ("Which volume governs",
         "Configuration determines the governing consensus volume. Top running bridge and "
         "trolley equipment, underhung trolley or bridge equipment, monorails and hoists "
         "are each addressed by their own volume.",
         "Cite the volume by name. Confirm the <b>edition</b> in force before relying on "
         "any scope statement &#8212; volume scopes have moved between editions."),
    ],
    "B": [
        ("Two branches, one question",
         "Every jurisdictional call on an overhead crane starts with one question: "
         "<b>is this crane permanently installed in a facility?</b>",
         "Answer that, and the governing regime follows. Answer it wrong and every "
         "downstream rule &#8212; inspection, marking, operator requirement &#8212; comes "
         "from the wrong place."),
        ("The facility branch",
         "A permanently installed overhead or gantry crane used in construction is routed "
         "to 29 CFR 1910.179, with paragraph (b)(1) carved out. Subpart CC does not apply.",
         "This is the branch most facility operators work under for their whole career."),
        ("The construction branch",
         "A crane that is <b>not</b> permanently installed, used in construction, falls "
         "under a hybrid: designated Subpart CC sections including the operator "
         "certification requirement, plus an enumerated list of 1910.179 paragraphs.",
         "Only the enumerated paragraphs carry across, together with the definitions "
         "except <i>hoist</i> and <i>load</i>. Paragraphs outside that list do not apply "
         "on this branch."),
        ("General industry",
         "Where the crane is operated in a facility outside any construction work, "
         "1910.179 is the direct spine with no routing question to answer.",
         "Same standard, arrived at directly rather than by cross-reference."),
        ("Federal and USACE work",
         "Federal work adds supplemental overhead and gantry requirements on top of "
         "whichever branch already applies.",
         "Note carefully: these supplemental requirements apply <b>whether or not the "
         "crane is permanently installed</b>. This is a layer across both branches, not a "
         "third branch."),
        ("One standard, two editions",
         "Both branches incorporate the overhead crane design standard &#8212; but "
         "<b>not the same edition</b>. The facility branch adopts the 1967 ANSI edition "
         "for cranes installed on or after 31 August 1971. The construction branch "
         "adopts named sections of the 2005 ASME edition for equipment manufactured on "
         "or after 19 September 2001.",
         "Learn <i>&quot;B30.2 is the overhead crane standard&quot;</i> and stop there, and you "
         "will cite the wrong edition on one branch or the other. The edition follows "
         "the branch, and the cut-off date follows the equipment."),
        ("Recognising permanent installation",
         "The indicators are physical: fastened to the building structure, not readily "
         "assembled or disassembled, and an irremovable part of the property.",
         "Time on site is not an indicator. A crane standing for two years that can be "
         "unbolted and moved is not permanently installed."),
    ],
    "C": [
        ("What this training does",
         "This module establishes your <b>standard of care</b> &#8212; what a competent "
         "operator is expected to know and to do.",
         "It does not qualify you. No training vendor can. Be precise about this "
         "difference; it is the difference between a defensible programme and an "
         "indefensible one."),
        ("Who qualifies the operator",
         "The determination that an operator is qualified belongs to the <b>controlling "
         "entity</b>. It is not delegable to a training provider.",
         "Your completion record is evidence that feeds that determination. It is not the "
         "determination itself."),
        ("The Designation Gate",
         "On the facility branch the rule is that <b>only designated personnel</b> may "
         "operate the crane. <i>Designated</i> means selected or assigned by the employer "
         "as qualified to perform specific duties.",
         "That is the whole architecture in one sentence: the employer designates, in "
         "writing, scoped to named equipment and control modes."),
        ("The Certification Gate",
         "On the non-permanently-installed construction branch the operator requirement is "
         "different: a certified operator under the Subpart CC operator certification "
         "section.",
         "Two branches, two gates. Knowing which one you are standing on is the point of "
         "this module."),
        ("Roles are distinct",
         "Designated personnel operate. An <b>appointed person</b> carries defined "
         "inspection and approval duties. Maintenance qualified persons adjust and repair.",
         "Undocumented roles produce blurred accountability, which is what makes an "
         "incident investigation go badly for everyone in it."),
    ],
}

SECTIONS = [
    ("A", "Equipment Identification and Classification",
     "Identify overhead and gantry crane types and configurations and their operational "
     "characteristics."),
    ("B", "Jurisdictional Determination",
     "Determine which federal regime governs a specific crane based on installation status "
     "and work context."),
    ("C", "Roles, Qualification Architecture, and Standard of Care",
     "Explain who qualifies the operator, what the designation covers, and the operator's "
     "standard of care."),
]


def opt_html(qnum, opts, fbid):
    rows = []
    for i, o in enumerate(opts):
        rows.append(
            '        <button class="quiz-option" '
            "onclick=\"cqAnswer(this,'%s_q%02d',%d,'%s')\">%s</button>"
            % (MODULE, qnum, i, fbid, o))
    return "\n".join(rows)


def question_slide(sid, qnum, element, stem, opts, correct, rationale, gated):
    fbid = "fb%02d" % qnum
    tag = ("GATE &#183; counts toward your 100%%" if gated
           else "PRACTICE &#183; not scored")
    letter = "ABCD"[correct]
    fb = "Correct answer: %s. %s" % (letter, rationale) if rationale else \
         "Correct answer: %s." % letter
    return """  <section class="slide" id="s%d">
    <div class="kicker">%s</div>
    <div class="elem">%s</div>
    <h2>Question %d</h2>
    <p class="stem">%s</p>
    <div class="quiz-group">
%s
    </div>
    <div class="quiz-feedback" id="%s">%s</div>
  </section>""" % (sid, tag, element, qnum, stem, opt_html(qnum, opts, fbid), fbid, fb)


def content_slide(sid, kicker, title, body, note):
    return """  <section class="slide" id="s%d">
    <div class="kicker">%s</div>
    <h2>%s</h2>
    <p>%s</p>
    <div class="note">%s</div>
  </section>""" % (sid, kicker, title, body, note)


def build():
    S = []
    sid = 0

    def add(html_):
        return html_

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="kicker">OCO301C &#183; Overhead Crane Operator</div>
    <h1>Module 1<br>Equipment Types, Configurations,<br>and Jurisdictional Framework</h1>
    <p class="lede">Determine the equipment class, installation status, and governing
    regulatory regime for any overhead or gantry crane before operation.</p>
  </section>""" % sid)

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="kicker">Objectives</div>
    <h2>What you will be able to do</h2>
    <ul>
      <li>Identify overhead and gantry crane types, girder configurations and trolley
          arrangements, and name the governing consensus volume for each.</li>
      <li>Walk the installation-status decision tree and state the governing regime for a
          given crane.</li>
      <li>Explain who qualifies the operator, what a designation covers, and where your
          own authority begins and ends.</li>
    </ul>
  </section>""" % sid)

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="kicker">How this module gates</div>
    <h2>Practice, then the gate</h2>
    <p>Nine practice questions run alongside the content. They are not scored and they
    show you the correct answer.</p>
    <p>The <b>Final Knowledge Check</b> that follows is the gate. It requires
    <b>100%%</b> &#8212; every gated answer must be correct. A missed gate question is not
    revealed; you review and retest.</p>
    <div class="note">Your live gate score appears in the chip at the top of the screen
    once the final check begins.</div>
  </section>""" % sid)

    pi = 0
    for code, title, objective in SECTIONS:
        sid += 1
        S.append("""  <section class="slide section-header" id="s%d">
    <div class="kicker">Task %s</div>
    <h1>%s</h1>
    <p class="lede">%s</p>
  </section>""" % (sid, code, title, objective))

        for t, b, n in CONTENT[code]:
            sid += 1
            S.append(content_slide(sid, "Task %s" % code, t, b, n))

        for _ in range(3):
            q = PRACTICE[pi]
            pi += 1
            sid += 1
            S.append(question_slide(sid, pi, q[1], q[2], q[3], q[4], q[5], False))

    sid += 1
    S.append("""  <section class="slide divider" id="s%d">
    <div class="kicker">Assessment</div>
    <h1>Final Knowledge Check</h1>
    <p class="lede">Twenty-four questions. This gate requires 100%% &#8212; every answer
    must be correct before the module can be completed.</p>
    <div class="note">Missed questions are listed for review by number. The correct
    option is not shown.</div>
  </section>""" % sid)

    for gi, q in enumerate(GATE):
        sid += 1
        S.append(question_slide(sid, len(PRACTICE) + 1 + gi, q[1], q[2], q[3], q[4], q[5], True))

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <h1>Module 1 complete</h1>
    <div class="completion-panel">
      <div id="score-summary">Complete the knowledge check to record this module.</div>
      <div id="review-list"></div>
    </div>
  </section>""" % sid)

    total = sid
    slides = "\n".join(S)

    tpl = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>OCO301C Module 1 &#8212; Equipment Types, Configurations, and Jurisdictional Framework</title>
<style>
:root{--navy:#1B3464;--gold:#C8991A;--ink:#0d1522;--paper:#f5f6f8;--line:#2b4478;}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;font-family:Calibri,"Segoe UI",system-ui,sans-serif;background:var(--ink);
     color:var(--paper);overflow:hidden}
#stage{position:relative;height:100dvh;width:100vw}
.slide{position:absolute;inset:0;padding:28px 22px 92px;overflow-y:auto;
       -webkit-overflow-scrolling:touch;opacity:0;pointer-events:none;
       transition:opacity .28s ease;background:linear-gradient(160deg,#111a2c,#0d1522)}
.slide.active{opacity:1;pointer-events:auto}
.slide.section-header,.slide.divider{background:linear-gradient(160deg,var(--navy),#12203c)}
h1{font-size:1.55rem;line-height:1.25;margin:.2em 0 .5em;color:#fff}
h2{font-size:1.25rem;margin:.2em 0 .6em;color:var(--gold)}
p{line-height:1.55;margin:0 0 .9em}
ul{line-height:1.55;padding-left:1.1em}
li{margin-bottom:.5em}
.lede{font-size:1.05rem;color:#cfd6e4}
.kicker{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);
        margin-bottom:.6em;font-weight:700}
.elem{font-size:.68rem;letter-spacing:.06em;color:#7d8ba6;margin-bottom:.5em;
      font-family:ui-monospace,Menlo,Consolas,monospace}
.note{border-left:3px solid var(--gold);padding:.6em .9em;background:#16203a;
      border-radius:0 6px 6px 0;font-size:.95rem;color:#cfd6e4}
.stem{font-size:1.05rem;color:#fff}
.quiz-group{display:flex;flex-direction:column;gap:10px;margin:1em 0}
.quiz-option{display:block;width:100%;text-align:left;padding:14px 16px;font-size:1rem;
             font-family:inherit;color:var(--paper);background:#16203a;
             border:1px solid var(--line);border-radius:10px;cursor:pointer}
.quiz-option:active{transform:scale(.995)}
.quiz-option.correct{border-color:#2f9e64;background:#12301f}
.quiz-option.wrong{border-color:#b4442f;background:#301513}
.quiz-feedback{display:none;margin-top:.4em;padding:.7em .9em;border-radius:8px;
               background:#16203a;font-size:.95rem;color:#cfd6e4}
.quiz-feedback.show{display:block}
.completion-panel{background:#16203a;border:1px solid var(--line);border-radius:12px;
                  padding:18px;margin-top:1em}
.review-item{padding:.5em 0;border-bottom:1px solid var(--line);font-size:.95rem}
.calc-btn{display:inline-block;width:100%;padding:14px 18px;font-size:1rem;
          font-family:inherit;font-weight:700;color:#12203c;background:var(--gold);
          border:0;border-radius:10px;cursor:pointer}
#chrome{position:fixed;left:0;right:0;bottom:0;display:flex;align-items:center;gap:12px;
        padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:#0b1220;
        border-top:1px solid var(--line)}
#chrome button{padding:10px 16px;font-size:.95rem;font-family:inherit;color:var(--paper);
               background:#16203a;border:1px solid var(--line);border-radius:8px}
#counter{font-size:.85rem;color:#7d8ba6;margin-left:auto}
#score-chip{position:fixed;top:calc(8px + env(safe-area-inset-top));right:12px;
            padding:6px 12px;font-size:.78rem;font-weight:700;letter-spacing:.05em;
            color:#12203c;background:var(--gold);border-radius:999px;z-index:20}
#cq-gatebar{display:none;position:fixed;left:12px;right:12px;
            bottom:calc(66px + env(safe-area-inset-bottom));padding:12px 14px;
            background:#16203a;border:1px solid var(--gold);border-radius:10px;
            font-size:.92rem;color:#fff;z-index:20}
#cq-gatebtn{display:none;margin-top:10px;padding:10px 16px;font-family:inherit;
            font-weight:700;color:#12203c;background:var(--gold);border:0;border-radius:8px}
</style>
</head>
<body data-cq-module="@@MODULE@@" data-cq-total="@@TOTAL@@" data-cq-gate="OHC-1" data-cq-course="OCO301C">

<div id="score-chip">GATE 0 / 24</div>
<div id="stage">
@@SLIDES@@
</div>

<div id="cq-gatebar">
  <div id="cq-gatemsg"></div>
  <button id="cq-gatebtn"></button>
</div>

<div id="chrome">
  <button onclick="navigate(-1)">Back</button>
  <button onclick="navigate(1)">Next</button>
  <span id="counter"></span>
</div>

<script>
var TOTAL=@@TOTAL@@, current=1;
function render(){
  var i;
  for(i=1;i<=TOTAL;i++){
    var el=document.getElementById('s'+i);
    if(el) el.classList.toggle('active', i===current);
  }
  var c=document.getElementById('counter');
  if(c) c.textContent=current+' / '+TOTAL;
  var st=document.getElementById('stage'); if(st) st.scrollTop=0;
}
window.jumpTo=function(n){
  if(n<1||n>TOTAL) return false;
  current=n; render(); return true;
};
window.navigate=function(dir){
  var t=current+dir;
  if(t<1||t>TOTAL) return false;
  current=t; render(); return true;
};
document.addEventListener('keydown',function(e){
  if(e.key==='ArrowRight') navigate(1);
  if(e.key==='ArrowLeft') navigate(-1);
});
window.cqAnswer=function(){};
render();
</script>
<script src="cq-module-bridge.js"></script>
</body>
</html>
"""
    return (tpl.replace("@@MODULE@@", MODULE)
               .replace("@@TOTAL@@", str(total))
               .replace("@@SLIDES@@", slides))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "..", "out",
                       "OHC_M01_EquipmentAndJurisdiction.pre.html")
    out = os.path.abspath(out)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out):
        os.remove(out)
    html = build()
    with open(out, "w", encoding="ascii") as f:
        f.write(html)
    print("wrote %s (%d bytes)" % (out, len(html)))
