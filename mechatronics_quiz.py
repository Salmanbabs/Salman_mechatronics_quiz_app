# Mechatronics Quiz App

questions = [
    {
        "question": "What does a sensor do in a mechatronic system?",
        "options": ["A. Produces motion", "B. Detects changes", "C. Stores fuel", "D. Makes noise"],
        "answer": "B"
    },
    {
        "question": "Which component produces mechanical motion?",
        "options": ["A. Actuator", "B. Sensor", "C. Resistor", "D. Switch"],
        "answer": "A"
    },
    {
        "question": "What does CPU mean?",
        "options": ["A. Central Processing Unit", "B. Control Power Unit", "C. Computer Personal Unit", "D. Central Power User"],
        "answer": "A"
    },
    {
        "question": "Which of these is an input device?",
        "options": ["A. Motor", "B. Actuator", "C. Sensor", "D. Wheel"],
        "answer": "C"
    },
    {
        "question": "Mechatronics combines mechanics, electronics and:",
        "options": ["A. Cooking", "B. Computing", "C. Farming", "D. Painting"],
        "answer": "B"
    }
]

# Function that checks the user's answer
def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer


score = 0
wrong_answers = []

print("================================")
print("   WELCOME TO MECHATRONICS QUIZ")
print("================================")

# Ask each question
for item in questions:
    print("\n" + item["question"])

    for option in item["options"]:
        print(option)

    # Keep asking until the user enters a valid answer
    while True:
        answer = input("Enter A, B, C or D: ").upper()

        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid answer! Please enter A, B, C or D.")

    # Check if the answer is correct
    if check_answer(answer, item["answer"]):
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")
        wrong_answers.append({
            "question": item["question"],
            "your_answer": answer,
            "correct_answer": item["answer"]
        })

# Calculate the final percentage
percentage = int((score / len(questions)) * 100)

print("\n========== QUIZ RESULT ==========")
print("Your score:", score, "out of", len(questions))
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent! You really know your Mechatronics.")
elif percentage >= 50:
    print("Good job! Keep practising.")
else:
    print("Don't give up. Read more and try again!")

# Our own twist: show corrections for wrong answers
if len(wrong_answers) > 0:
    print("\n--- QUESTIONS YOU GOT WRONG ---")

    for item in wrong_answers:
        print("\nQuestion:", item["question"])
        print("Your answer:", item["your_answer"])
        print("Correct answer:", item["correct_answer"])
else:
    print("\nPerfect score! You got everything correct! 🎉")