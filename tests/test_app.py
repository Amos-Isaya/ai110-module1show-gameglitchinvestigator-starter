"""Exercise the real Streamlit UI and session transitions."""
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parents[1] / "app.py")


def click(at, label):
    next(button for button in at.button if button.label == label).click().run()
    assert not at.exception


def guess(at, value):
    at.text_input[0].input(value).run()
    click(at, "Submit Guess 🚀")


def test_full_game_and_reset():
    at = AppTest.from_file(APP).run()
    at.session_state.secret = 50
    guess(at, "40")
    assert at.warning[0].value == "Too Low — go HIGHER!"
    assert at.session_state.attempts == 1
    assert at.session_state.secret == 50
    guess(at, "70")
    assert at.warning[0].value == "Too High — go LOWER!"
    guess(at, "50")
    assert at.session_state.status == "won"
    assert at.session_state.score == 70
    assert all(b.disabled for b in at.button if b.label == "Submit Guess 🚀")
    click(at, "New Game 🔁")
    assert at.session_state.status == "playing"
    assert at.session_state.attempts == at.session_state.score == 0
    assert at.session_state.history == []
    assert at.text_input[0].value == ""


def test_invalid_input_difficulty_and_loss():
    at = AppTest.from_file(APP).run()
    for value in ["", "3.9", "-2", "9" * 100]:
        guess(at, value)
        assert at.error
        assert at.session_state.attempts == 0
        assert at.session_state.history == []
    at.selectbox[0].select("Easy").run()
    assert 1 <= at.session_state.secret <= 20
    at.session_state.secret = 20
    for _ in range(6):
        guess(at, "1")
    assert at.session_state.status == "lost"
    assert at.session_state.attempts == 6
    assert "Attempts left: 0" in at.info[0].value
    at.selectbox[0].select("Hard").run()
    assert at.session_state.status == "playing"
    assert 1 <= at.session_state.secret <= 200
    assert at.session_state.attempts == 0
