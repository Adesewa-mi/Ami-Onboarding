"""
Àmì — Beginner Onboarding Path
--------------------------------
Standalone module for team review before merging into the main Àmì app.

Purpose: a "new to Yorùbá?" branch that teaches absolute beginners to
perceive the three tones (and basic syllable-level recognition) BEFORE
they hit the main minimal-pairs game, which currently assumes learners
can already hear/see tone.

Author: Popoola Adesewa
Course: CLN 733 — Language Sound Systems, Group 3
"""

import streamlit as st

# ----------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Àmì — Getting Started",
    page_icon="🎵",
    layout="centered",
)

# ----------------------------------------------------------------------
# STYLE
# ----------------------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #FBF7F0;
    }
    .tone-word {
        font-size: 3.2rem;
        font-weight: 700;
        text-align: center;
        margin: 0.2rem 0;
    }
    .tone-label {
        text-align: center;
        font-size: 0.95rem;
        color: #6B6157;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1.5rem;
    }
    .stage-badge {
        display: inline-block;
        background-color: #3F6659;
        color: white;
        padding: 0.15rem 0.7rem;
        border-radius: 999px;
        font-size: 0.8rem;
        letter-spacing: 0.04em;
        margin-bottom: 0.6rem;
    }
    .pitch-line {
        text-align: center;
        font-size: 1.1rem;
        color: #A8471F;
        margin-top: -0.5rem;
    }
    div.stButton > button {
        border-radius: 8px;
        border: 1.5px solid #3F6659;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------
# CONTENT DATA — kept separate from logic so teammates can extend it
# ----------------------------------------------------------------------

STAGE1_ITEMS = [
    {
        "sentence": "Ó ___ sí ilé.",
        "translation": "He/she ___ home.",
        "options": [("wá", "came"), ("wà", "is/exists")],
        "answer": "wá",
        "note": "wá (high tone) = 'came'. wà (low tone) = 'is/exists'. Same letters, same vowel — only the pitch changes the meaning.",
    },
    {
        "sentence": "Mo fẹ́ ra ___.",
        "translation": "I want to buy a ___.",
        "options": [("kọ̀", "reject (verb, wrong fit here)"), ("kọ́", "build (used loosely as 'plot/structure')")],
        "answer": "kọ́",
        "note": "This pair shows how the high tone changes the verb's meaning entirely — the mid/low form wouldn't make sense in this sentence.",
    },
    {
        "sentence": "Ẹyẹ náà ___.",
        "translation": "The bird ___.",
        "options": [("fò", "flew"), ("fó", "broke")],
        "answer": "fò",
        "note": "fò (low tone) = 'flew'. fó (high tone) = 'broke'. Context (a bird) tells you which one fits.",
    },
]

STAGE2_ITEMS = [
    {
        "sentence": "Ìyá mi ní ___ kan.",
        "translation": "My mother has one ___.",
        "options": [("ọkọ", "husband"), ("ọkọ̀", "vehicle")],
        "answer": "ọkọ",
        "note": "ọkọ (mid-mid) = 'husband'. ọkọ̀ (mid-low) = 'vehicle'. Two syllables now — listen for which syllable carries the shift.",
    },
    {
        "sentence": "A ja ___ ní àná.",
        "translation": "We fought a ___ yesterday.",
        "options": [("ogun", "war"), ("ọgún", "twenty")],
        "answer": "ogun",
        "note": "ogun (mid-mid) = 'war'. ọgún (mid-high) = 'twenty'. The vowel quality (ẹ/ọ dot) AND tone both matter here.",
    },
]

# ----------------------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------------------
if "screen" not in st.session_state:
    st.session_state.screen = "welcome"
if "stage1_idx" not in st.session_state:
    st.session_state.stage1_idx = 0
if "stage2_idx" not in st.session_state:
    st.session_state.stage2_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "last_choice" not in st.session_state:
    st.session_state.last_choice = None


def go_to(screen):
    st.session_state.screen = screen
    st.session_state.answered = False
    st.session_state.last_choice = None


# ----------------------------------------------------------------------
# SCREEN: WELCOME / PATH CHOICE
# ----------------------------------------------------------------------
if st.session_state.screen == "welcome":
    st.markdown("<h1 style='text-align:center;'>Àmì</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:#6B6157;'>A game for learning Yorùbá tone and vowel quality</p>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown("### Before we start — how familiar are you with Yorùbá?")
    st.write(
        "Tone marks like the ones on **wá**, **wà**, and **wa** change meaning "
        "in Yorùbá. If you've never trained your ear for this before, we'll "
        "walk you through it first."
    )
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌱 I'm new to Yorùbá", use_container_width=True):
            go_to("intro")
            st.rerun()
    with col2:
        if st.button("✅ I already know tone", use_container_width=True):
            go_to("handoff_skip")
            st.rerun()

# ----------------------------------------------------------------------
# SCREEN: INTRO — "Yorùbá is Singing"
# ----------------------------------------------------------------------
elif st.session_state.screen == "intro":
    st.markdown("<div class='stage-badge'>GETTING STARTED</div>", unsafe_allow_html=True)
    st.markdown("## Yorùbá is a bit like singing")
    st.write(
        "Every Yorùbá word carries a **pitch** — a musical note — on each "
        "syllable. Change the pitch, and you can change the whole meaning "
        "of the word, even if every letter stays the same."
    )
    st.write("There are three notes in Yorùbá. Think of them like **do – re – mi**:")

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='tone-word'>à</div>", unsafe_allow_html=True)
        st.markdown("<div class='tone-label'>Low</div>", unsafe_allow_html=True)
        st.markdown("<div class='pitch-line'>↘ like 'do'</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='tone-word'>a</div>", unsafe_allow_html=True)
        st.markdown("<div class='tone-label'>Mid (no mark)</div>", unsafe_allow_html=True)
        st.markdown("<div class='pitch-line'>→ like 're'</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='tone-word'>á</div>", unsafe_allow_html=True)
        st.markdown("<div class='tone-label'>High</div>", unsafe_allow_html=True)
        st.markdown("<div class='pitch-line'>↗ like 'mi'</div>", unsafe_allow_html=True)

    st.write("")
    st.info(
        "💡 **The mark tells you the note.** A line going down (`\\`) means "
        "low. No mark means mid. A line going up (`´`) means high. "
        "That's the whole system — the rest is practice."
    )
    st.write("")

    if st.button("Got it — let's practice →", use_container_width=True):
        go_to("stage1")
        st.rerun()

# ----------------------------------------------------------------------
# SCREEN: STAGE 1 — Monosyllabic words
# ----------------------------------------------------------------------
elif st.session_state.screen == "stage1":
    idx = st.session_state.stage1_idx
    if idx >= len(STAGE1_ITEMS):
        go_to("stage1_complete")
        st.rerun()
    else:
        item = STAGE1_ITEMS[idx]
        st.markdown("<div class='stage-badge'>STAGE 1 · ONE-SYLLABLE WORDS</div>", unsafe_allow_html=True)
        st.progress((idx) / len(STAGE1_ITEMS))
        st.markdown(f"### {item['sentence']}")
        st.caption(item["translation"])
        st.write("Which word fits?")

        if not st.session_state.answered:
            c1, c2 = st.columns(2)
            for col, (word, gloss) in zip([c1, c2], item["options"]):
                with col:
                    if st.button(word, key=f"s1_{idx}_{word}", use_container_width=True):
                        st.session_state.answered = True
                        st.session_state.last_choice = word
                        if word == item["answer"]:
                            st.session_state.score += 1
                        st.rerun()
        else:
            correct = st.session_state.last_choice == item["answer"]
            if correct:
                st.success(f"✅ Correct — **{item['answer']}**")
            else:
                st.error(f"Not quite. The answer was **{item['answer']}**")
            st.write(item["note"])
            if st.button("Next →", use_container_width=True):
                st.session_state.stage1_idx += 1
                st.session_state.answered = False
                st.session_state.last_choice = None
                st.rerun()

# ----------------------------------------------------------------------
# SCREEN: STAGE 1 COMPLETE
# ----------------------------------------------------------------------
elif st.session_state.screen == "stage1_complete":
    st.markdown("<div class='stage-badge'>STAGE 1 COMPLETE</div>", unsafe_allow_html=True)
    st.markdown("## Nice work 🎵")
    st.write(
        f"You scored **{st.session_state.score} / {len(STAGE1_ITEMS)}** on "
        "single-syllable words. Now let's try words with two syllables — "
        "this is closer to what you'll see in the main game."
    )
    if st.button("Continue to Stage 2 →", use_container_width=True):
        go_to("stage2")
        st.rerun()

# ----------------------------------------------------------------------
# SCREEN: STAGE 2 — Disyllabic words
# ----------------------------------------------------------------------
elif st.session_state.screen == "stage2":
    idx = st.session_state.stage2_idx
    if idx >= len(STAGE2_ITEMS):
        go_to("final_complete")
        st.rerun()
    else:
        item = STAGE2_ITEMS[idx]
        st.markdown("<div class='stage-badge'>STAGE 2 · TWO-SYLLABLE WORDS</div>", unsafe_allow_html=True)
        st.progress((idx) / len(STAGE2_ITEMS))
        st.markdown(f"### {item['sentence']}")
        st.caption(item["translation"])
        st.write("Which word fits?")

        if not st.session_state.answered:
            c1, c2 = st.columns(2)
            for col, (word, gloss) in zip([c1, c2], item["options"]):
                with col:
                    if st.button(word, key=f"s2_{idx}_{word}", use_container_width=True):
                        st.session_state.answered = True
                        st.session_state.last_choice = word
                        if word == item["answer"]:
                            st.session_state.score += 1
                        st.rerun()
        else:
            correct = st.session_state.last_choice == item["answer"]
            if correct:
                st.success(f"✅ Correct — **{item['answer']}**")
            else:
                st.error(f"Not quite. The answer was **{item['answer']}**")
            st.write(item["note"])
            if st.button("Next →", use_container_width=True):
                st.session_state.stage2_idx += 1
                st.session_state.answered = False
                st.session_state.last_choice = None
                st.rerun()

# ----------------------------------------------------------------------
# SCREEN: FINAL COMPLETE — handoff to main game
# ----------------------------------------------------------------------
elif st.session_state.screen == "final_complete":
    st.markdown("<div class='stage-badge'>ONBOARDING COMPLETE</div>", unsafe_allow_html=True)
    st.markdown("## You're ready for Àmì 🎉")
    total = len(STAGE1_ITEMS) + len(STAGE2_ITEMS)
    st.write(f"Final score: **{st.session_state.score} / {total}**")
    st.write(
        "You've practiced spotting tone on one- and two-syllable words. "
        "The main game will introduce longer sentences and, sometimes, "
        "vowel-quality contrasts (the dot under ẹ, ọ, and ṣ) alongside tone."
    )
    st.write("")
    if st.button("Enter the main game →", use_container_width=True):
        st.write("*(This is where we'd hand off to the main Àmì game screen.)*")
    st.write("")
    if st.button("↺ Restart onboarding"):
        for key in ["screen", "stage1_idx", "stage2_idx", "score", "answered", "last_choice"]:
            del st.session_state[key]
        st.rerun()

# ----------------------------------------------------------------------
# SCREEN: SKIP PATH (already knows tone)
# ----------------------------------------------------------------------
elif st.session_state.screen == "handoff_skip":
    st.markdown("## Skipping ahead 👋")
    st.write(
        "Since you're already comfortable with Yorùbá tone, you'll go "
        "straight into the main Àmì game."
    )
    if st.button("Enter the main game →", use_container_width=True):
        st.write("*(This is where we'd hand off to the main Àmì game screen.)*")
    st.write("")
    if st.button("← Actually, let me try the beginner path"):
        go_to("intro")
        st.rerun()
