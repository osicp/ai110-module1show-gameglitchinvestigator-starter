# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X ] Describe the game's purpose.
The purpose of the game is to guess a number. Depending on the difficulty the range of numbers where you guess varies and the number of attempts also varies. 

- [X ] Detail which bugs you found.
1. When secret: 48
When user presses enter or submit guess button, there is no reaction from the app
2. Input 40, system message: GO LOWER!
Input 50, system message: GO HIHER!
3. Once user wins or loses , the new game button refreshes the attempts left but there is no response once user presses the submit button for the the new guess, nor by pressing enter.  
4. Difficulty settings shows easy with 6 attempts and range 1 to 20, normal with 8 attempts and range 1 to 100, and hard with 5 attempts and range 1 to 50.
5. There is a link next to Make a guess that is not working
Return option is not working and clear cache option is buggy

- [X ] Explain what fixes you applied.
I fixed the bugs that I found, in addition, to testing for any bugs in logic, end-cases, and security vulnerabilites.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 40
2. Game returns "Too Low"
3. User enters a guess of 70 → "Too High"
4. Score and attempts left updates correctly after each guess
5. Game ends after the correct guess or user rans out of allowed attempts

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
[fix/refactor_app] $ pytest -v  tests/test_game_logic.py
================================================== test session starts ===================================================
platform darwin -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0 -- /Users/wizofoz/Documents/FAU/2026-2 Fall/CODEPATH_AI01_Foundation/WEEK2/ai110-module1show-gameglitchinvestigator-starter/.venv/bin/python3.14
cachedir: .pytest_cache
rootdir: /Users/wizofoz/Documents/FAU/2026-2 Fall/CODEPATH_AI01_Foundation/WEEK2/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 37 items                                                                                                       

tests/test_game_logic.py::test_winning_guess PASSED                                                                [  2%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                               [  5%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                [  8%]
tests/test_game_logic.py::test_check_guess_one_below_secret PASSED                                                 [ 10%]
tests/test_game_logic.py::test_check_guess_one_above_secret PASSED                                                 [ 13%]
tests/test_game_logic.py::test_check_guess_secret_at_minimum PASSED                                                [ 16%]
tests/test_game_logic.py::test_check_guess_secret_at_maximum PASSED                                                [ 18%]
tests/test_game_logic.py::test_check_guess_negative_guess PASSED                                                   [ 21%]
tests/test_game_logic.py::test_check_guess_returns_plain_string_not_tuple PASSED                                   [ 24%]
tests/test_game_logic.py::test_check_guess_outcome_values_are_exact PASSED                                         [ 27%]
tests/test_game_logic.py::test_parse_guess_valid_integer PASSED                                                    [ 29%]
tests/test_game_logic.py::test_parse_guess_zero PASSED                                                             [ 32%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED                                                  [ 35%]
tests/test_game_logic.py::test_parse_guess_float_string_truncates_to_int PASSED                                    [ 37%]
tests/test_game_logic.py::test_parse_guess_whitespace_around_number PASSED                                         [ 40%]
tests/test_game_logic.py::test_parse_guess_none_input PASSED                                                       [ 43%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED                                                     [ 45%]
tests/test_game_logic.py::test_parse_guess_non_numeric_word PASSED                                                 [ 48%]
tests/test_game_logic.py::test_parse_guess_mixed_alphanumeric PASSED                                               [ 51%]
tests/test_game_logic.py::test_parse_guess_only_whitespace PASSED                                                  [ 54%]
tests/test_game_logic.py::test_parse_guess_sql_injection PASSED                                                    [ 56%]
tests/test_game_logic.py::test_parse_guess_html_script_tag PASSED                                                  [ 59%]
tests/test_game_logic.py::test_parse_guess_path_traversal PASSED                                                   [ 62%]
tests/test_game_logic.py::test_parse_guess_null_byte PASSED                                                        [ 64%]
tests/test_game_logic.py::test_parse_guess_very_long_string_does_not_crash PASSED                                  [ 67%]
tests/test_game_logic.py::test_range_normal_is_1_to_100 PASSED                                                     [ 70%]
tests/test_game_logic.py::test_range_easy_is_positive PASSED                                                       [ 72%]
tests/test_game_logic.py::test_range_easy_narrower_than_normal PASSED                                              [ 75%]
tests/test_game_logic.py::test_range_hard_wider_than_normal PASSED                                                 [ 78%]
tests/test_game_logic.py::test_range_unknown_difficulty_falls_back_to_default PASSED                               [ 81%]
tests/test_game_logic.py::test_range_is_case_sensitive PASSED                                                      [ 83%]
tests/test_game_logic.py::test_update_score_win_on_first_attempt PASSED                                            [ 86%]
tests/test_game_logic.py::test_update_score_win_accumulates_on_existing_score PASSED                               [ 89%]
tests/test_game_logic.py::test_update_score_win_never_awards_less_than_10 PASSED                                   [ 91%]
tests/test_game_logic.py::test_update_score_too_low_always_penalizes PASSED                                        [ 94%]
tests/test_game_logic.py::test_update_score_too_high_always_penalizes PASSED                                       [ 97%]
tests/test_game_logic.py::test_update_score_unknown_outcome_unchanged PASSED                                       [100%]

=================================================== 37 passed in 0.03s ===============================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
