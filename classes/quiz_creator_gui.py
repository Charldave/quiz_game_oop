#quiz_creator_gui.py

import tkinter as tk
from tkinter import messagebox
from classes.quiz_creator_class import QuizCreator

class QuizCreatorGUI:
    def __init__(self, root):
        self.creator = QuizCreator("file_1.txt")

        self.root = root
        self.root.title("Quiz Creator")

        self.question_entry = tk.Entry(root, width=50)
        self.question_entry.pack(pady=5)
        self.choices = {}
        for letter in ['a', 'b', 'c', 'd']:
            self.choices[letter] = tk.Entry(root, width=40)
            self.choices[letter].pack(pady=2)

        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var, width=5)
        self.answer_entry.pack(pady=5)

        self.submit_btn = tk.Button(root, text="Save Question", command=self.save_question)
        self.submit_btn.pack(pady=10)

    def save_question(self):
        q = self.question_entry.get()
        a = self.choices['a'].get()
        b = self.choices['b'].get()
        c = self.choices['c'].get()
        d = self.choices['d'].get()
        ans = self.answer_var.get().lower()

        if ans not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Answer must be a, b, c, or d.")
            return

        with open(self.creator.filename, 'a') as f:
            f.write(f"Q: {q}\n")
            f.write(f"a.) {a}\n")
            f.write(f"b.) {b}\n")
            f.write(f"c.) {c}\n")
            f.write(f"d.) {d}\n")
            f.write(f"ans.) {ans}\n")

        messagebox.showinfo("Saved", "Question saved!")
        self.question_entry.delete(0, tk.END)
        for entry in self.choices.values():
            entry.delete(0, tk.END)
        self.answer_entry.delete(0, tk.END)