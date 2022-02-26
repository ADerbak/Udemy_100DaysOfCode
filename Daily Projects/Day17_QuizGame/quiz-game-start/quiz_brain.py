class QuizBrain:

    # Import question bank using Question objects
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    # TODO: 1. Ask a question

    def next_question(self):
        while self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?")
            self.check_answer(user_answer,current_question.answer)
        self.end_of_quiz()

# TODO: 2. Check if Correct
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"You current score is: {self.score}/{self.question_number}\n\n")
# TODO: 3. Check if we're at end of quiz

    def end_of_quiz(self):
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{len(self.question_list)}")