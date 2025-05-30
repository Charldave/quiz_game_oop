import random

with open('file_1.txt', 'r') as file_1:
    lines = file_1.readlines()

question_list = []
for i in range(0, len(lines), 6):
    set = lines[i:i+6]
    if len(set) == 6:
        question_list.append(set)

random.shuffle(question_list)

score = 0

for set in question_list:
    question = set[0].strip()
    a = set[1].strip()
    b = set[2].strip()
    c = set[3].strip()
    d = set[4].strip()
    answer = set[5].strip().split(')')[1].strip()

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

print(f"\nQuiz complete! Your score: {score}/{len(question_list)}")