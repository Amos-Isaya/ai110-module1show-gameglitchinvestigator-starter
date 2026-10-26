# Reflection: Game Glitch Investigator

AI-assisted reflection draft based on the actual repository changes and automated runs. Review it before submitting; automated play is distinguished from personal manual testing.

## 1. What was broken when you started?

The starter app rendered, but two automated play sessions exposed misleading hints and incomplete reset behavior. With the secret set to 50, guessing 60 displayed “Go HIGHER!”, counted two attempts, and awarded five points. After New Game, entering 3.9 silently became 3 and the previous history remained. The original three pytest tests all failed because logic_utils.check_guess raised NotImplementedError.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| Secret 50, guess 60 | Too High; go lower; score -5 | Go HIGHER!; score +5 | Warning: Go HIGHER! | app.py check_guess, update_score |
| First valid guess | One attempt consumed | Attempts becomes 2 | Debug attempts: 2 | app.py session initialization |
| New Game, then 3.9 | Reject decimal; empty prior history | Parsed as 3; history [60, 3] | No exception | app.py parse_guess, new_game |
| Run original pytest suite | Comparisons return outcome strings | All three fail | NotImplementedError | logic_utils.py check_guess |

## 2. How did you use AI as a teammate?

I used Codex to investigate the starter project, refactor the rules into logic_utils.py, and generate regression tests. One useful AI suggestion was to use one reset function for initialization, New Game, and difficulty changes, because all three actions need consistent state; the UI tests verify that attempts, history, score, and status reset together. One part of the original AI-generated design that needed modification was the tuple return described for check_guess: the existing tests expected an outcome string, so the repaired version returns a string and the UI supplies the message separately. This keeps the function compatible with the original test set and avoids mixing presentation with comparison logic. The automated results verify these technical choices, while I still need to review the finished changes and try the game myself.

## 3. Debugging and testing your fixes

Baseline evidence: three original pytest tests failed with NotImplementedError. Streamlit AppTest reproduced two game sessions without startup exceptions and exposed reversed hints, scoring, decimal parsing, and reset bugs. After repairs, all 23 pytest tests passed, including the three original tests and four Streamlit UI tests. The UI suite verifies both hint directions, a win with score 70 after three guesses, disabled submissions after completion, fresh-round reset, invalid inputs without attempt consumption, difficulty changes, and loss after six Easy misses. Additional boundary checks cover a first-try win, a win on the final allowed attempt, and restarting after a loss. A running Streamlit server also returned ok from its health endpoint, and pip check reported no broken requirements.

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script when a widget changes. Session state retains values between these reruns, so the secret should be generated only at initialization or explicit reset. Resetting a round must also reset attempts, history, and terminal status together. The starter already persisted its secret; the README claim that it always changes was not supported by the code.

## 5. Looking ahead: your developer habits

One habit I want to reuse is reproducing a bug with a specific input and expected output before changing the code. Next time, I would ask AI to focus on one bug at a time and explain its proposed fix before making broad edits. This project demonstrates why AI-generated code needs verification: even the starter documentation described a secret-reset bug that the code did not actually have. A human-in-the-loop process matters because passing tests are evidence about the tested behavior, not a guarantee that every AI claim is correct. I would use a small test set, diff review, and manual play together rather than relying only on an AI explanation or possible hallucination.
