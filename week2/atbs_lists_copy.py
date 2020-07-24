import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam))

cheese = copy.copy(spam)
print(id(cheese))

cheese[2] = 'Blue'
print(spam)
print(cheese)