# Problem Solving Submission

This file must be written by the student in their own words.

Use this template only for OJ problems that are marked as learning-log required.

Do not ask AI to write this file for you. AI may help check grammar, formatting, or clarity after you have written your own content.

If AI was used for this learning-log-required problem, also complete `ai_reflection.md`.

---

## 1. OJ Information

OJ problem number/title:

```text
3160/หาจำนวนเฉพาะ
```

OJ submission ID, if submitted:

```text
635569
```

OJ status:

```text
Pass
```

Independent time spent on this problem:

```text
0-15 minutes
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
The problem wants us to find all prime numbers within the given input range and count how many prime numbers there are.
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
Step 1: Create a split input variable.
Step 2: Set count to be 0.
Step 3: Create a loop and if command.
Step 4: Ignore numbers smaller than 2.
Step 5: Assume the current number is prime.
Step 6: Try dividing the number by numbers from 2 up to one less than itself. If it can be divided evenly, it is not prime.
Step: 7: If it is still prime, add it to the result and increase count by 1. If at least one prime number is found, display the prime numbers.
Step 8: Print all the total prime numbers.
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
Step 1: Create a split input variable for start as the beginning of the range and end as the end of the range.
Step 2: Set count to be 0 and set result as an empty string.
Step 3: Create a loop for number to be in the range of start and end.
Step 4: Create a if command inside. If number is less than 2, then skip. Then set prime as True.
Step 5: Create a second loop inside for divisor to start from 2 to number - 1.
Step 6: Create a second if command inside. If number divides(%) with divisor equals 0, set prime as False and stop checking the number.
Step: 7: Create a third if command outside the second loop. If prime is True, then add number to result and increase by 1.
Step 8: Create a forth if command outside the first loop. If count is more than 0, then print the result.
Step 9: Print "Total primes: " and count.
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
1 10
```

Expected output:

```text
2 3 5 7
Total primes: 4
```

Actual output:

```text
2 3 5 7
Total primes: 4
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
32 36
```

Expected output:

```text
Total primes: 0
```

Actual output:

```text
Total primes: 0
```

Result:

```text
Pass
```

### Test Case 3

Why I chose this case:

```text
To see if the code displays the correct answers
```

Input:

```text
50 75
```

Expected output:

```text
53 59 61 67 71 73
Total primes: 6
```

Actual output:

```text
53 59 61 67 71 73
Total primes: 6
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
Teaching, helping, and explaining how to do this code
```

What did you still do by yourself?

```text
Writing the code after what my friend taught
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
