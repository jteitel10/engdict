import json

data = json.load(open('data.json'))


def fooTranslate(word):
    if word in data:
        return data[word]
    else:
        return "Word not defined or does not exist. Please try again."


input_word = input('Enter word: ')

print(fooTranslate(input_word.lower()))
