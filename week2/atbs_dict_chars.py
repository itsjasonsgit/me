message = 'It was a bright cold day in April, the clocks were striking thirteen'
count_dictionary = {}

# For each character variable in message variable
for a_character in message:

    # Set a_character (an actual character) for this as
    # a key of a_character (if there isn't one)
    # and with the value of 0
    count_dictionary.setdefault(a_character, 0)

    # For the value of a_character in this loop
    # Set the value of a_character + 1 
    # Remember, when we call a dictionary[key] the returned value we get is the key's value
    # It wouldn't make sense to return the Key... you're calling, would it?
    count_dictionary[a_character] = count_dictionary[a_character] + 1

print(count)