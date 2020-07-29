list = ["one", "two"]
list_test = []
for test in list:
    list_test.append("one" in test)

print(list_test)

pattern_of_bools = [pet[0]]