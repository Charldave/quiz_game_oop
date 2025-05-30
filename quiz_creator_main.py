confirmation = input('Create a new set of question? Yes(new set) No(append questions): ').lower()
if confirmation == "yes":
    file_1 = open('file_1.txt', 'w')
elif confirmation == "no":
    file_1 = open('file_1.txt', 'a')
else:
    print('Please try again.')
    exit()

while True:
    question = input('Enter question or type "exit" to stop: ')
    if question.lower() == 'exit':
        break
    choice_a = input('Enter choice letter "a": ')
    choice_b = input('Enter choice letter "b": ')
    choice_c = input('Enter choice letter "c": ')
    choice_d = input('Enter choice letter "d": ')
    
    answer = ''
    while answer not in ['a', 'b', 'c', 'd']:
        answer = input('Enter the letter of the correct answer: ')
    
    file_1.write(f'Q: {question}\n')
    file_1.write(f'a.) {choice_a}\n')
    file_1.write(f'b.) {choice_b}\n')
    file_1.write(f'c.) {choice_c}\n')
    file_1.write(f'd.) {choice_d}\n')
    file_1.write(f'ans.) {answer}\n')
file_1.close()