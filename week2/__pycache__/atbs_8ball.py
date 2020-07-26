import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Concentrate and ask again'
    elif answer_number == 6:
        return 'My reply is no'

"""
r = random.randint(1,7)

fortune = get_answer(r)
print(fortune)
"""

print(get_answer(random.randint(1,7)))

print('this ', end='')
print('is a test')

print('a', 'b', 'c', sep='   ')