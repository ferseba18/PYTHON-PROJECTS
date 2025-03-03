import random

user_victories = 0
computer_victories = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Choose rock, paper or scissors. Type Q to quit: ').lower()
    if user_input == "q":
        break

    if user_input not in ['rock', 'paper', 'scissors']:
       continue

    random_number = random.randint(0, 2)
    
    computer_choice = options[random_number]
    # The random number variable will select a random number of the list of rock/paper/scissors options.
    # 0 stands for rock, 1 for paper and 2 for scissors.
    # The computer will pick at random one of the options.
    print(f'computer choice:', computer_choice + '.')

    if user_input == 'paper' and computer_choice == 'rock':
        print('You win!')
        user_victories += 1
        
    elif user_input == 'rock' and computer_choice == 'scissors':
        print('You win!')
        user_victories += 1
        
    elif user_input == 'scissors' and computer_choice == 'paper':
        print('You win!')
        user_victories += 1
        continue
    elif user_input == computer_choice:
        print('It is a tie!')
    else:
        print('Computer win!')
        computer_victories += 1

print(f'You won {user_victories} times.')
print(f'Computer won {computer_victories} times.')
if user_victories > computer_victories:
    print('You are the winner!')
elif user_victories == computer_victories:
    print('It is a draw!')
else:
    print('The computer is the winner!')

print('Game Over!')