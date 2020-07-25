# -*- coding: UTF-8 -*-
"""Modify each function until the tests pass."""


def is_odd(a_number):
    """Return True if a_number is odd, and False if a_number is even.

    Look into modulo division using the '%' operator as one way of doing this.
    """
    # if a_number divided by 2 has a remainder (not 0), then it MUST be uneven.
    # Otherwise, it's even.

    if((a_number % 2) != 0):
        return True
    else:
        return False


def fix_it(moves=True, should_move=True):
    """Decide what to do.

    Using the engineering flowchart (in week2 folder of the CODE1161-2019
    repo engineeringFlowchart.png) for the rules, return the apropriate
    response to the input parameters.
    Use conditional statements: if, else, elif etc.
    This function should return either:
    "WD-40"
    "Duct Tape"
    "No Problem"

    Most people write this function with 4 return statements. 
    As an extra challenge, see if you can get that down to three.
    """

    # As per the flowchart:
    # If it doesn't move and should, it's WD-40
    # If it moves and should move, it's Duct Tape
    # If it doesn't move and shouldn't move, or if it moves and should move, it's no problem
    if moves == should_move:
        return "No Problem"
    elif moves and not should_move:
        return "Duct Tape"
    elif not moves and should_move:
        return "WD-40"


def loops_1a():
    """Make 10 stars.

    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
 
    # We do this using append, adding one star to the existing variable
    # for each loop until we have 10.

    stars = []
    for i in range(10):
        stars.append("*")
    
    return stars


def loops_1c(number_of_items=5, symbol="#"):
    """Respond to variables.

    Using any method, return a list of number_of_items items, each one a
    string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']
    """

    hash_list = [] # Create an empty list for the hashes

    for i in range(number_of_items): # Start a loop based off a range from parameter number_of_items
        hash_list.append(symbol) # Append a symbol from the parameter each loop

    return hash_list


def loops_2():
    """Make a big square starfield.

    return a list of 10 items, each one a list of 10 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
          ]
    """

    star_list = [] # Create an empty list for the stars

    for i in range(10): # Start a loop that runs 10 times
        star_list.append('*') # Append a star to the list each loop

    star_block = [] # Now that we have our star list, create a star block

    for i in range(10): # Start a loop that runs 10 times
        star_block.append(star_list) # Append the previous star list to the loop 10 times

    return star_block



def loops_3():
    """Make a rising block of numbers.

    Return this:
    [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
        ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
        ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
        ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
        ['6', '6', '6', '6', '6', '6', '6', '6', '6', '6'],
        ['7', '7', '7', '7', '7', '7', '7', '7', '7', '7'],
        ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
        ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
    ]
    remember that range(10) produces a list of numbers from 0...9
    So for every step produced by `for i in range(10):` i is a different number
    TIP: notice that this needs to to return strings of numbers,
         so call str(number) to cast.
    """
    number_block = [] # Create an empty list for the number block
    for i in range(10): # Run the loop 10 times
        
        current_loop = i # Set a variable that is the current loop number
        number_list = [] # Reset the number list (otherwise it keeps accumulating numbers from prior loops)
        
        for i in range(10): # Run the loop 10 times
            number_list.append(str(0 + current_loop)) # Fill the list with 10 numbers that are the current loop's number + the previous loop's number
        
        number_block.append(number_list) # Append the number list to the number block
    
    return number_block

 
def loops_4():
    """Make a block of numbers that rises left to right.

    Return this:
    [
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    """
    number_list = []
    for i in range(10): 
        number_list.append(str(i)) # For each loop, append the current loop counter to number_list
    
    number_block = []
    for i in range(10):
        number_block.append(number_list) # Each loop, append the rising number block

    return number_block


def loops_5():
    """Make the coordinates of the block.

    Return this:
    [
      ['(i0, j0)', '(i0, j1)', '(i0, j2)', '(i0, j3)', '(i0, j4)'],
      ['(i1, j0)', '(i1, j1)', '(i1, j2)', '(i1, j3)', '(i1, j4)'],
      ['(i2, j0)', '(i2, j1)', '(i2, j2)', '(i2, j3)', '(i2, j4)'],
      ['(i3, j0)', '(i3, j1)', '(i3, j2)', '(i3, j3)', '(i3, j4)'],
      ['(i4, j0)', '(i4, j1)', '(i4, j2)', '(i4, j3)', '(i4, j4)'],
      ['(i5, j0)', '(i5, j1)', '(i5, j2)', '(i5, j3)', '(i5, j4)'],
      ['(i6, j0)', '(i6, j1)', '(i6, j2)', '(i6, j3)', '(i6, j4)'],
      ['(i7, j0)', '(i7, j1)', '(i7, j2)', '(i7, j3)', '(i7, j4)'],
      ['(i8, j0)', '(i8, j1)', '(i8, j2)', '(i8, j3)', '(i8, j4)'],
      ['(i9, j0)', '(i9, j1)', '(i9, j2)', '(i9, j3)', '(i9, j4)']
    ]

    TIP:
    You can construct strings either by concatinating them:
        "There are " + str(8) + " green bottles"
    or by using format:
        "There are {} green bottles".format(8)
    you'll come to see the pros and cons of each over time.
    """

    coordinate_block = []

    for i in range(10):
        
        block_loop = i
        coordinate_list = []
        
        for i in range(5):
            coordinate_list.append('(i' + str(block_loop) + ', j' + str(i) + ')')
        
        coordinate_block.append(coordinate_list)

    return coordinate_block


def loops_6():
    """Make a wedge of numbers.

    Return this:
    [
      ['0'],
      ['0', '1'],
      ['0', '1', '2'],
      ['0', '1', '2', '3'],
      ['0', '1', '2', '3', '4'],
      ['0', '1', '2', '3', '4', '5'],
      ['0', '1', '2', '3', '4', '5', '6'],
      ['0', '1', '2', '3', '4', '5', '6', '7'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    You don't have to use a literal number in the range function.
    You can use a variable.
    TIP: look out for the starting condition.
    """
    import copy

    wedge_list = []
    wedge_block = []
    for i in range(10):
        wedge_list.append(str(i)) # Append a number to the list from on the loop i

        # Copy the list into a new_list so when we append, it doesn't always reference
        # the original list. This seems kinda wrong, but it works. It doesn't work
        # if I just append wedge_list to wedge_block, presumably because of the reference
        # / mutability issue?
        new_list = copy.copy(wedge_list) 

        # append the copied list
        wedge_block.append(new_list)

    return wedge_block

    # I could probably do this properly by assigning a variable as the range which
    # would be the 0 + iteration, that'd fix it? It's fewer lines of code this way, though.



def loops_7():
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    or in more simple terms:
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    (this is what will print when you test from inside this file)
    This is a hard problem. Use lots of experimentation and draw
    lots of diagrams!
    """

    import copy

    pyramid_list = []
    
    pyramid_length = 9
    pyramid_height = 5
    
    for i in range(pyramid_height):

        # Empty the block list
        pyramid_block_list = []

        # We start with one block. Each loop we add an equivalent to the loop number (i*2).
        number_of_blocks = 1 + (i*2) # i is 0 for the first loop, so we end up with only one block.

        # Find out how much space we need
        # It'll be the length of the pyramid minus the current number of blocks
        # We'll divide it by 2 because it needs to go either side
        pyramid_space = int((pyramid_length - number_of_blocks) / 2)

        # Build the pyramid line (space, block, space)
        for i in range(pyramid_space):
            pyramid_block_list.append(' ')
        for i in range(number_of_blocks):  
            pyramid_block_list.append('*')
        for i in range(pyramid_space):
            pyramid_block_list.append(' ')

        # new_pyramid_block_list = copy.copy(pyramid_block_list)
        pyramid_list.append(pyramid_block_list)

    return pyramid_list






    return None


def lp(some_kind_of_list, exercise_name):
    """Help to see what's going on.

    This is a helper function that prints your
    results to check that they are tidy.
    Note: You don't have to do anything with it.
    """
    
    """
    if some_kind_of_list is not None:
        print("\n" + exercise_name)
        if type(some_kind_of_list[0]) is list:
            for row in some_kind_of_list:
                for column in row:
                    print(column, end="")
                print()
        else:
            for column in some_kind_of_list:
                print(column, end="")
            print()
    else:
        print(exercise_name, "maybe you haven't got to this one yet?")
    """


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    print(is_odd(1), "is_odd odd")
    print(is_odd(4), "is_odd even")
    print(fix_it(True, True), "fix_it")
    print(fix_it(True, False), "fix_it")
    print(fix_it(False, True), "fix_it")
    print(fix_it(False, False), "fix_it")
    lp(loops_1a(), "loops_1a")
    lp(loops_1c(4, "×°×"), "loops_1c")
    lp(loops_2(), "loops_2")
    lp(loops_3(), "loops_3")
    lp(loops_4(), "loops_4")
    lp(loops_5(), "loops_5")
    lp(loops_6(), "loops_6")
    lp(loops_7(), "loops_7")
