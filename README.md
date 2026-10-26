# Game Glitch Investigator

A repaired Streamlit number guessing game for CodePath AI110. Choose Easy (1–20, 6 attempts), Normal (1–100, 8 attempts), or Hard (1–200, 5 attempts). Valid misses cost 5 points; a win earns 100 points on attempt one, decreasing by 10 per attempt to a minimum of 10. Scores are per round and reset with New Game.

## Setup and run in VS Code

Install Python 3.12, Git, VS Code, and the Microsoft Python extension. In a terminal:

```bash
git clone https://github.com/Amos-Isaya/ai110-module1show-gameglitchinvestigator-starter.git
cd ai110-module1show-gameglitchinvestigator-starter
code .
python -m venv .venv
```

On macOS/Linux, use `python3` if `python` is unavailable, then activate:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

In VS Code, run **Python: Select Interpreter** from the Command Palette and choose `.venv`. Then use its integrated terminal:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m streamlit run app.py
```

Open the browser address Streamlit prints on your own computer. Stop the server with Ctrl+C. No API keys or paid services are needed. The cloud environment is separate from your laptop; clone or pull GitHub changes to work locally. If already cloned, commit or stash your local work before `git pull origin main`.

## Document Your Experience

- [x] Purpose: guess a persistent secret using accurate higher/lower feedback.
- [x] Bugs diagnosed: reversed hints, alternating string/numeric comparisons, incorrect attempt counting, inconsistent scoring, decimal truncation, and partial resets.
- [x] Repairs: moved pure rules into `logic_utils.py`, preserved the original string-return test contract, validated input before consuming attempts, and reset every round field together.
- [x] Verified through original tests, additional edge cases, and automated Streamlit interactions.

The starter already stored its secret in session state. Its claim that the secret changes on every submit was not supported by inspection. See `reflection.md` for reproduced evidence and the distinction between agent work and personal reflection.

## Demo Walkthrough

For this reproducible example, the automated UI test sets the secret to 50; normal play chooses randomly. Developer Debug Info reveals the live secret when trying it manually.

1. Start a Normal game with 8 attempts, score 0, and secret 50.
2. Submit 40: “Too Low — go HIGHER!”, 7 attempts remain, score -5.
3. Submit 70: “Too High — go LOWER!”, 6 attempts remain, score -10.
4. Submit 50: the game announces a win, adds 80 points, and ends at score 70.
5. Further submissions are disabled. New Game clears input, history, score, attempts, and outcome and generates a new secret.
6. A blank, decimal, negative, or out-of-range guess displays an error without consuming an attempt. Changing difficulty starts a fresh round with the new bounds.

## Test Results

Executed in the cloud environment with Python 3.12.14:

```text
$ python -m pytest -q
.......................                                                  [100%]
23 passed in 1.54s
```

`python -m pip check` reported no broken requirements. The live Streamlit health endpoint returned `ok`; AppTest exercised actual widgets and session state, including wins and losses. The three original tests are retained. Challenge 1 edge cases include negative values, decimals, and extremely large integers; see `ai_interactions.md`.

## Requirement audit

See `assignment_checklist.md` for the requirement-by-requirement review, verification evidence, and remaining personal/submission steps.

## Before submitting

Review the changes and play the game yourself. Read the AI-assisted draft in `reflection.md` and adjust it to match your understanding and experience. The audit confirmed the GitHub repository is public; recheck visibility if you change settings and submit its link through CodePath; pushing code does not submit the assignment.
