from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

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


# ---------------------------------------------------------------------------
# check_guess — boundary and edge cases
# ---------------------------------------------------------------------------

def test_check_guess_one_below_secret():
    # One below the secret is still Too Low
    assert check_guess(49, 50) == "Too Low"

def test_check_guess_one_above_secret():
    # One above the secret is still Too High
    assert check_guess(51, 50) == "Too High"

def test_check_guess_secret_at_minimum():
    # Secret at the smallest allowed value can still be won
    assert check_guess(1, 1) == "Win"

def test_check_guess_secret_at_maximum():
    # Secret at the largest allowed value can still be won
    assert check_guess(100, 100) == "Win"

def test_check_guess_negative_guess():
    # A negative guess is always Too Low for any positive secret
    assert check_guess(-1, 1) == "Too Low"

def test_check_guess_returns_plain_string_not_tuple():
    # Return value must be a str, not a (outcome, message) tuple
    result = check_guess(50, 50)
    assert isinstance(result, str)

def test_check_guess_outcome_values_are_exact():
    # Outcomes must match the exact strings the app and tests rely on
    assert check_guess(50, 50) in ("Win", "Too High", "Too Low")
    assert check_guess(60, 50) in ("Win", "Too High", "Too Low")
    assert check_guess(40, 50) in ("Win", "Too High", "Too Low")


# ---------------------------------------------------------------------------
# parse_guess — valid inputs
# ---------------------------------------------------------------------------

def test_parse_guess_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None

def test_parse_guess_zero():
    ok, val, err = parse_guess("0")
    assert ok is True
    assert val == 0

def test_parse_guess_negative_number():
    ok, val, err = parse_guess("-5")
    assert ok is True
    assert val == -5

def test_parse_guess_float_string_truncates_to_int():
    # "3.9" should be accepted and truncated to 3, not rounded
    ok, val, err = parse_guess("3.9")
    assert ok is True
    assert val == 3

def test_parse_guess_whitespace_around_number():
    # Leading/trailing whitespace should not reject a valid number
    ok, val, err = parse_guess("  42  ")
    assert ok is True
    assert val == 42


# ---------------------------------------------------------------------------
# parse_guess — invalid and edge-case inputs
# ---------------------------------------------------------------------------

def test_parse_guess_none_input():
    ok, val, err = parse_guess(None)  # type: ignore[arg-type]
    assert ok is False
    assert val is None
    assert isinstance(err, str)

def test_parse_guess_empty_string():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None

def test_parse_guess_non_numeric_word():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert val is None

def test_parse_guess_mixed_alphanumeric():
    ok, val, err = parse_guess("4abc")
    assert ok is False

def test_parse_guess_only_whitespace():
    ok, val, err = parse_guess("   ")
    assert ok is False


# ---------------------------------------------------------------------------
# parse_guess — security inputs
# ---------------------------------------------------------------------------

def test_parse_guess_sql_injection():
    # Injection payloads must never parse as a valid number
    ok, val, err = parse_guess("1; DROP TABLE users--")
    assert ok is False

def test_parse_guess_html_script_tag():
    ok, val, err = parse_guess("<script>alert(1)</script>")
    assert ok is False

def test_parse_guess_path_traversal():
    ok, val, err = parse_guess("../../etc/passwd")
    assert ok is False

def test_parse_guess_null_byte():
    ok, val, err = parse_guess("\x00")
    assert ok is False

def test_parse_guess_very_long_string_does_not_crash():
    # A pathologically long string must not raise an unhandled exception
    ok, val, err = parse_guess("A" * 10_000)
    assert isinstance(ok, bool)
    assert ok is False


# ---------------------------------------------------------------------------
# get_range_for_difficulty — correctness and ordering invariants
# ---------------------------------------------------------------------------

def test_range_normal_is_1_to_100():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_easy_is_positive():
    low, high = get_range_for_difficulty("Easy")
    assert low >= 1
    assert high > low

def test_range_easy_narrower_than_normal():
    # Easy must have a smaller range than Normal — fewer choices means easier
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high

def test_range_hard_wider_than_normal():
    # Hard must have a larger range than Normal — more choices means harder
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_range_unknown_difficulty_falls_back_to_default():
    # Any unrecognised string must return the Normal default
    low, high = get_range_for_difficulty("Impossible")
    assert low == 1
    assert high == 100

def test_range_is_case_sensitive():
    # "easy" (lowercase) is not a known key; must return the default
    low, high = get_range_for_difficulty("easy")
    assert low == 1
    assert high == 100


# ---------------------------------------------------------------------------
# update_score — scoring logic
# ---------------------------------------------------------------------------

def test_update_score_win_on_first_attempt():
    # Win on attempt 1: 100 - 10*(1+1) = 80
    score = update_score(0, "Win", 1)
    assert score == 80

def test_update_score_win_accumulates_on_existing_score():
    score = update_score(50, "Win", 1)
    assert score > 50

def test_update_score_win_never_awards_less_than_10():
    # Even a very late win should award at least 10 points
    score = update_score(0, "Win", 100)
    assert score >= 10

def test_update_score_too_low_always_penalizes():
    score = update_score(100, "Too Low", 1)
    assert score == 95

def test_update_score_too_high_always_penalizes():
    # Too High must reduce the score on both odd AND even attempts
    score_odd = update_score(100, "Too High", 1)
    score_even = update_score(100, "Too High", 2)
    assert score_odd < 100
    assert score_even < 100

def test_update_score_unknown_outcome_unchanged():
    # An unrecognised outcome must leave the score untouched
    score = update_score(100, "Tie", 1)
    assert score == 100
