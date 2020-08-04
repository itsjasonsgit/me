# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""
# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    """
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)
    """

# Imports
import math
import requests

# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    # Print stuff out (DONT USE A LIST, IT SAYS USE A LIST BUT DONT USE A DAMN LIST)
    # Based on a range that is stepping down
    for i in range(start, (stop - 1), -1):
        print(message + " " + str(i))
    print(completion_message)

# TRIANGLES

# This should be a series of functions that are ultimately used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    return hypotenuse



def calculate_area(base, height):
    area = (base * height) / 2
    return area


def calculate_perimeter(base, height):
    perimeter = calculate_hypotenuse(base, height) + base + height
    return perimeter


def calculate_aspect(base, height):
    if base > height:
        aspect_ratio = "wide"
    elif base == height:
        aspect_ratio = "equal"
    else:
        aspect_ratio = "tall"
    return aspect_ratio


print("aspect ratio is: " + str(calculate_aspect(4, 5)))

# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    # print("the input is: " + str(facts_dictionary))

    # Store the triangles in a dictionary
    # So we can pull them out later instead of using if statements
    triangle_dict = {
    "tall" : """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}""",
    
    "wide" : """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}""",

    "equal" : """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""
    }

    # This is just a variable with a string that describes the triangle
    # On some separate lines
    # With formatting targets
    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    # Using the "aspect" key from the facts_dictionary args we get the aspect value (tall/wide/equal)
    # Using that value we return the relevant diagram from the triangle_dictionary
    # And we then format that diagram using an unpacked facts_dictionary keys
    # And we then add on the pattern text
    # which is also formatted using the facts_dictionary args
    return str(triangle_dict[facts_dictionary["aspect"]].format(**facts_dictionary)) + "\n" + str(pattern.format(**facts_dictionary))


def triangle_master(base, height, return_diagram=False, return_dictionary=False):

    # Get a dictionay of facts
    dictionary = get_triangle_facts(base, height)

    # Get a triangle diagram using the dictionary of facts
    diagram = tell_me_about_this_right_triangle(dictionary)
    
    # Return both
    if return_diagram and return_dictionary:
        # This has to be returned as a dictionary or it fails one of the tests. I have no idea why.
        return {"diagram": diagram, "dictionary": dictionary}
    # Return the diagram
    elif return_diagram:
        return diagram
    # Return the dictionary
    elif return_dictionary:
        return dictionary
    # Return nothing
    else:
        print("You're an odd one, you don't want anything!")


baseURL =  "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={}"

def wordy_pyramid():
    # blah
    pyramid_list = []
    for i in range(3, 21, 2):
        pyramid_list.append(get_a_word_of_length_n(i))

    for i in range(20, 3, -2):
        pyramid_list.append(get_a_word_of_length_n(i))

    return pyramid_list


def get_a_word_of_length_n(length):
    # baseURL =  "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={}"
    url = baseURL.format(length)
    r = requests.get(url)
    if r.status_code is 200:
        message = r.text
        return message
    else:
        print("failed a request", r.status_code)

def list_of_words_with_lengths(list_of_lengths):

    # Map exectutes a function (get_a_word_of_length_n)
    # for each iteration of list_of_lengths (3)
    # And, for each iteration, passed through the value from list_of_lengths
    # to the function in the map
    return map(get_a_word_of_length_n, list_of_lengths)


if __name__ == "__main__":
    do_bunch_of_bad_things()
    wordy_pyramid()