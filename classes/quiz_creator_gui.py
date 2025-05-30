#quiz_creator_gui.py

import tkinter as tk
from tkinter import messagebox, ttk
from classes.quiz_creator_class import QuizCreator

class QuizCreatorGUI:
    def __init__(self, root):
        self.creator = QuizCreator("file_1.txt")
        self.root = root
        self.root.title("Quiz Creator")
        self.root.geometry("500x500")
        self.root.resizable(True, True)
        
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(self.main_frame, text="Question:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.question_entry = ttk.Entry(self.main_frame, width=50)
        self.question_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)
        
        choices_frame = ttk.LabelFrame(self.main_frame, text="Choices", padding="10")
        choices_frame.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(0, 10))
        
        self.choices = {}
        for i, letter in enumerate(['a', 'b', 'c', 'd']):
            ttk.Label(choices_frame, text=f"Choice {letter}:").grid(row=i, column=0, sticky=tk.W, padx=(0, 5))
            self.choices[letter] = ttk.Entry(choices_frame, width=40)
            self.choices[letter].grid(row=i, column=1, pady=2, sticky=tk.W)
        
        answer_frame = ttk.Frame(self.main_frame)
        answer_frame.grid(row=3, column=0, columnspan=2, pady=(0, 15), sticky=tk.W)
        
        ttk.Label(answer_frame, text="Correct Answer:").pack(side=tk.LEFT, padx=(0, 5))
        self.answer_var = tk.StringVar()
        self.answer_entry = ttk.Entry(answer_frame, textvariable=self.answer_var, width=5)
        self.answer_entry.pack(side=tk.LEFT)
        ttk.Label(answer_frame, text="(must be a, b, c, or d)").pack(side=tk.LEFT, padx=(5, 0))
        
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        
        self.submit_btn = ttk.Button(buttons_frame, text="Save Question", command=self.save_question)
        self.submit_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = ttk.Button(buttons_frame, text="Clear Fields", command=self.clear_fields)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        ttk.Label(self.main_frame, textvariable=self.status_var, relief=tk.SUNKEN).grid(
            row=5, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0))
    
    def save_question(self):
        q = self.question_entry.get()
        a = self.choices['a'].get()
        b = self.choices['b'].get()
        c = self.choices['c'].get()
        d = self.choices['d'].get()
        ans = self.answer_var.get().lower()

        if not q:
            messagebox.showerror("Error", "Question cannot be empty!")
            return
        if not all([a, b, c, d]):
            messagebox.showerror("Error", "All choices must be filled!")
            return
        if ans not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Answer must be a, b, c, or d.")
            return

        try:
            with open(self.creator.filename, 'a') as f:
                f.write(f"Q: {q}\n")
                f.write(f"a.) {a}\n")
                f.write(f"b.) {b}\n")
                f.write(f"c.) {c}\n")
                f.write(f"d.) {d}\n")
                f.write(f"ans.) {ans}\n")

            self.status_var.set("Question saved successfully!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save question: {str(e)}")
    
    def clear_fields(self):
        self.question_entry.delete(0, tk.END)
        for entry in self.choices.values():
            entry.delete(0, tk.END)
        self.answer_entry.delete(0, tk.END)
        self.status_var.set("Fields cleared. Ready for new question.")
        self.question_entry.focus_set()