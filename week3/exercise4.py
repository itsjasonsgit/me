# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    # Set the tries and final guess to 0
    tries = 0
    guess = 0

    # Split the initial search range in half
    guess = int(high - ((high - low) / 2))
    print(guess)

    # If the guess does not equal the actual number we're looking for
    while guess != actual_number:
        # Figure out what the midpoint is between
        guess = int(high - ((high - low) / 2))

        # If the guess is greater than the actual number
        if guess > actual_number:
            # We slice out the values that are higher than the guess
            # The highest search value thgen becomes the guess
            # And - 1 removes the current number from the guess range
            high = guess - 1
            
            # Add one to tries
            tries += 1

        # If the guess is less than the actual number
        elif guess < actual_number:
            # We slice out the values that are LOWER than the guess
            # The guess beceomes the LOWEST number
            # And + to remove the current guess from the range
            low = guess + 1
            
            # Add one to tries
            tries += 1

    # Otherwise, we're done
    else:
        print('Got it!')
        print(guess)

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
