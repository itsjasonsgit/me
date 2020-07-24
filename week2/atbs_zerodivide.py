def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError: # runs if there's a division error
        print('Error')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))