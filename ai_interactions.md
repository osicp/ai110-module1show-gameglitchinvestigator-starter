# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

write PEP 8 compliant docstrings for logic_utils.py and review for style issues

**What did the agent do?**

Here are the exact steps, in order:

1. Read the file

Tool: Read on logic_utils.py
Purpose: see the current state before making any changes
2. Identified the following issues before editing:

Category	Issue
Docstrings	No Args / Returns sections on any function
Docstrings	parse_guess and update_score one-liners too terse for public functions
Type hints	check_guess had no parameter types (guess, secret untyped)
Type hints	parse_guess declared raw: str but the body handles None → should be str | None
Type hints	No return-type annotations on any function
Whitespace	Trailing spaces after return "Too High" and return "Too Low" (lines 49, 51)
Blank lines	Three blank lines between check_guess and update_score (PEP 8 requires exactly two)
Control flow	Redundant else after a return inside check_guess
3. Rewrote the file

Tool: Write on logic_utils.py
Changes made:
Added Google-style Args and Returns sections to all four functions
Added return-type annotations (-> tuple[int, int], -> tuple[bool, int | None, str | None], -> str, -> int)
Changed raw: str to raw: str | None in parse_guess
Added guess: int, secret: int type hints to check_guess
Removed trailing whitespace on the two return lines
Removed the extra blank line between functions
Removed the redundant else after return "Too High"
4. Type checker flagged a new error on line 85

The except TypeError fallback block compared g (a str) with secret (now explicitly typed int) — str > int is not valid
Root cause: that block was dead code left over from the A3 bug (even/odd secret cast), which had already been fixed in app.py
5. Removed the dead TypeError fallback block

Tool: Edit on logic_utils.py
Replaced the entire try/except TypeError construct in check_guess with three direct lines:

if guess == secret:
    return "Win"
if guess > secret:
    return "Too High"
return "Too Low"
No terminal commands were run. All changes were file edits only.

**What did you have to verify or fix manually?**

guess_int has type int | None — that comes from parse_guess's return type tuple[bool, int | None, str | None]. Even though line 99 is inside the else: branch (meaning ok is True, which guarantees guess_int is an int), the type checker can't infer that automatically from a flat tuple return. check_guess now declares guess: int, so passing int | None is a type mismatch.

The fix is one line — an assert immediately narrows the type to int for everything that follows:

Before line 99, add:


assert guess_int is not None
The block becomes:


    else:
        st.session_state.attempts += 1
        st.session_state.history.append(guess_int)
        assert guess_int is not None
        outcome = check_guess(guess_int, st.session_state.secret)
        message = OUTCOME_MESSAGES.get(outcome, "")
assert acts as a type guard — after it, pyright narrows int | None down to int and the type error on line 99 disappears. At runtime the assert is never reachable in a false state (because ok=True always pairs with a non-None guess_int), so it has zero effect on behavior — it exists purely to inform the type checker of what the logic already guarantees.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
write PEP 8 compliant docstrings for logic_utils.py and review for style issues
```

**Linting output before:**

```
BEFORE — 3 violations:


logic_utils.py:49:30  W291  trailing whitespace        ← return "Too High"  
logic_utils.py:51:29  W291  trailing whitespace        ← return "Too Low"   
logic_utils.py:62:1   E303  too many blank lines (3)   ← 3 blank lines before update_score
```

**Changes applied:**

AFTER — clean:


(no output)

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
