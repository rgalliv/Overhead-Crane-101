#!/usr/bin/env python3
"""Shared authoring scaffold for OCO301C modules.

Emits the pre-retrofit DOM expected by retrofit.py / cq_module_kit:
  <body data-cq-module data-cq-total>, <section class="slide" id="sN">,
  cqAnswer(this,'<MOD>_qNN',IDX,'fbNN') onclicks, plaintext feedback keys
  (stripped by retrofit), a Final Knowledge Check divider, .completion-panel,
  #score-chip, and the cq-module-bridge.js anchor the gate engine inserts after.

ASCII-only source; non-ASCII reaches the HTML as entities.
Visual pack (2026-08): hero media, decision trees, flip cards, motion.
"""
from __future__ import annotations

import base64
import os

_ASSET_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "assets", "images")
_DATA_URI_CACHE = {}


def data_uri(filename: str) -> str:
    """Inline a JPEG/PNG from assets/images as a data URI (self-contained modules)."""
    if filename in _DATA_URI_CACHE:
        return _DATA_URI_CACHE[filename]
    path = os.path.join(_ASSET_DIR, filename)
    raw = open(path, "rb").read()
    mime = "image/jpeg" if filename.lower().endswith((".jpg", ".jpeg")) else "image/png"
    uri = "data:%s;base64,%s" % (mime, base64.b64encode(raw).decode("ascii"))
    _DATA_URI_CACHE[filename] = uri
    return uri


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>OCO301C @@MODLABEL@@ &#8212; @@TITLE@@</title>
<style>
:root{
  --navy:#1B3464;--gold:#C8991A;--ink:#0d1522;--paper:#f5f6f8;--line:#2b4478;
  --ok:#2f9e64;--bad:#b4442f;--mist:#cfd6e4;--panel:#16203a;--glow:rgba(200,153,26,.35);
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;font-family:"Source Sans 3",Calibri,"Segoe UI",system-ui,sans-serif;
     background:var(--ink);color:var(--paper);overflow:hidden}
