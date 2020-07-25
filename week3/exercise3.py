"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    is_int = False

    # Run the loop so long as is_int returns False
    while is_int == False:

        # Ask for an input, store it as a variable
        number_to_test = input(message)
        
        # Try to see if user_input is an integer.
        try:
            number_to_test = int(number_to_test)
        
        # If it's not an integer, do this...
        except:
            print('Hey... that is not a number. Try again. Jeez.')

        # Otherwise...
        else:
            is_int = True

    return int(number_to_test)


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    # Prompt the user for the range, test to see if it's acceptable
    acceptableLowerBound = False
    while not acceptableLowerBound:
      lowerBound = not_number_rejector('Okay, now enter a lower bound: ')
      if lowerBound < 1:
        print('Nah, too low. Gotta be at least 1.')
      else:
        acceptableLowerBound = True
    
    acceptableUpperBound = False
    while not acceptableUpperBound:
      upperBound = not_number_rejector('Okay, now enter an upper bound: ')
      if upperBound <= lowerBound:
        print('Gotta be more than the lower bounds.')
      else:
        acceptableUpperBound = True


    
    # Prompt the user to guess a number
    print("OK then, a number between {} and {} ?".format(lowerBound, upperBound))

    # Set an "actual number" variable that is a random integer between
    # the bounds
    actualNumber = random.randint(lowerBound, upperBound)

    # Set the state of the guess as False to start
    guessed = False

    # I used while guessed != True, is using booleans like "not" better?
    while not guessed:

        # Get the user to put in a number as a guess, store it as guessedNumber
        # Why are we using camelcase?
        acceptableGuessedNumber = False
        while not acceptableGuessedNumber:
          guessedNumber = not_number_rejector('Guess a number and only a number: ')
          if guessedNumber < lowerBound or guessedNumber > upperBound:
            print('That is outside the boundary that YOU set!')
          else:
            acceptableGuessedNumber = True
        

        # Print the result using the new formatting method
        print("You guessed {},".format(guessedNumber))

        # Check the result etc.
        if guessedNumber == actualNumber:
            print("Nice!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())