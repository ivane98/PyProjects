import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or type Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    computer_pick = random.choice(options)

    if user_input == computer_pick:
        print('it is a tie!')
    elif user_input == 'rock' and computer_pick == 'scissors':
        print('you win!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('you win!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('you win!')
        user_wins += 1
    else:
        print('You lost')
        computer_wins += 1
        

print('User won', user_wins, 'times')
print('Computer won', computer_wins, 'times')
print('Goodbye')

