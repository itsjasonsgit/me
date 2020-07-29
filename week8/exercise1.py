# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import string
import time


def string_please() -> str:
    """Returns a string, anything you like."""
    string = "string"
    return string


def list_please() -> list:
    """Returns a list, anything you like."""
    list = ['one', 'two', 'three']
    return list


def dictionary_please() -> dict:
    """Returns a dictionary, anything you like."""
    dict = {'one': 1, 'two': 2, 'three': 3}
    return dict


def is_it_5(some_number) -> bool:
    """Returns True if the argument passed is 5, otherwise returns False."""
    well_is_it = some_number == 5
    return well_is_it


def take_five(some_number) -> int:
    """Subtracts 5 from some_number."""
    subtract = some_number - 5
    return subtract


def greet(name="Towering Timmy"):
    """Return a greeting.
    return a string of "Hello " and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    string = "Hello " + name
    return string


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    count = 0
    for i in range(len(input_list)):
        if input_list[i - 1] == 3:
            count += 1

    return count


def n_counter(search_for_this, input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    count = 0
    for i in range(len(input_list)):
        if input_list[i] == search_for_this:
            count += 1

    return count


def fizz_buzz():
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!
       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
    from https://blog.codinghorror.com/why-cant-programmers-program/
    
    Return a list that has an integer if the number isn't special, 
    and a string if it is. E.g. 
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14, 
         'FizzBuzz', 16, 17, ...]
    """

    fizzBuzzList = []
    for i in range(1, 101):
        if i % 3 is 0 and i % 5 is 0:
            fizzBuzzList.append('FizzBuzz')
        elif i % 3 is 0:
            fizzBuzzList.append('Fizz')
        elif i % 5 is 0:
            fizzBuzzList.append('Buzz')
        else:
            fizzBuzzList.append(i)
   
    return fizzBuzzList


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.
    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return the string
    "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: strings are pretty much lists of chars. 
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a pipe on both ends of the string.
    """
    separator = "|"
    interleave = separator + separator.join(input_string) + separator
    print(interleave)

    return interleave


def pet_filter(letter="a"):
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
            "dog", "goat","pig","sheep","cattle","zebu","cat","chicken",
            "guinea pig","donkey","duck","water buffalo","western honey bee",
            "dromedary camel","horse","silkmoth","pigeon","goose","yak",
            "bactrian camel","llama","alpaca","guineafowl","ferret",
            "muscovy duck","barbary dove","bali cattle","gayal","turkey",
            "goldfish","rabbit","koi","canary","society finch","fancy mouse",
            "siamese fighting fish","fancy rat and lab rat","mink","red fox",
            "hedgehog","guppy",]
    # fmt: on
    filtered = []

    for i in range(len(pets)):
        if letter in pets[i]:
            filtered.append(pets[i])
    
    return filtered 


def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.
    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string

    # Return the letter that exists in the most pet names

    pet_list = []
    letter_count = []
    the_alphabet = string.ascii_lowercase
    
    # Do this thing for each letter in the alphabet
    for i in range(len(the_alphabet)):

        # Get the letter, assign it
        letter_to_test = the_alphabet[i]

        # Test it using pet_filter
        # Which returns a list of pets using this letter
        pet_list = pet_filter(letter_to_test)

        # List length =  number of pets with letter in name
        letter_count.append(len(pet_list))
    
    # Get the index of the highest number and use it as an index for popular_letter
    popular_letter = the_alphabet[letter_count.index(max(letter_count))]

    return popular_letter


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4 
    If we set minLength=18 and maxLength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"
    
    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    { 
        3: ['Sep', 'the', 'yob'],
        4: ['aaaa', 'bbbb', 'cccc'],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc']
    }
    Use the API to get the 3 words.
    
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: you'll need the requests library
    """

    import requests

    # url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="
    # wd = {}

    # Create a dictionary with words
    # The lengths of the words go from 3-7 chars
    # Return 3 words for each character

    # From previous exercises
    def get_word(word_length):
            payload = {"wordlength": word_length}
            response = requests.get("https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word", params=payload)
            return response.text

    # make it Global, gotta use it for the next question
    # global word_dict
    word_dict = {}
 
    # Loop it from 3-7
    for i in range(3, 8):
        word_length = i

        # Get a random word 3 times and put it in a list
        word_list = []
        for i in range(3):
            word = get_word(word_length)
            word_list.append(word)
            
        # Append to dictionary
        word_dict[word_length] = word_list
    
    print(word_dict)

    return word_dict


