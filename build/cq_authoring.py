#!/usr/bin/env python3
"""Shared authoring scaffold for OCO301C modules.

Emits the pre-retrofit DOM expected by cq_module_kit.py:
  <body data-cq-module data-cq-total>, <section class="slide" id="sN">,
  cqAnswer(this,'<MOD>_qNN',IDX,'fbNN') onclicks, plaintext feedback keys
  (stripped by retrofit), a Final Knowledge Check divider, .completion-panel,
  #score-chip, and the cq-module-bridge.js anchor the gate engine inserts after.

ASCII-only source; non-ASCII reaches the HTML as entities.
"""

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>OCO301C @@MODLABEL@@ &#8212; @@TITLE@@</title>
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

<div id="score-chip">GATE 0 / @@NGATE@@</div>
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


def opt_html(module, qnum, opts, fbid):
    rows = []
    for i, o in enumerate(opts):
        rows.append(
            '        <button class="quiz-option" '
            "onclick=\"cqAnswer(this,'%s_q%02d',%d,'%s')\">%s</button>"
            % (module, qnum, i, fbid, o))
    return "\n".join(rows)


def question_slide(module, sid, qnum, element, stem, opts, correct, rationale, gated):
    fbid = "fb%02d" % qnum
    tag = ("GATE &#183; counts toward your 100&#37;" if gated
           else "PRACTICE &#183; not scored")
    letter = "ABCD"[correct]
    fb = ("Correct answer: %s. %s" % (letter, rationale)) if rationale else \
         ("Correct answer: %s." % letter)
    return """  <section class="slide" id="s%d">
    <div class="kicker">%s</div>
    <div class="elem">%s</div>
    <h2>Question %d</h2>
    <p class="stem">%s</p>
    <div class="quiz-group">
%s
    </div>
    <div class="quiz-feedback" id="%s">%s</div>
  </section>""" % (sid, tag, element, qnum, stem,
                   opt_html(module, qnum, opts, fbid), fbid, fb)


def content_slide(sid, kicker, title, body, note):
    return """  <section class="slide" id="s%d">
    <div class="kicker">%s</div>
    <h2>%s</h2>
    <p>%s</p>
    <div class="note">%s</div>
  </section>""" % (sid, kicker, title, body, note)


def section_header(sid, code, title, objective):
    return """  <section class="slide section-header" id="s%d">
    <div class="kicker">Task %s</div>
    <h1>%s</h1>
    <p class="lede">%s</p>
  </section>""" % (sid, code, title, objective)


def assemble(module, modlabel, title, subtitle, objectives, gate_count,
             sections, content, practice, gate):
    """Build the full pre-retrofit HTML. Question numbers derive from list
    position, so inserting an element renumbers everything automatically."""
    S = []
    sid = 0

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="kicker">OCO301C &#183; Overhead Crane Operator</div>
    <h1>%s<br>%s</h1>
    <p class="lede">%s</p>
  </section>""" % (sid, modlabel, title, subtitle))

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="kicker">Objectives</div>
    <h2>What you will be able to do</h2>
    <ul>
%s
    </ul>
  </section>""" % (sid, "\n".join("      <li>%s</li>" % o for o in objectives)))

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="kicker">How this module gates</div>
    <h2>Practice, then the gate</h2>
    <p>%d practice questions run alongside the content. They are not scored and they
    show you the correct answer.</p>
    <p>The <b>Final Knowledge Check</b> that follows is the gate. It requires
    <b>100&#37;</b> &#8212; every gated answer must be correct. A missed gate question is
    not revealed; you review and retest.</p>
    <div class="note">Your live gate score appears in the chip at the top of the screen
    once the final check begins.</div>
  </section>""" % (sid, len(practice)))

    pi = 0
    for code, sec_title, objective in sections:
        sid += 1
        S.append(section_header(sid, code, sec_title, objective))
        for t, b, n in content[code]:
            sid += 1
            S.append(content_slide(sid, "Task %s" % code, t, b, n))
        for _ in range(3):
            q = practice[pi]
            pi += 1
            sid += 1
            S.append(question_slide(module, sid, pi, q[0], q[1], q[2], q[3], q[4], False))

    sid += 1
    S.append("""  <section class="slide divider" id="s%d">
    <div class="kicker">Assessment</div>
    <h1>Final Knowledge Check</h1>
    <p class="lede">%d questions. This gate requires 100&#37; &#8212; every answer must be
    correct before the module can be completed.</p>
    <div class="note">Missed questions are listed for review by number. The correct
    option is not shown.</div>
  </section>""" % (sid, gate_count))

    for gi, q in enumerate(gate):
        sid += 1
        S.append(question_slide(module, sid, len(practice) + 1 + gi,
                                q[0], q[1], q[2], q[3], q[4], True))

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <h1>%s complete</h1>
    <div class="completion-panel">
      <div id="score-summary">Complete the knowledge check to record this module.</div>
      <div id="review-list"></div>
    </div>
  </section>""" % (sid, modlabel))

    total = sid
    return (SHELL.replace("@@MODULE@@", module)
                 .replace("@@MODLABEL@@", modlabel)
                 .replace("@@TITLE@@", title)
                 .replace("@@TOTAL@@", str(total))
                 .replace("@@NGATE@@", str(gate_count))
                 .replace("@@SLIDES@@", "\n".join(S)))
