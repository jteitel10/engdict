import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def fooTranslate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean {} instead?  Enter y or n. ".format(
            get_close_matches(word, data.keys())[0]))
        if yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return 'Word not defined or does not exist.  Please try again.'
    else:
        return "Word not defined or does not exist. Please try again."


input_word = input('Enter word: ')

print(fooTranslate(input_word))
