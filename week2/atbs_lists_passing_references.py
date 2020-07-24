def eggs(some_parameter):
    some_parameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# Sets the function eggs, which accepts a parameter
# We set a variable with a list of numbers
# We then run eggs and pass the parameter spam into it, which contains a list
# In other words, we're just saying, run "eggs" and shovel the "spam" data into it
# If we didn't reference some_data in the function, nothing would happen with
# the shovelled data.
# But in the function, we say:
# Whatever data you put in the eggs function (some_parameter)
# I'm gonna append 'Hello' to that.
# Easy as that.