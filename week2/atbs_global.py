def spam(): # defines the spam() function
    global eggs # sets the variable eggs as global
    eggs = 'spam'

eggs = 'global' # changes the egg variable to 'global'
print(eggs)
spam() # runs spam(), which changes the eggs variable from 'global' to 'spam'
print(eggs)