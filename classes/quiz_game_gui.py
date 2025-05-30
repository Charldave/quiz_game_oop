# quiz_game_gui.py

import tkinter as tk
from tkinter import messagebox
import random
from classes.quiz_game_class import QuizGame

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x500+100+100")
        self.root.minsize(400, 400)
        self.root.configure(bg='#f0f0f0')

        #menu
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

        self.quiz = QuizGame("file_1.txt")
        self.quiz.load_questions()
        random.shuffle(self.quiz.questions)
        self.index = 0
        self.score = 0

        #progress and score
        self.progress_label = tk.Label(root, text="", bg='#f0f0f0', font=('Arial', 10))
        self.progress_label.pack(pady=5)
        
        self.score_label = tk.Label(root, text="Score: 0/0", bg='#f0f0f0', font=('Arial', 10))
        self.score_label.pack(pady=5)

        #question display
        self.question_label = tk.Label(root, text="", wraplength=400, 
                                     justify="left", bg='#f0f0f0', font=('Arial', 10))
        self.question_label.pack(pady=10)

        #choice buttons
        self.choice_buttons = {}
        button_colors = {'a': '#FF5722', 'b': '#2196F3', 'c': '#4CAF50', 'd': '#9C27B0'}
        for letter in ['a', 'b', 'c', 'd']:
            btn = tk.Button(root, text="", width=30, 
                          command=lambda l=letter: self.check_answer(l),
                          bg=button_colors[letter], fg='white',
                          font=('Arial', 10), padx=10, pady=5)
            btn.pack(pady=5)
            self.choice_buttons[letter] = btn

        self.load_question()

    def load_question(self):
        if self.index >= len(self.quiz.questions):
            messagebox.showinfo("Quiz Over", 
                              f"Your final score: {self.score}/{len(self.quiz.questions)}")
            self.root.quit()
            return

        self.progress_label.config(
            text=f"Question {self.index+1} of {len(self.quiz.questions)}")
        self.score_label.config(text=f"Score: {self.score}/{len(self.quiz.questions)}")

        block = self.quiz.questions[self.index]
        self.answer = block[5].split(')')[1].strip()
        self.question_label.config(text=block[0].strip())
        
        for letter in ['a', 'b', 'c', 'd']:
            self.choice_buttons[letter].config(text=block[ord(letter)-ord('a')+1].strip())

    def check_answer(self, user_choice):
        if user_choice == self.answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct! 🎉")
        else:
            messagebox.showinfo("Result", 
                              f"Wrong! The correct answer was {self.answer.upper()}.")
        
        self.index += 1
        self.load_question()