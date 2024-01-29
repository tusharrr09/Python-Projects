import random

#define function
def guess(x):                                # x is range of random number
    random_number = random.randint(1,x)      # randint is random integer
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Wrong, guess again. Too low.')
        elif guess > random_number:
            print('Wrong, guess again. Too high.')

    print(f'Yay, congrats. You guessed the number {random_number} correctly.')

guess(10)                               #upto which value to choose