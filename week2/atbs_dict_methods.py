my_dictionary = {'color': 'red', 'age': 42}

# For every item (v) in the dictionary's VALUES, set to v for each iteration of the loop
for v in my_dictionary.values():
    print(v)

# A method of checking if true or false for a key or value entry
print('color' in my_dictionary.keys())
print('color' not in my_dictionary.keys())

# Get()
print('Answer is ' + str(my_dictionary.get('age', 0)))

# .setdefault()
my_dictionary.setdefault('size', 'medium')
print(my_dictionary)