#quiz_questions_main.py
from tkinter import Tk
from classes.quiz_game_gui import QuizGameGUI

root = Tk()
app = QuizGameGUI(root)
root.mainloop()