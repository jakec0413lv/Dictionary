import json
from difflib import SequenceMatcher
from difflib import get_close_matches

#User input
def getWord():
    value = input("Enter a word: ")
    return value

def getDefinition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif get_close_matches(w, data, 1, .6) != []:
        closeMatch = get_close_matches(w, data, 1, .6)[0]
        additionalInput = input("Did you mean " + closeMatch + " instead? Y/N: ").lower()
        if(additionalInput == "y"):
            return data[closeMatch]
        elif(additionalInput == "n"):
            return("Word does not exist. Please double check it!") 
        else:
            return("We didn't understand your entry! [Expected Y/N]")
    else:
        return("Word does not exist. Please double check it!")

#Import data into variable

data = json.load(open("data.json"))
word = getWord()
definitions = getDefinition(word)

i = 1

if type(definitions) == list:
    for definition in definitions:
        print(str(i) + ". " + definition)
        i+=1
else:
    print(str(i) + ". " + definitions)

