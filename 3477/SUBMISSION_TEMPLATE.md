# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3477/Pad Thai
```

OJ submission ID, if submitted:

```text
683168
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
30-60 minutes
```

Choose one:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

How to count this time:

- Count only the time you actively worked on this problem independently.
- Start counting from when you first read the problem.
- Do not include breaks, meals, classes, sleep, time spent on other problems, or time when you were not working on this problem.
- If you used AI, count only the independent time before your first AI prompt.
- If you asked a friend, TA, or instructor for help, count only the independent time before your first help request.
- If you used both AI and human help, count only the independent time before the first outside help of any kind.
- If you did not use AI or human help, count the time before writing this `submission.md`.
- An estimate is acceptable, but it must be honest.

---

## 2. My Understanding

Write the problem in your own words.

Also explain the input, output, and important constraints.

If you do not fully understand the problem yet, write what you currently understand. Your understanding may be incomplete or incorrect, but you must make a genuine attempt.

```text
The problem wants us to input the ingredients for making Pad Thai until the input is "Cook" before input the flavors until the input is "End". Then print what the chef says about the Pad Thai.
```

---

## 3. My First Plan

Write your first plan before getting help from AI, a friend, a TA, an instructor, or before finalizing your code.

If you used AI, write the plan you had before your first AI prompt.

If you asked a friend, TA, or instructor for help, write the plan you had before asking for help.

If you did not use AI or human help, write the plan you had before or while you started coding.

This can be rough. It may be incomplete or different from your final solution.

You may write pseudocode, a flowchart idea, or step-by-step thinking.

```text
Step 1: Create a set that contains the given ingredients for the Pad Thai.
Step 2: Create a set that contains the three required flavors.
Step 3: Create a loop for inputing ingredient until the input is "Cook" and store them in a set.
Step 4: Create another loop for inputing flavors until the input is "End" and store them in another set.
Step 5: Create a Boolean variable named invalid and set it to False.
Step 6: Use a for loop to check each ingredient. If an ingredient is not in the allowed ingredient set, set invalid to True.
Step 7: Create an if condition to check the ingredients and flavors in the given orders and print the output.
```

---

## 4. My Final Approach

Briefly explain the final algorithm or method you actually used in your submitted code.

This section is different from Section 3:

- Section 3 is your first plan before AI, human help, or before the final code.
- Section 4 is the final method used in your actual solution.
- If your final approach is the same as your first plan, write that it is the same and briefly explain why.

Do not copy AI's explanation.

Do not copy another person's explanation.

```text
Step 1: Create two sets each for the allowed ingredients and flavors.
Step 2: Create two empty sets for the ingredients used and the flavors used.
Step 3: Create a loop for inputing ingredient until the input is "Cook" and each ingredient to the set.
Step 4: Create another loop for inputing flavors until the input is "End" and each flavor to the set.
Step 5: Set invalid to False.
Step 6: Use a loop to check every ingredient in ingredients. If an ingredient is not in the allowed ingredient set, set invalid to True.
Step 7: Create an if condition to check the ingredients and flavors in the given orders:
- If invalid is True, print "This is not Pad Thai!!!".
- Elif the ingredients used do not contain all 11 required ingredients, print "This is bad!".
- Elif the flavors used are not exactly Sweet, Sour, and Salty, print "Not Bad...".
- Else, print "Delicious!".
```

---

## 5. My Tests

Write at least 3 test cases that you tried or designed by yourself.

Try to choose test cases that are different from each other.

For each test case, explain why you chose it.

If the input or output has many lines, write them inside the text blocks.

### Test Case 1

Why I chose this case:

```text
To test if the code's output is the same as in the testcases.
```

Input:

```text
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Peanuts
Cook
Sweet
Sour
End
```

Expected output:

```text
This is bad!
```

Actual output:

```text
This is bad!
```

Result:

```text
Pass
```

### Test Case 2

Why I chose this case:

```text
To test if the code's output is the same as in the testcases.
```

Input:

```text
Pad Thai Sauce
Tofu
Pickle Turnip
Shrimp
Bean Sprouts
Noodle
Chives
Lime
Egg
Oil
Peanuts
Cook
Sweet
Sour
Salty
Bitter
End
```

Expected output:

```text
Not Bad...
```

Actual output:

```text
Not Bad...
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
To see if the code works
```

Input:

```text
Pickle Turnip
Tofu
Lime
Shrimp
Cook
Sour
End
```

Expected output:

```text
This is bad!
```

Actual output:

```text
This is bad!
```

Result:

```text
Pass
```

---

## 6. AI Use

Did you use AI for this problem?

```text
No
```

If yes, also complete:

```text
ai_reflection.md
```

If you only asked a friend, TA, or instructor and did not use AI, you do not need to complete `ai_reflection.md`.

---

## 7. Human Help / Collaboration

Did you ask a friend, TA, instructor, or another person for help on this problem?

```text
Yes
```

If yes, briefly explain what kind of help you received.

Allowed examples:

- explanation of the problem statement
- explanation of a programming concept
- hint about the approach
- debugging discussion
- test-case discussion
- help understanding an error message

Not allowed:

- copying another person's code
- submitting another person's solution
- asking another person to write the solution for you
- using another person's OJ submission
- asking another person to submit to the OJ for you

Who helped you?

```text
A friend
```

What did they help with?

```text
Telling me about using invalid for the loop part
```

What did you still do by yourself?

```text
Writing and figuring out how to use the invalid like what my friend suggested
```

Did you copy any code from another person?

```text
No
```

---

## 8. Student Declaration

Write `Yes` for each statement.

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
