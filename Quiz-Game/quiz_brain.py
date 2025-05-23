class QuizBrain:

    def __init__(self,list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        # if len(self.question_list) == self.question_number:
        #     return False
        # return True
        return len(self.question_list) != self.question_number

    def next_question(self):
        answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(answer,self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number+1}")
        print("\n")

