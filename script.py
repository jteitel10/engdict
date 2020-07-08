import json

data = json.load(open('data.json'))


def fooTranslate(word):
    return data[word]


input_word = input('Enter word: ')

print(fooTranslate(input_word))
