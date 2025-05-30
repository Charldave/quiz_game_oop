#quiz_game_gui.py

import tkinter as tk
from tkinter import messagebox
import random
from classes.quiz_game_class import QuizGame

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.quiz = QuizGame("file_1.txt")
        self.quiz.load_questions()
        random.shuffle(self.quiz.questions)
        self.index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=10)

        self.choice_buttons = {}
        for letter in ['a', 'b', 'c', 'd']:
            btn = tk.Button(root, text="", width=30, command=lambda l=letter: self.check_answer(l))
            btn.pack(pady=2)
            self.choice_buttons[letter] = btn

        self.load_question()

    def load_question(self):
        if self.index >= len(self.quiz.questions):
            messagebox.showinfo("Quiz Over", f"Your score: {self.score}/{len(self.quiz.questions)}")
            self.root.quit()
            return

        block = self.quiz.questions[self.index]
        self.answer = block[5].split(')')[1].strip()
        self.question_label.config(text=block[0].strip())
        self.choice_buttons['a'].config(text=block[1].strip())
        self.choice_buttons['b'].config(text=block[2].strip())
        self.choice_buttons['c'].config(text=block[3].strip())
        self.choice_buttons['d'].config(text=block[4].strip())

    def check_answer(self, user_choice):
        if user_choice == self.answer:
            self.score += 1
        self.index += 1
        self.load_question()
