import json
from difflib import get_close_matches

#loading json file data to object
data = json.load(open("C:\\Users\\admin\\Desktop\\app1\\data.json"))

def foo(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif w.title() in data:#for word with starting letter caps
        return data[w.title()]
    elif w.upper() in data:#for words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: #checks words similar to input word
        inp=input("Did you mean %s press y if yes or n if NO:" % get_close_matches(w, data.keys())[0]) #[0] means first word
        if inp=="y" or inp=="Y":
            return data[get_close_matches(w, data.keys())[0]] #return first word
        elif inp=="n" or inp=="N":
            return "THEN word is wrong.Double check it"
        else:
            return "Only y or n"
    else:
        return "Your word is not present.Check again"

word = input("ENTER A WORD: \n")
op = foo(word)

if type(op) == list:#if word has more lines of meaning
    for i in op:#then print meaning line by line
        print(i)
else:
    print(op)