import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Input must be greater than 0")
        quit()
else:
    print("Input must be a number")
    quit()

random_num = random.randint(0,top_of_range)
tries = 0
while True:
    tries += 1
    user_guess = input("Guess a number:")
    if user_guess.isdigit():
         user_guess = int(user_guess)
    else:
     print('You must type a number!')
     continue

    if user_guess == random_num:
        print('Correct!')
        break
    elif user_guess < random_num:
            print('Guess higher!')
    else:
            print('Guess lower!')
if tries == 1:
    print('Congratulations! You got it on your first try!')
else:
    print('Good Job! You got it in', tries, 'tries')