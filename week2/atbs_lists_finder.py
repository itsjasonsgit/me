
list = ['cat', 'hat', 'bat'] # Define a list

def list_selector():
    print('Select 1-3')
    list_selection = input() # Make the user define the list_selection variable
    print(list[int(list_selection)]) # Print the output
    global i
    i = i + 1 # Sets the global i counter

i = 0 # Loop counter starts at zero
while i < 3: # Simple loop, 3 times
    list_selector() # Run the list selector in the loop

