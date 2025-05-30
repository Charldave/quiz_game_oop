#quiz_game_class.py

import random

class QuizGame:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def load_questions(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        for i in range(0, len(lines), 6):
            block = lines[i:i+6]
            if len(block) == 6:
                self.questions.append(block)

    def start(self):
        random.shuffle(self.questions)
        score = 0

        for block in self.questions:
            question = block[0].strip()
            a = block[1].strip()
            b = block[2].strip()
            c = block[3].strip()
            d = block[4].strip()
            answer = block[5].split(')')[1].strip()

            print(f"\n{question}")
            print(a)
            print(b)
            print(c)
            print(d)

            user_answer = input("Pick your answer (a/b/c/d): ").lower()
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. Correct answer is ({answer})")

        print(f"\nQuiz complete! Your score: {score}/{len(self.questions)}")