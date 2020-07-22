def hello(name):
    print('Hello,' + name)

hello('ALice')
hello('Bob')

# Calls hello and passes through the argument as a string.
# The function is defined with name as a parameter, so whatever
# is passed through that parameter becomes the is set within
# the function. The parameter is forgotten once the function is done.
# It's not a global variable.