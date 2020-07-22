"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# Declare a list in a variable
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# Prting each item in the list of some_words
for word in some_words:
    print(word)

# Same deal
for x in some_words:
    print(x)

# Print the variable some_words (it's list)
print(some_words)

# If the length of the list some_words is greater than 3, print the message
if len(some_words) > 3:
    print('some_words contains more than 3 words')

# Print the user's "system, node, release, version, machine, and processor."
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
