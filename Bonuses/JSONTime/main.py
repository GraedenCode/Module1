import json

with open("questions.json") as file:
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"])
    for i , alternative in enumerate(question["alternatives"]):
        print("    ",i+1, alternative)

    user_answer = int(input("Choose a number : "))
    question["user_choice"] = user_answer

score = 0

for i,question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "CORRECT"
    else:
        result = "WRONG"

    message = f"{i + 1} -{result}- Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}."
    print(message)

print("\n", score, "/", len(data))