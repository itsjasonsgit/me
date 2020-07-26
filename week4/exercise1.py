"""All about IO."""
# New website?
# https://l.facebook.com/l.php?u=https%3A%2F%2Fus-central1-waldenpondpress.cloudfunctions.net%2Fgive_me_a_word%3Ffbclid%3DIwAR3QaN0Sgp7XCoPKn5KLpy9_p9diC-ja24hSKM2DyUHUM1W2YGX9OZ8sPYk&h=AT3F1o0qFGj4mdptMr2U9qWWxaWQrqThhV13efZ4YMQCXAOKqrE4eeeDB1Y4CmnOYTLjv7ZjIPHyFcoRxaBzdfYGtz5NWk3drT5N3Rtdx-mGmn8rDOcY_oIAJprBBEg0oqWBYuO1a9up12g
# Specify how many characters you want and it'll generate a random word

import json
import os
import requests
import inspect
import sys




# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    # Return to dictionary:
    # last name
    # password
    # number you get when you add (literally) the postcode to the ID value

    json_data = open(LOCAL + "\lazyduck.json").read()
    data = json.loads(json_data)
 
    # Use the data variable (json data)
    # Look in "results" - which is a dictionary
    # Then look in the index of 0 - because
    # the json data is then nested in a list
    # This is a terrible, terrible way to do this but it works
    # IN ONLY THIS CIRCUMSTANCE
    json_last_name = data["results"][0]["name"]["last"]
    json_password = data["results"][0]["login"]["password"]
    json_postcode = data["results"][0]["location"]["postcode"]
    json_id = data["results"][0]["id"]["value"]

    # Should have like a variable set for the values we're looking for
    # Then run a thing that scans the json data and sees if its there
    # And prints to the dictionary for each, not just one.
     
    return {
        "lastName": json_last_name,
        "password": json_password,
        "postcodePlusID": json_postcode + int(json_id)
        }

get_some_details()


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word
    http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=10&maxLength=10&limit=1
    The arguments that the generator takes is the minLength and maxLength of the word
    as well as the limit, which is the the number of words. 
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &minLength=
    """
    # My function to get a word
    # Based on the length of the argument
    def get_word(word_length):
        payload = {"wordlength": word_length}
        response = requests.get("https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word", params=payload)
        return response.text

    # Min/max word lengths
    min_word_length = 3
    max_word_length = 20

    # Empty pyramid list
    pyramid_list = []

    # Stepping from min to max in a range loop
    for i in range(min_word_length, max_word_length, 2):
        # Parsing the current step as the word length into my get_word function
        new_word = get_word(i)
        # Appending the data to the list
        pyramid_list.append(new_word)

    # Repeating, but stepping down
    # (could probably wrap the prior loop in a function and just change the -2)
    # DRY... but it works
    for i in range(max_word_length, min_word_length, -2):
        new_word = get_word(i)
        pyramid_list.append(new_word)

    print(pyramid_list)

    return pyramid_list


def pokedex(low=1, high=5):
    """ Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.
    
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    template = "https://pokeapi.co/api/v2/pokemon/{id}"

    # The pokemon have a name in their index 
    # But the problem you'll have is, inbetween the pokemon
    # You wanna know which is the tallest
    # So you need the name and height of the range of pokemon
    # And it's your job to make a function that does that
    # Regardless of the number we're actually asking for.
    # You could just look at it and go which one is the highest
    # from whatever range you manually select.
    # But the test will test for different numbers
    # This is relatively challenging, the others are straight
    # foward... #


    url = template.format(id=5)
    r = requests.get(url)
    if r.status_code is 200:
        the_json = json.loads(r.text)
    return {"name": None, "weight": None, "height": None}


def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the week4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.
    """
    pass


if __name__ == "__main__":
    functions = [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj))
    ]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print("diarist did not create lasers.pew")
