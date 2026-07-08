"""
Àmì — Beginner Onboarding (standalone)
----------------------------------------
Separate script, built to match the style of the main app.py (single
self-contained HTML/CSS/JS block rendered via components.html), so it can
be reviewed on its own and merged in later.

Flow:
  1. Title screen — just "Àmì", nothing else
  2. "New to Yorùbá?" choice (minimal, no long paragraph)
  3. Tone intro — what tone is, where it occurs, how it changes meaning,
     minimal pairs — then straight into a short practice exercise
  4. Stage 1 (one-syllable words) -> Stage 2 (two-syllable words) -> done

Author: Popoola Adesewa
Course: CLN 733 — Language Sound Systems, Group 3
"""

import json
import streamlit as st
import streamlit.components.v1 as components

# ---- settings you can edit -------------------------------------------------
GAME_NAME = "Àmì"
POINTS_CORRECT = 10
# ---------------------------------------------------------------------------

st.set_page_config(page_title=f"{GAME_NAME} — Getting Started", page_icon="🎵", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}
.block-container{padding:0 !important; max-width:720px !important;}
[data-testid="stAppViewContainer"]{background:#faf7f2;}
</style>
""", unsafe_allow_html=True)

# Practice items — separated from logic, same shape as the main app's
# questions.json so they can be merged into that file later.
STAGE1_ITEMS = [
    {
        "id": "s1_1",
        "sentence": "Ó ___ sí ilé.",
        "translation": "He/she ___ home.",
        "A": {"word": "wá", "meaning": "came"},
        "B": {"word": "wà", "meaning": "is / exists"},
        "correct": "A",
        "explanation": "wá (high tone) means 'came'. wà (low tone) means 'is/exists'. Same letters — only the pitch changes the meaning.",
    },
    {
        "id": "s1_2",
        "sentence": "Ẹyẹ náà ___.",
        "translation": "The bird ___.",
        "A": {"word": "fò", "meaning": "flew"},
        "B": {"word": "fó", "meaning": "broke"},
        "correct": "A",
        "explanation": "fò (low tone) means 'flew'. fó (high tone) means 'broke'. The context (a bird) tells you which one fits.",
    },
    {
        "id": "s1_3",
        "sentence": "Mo ní owó ___.",
        "translation": "I have ___ money.",
        "A": {"word": "kan", "meaning": "one / a certain amount"},
        "B": {"word": "kán", "meaning": "to be urgent"},
        "correct": "A",
        "explanation": "kan (mid tone) here means 'one/some'. kán (high tone) is a different word meaning 'to be urgent'.",
    },
]

STAGE2_ITEMS = [
    {
        "id": "s2_1",
        "sentence": "Ìyá mi ní ___ kan.",
        "translation": "My mother has one ___.",
        "A": {"word": "ọkọ", "meaning": "husband"},
        "B": {"word": "ọkọ̀", "meaning": "vehicle"},
        "correct": "A",
        "explanation": "ọkọ (mid-mid) means 'husband'. ọkọ̀ (mid-low) means 'vehicle'. Two syllables now — listen for which one shifts.",
    },
    {
        "id": "s2_2",
        "sentence": "A ja ___ ní àná.",
        "translation": "We fought a ___ yesterday.",
        "A": {"word": "ogun", "meaning": "war"},
        "B": {"word": "ọgún", "meaning": "twenty"},
        "correct": "A",
        "explanation": "ogun (mid-mid) means 'war'. ọgún (mid-high) means 'twenty'. Tone and vowel quality both matter here.",
    },
]

GAME_HTML = r'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>AMI Onboarding</title>
<style>
:root{--indigo:#1d2b53;--indigo2:#2c3e6b;--gold:#c8902a;--paper:#faf7f2;
--good:#2e7d5b;--bad:#b23a48;--ink:#222838;}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}
.wrap{max-width:680px;margin:0 auto;padding:24px 18px 70px;}
button{font-family:inherit;cursor:pointer;}
.btn{width:100%;border:1px solid var(--indigo);background:var(--indigo);color:#fff;
font-weight:700;border-radius:10px;padding:13px;font-size:1rem;margin-top:10px;}
.btn:hover{background:var(--indigo2);}
.btn.ghost{background:#fff;color:var(--indigo);}
.btn.gold{background:var(--gold);border-color:var(--gold);}
.btn:disabled{opacity:.45;cursor:default;}
.row{display:flex;gap:10px;}
.home{text-align:center;margin:4.5rem 0 2rem;}
.title{color:var(--indigo);font-weight:800;font-size:4.6rem;line-height:1;letter-spacing:-1px;margin:0;}
.h2{color:var(--indigo);font-weight:800;font-size:1.7rem;margin:.2rem 0 .7rem;}
.lead{color:#555;margin:0 0 8px;}
.meta{display:flex;justify-content:space-between;color:#6b7280;font-size:.85rem;margin:14px 0 6px;}
.bar{height:6px;background:#eadfce;border-radius:6px;overflow:hidden;margin-bottom:14px;}
.bar>i{display:block;height:100%;background:var(--gold);transition:width .3s;}
.sentence{background:#fff;border:1px solid #ece5d8;border-left:5px solid var(--gold);
border-radius:10px;padding:18px 20px;font-size:1.5rem;margin:.2rem 0;}
.hint{color:#6b7280;font-size:1.02rem;margin:8px 2px 16px;}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.card{background:#fff;border:2px solid #e6ded0;border-radius:12px;padding:18px 14px;text-align:center;cursor:pointer;transition:.15s;}
.card:hover{border-color:var(--indigo);}
.card.good{border-color:var(--good);background:#eaf5ef;}
.card.bad{border-color:var(--bad);background:#fbeef0;}
.card.lock{cursor:default;}
.word{font-size:2rem;font-weight:800;color:var(--indigo);}
.mean{color:#6b7280;font-size:.92rem;margin-top:4px;min-height:1.1em;}
.feed{margin-top:16px;padding:14px 16px;border-radius:10px;font-size:1.02rem;}
.feed.good{background:#eaf5ef;border-left:5px solid var(--good);color:#1c5a40;}
.feed.bad{background:#fbeef0;border-left:5px solid var(--bad);color:#7c2531;}
.lesson{background:#fff;border:1px solid #ece5d8;border-radius:10px;padding:6px 20px;line-height:1.65;}
.lesson li{margin:8px 0;}
.tonerow{display:flex;justify-content:center;gap:2.4rem;margin:1.4rem 0;}
.tonecell{text-align:center;}
.toneword{font-size:2.6rem;font-weight:800;color:var(--indigo);}
.tonelabel{color:#6b7280;font-size:.85rem;text-transform:uppercase;letter-spacing:.04em;margin-top:2px;}
.tonepitch{color:var(--gold);font-size:1rem;margin-top:2px;}
.muted{color:#6b7280;}
</style></head><body><div class="wrap"><div id="app"></div></div>
<script>
const NAME="__NAME__", PTS=__PTS__;
const S1=__S1__, S2=__S2__;
let stage=[], si=0, points=0;
const app=()=>document.getElementById("app");

// ---------- Page 1: title only ----------
function titlePage(){
app().innerHTML=`
<div class="home"><div class="title">${NAME}</div></div>
<button class="btn" onclick="checkLevel()">Start</button>`;
}

// ---------- Page 2: new to Yorùbá? ----------
function checkLevel(){
app().innerHTML=`
<div class="h2">Are you new to Yorùbá?</div>
<button class="btn" onclick="introTones()">Yes, I'm new</button>
<button class="btn ghost" onclick="doneOnboarding()">No, take me to the game</button>`;
}

// ---------- Tone intro: expanded ----------
function introTones(){
app().innerHTML=`
<div class="h2">Yorùbá tone</div>
<div class="lesson">
<p>Yorùbá is a <b>tonal language</b>: the pitch of your voice on a word is part of the word itself, the same way a consonant or a vowel is. Say the same letters with a different pitch, and you often get a completely different word.</p>
<p>There are three tones. Think of them like the notes <b>do &ndash; re &ndash; mi</b>:</p>
</div>
<div class="tonerow">
<div class="tonecell"><div class="toneword">à</div><div class="tonelabel">Low</div><div class="tonepitch">do</div></div>
<div class="tonecell"><div class="toneword">a</div><div class="tonelabel">Mid, no mark</div><div class="tonepitch">re</div></div>
<div class="tonecell"><div class="toneword">á</div><div class="tonelabel">High</div><div class="tonepitch">mi</div></div>
</div>
<div class="lesson">
<p><b>Where tone appears.</b> Tone is not just carried by vowels. It also appears on the syllabic nasal consonants <b>m</b> and <b>n</b> when they form their own syllable, as in <i>m&#768;</i> (I) or <i>n&#768;l&#7909;&#768;</i> (to be big). So when you're listening or reading for tone, watch vowels <i>and</i> these nasal syllables.</p>
<p><b>How tone changes meaning.</b> Two words can be spelled with the exact same letters and still mean entirely different things, because the tone marks are different. For example: <b>ọkọ</b> (husband), <b>ọkọ̀</b> (vehicle) &mdash; same letters, different tone, different word.</p>
<p><b>Minimal pairs.</b> A pair of words like that, identical except for one tone (or one vowel-quality dot), is called a <b>minimal pair</b>. That's exactly what this game trains you to notice: the smallest difference that changes meaning.</p>
</div>
<button class="btn" onclick="startStage(1)">Try a quick example →</button>`;
}

// ---------- Practice stages ----------
function startStage(n){
stage = n===1 ? S1 : S2;
si=0;
if(n===1) points=0;
playItem(n);
}

function playItem(stageNum){
const q=stage[si], N=stage.length;
const label = stageNum===1 ? "ONE-SYLLABLE WORDS" : "TWO-SYLLABLE WORDS";
function card(s){
let c="card"; if(q._answered){ c+=" lock"; if(s===q.correct) c+=" good"; else if(s===q._picked) c+=" bad"; }
const o=q[s];
return `<div class="${c}" data-s="${s}"><div class="word">${o.word}</div><div class="mean">${(q._answered)?o.meaning:""}</div></div>`;
}
let feed="";
if(q._answered){
const ok=q._picked===q.correct;
feed=`<div class="feed ${ok?'good':'bad'}">${ok?'\u2713 Correct. ':'\u2717 Not quite. The answer is <b>'+q[q.correct].word+'</b>. '}${q.explanation}</div>
<button class="btn" onclick="nextItem(${stageNum})">${(si===N-1)?'Continue':'Next'} →</button>`;
}
app().innerHTML=`
<div class="meta"><span>${label} &middot; ${si+1} of ${N}</span></div>
<div class="bar"><i style="width:${(si+1)/N*100}%"></i></div>
<div class="sentence">${q.sentence}</div>
<div class="hint">💬 ${q.translation}</div>
<div class="opts">${card("A")}${card("B")}</div>
${feed}`;
if(!q._answered){
app().querySelectorAll(".card").forEach(c=>c.onclick=()=>{
q._answered=true; q._picked=c.dataset.s;
if(c.dataset.s===q.correct) points+=PTS;
playItem(stageNum);
});
}
}

function nextItem(stageNum){
si++;
if(si>=stage.length){
if(stageNum===1){ startStage(2); }
else { stageComplete(); }
} else {
playItem(stageNum);
}
}

function stageComplete(){
const total = S1.length + S2.length;
app().innerHTML=`
<div class="h2">You're ready 🎉</div>
<div class="sentence">Score: <b>${points} points</b> across ${total} practice words.
<br><span class="muted">You've practiced spotting tone on one- and two-syllable words. The main game moves into full sentences, and sometimes vowel-quality contrasts too.</span></div>
<button class="btn" onclick="doneOnboarding()">Enter the main game →</button>
<button class="btn ghost" onclick="titlePage()">↺ Restart</button>`;
}

function doneOnboarding(){
app().innerHTML=`<div class="h2">Handoff point</div>
<div class="lesson">This is where onboarding ends and the main Àmì game's <code>home()</code> screen takes over.</div>
<button class="btn ghost" onclick="titlePage()">↺ Back to start</button>`;
}

// init: mark all items unanswered
S1.forEach(q=>{q._answered=false;q._picked=null;});
S2.forEach(q=>{q._answered=false;q._picked=null;});

window.checkLevel=checkLevel; window.introTones=introTones; window.startStage=startStage;
window.nextItem=nextItem; window.doneOnboarding=doneOnboarding; window.titlePage=titlePage;
titlePage();
</script></body></html>'''

html = (GAME_HTML
        .replace("__NAME__", GAME_NAME)
        .replace("__PTS__", str(POINTS_CORRECT))
        .replace("__S1__", json.dumps(STAGE1_ITEMS, ensure_ascii=False))
        .replace("__S2__", json.dumps(STAGE2_ITEMS, ensure_ascii=False)))

components.html(html, height=900, scrolling=True)
