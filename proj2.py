import json
from difflib import get_close_matches

data = json.load(open("data.json"))

z = input("This is a dictionary. Enter y to continue ")
if z == "y":
    while z == "y":
        word = input("Enter the word you want to search ")
        word = word.lower()
        if word in data:
            output = data[word]
        elif word.title() in data:
            output = data[word.title()]
        elif word.upper() in data:
            output = data[word.upper()]
        elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0 :
            print("Did you mean %s ?" %get_close_matches(word, data.keys(), cutoff = 0.8) [0])
            new = input("Enter y if yes and Enter n if no ")
            if new == "y":
                output = data[get_close_matches(word, data.keys(), cutoff = 0.8) [0]]
            elif new == "n":
                output = "You have entered a wrong word"
            else:
                output = "You have entered wrong input"
        else:
            output = "you have entered a wrong word"

        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

        z = input("Press y to continue or n to exit ")
