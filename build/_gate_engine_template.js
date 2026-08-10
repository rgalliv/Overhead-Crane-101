<script>
/* ============================================================
   CraneQualified KC Gate Engine v1  (Stage OHC / OHC_M02)
   Server-authoritative; installs a local FNV-1a shim ONLY if the
   platform has not defined window.CQ. Answers are stored as FNV-1a
   hashes, never plaintext, and the correct option is never revealed
   on a gate miss. Gate = the final knowledge-check questions at 100%. Forward navigation
   to the completion slide is locked until the gate passes.
   ============================================================ */
(function(){
"use strict";
var SALT="CQ1:OHC_M02_ComponentsAndSystems";
var HASHES={"OHC_M02_q01": "1c1ba8ca", "OHC_M02_q02": "7c8bd04b", "OHC_M02_q03": "726a1f14", "OHC_M02_q04": "fc1b9fed", "OHC_M02_q05": "e0a9194e", "OHC_M02_q06": "424051d2", "OHC_M02_q07": "b5b99198", "OHC_M02_q08": "0e4cd611", "OHC_M02_q09": "f1da4ddf", "OHC_M02_q10": "bc1600e4", "OHC_M02_q11": "c874e82e", "OHC_M02_q12": "e6c855ad", "OHC_M02_q13": "de3aa3a0", "OHC_M02_q14": "80a37168", "OHC_M02_q15": "8aec320f", "OHC_M02_q16": "2a54fb1e", "OHC_M02_q17": "45c781bd", "OHC_M02_q18": "92d4a78c", "OHC_M02_q19": "9e338d43", "OHC_M02_q20": "5a3a7d7a", "OHC_M02_q21": "2db45460", "OHC_M02_q22": "efd85ffc", "OHC_M02_q23": "d8a31296", "OHC_M02_q24": "7485c993", "OHC_M02_q25": "e927ad5c", "OHC_M02_q26": "af88f231", "OHC_M02_q27": "94166b92", "OHC_M02_q28": "627ba2df", "OHC_M02_q29": "56f5adb8", "OHC_M02_q30": "6a68a7e2", "OHC_M02_q31": "85db2e81", "OHC_M02_q32": "c0b71e2c", "OHC_M02_q33": "cad8cf63"};
var GATE=["OHC_M02_q10", "OHC_M02_q11", "OHC_M02_q12", "OHC_M02_q13", "OHC_M02_q14", "OHC_M02_q15", "OHC_M02_q16", "OHC_M02_q17", "OHC_M02_q18", "OHC_M02_q19", "OHC_M02_q20", "OHC_M02_q21", "OHC_M02_q22", "OHC_M02_q23", "OHC_M02_q24", "OHC_M02_q25", "OHC_M02_q26", "OHC_M02_q27", "OHC_M02_q28", "OHC_M02_q29", "OHC_M02_q30", "OHC_M02_q31", "OHC_M02_q32", "OHC_M02_q33"];
var GATESET=new Set(GATE);
var LOCK_AFTER=58;            /* completion slide (59) blocked until gate passes */
var gatePassed=false, answered={}, gateOK={};

function fnv(s){var h=0x811c9dc5;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,0x01000193)>>>0;}return ('0000000'+h.toString(16)).slice(-8);}

/* 1) Local CQ shim (platform can pre-define window.CQ and win) */
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

/* gate-bar + tracking helpers */
function bar(){return document.getElementById('cq-gatebar');}
function btn(){return document.getElementById('cq-gatebtn');}
function msg(t){var m=document.getElementById('cq-gatemsg'); if(m)m.textContent=t; var b=bar(); if(b)b.style.display='block';}
function gateRight(){var r=0,i;for(i=0;i<GATE.length;i++)if(gateOK[GATE[i]])r++;return r;}
function chip(){var c=document.getElementById('score-chip'); if(c)c.textContent='GATE '+gateRight()+' / '+GATE.length;}
function buildReview(passed,score){
  var sum=document.getElementById('score-summary'), list=document.getElementById('review-list');
  if(sum) sum.textContent = passed ? ('Knowledge check passed \u2014 '+score+' (100%).') : ('Gate score '+score+'. This gate requires 100%. Review the items below, then retest.');
  if(list){ list.innerHTML='';
    if(!passed){ var i; for(i=0;i<GATE.length;i++){ if(GATE[i] in gateOK && !gateOK[GATE[i]]){ var d=document.createElement('div'); d.className='review-item'; d.innerHTML='<b>Final Question '+(Number(GATE[i].match(/(\d+)$/)[1])-9)+'</b> - revisit this topic before retesting.'; list.appendChild(d); } } }
  }
}

/* 2) Answer handler (bound to existing cqAnswer(this,qid,idx,fbid) onclicks) */
window.cqAnswer=async function(b,qid,idx,fbid){
  if(answered[qid])return; answered[qid]=true;
  var grp=b.parentElement;
  grp.querySelectorAll('.quiz-option').forEach(function(o){o.disabled=true;o.style.pointerEvents='none';o.classList.remove('correct','wrong');});
  var r=await CQ.scoreAnswer(qid,idx);
  b.classList.add(r.correct?'correct':'wrong');
  var isGate=GATESET.has(qid), fb=fbid?document.getElementById(fbid):null;
  if(!isGate){
    if(!r.correct && typeof r.correctIndex==='number'){ var os=grp.querySelectorAll('.quiz-option'); if(os[r.correctIndex]) os[r.correctIndex].classList.add('correct'); }
    if(fb){ fb.textContent=r.feedbackHtml; fb.classList.add('show'); }
  } else {
    gateOK[qid]=r.correct;
    if(fb){ fb.textContent=r.feedbackHtml; fb.classList.add('show'); }
    chip();
    if(GATE.every(function(q){return q in gateOK;})) checkGate();
  }
};

async function checkGate(){
  msg('Submitting knowledge check...'); var bt=btn(); if(bt)bt.style.display='none';
  var r=await CQ.requestComplete();
  buildReview(r.passed,r.score);
  if(r.passed){ msg('Knowledge check passed ('+r.score+'). You may continue to completion.'); }
  else{ msg('Not yet - this gate requires 100%. Review the module, then retest.');
        if(bt){ bt.style.display='inline-block'; bt.textContent='Review and Retest'; bt.onclick=function(){location.reload();}; } }
}

document.addEventListener('cq-complete',function(){ msg('Module complete - recorded by the platform.'); var bt=btn(); if(bt)bt.style.display='none'; chip(); if(window.CQ&&CQ.ack)CQ.ack(); });
document.addEventListener('cq-denied',function(){ msg('Completion denied by the platform. Review and retest.'); });

/* 3) Forward navigation lock - completion slide (59) blocked until gate passes */
function blocked(t){ return !gatePassed && t>LOCK_AFTER; }
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

/* platform progress beacon + initial chip */
window.addEventListener('load',function(){
  if(window.CQ&&CQ.start){try{CQ.start();}catch(e){}}
  if(window.CQ&&CQ.slide){ var _n2=window.navigate; window.navigate=function(d){var rr=_n2(d); try{CQ.slide(current,TOTAL);}catch(e){} return rr;}; }
  chip();
});
})();
</script>