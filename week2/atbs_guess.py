# Guess the number

import random

secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask how many guesses they'd like, store it
print('How many guesses would you like?')
max_guesses = input()

# Ask the player to guess 5 times.
for guesses_taken in range(1, int(max_guesses) + 1): # Between 1 and wwhatever they want
    print('Take a guess.')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is too low')
    elif guess > secret_number:
        print('Your guess is too high')
    else:
        break # This is if they get it right

if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')

else:
    print('Nope. The number I was thinking of was ' + str(secret_number))