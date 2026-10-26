"""Pure rules for the number guessing game, independent of Streamlit."""


def get_range_for_difficulty(difficulty: str):
    """Return inclusive bounds; unknown difficulty defaults to Normal."""
    return {"Easy": (1, 20), "Normal": (1, 100), "Hard": (1, 200)}.get(
        difficulty, (1, 100)
    )


def parse_guess(raw: str):
    """Accept signed integer text and reject empty, decimal, or nonnumeric input."""
    if raw is None or not raw.strip():
        return False, None, "Enter a guess."
    text = raw.strip()
    if not text.lstrip("+-").isascii() or not text.lstrip("+-").isdigit():
        return False, None, "Enter a whole number."
    try:
        return True, int(text), None
    except ValueError:
        return False, None, "That number is too large."


def check_guess(guess: int, secret: int):
    """Return the outcome string required by the original test contract."""
    # FIX: Codex refactored comparisons; keep numbers numeric and hints separate.
    if guess == secret:
        return "Win"
    return "Too High" if guess > secret else "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Award 100 points for a first-try win, then 10 fewer; misses cost 5."""
    # FIX: Codex removed the even-attempt bonus for incorrect guesses.
    if outcome == "Win":
        return current_score + max(10, 100 - 10 * (attempt_number - 1))
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    return current_score