def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library, 
        see line 77 of week4/hangman_leadboard.py for an example.
    """
    # Use word_dict words
    # Pick one of the 5 keys (word lengths) at random
    # Using that key, pick one of the 3 words in the key's list at random
    # Make a paragraph with those words with a numnber of words
    # in it that = number_of_words
    # Return as a string, not list

    # I don't want to run this again because it takes
    # so long so I'm not doing this:
    # my_dict = make_filler_text_dictionary()
    # I'm using global variables (unless it doesn't pass the test)

    import random

    word_dict = make_filler_text_dictionary()

    random_paragraph_list = []
    
    for i in range(number_of_words):

        # Create a random number between 3-7 for the dictionary keys
        random_key =  random.randint(3, 7)
        # print('random key is... ' + str(random_key))

        # Get the list from the random index
        random_word_list = word_dict.get(random_key)
        # print('random values are... ' + str(random_word_list))

        # create a random number for the index
        random_index = random.randint(0, 2)
        # print('random index is... ' + str(random_index))

        # Get a random word from the list
        random_word = random_word_list[random_index]
        # print('random word is... ' + random_word)

        # Append it to a list of random words
        random_paragraph_list.append(random_word)
    
    # Join each word in the list with a space
    random_paragraph = " ".join(random_paragraph_list) + "."

    return random_paragraph.capitalize()
    


def fast_filler(number_of_words=200):
    """Reimplement random_filler_text.
    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the 
    dictionary into and out of the file. Be careful when you read it back in, 
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """
    # run random_filler_text()
    # Save make_filler_text as a file
    # The test will probably run the fast_filler() again
    # So check if the file exists already, if it does - use the file
    # Not the internet data - so DON'T run random_filler_text() if
    # the file exists.

    import random
    import os
    import requests
    import inspect
    import json



    # From week 4
    LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
    """
    CWD = os.getcwd()  # The curent working directory
    if LOCAL != CWD:
        print("Be careful that your relative paths are")
        print("relative to where you think they are")
        print("LOCAL", LOCAL)
        print("CWD", CWD)
    """
    # Function that reads the json data and fixes the keys
    # Turning them from strings to integers
    def read_json():
        with open(LOCAL + "\dict_racey.json") as json_file:
            json_data = json.load(json_file)

        # Fix the keys
        fixed_data = {int(str_key): index for str_key, index in json_data.items()}

        return fixed_data

    if os.path.exists(LOCAL + "\dict_racey.json") != True:
        # Get the file data from make_filler_text_dictionary()
        file_data = make_filler_text_dictionary()

        # Open a new file (and create one if there isn't one already)
        with open(LOCAL + "\dict_racey.json", "w+") as json_file:
            json.dump(file_data, json_file)

        # Return the json_data as a fixed dictionary
        json_data = read_json()

    # Run if the file exists:
    else:
        # Return the json_data as a fixed dictionary
        json_data = read_json()

    # The random_filler function again
    random_paragraph_list = []
    
    for i in range(number_of_words):
        # Create a random number between 3-7 for the dictionary keys
        random_key =  random.randint(3, 7)
        # Get the list from the random index
        random_word_list = json_data.get(random_key)
        # create a random number for the index
        random_index = random.randint(0, 2)
        # Get a random word from the list
        random_word = random_word_list[random_index]
        # Append it to a list of random words
        random_paragraph_list.append(random_word)
    
    # Join each word in the list with a space
    random_paragraph = " ".join(random_paragraph_list) + "."

    return random_paragraph.capitalize()



if __name__ == "__main__":
    print("string_please", type(string_please()) == str)
    print("list_please", type(list_please()) == list)
    print("dictionary_please", type(dictionary_please()) == dict)
    print("is_it_5", is_it_5(5))
    print("is_it_5", is_it_5(6))
    print("take_five", take_five(5))
    print("take_five", take_five(3))
    print("greet:", greet())
    print("three_counter:", three_counter())
    print("n_counter:", n_counter(7))
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", put_behind_bars())
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(10):
        print(i, fast_filler())
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
