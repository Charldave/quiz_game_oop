#quiz_creator_class.py

class QuizCreator:
    def __init__(self, filename):
        self.filename = filename

    def create_quiz(self, mode):
        mode_flag = 'w' if mode == 'yes' else 'a'
        with open(self.filename, mode_flag) as file:
            while True:
                question = input('Enter question or type "exit" to stop: ')
                if question.lower() == 'exit':
                    break
                a = input('Enter choice letter "a": ')
                b = input('Enter choice letter "b": ')
                c = input('Enter choice letter "c": ')
                d = input('Enter choice letter "d": ')
                answer = ''
                while answer not in ['a', 'b', 'c', 'd']:
                    answer = input('Enter the correct answer (a/b/c/d): ')
                file.write(f'Q: {question}\n')
                file.write(f'a.) {a}\n')
                file.write(f'b.) {b}\n')
                file.write(f'c.) {c}\n')
                file.write(f'd.) {d}\n')
                file.write(f'ans.) {answer}\n')