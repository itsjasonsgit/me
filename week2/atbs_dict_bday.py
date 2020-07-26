birthdays = {'Rose': 'Apr 1', 'Bianca': 'Dec 12', 'Kayleigh': 'Aug 10'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    # Quit if no data is entered
    if name == '':
        break
    
    # If there is a matching name (input data) in birthdays (dictionary)
    if name in birthdays:
        # Use the birthdays dictionary, get the key of
        # the name input to find the value (bday)
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        # No birthday information for the name, let the user know...
        print('I do not have birthday information for ' + name)
        # And then ask for them to input the data
        print('What is their birthday?')
        bday = input()
        # Then append that to the dictionary
        # (this is easier than .append, it seems?)
        birthdays[name] = bday
        print('Birthday database updated.')

    # asdf