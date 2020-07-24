cat_list = [] # Create an empty list of cat names

while True: # Start a loop until the condition is set to False (forever)
    # Get the user to enter a cat name, showing what number it is
    # We do this by getting the length of the cat_list list and adding 1 (new cat)
    print('Enter the name of cat ' + str(len(cat_list) + 1) + ' (Or enter nothing to stop.):')

    cat_name = input() # Make a variable that is the new cat's name

    # If the user enters nothing, ext the program
    if cat_name == '':
        break
    
    # If we've got some input data, we don't break, so...
    # Concantonate the list with the new cat name
    # We have to concantonate cat_name within [] so that Python knows its a list
    # Otherwise you'd be adding a variable to a list
    cat_list = cat_list + [cat_name]

print('The cat names are:')

for cat_name in cat_list: # For each cat_name in cat_list
    print(' ' + cat_name)