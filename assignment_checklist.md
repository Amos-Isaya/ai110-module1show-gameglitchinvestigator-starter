# CodePath requirement audit

Checked against the project instructions supplied in this conversation. “Verified” means evidence from the actual repository or executed commands; it does not claim a student performed a manual activity.

| Requirement | Status and evidence |
|---|---|
| Fork under own account | Verified: GitHub page reports Public and isFork=true for Amos-Isaya/ai110-module1show-gameglitchinvestigator-starter. |
| Clone, virtual environment, dependencies | Verified in cloud with Python 3.12.14 and /workspace/.venvs/gameglitch. pip check reports no broken requirements. Local VS Code instructions are in README. |
| Start Streamlit and observe two games | Verified using the actual app through AppTest before repairs: guess 60 with secret 50, then New Game and decimal 3.9. Live server health returned ok. Student manual play remains recommended. |
| At least three bugs with trigger, expected, actual, output, location | Verified: four rows in reflection.md section 1, with baseline outputs. |
| Ask AI to explain a glitch | AI diagnosis is recorded in reflection and ai_interactions. No separate student-authored per-bug chat sessions were conducted. |
| Choose two fixes and mark crime scenes | Multiple fixes completed; explanatory FIX comments remain near comparison, scoring, reset, and attempt handling. Temporary FIXME markers were not added before repair; that historical step cannot be reconstructed honestly. |
| Separate AI chat for each bug | Not followed literally: one continuous Codex conversation handled the related repairs. No invented chat history. |
| Refactor pure rules to logic_utils.py and import in UI | Verified: range, parsing, comparison, scoring are independent of Streamlit. |
| Review every changed file | Agent inspected code and diffs and ran git diff --check; student review remains pending. |
| Original tests plus new regression test | Verified: original three tests retained; 23 tests pass, including four UI workflow tests. |
| Confirm live game repairs | Verified through AppTest widget interactions plus live health check. Manual student play remains pending. |
| Collaboration comments near fixes | Verified: FIX comments name Codex and explain each change. |
| Reflection section 2: useful suggestion and modified suggestion | Draft explains unified reset and modifying the original AI-generated tuple interface to match the string-return test contract. It does not assert a separate student rejection conversation. Student should confirm this meets the instructor's interpretation and their own experience. |
| Reflection section 3: debugging and verification evidence | Verified: baseline failures, repaired behaviors, 23 passing tests, health and dependency checks documented. |
| Complete five reflection prompts, 3–5 sentences each | Draft contains 4, 5, 5, 4, and 5 prose sentences respectively, plus reproduction table. Student should review the AI-assisted draft. |
| README overview, purpose, bugs and repairs | Verified. |
| Numbered textual demo | Verified: deterministic 40, 70, 50 example matches UI test, including final score 70. |
| Challenge 1: three edge cases and pytest output | Verified: negative, decimal, large integer cases, test output in README, request provenance and reasons in ai_interactions.md. No separate student edge-case prompt is invented. |
| Other optional challenges | Not claimed or required. No model comparison, file-backed high score, or linting output claimed. |
| Required files | Verified: app.py, logic_utils.py, README.md, reflection.md, tests/test_game_logic.py, ai_interactions.md; additional UI tests included. |
| At least three meaningful commits | Verified: a9e1020 bug logs, 43d9c33 repairs/tests, 339cf0f final documentation, plus subsequent audit. |
| Push to origin main | Verified before audit; final audit changes are pushed separately and checked against remote HEAD. |
| Public repository | Verified from GitHub HTML repository metadata and Public label. GitHub API returned 403, so API access was not assumed. |
| Final changes before deadline | Pasted instructions list October 5, 2026 at 2:59 AM EDT; work occurred October 26, 2026. Cannot claim on-time submission or an extension. Confirm late-submission rules with CodePath. |
| Submit through CodePath | Pending user action. No submission was performed. |

## Current validation

```text
python -m pytest -q
23 passed in 1.54s

python -m pip check
No broken requirements found.
```

No test failures, skips, or expected failures. The cloud app health endpoint returned ok. Working tree and remote main are checked after the final push. Cloud configuration has saved installation and startup instructions; publication is a separate environment-settings action and is not required to submit the GitHub project.

## Before submission

Read the reflection and code diff, run/play the project yourself, confirm any course-specific expectations about the AI critique and separate chat steps, and submit the repository URL through CodePath. This audit cannot guarantee a grade or establish that personal process steps occurred.
