# Reflection: Game Glitch Investigator

These notes describe Codex-assisted inspection and automated runs. Personal learning statements should be reviewed and completed by Amos before submission.

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

Codex inspected the repository and reproduced failures using Streamlit AppTest and pytest. Its initial setup plan proposed leaving the intentionally broken starter untouched; the user changed that scope by requesting the CodePath repairs and push. The repair plan keeps check_guess returning a string, matching the existing tests, instead of copying the starter tuple interface suggested by its docstring. Tests and app interactions verify that interface decision; these are agent decisions, not a claim that the student personally reviewed a diff.

## 3. Debugging and testing your fixes

Baseline evidence: three original pytest tests failed with NotImplementedError. Streamlit AppTest reproduced two game sessions without startup exceptions and exposed reversed hints, scoring, decimal parsing, and reset bugs. Final verification results will be recorded after the repairs.

## 4. What did you learn about Streamlit and state?

Streamlit reruns the script when a widget changes. Session state retains values between these reruns, so the secret should be generated only at initialization or explicit reset. Resetting a round must also reset attempts, history, and terminal status together. The starter already persisted its secret; the README claim that it always changes was not supported by the code.

## 5. Looking ahead: your developer habits

Suggested habits are to reproduce a bug before editing, retain existing tests, and verify both pure logic and UI transitions. AI output needs verification because comments and documentation can disagree with executable behavior. Amos should add his own account of what he learned and what he would do differently after reviewing and playing the finished project. No personal experiences or manual reviews are asserted on his behalf.
