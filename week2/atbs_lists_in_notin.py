my_pets = ['Akela', 'Mars', 'Charlie']
print('Enter a pet name')
pet_name = input()
if pet_name not in my_pets:
    print('I do not have a pet named ' + pet_name)
else:
    print('Yeah! ' + pet_name + ' is my pet.')