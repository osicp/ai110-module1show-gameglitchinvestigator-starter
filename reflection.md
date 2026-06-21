# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game felt very glitchy. The functionality had many errors. The logic made no sense. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. The enter/submit buttom was not intercepted by code on the first try.
2. The difficulty setting and logic was backwards.
3. The new game game button only refreshed the attempt but did not reset the game


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|   5   |Too Low, GO HIGHER |Too Low, GO LOWER|     📉 Go LOWER!       |
|   7   |Too high, GO LOWER |Too high, GO HIGHER |  📈Go HIGHER!       |
|   101 | Out of range      |Too high, GO HIGHER |  📈Go HIGHER!       |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude as a macro AI debugger.I used Copilot for inline pre-filling.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I was entering the FIXME comments, Copilot auto-fill feature kept pre filling information about the bug I had already found. I used this to expedite my work always verifying that aligns with my intentions. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
In app.py line 108 the intented FIXME comment should've been: FIXME: st. subheader anchor is not set correctly, and the link does not scroll to the guess input. But instead Copilot suggested FIXME: Subheader is misleading since the user has not made a guess yet. It should be something like "Welcome to the Glitchy Guesser!" or "Try to guess the secret number!"
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Once I found the bugs, I prompted Claude to create a test and eval suite based on my findings. When I ran the tests and evals it failed as predicted. Then I corrected the bugs manually and all tests and evals passed. 

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I tested the app for inputs out of range using pytest. The test failed showing the code still accepted the input. Once the bug was fixed manually, the test passed assuring bug was indeed fixed.

- Did AI help you design or understand any tests? How?
Yes, I used Claude to create an architecture.md to then use the same as a reference to build a test suite. Copilot helped me fix the bugs manually.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit "reruns" happens when a user interacts with a widget or pressing a button streamlit automatically rewinds and runs your entire Python script from the first line to the last.
Streamlit session state is your app's short-term memory that survives the rerun. It forgets everything only when the user closes or refreshes the browser.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I liked the overall process: starting with documenting bugs (commit), drafting initial architectural model (commit), build test and eval suites with found bugs (commit), Refactor and fix code based on referenced files (commit), run pytest (commit), apply AI suggested code quality and linting (commit), and final documentation (final commit)

- What is one thing you would do differently next time you work with AI on a coding task?
I would try to be more specific. In the sense that intead of ask AI to find a bug in a block of code, I would ask AI what would be the most efficient way to correct a bug in xx line of a block of code that has y functionality.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
Definately considering AI more as a knowledgable teamate. Also using different AIs for different tasks.
