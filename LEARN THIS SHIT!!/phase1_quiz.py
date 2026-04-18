#!/usr/bin/env python3
"""
Phase 1 Quick Quiz - Test your Python basics!
Topics: Variables/Data Types, I/O, Conditionals, Loops, Data Structures, Functions, OOP.
Answer all 10 questions. Enter answers as specified (case-insensitive).
"""

questions = [
    {
        "q": "1. What is the data type of 'Hello'? (str/int/float/bool)",
        "a": "str"
    },
    {
        "q": "2. Which syntax creates a variable? (A: var = 5, B: 5 = var, C: var(5))",
        "a": "a"
    },
    {
        "q": "3. What does input() always return? ",
        "a": "str"
    },
    {
        "q": "4. Output of if age >= 18: print('Adult') else: print('Minor') for age=16?",
        "a": "minor"
    },
    {
        "q": "5. For loop iterates over what? (list/str/range)",
        "a": "iterable"
    },
    {
        "q": "6. What prevents infinite while loop? ",
        "a": "update"
    },
    {
        "q": "7. List indexing starts at? (0/1)",
        "a": "0"
    },
    {
        "q": "8. How to access dict value? (user['name']/user.name)",
        "a": "user['name']"
    },
    {
        "q": "9. Keyword to define function? ",
        "a": "def"
    },
    {
        "q": "10. In class, instance vars use? (self/other)",
        "a": "self"
    }
]

def run_quiz():
    print("=== Phase 1 Quiz ===")
    score = 0
    for i, item in enumerate(questions, 1):
        print(f"\n{item['q']}")
        ans = input("Your answer: ").strip().lower()
        if ans in item['a'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct: {item['a']}")
    
    percent = (score / 10) * 100
    print(f"\nScore: {score}/10 ({percent:.0f}%)")
    if percent >= 90:
        print("Excellent! Mastered Phase 1.")
    elif percent >= 70:
        print("Good! Review weak areas.")
    else:
        print("Keep learning! Reread phase1.py.")

if __name__ == "__main__":
    run_quiz()

