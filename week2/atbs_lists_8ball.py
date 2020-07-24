import random

messages = [
    'It is certain',
    'Not sure',
    'Possibly?',
    'Maybe, maybe not',
    'Meh',
    'You wish',
    'Done',
    'Unlikely at best'
    ]

# Get an index of messages
# Get that index by finding a random integer (random.randint())
# Make the random int between 0 and the length of the messages list - 1
# We need the - 1 because the indexes start at 0
print(messages[random.randint(0, len(messages) - 1)])