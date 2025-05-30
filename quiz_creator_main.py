#quiz_creator_main.py
from tkinter import Tk
from classes.quiz_creator_gui import QuizCreatorGUI

root = Tk()
app = QuizCreatorGUI(root)
root.mainloop()