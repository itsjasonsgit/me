import pprint
message = 'It was a bright cold day in April, the clocks were striking thirteen'
character_count_dictionary = {}

for character in message:
    character_count_dictionary.setdefault(character, 0)
    character_count_dictionary[character] = character_count_dictionary[character] + 1

pprint.pprint(character_count_dictionary)