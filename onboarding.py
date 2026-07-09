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
     minimal pairs
  4. "Guess the Tone" — no sentences yet. A bare word (+ optional picture)
     and its English meaning are shown; the learner picks the correctly
     toned Yorùbá form from the options. Feedback names the tone (low,
     mid, high) and explains why the other option(s) are wrong.
     Starts with monosyllabic words, then moves to bisyllabic words
     (mix of nouns, verbs, a couple of adjectives).

NOTE ON THE WORD LIST: 9 monosyllabic + 6 bisyllabic items are included
below (not yet 20 each). Every item is drawn from forms already used/
verified elsewhere in the group's report (fò/fó, ọkọ/ọkọ̀, ogun/ọgún) or
cross-checked against academic/dictionary sources (wá/wà/wa, kan/kán,
pa/pá, owó/òwò). I deliberately stopped short of fabricating pairs I
couldn't verify — wrong tone marks would actively mislead the very
beginners this page is meant to help, and the report itself raises this
exact caution in section 6.4 about dataset composition. To reach ~20/20,
pull words straight from the team's verified 49-item question bank, or
have a native speaker check any additions before they ship.

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

# ---------------------------------------------------------------------------
# GUESS-THE-TONE ITEMS
# Each item: bare (untoned) spelling, optional picture (emoji placeholder —
# swap for a real image asset later), English gloss, word class, a list of
# tone-marked options, which one is correct, and an explanation.
# ---------------------------------------------------------------------------

GUESS1_MONO = [
    {
        "id": "g1_1",
        "bare": "wa",
        "picture": "🚶➡️",
        "gloss": "to come",
        "class": "verb",
        "options": [
            {"form": "wá", "tone": "High"},
            {"form": "wà", "tone": "Low"},
            {"form": "wa", "tone": "Mid"},
        ],
        "correct": "wá",
        "explanation": "wá is High and means 'to come'. wà is Low and means 'to exist/be'. wa is Mid and means 'our'. Three different words, same letters.",
    },
    {
        "id": "g1_2",
        "bare": "wa",
        "picture": "🌍",
        "gloss": "to exist / to be (somewhere)",
        "class": "verb",
        "options": [
            {"form": "wá", "tone": "High"},
            {"form": "wà", "tone": "Low"},
            {"form": "wa", "tone": "Mid"},
        ],
        "correct": "wà",
        "explanation": "wà is Low and means 'to exist/be'. wá (High) means 'to come'. wa (Mid) means 'our'.",
    },
    {
        "id": "g1_3",
        "bare": "fo",
        "picture": "🐦",
        "gloss": "flew",
        "class": "verb",
        "options": [
            {"form": "fò", "tone": "Low"},
            {"form": "fó", "tone": "High"},
        ],
        "correct": "fò",
        "explanation": "fò is Low and means 'flew'. fó is High and means 'broke'. Same spelling without the mark, opposite tone, different word.",
    },
    {
        "id": "g1_4",
        "bare": "fo",
        "picture": "💔",
        "gloss": "broke",
        "class": "verb",
        "options": [
            {"form": "fò", "tone": "Low"},
            {"form": "fó", "tone": "High"},
        ],
        "correct": "fó",
        "explanation": "fó is High and means 'broke'. fò is Low and means 'flew'.",
    },
    {
        "id": "g1_5",
        "bare": "kan",
        "picture": "1️⃣",
        "gloss": "one / a certain (amount)",
        "class": "adjective",
        "options": [
            {"form": "kan", "tone": "Mid"},
            {"form": "kán", "tone": "High"},
        ],
        "correct": "kan",
        "explanation": "kan is Mid and means 'one/a certain'. kán is High and means 'to be urgent/tight'.",
    },
    {
        "id": "g1_6",
        "bare": "kan",
        "picture": "⏰",
        "gloss": "to be urgent / tight",
        "class": "adjective",
        "options": [
            {"form": "kan", "tone": "Mid"},
            {"form": "kán", "tone": "High"},
        ],
        "correct": "kán",
        "explanation": "kán is High and means 'to be urgent/tight'. kan is Mid and means 'one/a certain'.",
    },
    {
        "id": "g1_7",
        "bare": "wa",
        "picture": "👥",
        "gloss": "our",
        "class": "pronoun",
        "options": [
            {"form": "wá", "tone": "High"},
            {"form": "wà", "tone": "Low"},
            {"form": "wa", "tone": "Mid"},
        ],
        "correct": "wa",
        "explanation": "wa is Mid and means 'our'. wá (High) means 'to come'. wà (Low) means 'to exist/be'.",
    },
    {
        "id": "g1_8",
        "bare": "pa",
        "picture": "⚔️",
        "gloss": "to kill",
        "class": "verb",
        "options": [
            {"form": "pa", "tone": "Mid"},
            {"form": "pá", "tone": "High"},
        ],
        "correct": "pa",
        "explanation": "pa is Mid and means 'to kill'. pá is High and means 'bald'.",
    },
    {
        "id": "g1_9",
        "bare": "pa",
        "picture": "👨‍🦲",
        "gloss": "bald",
        "class": "adjective",
        "options": [
            {"form": "pa", "tone": "Mid"},
            {"form": "pá", "tone": "High"},
        ],
        "correct": "pá",
        "explanation": "pá is High and means 'bald'. pa is Mid and means 'to kill'.",
    },
]