#stage{position:relative;height:100dvh;width:100vw}
.slide{position:absolute;inset:0;padding:28px 22px 92px;overflow-y:auto;
       -webkit-overflow-scrolling:touch;opacity:0;pointer-events:none;
       transition:opacity .35s ease, transform .35s ease;
       transform:translateY(8px);
       background:
         radial-gradient(1200px 500px at 10% -10%, rgba(27,52,100,.55), transparent 60%),
         linear-gradient(160deg,#111a2c,#0d1522 55%,#0a101c)}
.slide.active{opacity:1;pointer-events:auto;transform:translateY(0)}
.slide.section-header,.slide.divider{
  background:linear-gradient(160deg,var(--navy),#12203c 70%,#0d1522)}
.slide.hero{padding:0 0 92px;display:flex;flex-direction:column}
.hero-media{position:relative;flex:0 0 46vh;min-height:220px;overflow:hidden}
.hero-media img{width:100%;height:100%;object-fit:cover;display:block;
  animation:heroKen 18s ease-in-out infinite alternate}
.hero-media::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(13,21,34,.15),rgba(13,21,34,.92) 78%)}
.hero-copy{padding:18px 22px 8px;position:relative;z-index:1;margin-top:-48px}
@keyframes heroKen{from{transform:scale(1.04)}to{transform:scale(1.12)}}
@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
.slide.active .rise{animation:rise .55s ease both}
.slide.active .rise.d1{animation-delay:.08s}
.slide.active .rise.d2{animation-delay:.16s}
.slide.active .rise.d3{animation-delay:.24s}
h1{font-size:1.55rem;line-height:1.25;margin:.2em 0 .5em;color:#fff;
   font-family:Georgia,"Source Serif 4",serif;letter-spacing:-.01em}
h2{font-size:1.25rem;margin:.2em 0 .6em;color:var(--gold)}
p{line-height:1.55;margin:0 0 .9em}
ul{line-height:1.55;padding-left:1.1em}
li{margin-bottom:.5em}
.lede{font-size:1.05rem;color:var(--mist)}
.kicker{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);
        margin-bottom:.6em;font-weight:700}
.elem{font-size:.68rem;letter-spacing:.06em;color:#7d8ba6;margin-bottom:.5em;
      font-family:ui-monospace,Menlo,Consolas,monospace}
.note{border-left:3px solid var(--gold);padding:.6em .9em;background:var(--panel);
      border-radius:0 6px 6px 0;font-size:.95rem;color:var(--mist)}
.stem{font-size:1.05rem;color:#fff}
.quiz-group{display:flex;flex-direction:column;gap:10px;margin:1em 0}
.quiz-option{display:block;width:100%;text-align:left;padding:14px 16px;font-size:1rem;
             font-family:inherit;color:var(--paper);background:var(--panel);
             border:1px solid var(--line);border-radius:10px;cursor:pointer;
             transition:border-color .15s, background .15s, transform .1s}
.quiz-option:hover{border-color:var(--gold)}
.quiz-option:active{transform:scale(.995)}
.quiz-option.correct{border-color:var(--ok);background:#12301f}
.quiz-option.wrong{border-color:var(--bad);background:#301513}
.quiz-feedback{display:none;margin-top:.4em;padding:.7em .9em;border-radius:8px;
               background:var(--panel);font-size:.95rem;color:var(--mist)}
.quiz-feedback.show{display:block}
.completion-panel{background:var(--panel);border:1px solid var(--line);border-radius:12px;
                  padding:18px;margin-top:1em}
.review-item{padding:.5em 0;border-bottom:1px solid var(--line);font-size:.95rem}
.calc-btn{display:inline-block;width:100%;padding:14px 18px;font-size:1rem;
          font-family:inherit;font-weight:700;color:#12203c;background:var(--gold);
          border:0;border-radius:10px;cursor:pointer}
.media-frame{margin:0 0 1em;border-radius:12px;overflow:hidden;border:1px solid var(--line);
  box-shadow:0 12px 40px rgba(0,0,0,.35);position:relative}
.media-frame img{width:100%;display:block;max-height:42vh;object-fit:cover}
.media-cap{font-size:.78rem;color:#7d8ba6;margin:.45em 0 0;letter-spacing:.04em}
.card-row{display:grid;grid-template-columns:1fr;gap:10px;margin:1em 0}
@media(min-width:720px){.card-row.cols-2{grid-template-columns:1fr 1fr}
.card-row.cols-3{grid-template-columns:1fr 1fr 1fr}}
.flip{perspective:900px;min-height:120px}
.flip-inner{position:relative;width:100%;min-height:120px;transform-style:preserve-3d;
  transition:transform .55s ease;cursor:pointer}
.flip.is-flipped .flip-inner{transform:rotateY(180deg)}
.flip-face{position:absolute;inset:0;backface-visibility:hidden;border-radius:12px;
  padding:14px 16px;border:1px solid var(--line);background:var(--panel)}
.flip-face.back{transform:rotateY(180deg);background:#1a2744;border-color:var(--gold)}
.flip-face h3{margin:0 0 .4em;font-size:1rem;color:var(--gold)}
.flip-face p{margin:0;font-size:.92rem;color:var(--mist)}
.tree{margin:1em 0;display:flex;flex-direction:column;gap:10px}
.tree-q{font-weight:700;color:#fff;margin-bottom:.2em}
.tree-opts{display:flex;flex-wrap:wrap;gap:8px}
.tree-opts button{flex:1 1 140px;padding:12px 14px;border-radius:10px;border:1px solid var(--line);
  background:var(--panel);color:var(--paper);font:inherit;cursor:pointer}
.tree-opts button:hover,.tree-opts button.active{border-color:var(--gold);box-shadow:0 0 0 1px var(--glow)}
.tree-result{display:none;padding:14px 16px;border-radius:12px;border:1px solid var(--gold);
  background:linear-gradient(135deg,#1a2744,#12203c);margin-top:.4em}
.tree-result.show{display:block;animation:rise .4s ease}
.tree-result strong{color:var(--gold)}
.chip-row{display:flex;flex-wrap:wrap;gap:8px;margin:.8em 0 1em}
.meta-chip{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;padding:6px 10px;
  border-radius:999px;border:1px solid var(--line);color:var(--mist);background:rgba(22,32,58,.8)}
.meta-chip.gold{border-color:var(--gold);color:var(--gold)}
.progress-rail{height:3px;background:#1a2744;border-radius:2px;overflow:hidden;margin:0 0 14px}
.progress-rail > span{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--gold),#e6c15a);
  transition:width .35s ease}
#chrome{position:fixed;left:0;right:0;bottom:0;display:flex;align-items:center;gap:12px;
        padding:10px 16px calc(10px + env(safe-area-inset-bottom));background:#0b1220;
        border-top:1px solid var(--line);backdrop-filter:blur(8px)}
#chrome button{padding:10px 16px;font-size:.95rem;font-family:inherit;color:var(--paper);
               background:var(--panel);border:1px solid var(--line);border-radius:8px}
#counter{font-size:.85rem;color:#7d8ba6;margin-left:auto}
#score-chip{position:fixed;top:calc(8px + env(safe-area-inset-top));right:12px;
            padding:6px 12px;font-size:.78rem;font-weight:700;letter-spacing:.05em;
            color:#12203c;background:var(--gold);border-radius:999px;z-index:20;
            box-shadow:0 0 24px var(--glow)}
#cq-gatebar{display:none;position:fixed;left:12px;right:12px;
            bottom:calc(66px + env(safe-area-inset-bottom));padding:12px 14px;
            background:var(--panel);border:1px solid var(--gold);border-radius:10px;
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
  var rail=document.querySelector('#s'+current+' .progress-rail > span');
  if(rail) rail.style.width=Math.round((current/TOTAL)*100)+'%';
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
window.cqFlip=function(el){ el.classList.toggle('is-flipped'); };
window.cqTree={};
window.cqTreePick=function(treeId, step, value, label){
  var t=window.cqTree[treeId]||(window.cqTree[treeId]={});
  t[step]=value;
  var root=document.getElementById(treeId);
  if(!root) return;
  var btns=root.querySelectorAll('[data-step=\"'+step+'\"]');
  for(var i=0;i<btns.length;i++){ btns[i].classList.toggle('active', btns[i].getAttribute('data-val')===value); }
  var next=root.querySelector('[data-show-after=\"'+step+'\"]');
  if(next){ next.style.display='block'; }
  if(typeof window['cqTreeResolve_'+treeId]==='function'){
    window['cqTreeResolve_'+treeId](t, root);
  }
};
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
    <div class="progress-rail"><span></span></div>
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


def content_slide(sid, kicker, title, body, note, image=None, caption=None):
    media = ""
    if image:
        media = (
            '<div class="media-frame rise">'
            '<img src="%s" alt="">'
            '</div>' % data_uri(image)
        )
        if caption:
            media += '<p class="media-cap">%s</p>' % caption
    return """  <section class="slide" id="s%d">
    <div class="progress-rail"><span></span></div>
    <div class="kicker">%s</div>
    <h2 class="rise">%s</h2>
    %s
    <p class="rise d1">%s</p>
    <div class="note rise d2">%s</div>
  </section>""" % (sid, kicker, title, media, body, note)


def hero_slide(sid, kicker, title, lede, image, chips=None):
    chip_html = ""
    if chips:
        chip_html = '<div class="chip-row rise d2">' + "".join(
            '<span class="meta-chip%s">%s</span>'
            % (" gold" if c.get("gold") else "", c["text"]) for c in chips
        ) + "</div>"
    return """  <section class="slide hero" id="s%d">
    <div class="hero-media"><img src="%s" alt=""></div>
    <div class="hero-copy">
      <div class="kicker rise">%s</div>
      <h1 class="rise d1">%s</h1>
      <p class="lede rise d2">%s</p>
      %s
    </div>
  </section>""" % (sid, data_uri(image), kicker, title, lede, chip_html)


def section_header(sid, code, title, objective):
    return """  <section class="slide section-header" id="s%d">
    <div class="progress-rail"><span></span></div>
    <div class="kicker">Task %s</div>
    <h1 class="rise">%s</h1>
    <p class="lede rise d1">%s</p>
  </section>""" % (sid, code, title, objective)


def flip_cards_slide(sid, kicker, title, cards):
    """cards: list of (front_title, front_body, back_title, back_body)"""
    parts = []
    for i, (ft, fb, bt, bb) in enumerate(cards):
        parts.append(
            '<div class="flip" onclick="cqFlip(this)">'
            '<div class="flip-inner">'
            '<div class="flip-face front"><h3>%s</h3><p>%s</p>'
            '<p class="media-cap">Tap to flip</p></div>'
            '<div class="flip-face back"><h3>%s</h3><p>%s</p></div>'
            '</div></div>' % (ft, fb, bt, bb)
        )
    cols = "cols-2" if len(cards) == 2 else ("cols-3" if len(cards) >= 3 else "")
    return """  <section class="slide" id="s%d">
    <div class="progress-rail"><span></span></div>
    <div class="kicker">%s</div>
    <h2 class="rise">%s</h2>
    <div class="card-row %s rise d1">
%s
    </div>
  </section>""" % (sid, kicker, title, cols, "\n".join(parts))


def na_jurisdiction_tree_slide(sid, kicker="Interactive", title="Walk the jurisdiction tree"):
    """Standalone interactive US/Canada jurisdiction picker (practice, not gated)."""
    return """  <section class="slide" id="s%d">
    <div class="progress-rail"><span></span></div>
    <div class="kicker">%s</div>
    <h2 class="rise">%s</h2>
    <p class="rise d1">Tap through the tree. This is unscored practice &#8212; the gate still tests the same decision.</p>
    <div class="tree rise d2" id="jtree">
      <div>
        <div class="tree-q">1. Where is the work?</div>
        <div class="tree-opts">
          <button type="button" id="jt_us" onclick="jtRegion('US')">United States</button>
          <button type="button" id="jt_ca" onclick="jtRegion('CA')">Canada</button>
        </div>
      </div>
      <div id="jt_step2" style="display:none;margin-top:10px">
        <div class="tree-q">2. Context</div>
        <div class="tree-opts" id="jt_opts2"></div>
      </div>
      <div class="tree-result" id="jt_result"></div>
    </div>
    <script>
    (function(){
      var region=null;
      var map={
        fac:['US Facility Branch','29 CFR 1910.179 direct. Designation Gate: only designated personnel may operate (&#167;1910.179(b)(8)). Controlling entity qualifies.'],
        con:['US Construction Branch','&#167;1926.1438(b) hybrid + &#167;1926.1427 Certification Gate. Enumerated 1910.179 paragraphs only.'],
        fed:['US Federal / USACE Layer','EM 385-1-1 Ch. 16 supplements the OSHA branch already in force. Class I / II tiers.'],
        fedca:['Canada — Federal workplaces','Canada Labour Code Part II / COHSR. Consensus spine: CSA B167. Employer authorizes competent workers in writing.'],
        on:['Canada — Ontario','OHSA + Reg. 851 / Reg. 213. Competent worker model; align to CSA B167 + site designation.'],
        bc:['Canada — British Columbia','WorkSafeBC OHS Regulation Part 14. Qualified operator + CSA B167 discipline.'],
        ab:['Canada — Alberta','OHS Code Part 6. Competent worker + CSA B167.'],
        qc:['Canada — Quebec','CNESST / LSST. Prefer French designation paperwork. CSA B167 + employer competency proof.']
      };
      function show(key){
        var m=map[key], el=document.getElementById('jt_result');
        if(!m||!el) return;
        el.innerHTML='<strong>'+m[0]+'</strong><p style="margin:.5em 0 0">'+m[1]+'</p>';
        el.classList.add('show');
      }
      window.jtRegion=function(r){
        region=r;
        document.getElementById('jt_us').classList.toggle('active', r==='US');
        document.getElementById('jt_ca').classList.toggle('active', r==='CA');
        var box=document.getElementById('jt_opts2');
        var wrap=document.getElementById('jt_step2');
        var res=document.getElementById('jt_result');
        res.classList.remove('show'); res.innerHTML='';
        wrap.style.display='block';
        if(r==='US'){
          box.innerHTML='<button type="button" onclick="jtCtx(\\x27fac\\x27)">Facility / general industry</button>'+
            '<button type="button" onclick="jtCtx(\\x27con\\x27)">Construction (non-permanent)</button>'+
            '<button type="button" onclick="jtCtx(\\x27fed\\x27)">Federal / USACE</button>';
        } else {
          box.innerHTML='<button type="button" onclick="jtCtx(\\x27fedca\\x27)">Federally regulated</button>'+
            '<button type="button" onclick="jtCtx(\\x27on\\x27)">Ontario</button>'+
            '<button type="button" onclick="jtCtx(\\x27bc\\x27)">British Columbia</button>'+
            '<button type="button" onclick="jtCtx(\\x27ab\\x27)">Alberta</button>'+
            '<button type="button" onclick="jtCtx(\\x27qc\\x27)">Quebec</button>';
        }
      };
      window.jtCtx=function(k){ show(k); };
    })();
    </script>
  </section>""" % (sid, kicker, title)


LAST_TOTAL = 0


def assemble(module, modlabel, title, subtitle, objectives, gate_count,
             sections, content, practice, gate, hero_image=None,
             extra_before_gate=None):
    """Build the full pre-retrofit HTML. Returns HTML string.

    content[code] entries may be 3-tuples (title, body, note) or 5-tuples
    (title, body, note, image, caption).
    """
    global LAST_TOTAL
    S = []
    sid = 0

    sid += 1
    if hero_image:
        S.append(hero_slide(
            sid,
            "OCO301C &#183; Overhead Crane Operator",
            "%s<br>%s" % (modlabel, title),
            subtitle,
            hero_image,
            chips=[{"text": "100% gate", "gold": True},
                   {"text": "US + Canada", "gold": False},
                   {"text": "Designation Gate", "gold": False}],
        ))
    else:
        S.append("""  <section class="slide" id="s%d">
    <div class="kicker">OCO301C &#183; Overhead Crane Operator</div>
    <h1>%s<br>%s</h1>
    <p class="lede">%s</p>
  </section>""" % (sid, modlabel, title, subtitle))

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="progress-rail"><span></span></div>
    <div class="kicker">Objectives</div>
    <h2 class="rise">What you will be able to do</h2>
    <ul class="rise d1">
%s
    </ul>
  </section>""" % (sid, "\n".join("      <li>%s</li>" % o for o in objectives)))

    sid += 1
    S.append("""  <section class="slide" id="s%d">
    <div class="progress-rail"><span></span></div>
    <div class="kicker">How this module gates</div>
    <h2 class="rise">Practice, then the gate</h2>
    <p class="rise d1">%d practice questions run alongside the content. They are not scored and they
    show you the correct answer.</p>
    <p class="rise d2">The <b>Final Knowledge Check</b> that follows is the gate. It requires
    <b>100&#37;</b> &#8212; every gated answer must be correct. A missed gate question is
    not revealed; you review and retest.</p>
    <div class="note rise d3">Your live gate score appears in the chip at the top of the screen
    once the final check begins.</div>
  </section>""" % (sid, len(practice)))

    pi = 0
    for code, sec_title, objective in sections:
        sid += 1
        S.append(section_header(sid, code, sec_title, objective))
        for entry in content[code]:
            if len(entry) == 5:
                t, b, n, img, cap = entry
            else:
                t, b, n = entry[:3]
                img = cap = None
            sid += 1
            S.append(content_slide(sid, "Task %s" % code, t, b, n, img, cap))
        remain = max(0, min(3, len(practice) - pi))
        for _ in range(remain):
            q = practice[pi]
            pi += 1
            sid += 1
            S.append(question_slide(module, sid, pi, q[0], q[1], q[2], q[3], q[4], False))

    while pi < len(practice):
        q = practice[pi]
        pi += 1
        sid += 1
        S.append(question_slide(module, sid, pi, q[0], q[1], q[2], q[3], q[4], False))

    if extra_before_gate:
        for block in extra_before_gate:
            sid += 1
            if callable(block):
                S.append(block(sid))
            else:
                S.append(block.replace("@@SID@@", str(sid)))

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

    LAST_TOTAL = sid
    return (SHELL.replace("@@MODULE@@", module)
                 .replace("@@MODLABEL@@", modlabel)
                 .replace("@@TITLE@@", title)
                 .replace("@@TOTAL@@", str(sid))
                 .replace("@@NGATE@@", str(gate_count))
                 .replace("@@SLIDES@@", "\n".join(S)))
