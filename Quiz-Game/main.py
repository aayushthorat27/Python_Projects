import os
import question_model
import data
import quiz_brain

os.system('cls')

question_bank = []

for i in data.question_data:
    question_bank.append(question_model.Question(i["question"], i["correct_answer"]))

quiz = quiz_brain.QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")