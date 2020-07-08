import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def fooTranslate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead?  Enter y or n. ".format(
            get_close_matches(word, data.keys())[0]))
        if yn.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == 'n':
            return 'Word not defined or does not exist.  Please try again.'
        else:
            return 'Entry not understood.  Please try again.'
    else:
        return "Word not defined or does not exist. Please try again."


input_word = input('Enter word: ')

output = fooTranslate(input_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
