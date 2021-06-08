from abc import abstractmethod
import json
import difflib
from difflib import get_close_matches


data = json.load(open("english_dictionary\data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

print(translate(word))