GUESS2_BI = [
    {
        "id": "g2_1",
        "bare": "oko",
        "picture": "💑",
        "gloss": "husband",
        "class": "noun",
        "options": [
            {"form": "ọkọ", "tone": "Mid-Mid"},
            {"form": "ọkọ̀", "tone": "Mid-Low"},
        ],
        "correct": "ọkọ",
        "explanation": "ọkọ (Mid-Mid) means 'husband'. ọkọ̀ (Mid-Low) means 'vehicle'. Two syllables — the second one carries the difference.",
    },
    {
        "id": "g2_2",
        "bare": "oko",
        "picture": "🚗",
        "gloss": "vehicle",
        "class": "noun",
        "options": [
            {"form": "ọkọ", "tone": "Mid-Mid"},
            {"form": "ọkọ̀", "tone": "Mid-Low"},
        ],
        "correct": "ọkọ̀",
        "explanation": "ọkọ̀ (Mid-Low) means 'vehicle'. ọkọ (Mid-Mid) means 'husband'.",
    },
    {
        "id": "g2_3",
        "bare": "ogun",
        "picture": "⚔️",
        "gloss": "war",
        "class": "noun",
        "options": [
            {"form": "ogun", "tone": "Mid-Mid"},
            {"form": "ọgún", "tone": "Mid-High"},
        ],
        "correct": "ogun",
        "explanation": "ogun (Mid-Mid) means 'war'. ọgún (Mid-High) means 'twenty' — note it also has the vowel-quality dot under the o, not just a different tone.",
    },
    {
        "id": "g2_4",
        "bare": "ogun",
        "picture": "2️⃣0️⃣",
        "gloss": "twenty",
        "class": "noun",
        "options": [
            {"form": "ogun", "tone": "Mid-Mid"},
            {"form": "ọgún", "tone": "Mid-High"},
        ],
        "correct": "ọgún",
        "explanation": "ọgún (Mid-High, with the dotted ọ) means 'twenty'. ogun (Mid-Mid) means 'war'.",
    },
    {
        "id": "g2_5",
        "bare": "owo",
        "picture": "💰",
        "gloss": "money",
        "class": "noun",
        "options": [
            {"form": "owó", "tone": "High-High"},
            {"form": "òwò", "tone": "Low-Low"},
        ],
        "correct": "owó",
        "explanation": "owó (High-High) means 'money'. òwò (Low-Low) means 'trade/business'.",
    },
    {
        "id": "g2_6",
        "bare": "owo",
        "picture": "🏪",
        "gloss": "trade / business",
        "class": "noun",
        "options": [
            {"form": "owó", "tone": "High-High"},
            {"form": "òwò", "tone": "Low-Low"},
        ],
        "correct": "òwò",
        "explanation": "òwò (Low-Low) means 'trade/business'. owó (High-High) means 'money'.",
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
.lesson{background:#fff;border:1px solid #ece5d8;border-radius:10px;padding:6px 20px;line-height:1.65;}
.lesson li{margin:8px 0;}
.tonerow{display:flex;justify-content:center;gap:2.4rem;margin:1.4rem 0;}
.tonecell{text-align:center;}
.toneword{font-size:2.6rem;font-weight:800;color:var(--indigo);}
.tonelabel{color:#6b7280;font-size:.85rem;text-transform:uppercase;letter-spacing:.04em;margin-top:2px;}
.tonepitch{color:var(--gold);font-size:1rem;margin-top:2px;}
.muted{color:#6b7280;}
.promptcard{background:#fff;border:1px solid #ece5d8;border-radius:10px;padding:24px 20px;text-align:center;margin:.2rem 0 16px;}
.promptpic{font-size:2.6rem;margin-bottom:6px;}
.promptbare{font-size:1.1rem;color:#6b7280;letter-spacing:.03em;}
.promptgloss{font-size:1.6rem;font-weight:800;color:var(--indigo);margin-top:2px;}
.promptclass{color:#a8471f;font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;margin-top:4px;}
.opts{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:12px;}
.card{background:#fff;border:2px solid #e6ded0;border-radius:12px;padding:16px 10px;text-align:center;cursor:pointer;transition:.15s;}
.card:hover{border-color:var(--indigo);}
.card.good{border-color:var(--good);background:#eaf5ef;}
.card.bad{border-color:var(--bad);background:#fbeef0;}
.card.lock{cursor:default;}
.word{font-size:1.9rem;font-weight:800;color:var(--indigo);}
.tonetag{color:#6b7280;font-size:.8rem;margin-top:4px;text-transform:uppercase;letter-spacing:.03em;}
.feed{margin-top:16px;padding:14px 16px;border-radius:10px;font-size:1.02rem;}
.feed.good{background:#eaf5ef;border-left:5px solid var(--good);color:#1c5a40;}
.feed.bad{background:#fbeef0;border-left:5px solid var(--bad);color:#7c2531;}
</style></head><body><div class="wrap"><div id="app"></div></div>
<script>
const NAME="__NAME__", PTS=__PTS__;
const G1=__G1__, G2=__G2__;
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

// ---------- Tone intro ----------
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
<p><b>Where tone appears.</b> Tone is not just carried by vowels. It also appears on the syllabic nasal consonants <b>m</b> and <b>n</b> when they form their own syllable. So watch vowels <i>and</i> these nasal syllables.</p>
<p><b>How tone changes meaning.</b> Two words can be spelled with the same letters and mean entirely different things, because the tone marks are different. For example: <b>ọkọ</b> (husband), <b>ọkọ̀</b> (vehicle) &mdash; same letters, different tone, different word.</p>
<p><b>Minimal pairs.</b> A pair of words like that, identical except for one tone (or one vowel-quality dot), is called a <b>minimal pair</b>. That's exactly what you're about to practise spotting.</p>
</div>
<button class="btn" onclick="startStage(1)">Guess the Tone →</button>`;
}

// ---------- Guess the Tone stages ----------
function startStage(n){
stage = n===1 ? G1 : G2;
si=0;
if(n===1) points=0;
playItem(n);
}

function playItem(stageNum){
const q=stage[si], N=stage.length;
const label = stageNum===1 ? "GUESS THE TONE · ONE SYLLABLE" : "GUESS THE TONE · TWO SYLLABLES";
function card(opt){
let c="card";
if(q._answered){
c+=" lock";
if(opt.form===q.correct) c+=" good";
else if(opt.form===q._picked) c+=" bad";
}
return `<div class="${c}" data-f="${opt.form}"><div class="word">${opt.form}</div><div class="tonetag">${opt.tone}</div></div>`;
}
let feed="";
if(q._answered){
const ok=q._picked===q.correct;
feed=`<div class="feed ${ok?'good':'bad'}">${ok?'\u2713 Correct. ':'\u2717 Not quite. The answer is <b>'+q.correct+'</b>. '}${q.explanation}</div>
<button class="btn" onclick="nextItem(${stageNum})">${(si===N-1)?'Continue':'Next'} →</button>`;
}
const pic = q.picture ? `<div class="promptpic">${q.picture}</div>` : "";
app().innerHTML=`
<div class="meta"><span>${label} &middot; ${si+1} of ${N}</span></div>
<div class="bar"><i style="width:${(si+1)/N*100}%"></i></div>
<div class="promptcard">
${pic}
<div class="promptbare">${q.bare}</div>
<div class="promptgloss">${q.gloss}</div>
<div class="promptclass">${q.class}</div>
</div>
<div class="opts">${q.options.map(card).join("")}</div>
${feed}`;
if(!q._answered){
app().querySelectorAll(".card").forEach(c=>c.onclick=()=>{
q._answered=true; q._picked=c.dataset.f;
if(c.dataset.f===q.correct) points+=PTS;
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
const total = G1.length + G2.length;
app().innerHTML=`
<div class="h2">You're ready 🎉</div>
<div class="promptcard">Score: <b>${points} points</b> across ${total} words.
<br><span class="muted">You've practised guessing tone on one- and two-syllable words. The main game moves into full sentences next.</span></div>
<button class="btn" onclick="doneOnboarding()">Enter the main game →</button>
<button class="btn ghost" onclick="titlePage()">↺ Restart</button>`;
}

function doneOnboarding(){
app().innerHTML=`<div class="h2">Handoff point</div>
<div class="lesson">This is where onboarding ends and the main Àmì game's <code>home()</code> screen takes over.</div>
<button class="btn ghost" onclick="titlePage()">↺ Back to start</button>`;
}

G1.forEach(q=>{q._answered=false;q._picked=null;});
G2.forEach(q=>{q._answered=false;q._picked=null;});

window.checkLevel=checkLevel; window.introTones=introTones; window.startStage=startStage;
window.nextItem=nextItem; window.doneOnboarding=doneOnboarding; window.titlePage=titlePage;
titlePage();
</script></body></html>'''

html = (GAME_HTML
        .replace("__NAME__", GAME_NAME)
        .replace("__PTS__", str(POINTS_CORRECT))
        .replace("__G1__", json.dumps(GUESS1_MONO, ensure_ascii=False))
        .replace("__G2__", json.dumps(GUESS2_BI, ensure_ascii=False)))

components.html(html, height=900, scrolling=True)
