"""Streamlit interface for the repaired guessing game."""

import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

st.set_page_config(page_title="Game Glitch Investigator", page_icon="🎮")
st.title("🎮 Game Glitch Investigator")
st.caption("Guess the secret number using the higher/lower hints.")

st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox("Difficulty", ["Easy", "Normal", "Hard"], index=1)
low, high = get_range_for_difficulty(difficulty)
attempt_limit = {"Easy": 6, "Normal": 8, "Hard": 5}[difficulty]


def reset_game():
    """Reset every round field together, using the selected difficulty."""
    # FIX: Codex unified initialization, New Game, and difficulty changes.
    st.session_state.update(
        secret=random.randint(low, high),
        attempts=0,
        score=0,
        status="playing",
        history=[],
        round_difficulty=difficulty,
        guess_input="",
        feedback=None,
    )


if st.session_state.get("round_difficulty") != difficulty:
    reset_game()

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")
st.button("New Game 🔁", on_click=reset_game)
st.subheader("Make a guess")
active = st.session_state.status == "playing"
st.text_input("Enter your guess:", key="guess_input", disabled=not active)
submit = st.button("Submit Guess 🚀", disabled=not active)
show_hint = st.checkbox("Show hint", value=True)

if submit:
    ok, guess, error = parse_guess(st.session_state.guess_input)
    if not ok:
        st.error(error)
    elif not low <= guess <= high:
        st.error(f"Enter a number between {low} and {high}.")
    else:
        # FIX: Codex counts only valid, in-range guesses, exactly once.
        st.session_state.attempts += 1
        st.session_state.history.append(guess)
        outcome = check_guess(guess, st.session_state.secret)
        st.session_state.feedback = outcome
        st.session_state.score = update_score(
            st.session_state.score, outcome, st.session_state.attempts
        )
        if outcome == "Win":
            st.session_state.status = "won"
            st.balloons()
        elif st.session_state.attempts >= attempt_limit:
            st.session_state.status = "lost"
        st.rerun()

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)
st.write("Score:", st.session_state.score)
if st.session_state.status == "won":
    st.success(f"🎉 You won! The secret was {st.session_state.secret}.")
elif st.session_state.status == "lost":
    st.error(f"Out of attempts! The secret was {st.session_state.secret}.")
elif show_hint and st.session_state.feedback:
    hints = {"Too High": "Too High — go LOWER!", "Too Low": "Too Low — go HIGHER!"}
    st.warning(hints[st.session_state.feedback])

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)
