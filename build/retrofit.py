#!/usr/bin/env python3
"""Retrofit a pre.html module into a gated HTML file.

Replaces plaintext quiz-feedback answer keys with FNV-1a hashes and installs
the CraneQualified KC Gate Engine (local shim when platform CQ is absent).
"""
from __future__ import annotations

import json
import os
import re
import sys


def fnv1a(s: str) -> str:
    h = 0x811C9DC5
    for ch in s:
        h ^= ord(ch)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return "%08x" % h


ENGINE = r"""<script>
/* ============================================================
   CraneQualified KC Gate Engine v1  (Stage OHC / @@MODULE@@)
   Server-authoritative; installs a local FNV-1a shim ONLY if the
   platform has not defined window.CQ. Answers are stored as FNV-1a
   hashes, never plaintext, and the correct option is never revealed
   on a gate miss. Gate = the final knowledge-check questions at 100%. Forward navigation
   to the completion slide is locked until the gate passes.
   ============================================================ */
(function(){
"use strict";
var SALT=@@SALT@@;
var HASHES=@@HASHES@@;
var GATE=@@GATE@@;
var GATESET=new Set(GATE);
var LOCK_AFTER=@@LOCK_AFTER@@;
var gatePassed=false, answered={}, gateOK={};

function fnv(s){var h=0x811c9dc5;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,0x01000193)>>>0;}return ('0000000'+h.toString(16)).slice(-8);}

if(!window.CQ){
  window.CQ={
    scoreAnswer:function(qid,idx){
      var correct=fnv(SALT+':'+qid+':'+idx)===HASHES[qid];
      var isGate=GATESET.has(qid), out={correct:correct};
      if(!isGate){
        for(var i=0;i<4;i++){ if(fnv(SALT+':'+qid+':'+i)===HASHES[qid]){out.correctIndex=i;break;} }
        out.feedbackHtml = correct ? 'Correct.' : 'Not correct \u2014 the correct option is now highlighted. Review the reasoning, then continue.';
      } else {
        out.feedbackHtml = correct ? 'Correct.' : 'Not correct. This gate requires 100% \u2014 the correct answer is not shown. Review the module and retest.';
      }
      return Promise.resolve(out);
    },
    requestComplete:function(){
      var right=0,i; for(i=0;i<GATE.length;i++){ if(gateOK[GATE[i]]) right++; }
      var passed=right===GATE.length, score=right+' / '+GATE.length;
      if(passed){ gatePassed=true; setTimeout(function(){ document.dispatchEvent(new CustomEvent('cq-complete',{detail:{completionId:'local-'+Date.now()}})); },300); }
      return Promise.resolve({passed:passed,score:score});
    },
    ack:function(){}
  };
}
document.addEventListener('cq-complete',function(){ gatePassed=true; });

function bar(){return document.getElementById('cq-gatebar');}
function btn(){return document.getElementById('cq-gatebtn');}
function msg(t){var m=document.getElementById('cq-gatemsg'); if(m)m.textContent=t; var b=bar(); if(b)b.style.display='block';}
function gateRight(){var r=0,i;for(i=0;i<GATE.length;i++)if(gateOK[GATE[i]])r++;return r;}
function chip(){var c=document.getElementById('score-chip'); if(c) c.textContent='GATE '+gateRight()+' / '+GATE.length;}
function blocked(n){ return (!gatePassed) && (n>LOCK_AFTER); }

window.cqAnswer=function(el,qid,idx,fbid){
  if(answered[qid] && GATESET.has(qid) && gateOK[qid]) return;
  CQ.scoreAnswer(qid,idx).then(function(res){
    var group=el.parentNode, opts=group?group.querySelectorAll('.quiz-option'):[];
    var i, fb=document.getElementById(fbid);
    for(i=0;i<opts.length;i++){ opts[i].classList.remove('correct','wrong'); }
    if(res.correct){
      el.classList.add('correct');
      answered[qid]=true;
      if(GATESET.has(qid)) gateOK[qid]=true;
      if(fb){ fb.textContent=res.feedbackHtml||'Correct.'; fb.classList.add('show'); }
    } else {
      el.classList.add('wrong');
      if(!GATESET.has(qid) && typeof res.correctIndex==='number' && opts[res.correctIndex]){
        opts[res.correctIndex].classList.add('correct');
      }
      if(fb){ fb.textContent=res.feedbackHtml||'Not correct.'; fb.classList.add('show'); }
    }
    chip();
    var done=gateRight()===GATE.length;
    if(done){
      msg('Gate complete — 100%. You may finish the module.');
      var b=btn(); if(b){ b.style.display='inline-block'; b.textContent='Complete module'; b.onclick=function(){ CQ.requestComplete().then(function(r){ if(r.passed && typeof window.jumpTo==='function') window.jumpTo(LOCK_AFTER+1); }); }; }
    }
  });
};

if(typeof window.navigate==='function'){
  var _nav=window.navigate;
  window.navigate=function(dir){
    var tgt=(typeof current!=='undefined'?current:1)+dir;
    if(blocked(tgt)){ msg('Pass the knowledge check (100%) before completing the module.'); if(typeof window.jumpTo==='function')window.jumpTo(LOCK_AFTER); return; }
    return _nav(dir);
  };
}
if(typeof window.jumpTo==='function'){
  var _jmp=window.jumpTo;
  window.jumpTo=function(n){ if(blocked(n)){ msg('Pass the knowledge check (100%) before completing the module.'); return _jmp(LOCK_AFTER); } return _jmp(n); };
}

window.addEventListener('load',function(){
  if(window.CQ&&CQ.start){try{CQ.start();}catch(e){}}
  if(window.CQ&&CQ.slide){ var _n2=window.navigate; window.navigate=function(d){var rr=_n2(d); try{CQ.slide(current,TOTAL);}catch(e){} return rr;}; }
  chip();
});
})();
</script>
"""


