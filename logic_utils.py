def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the inclusive numeric range for a given difficulty level.

    Args:
        difficulty: One of ``"Easy"``, ``"Normal"``, or ``"Hard"``.
            Unrecognised values fall back to the Normal range.

    Returns:
        A ``(low, high)`` tuple of inclusive integer boundaries.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 1000
    return 1, 100


def parse_guess(
    raw: str | None, low: int, high: int
) -> tuple[bool, int | None, str | None]:
    """Parse and range-validate a raw user input string.

    Accepts integer strings and decimal strings (truncated to ``int``).
    Rejects non-numeric input and values outside ``[low, high]``.

    Args:
        raw: The raw string from the user input widget. ``None`` and
            empty strings are treated as missing input.
        low: Inclusive lower bound of the valid guess range.
        high: Inclusive upper bound of the valid guess range.

    Returns:
        A three-tuple ``(ok, guess_int, error_message)`` where:

        - ``ok`` is ``True`` if the input is a valid in-range integer.
        - ``guess_int`` is the parsed integer, or ``None`` on failure.
        - ``error_message`` is a human-readable string on failure,
          or ``None`` on success.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: int) -> str:
    """Compare a guess to the secret number and return an outcome string.

    Args:
        guess: The player's integer guess.
        secret: The secret integer to guess.

    Returns:
        ``"Win"`` if the guess matches the secret,
        ``"Too High"`` if the guess exceeds the secret, or
        ``"Too Low"`` if the guess is below the secret.
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(
    current_score: int, outcome: str, attempt_number: int
) -> int:
    """Apply a score delta based on the outcome of a single guess.

    Scoring rules:

    - **Win**: ``100 - 10 * (attempt_number + 1)``, floored at ``10``.
    - **Too Low**: ``-5`` points.
    - **Too High**: ``-10`` points (even attempt) or ``-5`` (odd attempt).
    - **Unknown outcome**: no change.

    Args:
        current_score: The score before this guess.
        outcome: One of ``"Win"``, ``"Too High"``, or ``"Too Low"``.
        attempt_number: The 1-based attempt count for this guess.

    Returns:
        The updated integer score.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score - 10
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
