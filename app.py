import random

options_dict = {'scissors':'paper', 'rock':'scissors', 'paper':'rock'}
options = ['rock', 'paper', 'scissors']
computer_choice = ""

def check_for_winner(computer_choice, user_choice):
    for x in options_dict:
        if computer_choice.lower() == x and user_choice.lower() == options_dict[x]:
            return 'Computer wins!'
        else:
            return 'User wins!'    

running = True

while running:
    print('Welcome to Rock, Paper, Scissors! A fun game coded in Python.')
    print('You may type exit to exit the game.')
    print('-------------------------------------------------')
    user_choice = input('Please type rock, paper, or scissors: ')
    if user_choice.lower() in options:
        computer_choice = random.choice(options)
        print('The computer picked: ' + computer_choice)
        if computer_choice.lower() == user_choice.lower():
            print('tie!')   
        elif computer_choice.lower() != user_choice.lower():
            print(check_for_winner(computer_choice, user_choice))
    elif user_choice == 'exit':
        break  
    elif not user_choice in options:
        print('oops that is not a valid move!')    


