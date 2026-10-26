from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


import pytest

from logic_utils import get_range_for_difficulty, parse_guess, update_score


@pytest.mark.parametrize("raw", [None, "", "  ", "3.9", "abc", "1e3", "--2"])
def test_invalid_input(raw):
    assert parse_guess(raw)[0] is False


@pytest.mark.parametrize("raw, expected", [(" 42 ", 42), ("-3", -3), ("+7", 7), ("9" * 100, int("9" * 100))])
def test_integer_input(raw, expected):
    assert parse_guess(raw) == (True, expected, None)


def test_score_rules():
    assert update_score(0, "Win", 1) == 100
    assert update_score(0, "Win", 20) == 10
    assert update_score(0, "Too High", 2) == -5
    assert update_score(0, "Too Low", 1) == -5


@pytest.mark.parametrize("difficulty, bounds", [("Easy", (1, 20)), ("Normal", (1, 100)), ("Hard", (1, 200)), ("unknown", (1, 100))])
def test_difficulty_ranges(difficulty, bounds):
    assert get_range_for_difficulty(difficulty) == bounds
