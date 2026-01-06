playing = input("Do you want to play? ")
if playing.lower() !="yes":
    print("Maybe next time 👋")
    exit()
else:
    print("Game starts 🙂")

score=0

questions={
    "What CPU stands for?":"central processing unit",
    "What GPU stands for? ":"graphics processing unit",
    "What RAM stands for? ":"random access memory",
    "What ROM stands for? ":"read only memory"
    
}
score = 0

for question, correct_answer in questions.items():
    answer = input(question).lower()
    if answer == correct_answer:
        print("Correct ✅")
        score += 1
    else:
        print("Incorrect ❌")

total_questions = len(questions)
percentage = (score / total_questions) * 100

print(f"\nYou got {score} out of {total_questions} correct.")
print(f"Your score: {percentage:.2f}%")

