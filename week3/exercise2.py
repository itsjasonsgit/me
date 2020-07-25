"""Week 3, Exercise 2.

An example of how a guessing game might be written.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")

    # Prompt the user to get a maximum number for the range
    upperBound = input("Enter an upper bound: ")
    
    # What is this formatting method?
    # Presumably it takes whatever is between the {} brackets
    # and inputs the upperboard/whatever data, which I guess
    # is better than tons of concantonation. Question is...
    # by Python logic, if I had multiple data to input, would it be like:
    # print("something {} then {} something {}".format(first, second, third))?
    # Yes, better yet - you can include placeholders within the {}
    # for readability.
    print("OK then, a number between 0 and {} ?".format(upperBound))

    # Turn the input number into an integer
    upperBound = int(upperBound)

    # Set an "actual number" variable that is a random integer between
    # 0 and whatever the upper bounds is
    actualNumber = random.randint(0, upperBound)

    # Set the state of the guess as False to start
    guessed = False

    # I used while guessed != True, is using booleans like "not" better?
    while not guessed:
        # Get the user to put in a number as a guess, store it as guessedNumber
        # Why are we using camelcase?
        guessedNumber = int(input("Guess a number: "))

        # Print the result using the new formatting method
        # Why is there a comma after the .format?
        print("You guessed {},".format(guessedNumber),)

        # Check the result etc.
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"

# wut
if __name__ == "__main__":
    exampleGuessingGame()