def strip_feedback(html: str) -> str:
    """Blank gate/practice feedback bodies so answers are not in plaintext."""
    return re.sub(
        r'(<div class="quiz-feedback" id="fb\d+">)(.*?)(</div>)',
        r'\1\3',
        html,
        flags=re.S,
    )


def retrofit(pre_path: str, manifest_path: str, out_path: str) -> None:
    man = json.load(open(manifest_path, encoding="utf-8"))
    html = open(pre_path, encoding="utf-8").read()
    salt = man["salt"]
    answer_key = man["answer_key"]
    gate = man["gate"]
    total = man["total"]
    lock_after = total - 1  # completion slide blocked until gate passes

    hashes = {qid: fnv1a("%s:%s:%d" % (salt, qid, idx))
              for qid, idx in answer_key.items()}

    html = strip_feedback(html)
    # Ensure score chip uses live gate length
    html = re.sub(
        r'(id="score-chip">GATE 0 / )\d+',
        r'\g<1>%d' % len(gate),
        html,
    )

    engine = (ENGINE
              .replace("@@MODULE@@", man["module"])
              .replace("@@SALT@@", json.dumps(salt))
              .replace("@@HASHES@@", json.dumps(hashes, separators=(", ", ": ")))
              .replace("@@GATE@@", json.dumps(gate))
              .replace("@@LOCK_AFTER@@", str(lock_after)))

    if "CraneQualified KC Gate Engine" in html:
        html = re.sub(
            r'<script>\s*/\* =+.*?CraneQualified KC Gate Engine.*?</script>\s*\Z',
            engine,
            html,
            flags=re.S,
        )
    else:
        if html.rstrip().endswith("</html>"):
            html = html.rstrip()[:-7] + engine + "\n</html>\n"
        else:
            html = html + "\n" + engine

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("retrofit %s -> %s (%d hashes, gate %d, lock_after %d)"
          % (pre_path, out_path, len(hashes), len(gate), lock_after))


def main(argv):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if len(argv) < 2:
        print("usage: retrofit.py M01 [M02 ...]|all")
        return 2
    targets = argv[1:]
    if targets == ["all"]:
        targets = ["M%02d" % i for i in range(1, 13)]
    mapping = {
        "M01": "OHC_M01_EquipmentAndJurisdiction",
        "M02": "OHC_M02_ComponentsAndSystems",
        "M03": "OHC_M03_ControlsAndOperatingModes",
        "M04": "OHC_M04_RatedLoadAndWeight",
        "M05": "OHC_M05_InspectionRegime",
        "M06": "OHC_M06_RiggingInterface",
        "M07": "OHC_M07_LoadHandling",
        "M08": "OHC_M08_OperationalRules",
        "M09": "OHC_M09_CommunicationAndSignals",
        "M10": "OHC_M10_EnvironmentalHazards",
        "M11": "OHC_M11_MalfunctionsAndEmergencies",
        "M12": "OHC_M12_Capstone",
    }
    for t in targets:
        key = t if t.startswith("M") else "M" + t
        stem = mapping[key]
        man = os.path.join(root, "manifests", "OHC_%s.json" % key)
        pre = os.path.join(root, "out", stem + ".pre.html")
        out = os.path.join(root, "out", stem + ".html")
        retrofit(pre, man, out)


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
