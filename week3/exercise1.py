# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    # Start and stop are values (integers presumably) that'll be parsed into the function
    # This is how I'd do it using a a loop
    my_loop_list = [] # Set an empty list
    i = start # Start the loop counter at whatever the start value is
    while i < stop: # If i (the initial step) is less than the stop number, keep looping
        my_loop_list.append(i) # Append the current step amount
        i += step # Increase the loop counter as per the step amount
  
    return my_loop_list




def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    # He means create a function that does the same thing as range, I guess?
    # Wrap it in a 1:1 way is the most absurd way of describing anything.
    # What does "wrap it" even mean? What is "it" - the docs? The functionality of range?
    # How do you "wrap" the functionality something?
    # What is 1:1 - why is there a ratio involved here?
    # I have no idea what that means.

    # I guess then, while start < stop is the same as for i in range()
    # I suppose the function I'd be "duplicating" is:
    # my_list = [start]
    # for i in range(start, stop, step)
    #   my_list.append(step)
    # return my_list

    my_list = [] # Create an empty list

    # I don't *need* to do this, but I think it makes the code more
    # readable and could possibly reduce errors by not changing
    # the "start" variable, which could be used in other parts of the code.\
    i = start 

    while i < stop: # If the iteration is less than stop, keep loopin'
        my_list.append(i) # Appends the start number to begin with, then...
        i += step # For each iteration, add the step amount
    return my_list # Done


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """

    my_list = []
    i = start
    while i < stop:
        my_list.append(i)
        i += 2
    return my_list



def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    answer = False
    while answer != True:
        print('Guess a number between a range...')
        user_guess = int(input()) # Ask the user to input an integer
        print('You guessed ' + str(user_guess))
        if user_guess < high and user_guess > low: # If the guess is within a range...
            answer = True
        else: # Otherwise, run the loop again.
            print('Wrong. Try again.')
  
    # Oh, you're here. I guess that means answer = True so...
    print('Nice guess! The answer was between ' + str(low) + ' and ' + str(high) + '.')
    return user_guess # Not necessary? But if you don't do this the test will fail



def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    

    is_int = False

    # Run the loop so long as is_int returns False
    while is_int == False:

        # Ask for an input, store it as a variable
        user_input = input('Gimme a number. Not a word. Do not test me: ')
        
        # Try to see if user_input is an integer.
        try:
            user_input = int(user_input)
        
        # If it's not an integer, do this...
        except:
            print('I said do not test me!')

        # Otherwise...
        else:
            print('Nice.')
            is_int = True

    print(user_input)
    return user_input


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """

    # Meaning a function that asks for a number...
    # Tests to see if it's actually a number..
    # Then checks if its between a range.

    answer = False
    while answer != True:
        print('Guess a number between a range...')
        user_guess = not_number_rejector('') # User the previous function
        print('You guessed ' + str(user_guess))
        if user_guess < high and user_guess > low:
            answer = True
        else:
            print('Wrong. Try again.')
  
    print('Nice guess! The answer was between ' + str(low) + ' and ' + str(high) + '.')
    return user_guess


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
