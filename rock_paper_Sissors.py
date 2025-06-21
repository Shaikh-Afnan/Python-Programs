import random

def u_choice(user):
    '''This function converts single character user response to the corresponding choice letter
    i.e. "r" converted to Rock'''
    if user == 'r':
        return 'Rock'
    elif user == 'p':
        return 'Paper'
    elif user == 's':
        return 'Scissors'

#                   Making a list of Choices
choice_list = ['Rock' , 'Paper' , 'Scissors']
u_score = 0
c_score = 0

print('Play rock paper scissors type your Choice(r = rock , p = paper , s = scissors)')
print('Press type q to quit')
while u_score < 5 and c_score < 5 :
    choice = random.choice(choice_list)
    user = input()
    if user == 'r' and choice == 'Scissors':
        u_score += 1
        print(f'You chose {u_choice(user)} and Computer chose {choice}, Scores = User : {u_score}    Computer = {c_score} .')
    elif user == 'p' and choice == 'Rock':
        u_score += 1
        print(f'You chose {u_choice(user)} and Computer chose {choice}, Scores = User : {u_score}    Computer = {c_score} .')
    elif user == 's' and choice == 'Paper':
        u_score += 1
        print(f'You chose {u_choice(user)} and Computer chose {choice}, Scores = User : {u_score}    Computer = {c_score} .')
    elif u_choice(user) == choice:
        print(f'Both chose {choice}, Scores = User : {u_score}    Computer = {c_score} .')
    elif choice == 'Rock' and user == 's':
        c_score += 1
        print(f'You chose {u_choice(user)} and Computer chose {choice}, Scores = User : {u_score}    Computer = {c_score} .')
    elif choice == 'Paper' and user == 'r':
        c_score += 1
        print(f'You chose {u_choice(user)} and Computer chose {choice}, Scores = User : {u_score}    Computer = {c_score} .')
    elif choice == 'Scissors' and user == 'p':
        c_score += 1
        print(f'You chose {u_choice(user)} and Computer chose {choice}, Scores = User : {u_score}    Computer = {c_score} .')
    elif user == 'q':
        print('Thank you for playing')
        break
    else:
        print('Invalid Choice')

if u_score == 5:
    print('Congratulations you Won !')
else:
    print('The Computer Won , Better Luck Next Time')