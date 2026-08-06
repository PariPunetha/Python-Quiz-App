import time
print("=" *40)
print("WELCOME TO THE QUIZ GAME!")
print("=" *40)
start_time = time.time()
score = 0
questions = ["What is the capital of India?",
              "Which keyboard is used to create a function in python?",
              "What does CPU stand for?",
              "What is the full form of RAM?",
              "What is the full form of ROM?"]
options = [["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
           ["A. Ctrl", "B. Alt", "C. Shift", "D. Tab"],
           ["A. Central Processing Unit", "B. Computer Processing Unit", "C. Central Program Unit", "D. Computer Program Unit"],
           ["A. Random Access Memory", "B. Read Access Memory", "C. Real Access Memory", "D. Rapid Access Memory"],
           ["A. Read-Only Memory", "B. Read-Only Machine", "C. Random-Only Memory", "D. Random-Only Machine"]]
answers = ["A", "C", "A", "A", "A"]
for i in range(len(questions)):
    print(f"\nQuestion {i+1}: {questions[i]}")
    for option in options[i]:
        print(option)
    user_answer = input("Your answer: ").strip()
    if user_answer.upper() == answers[i]:
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is: {answers[i]}")

end_time = time.time()
print("\nQuiz Completed!")
print(f"\n{'=' * 50}")
print(f"Time taken to complete the quiz: {end_time - start_time:.2f} seconds")
print(f"Your final score is: {score}/{len(questions)}")
print(f"Your percentage score is {(score/len(questions))*100}%")
print(f"{'=' * 50}")
percentage = (score/len(questions))*100
if percentage >= 80:
    print("Excellent! You have a great knowledge.")
elif percentage >= 50:
    print("Good job! You have a decent understanding.")
else:
    print("You need to improve. Keep learning!")
while True:
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("\nRestarting the quiz...\n")
        break
    elif play_again == "no":
        print("\nThank you for playing the quiz! Goodbye!")
        break
    else:
        print("Please enter 'yes' or 'no'.")