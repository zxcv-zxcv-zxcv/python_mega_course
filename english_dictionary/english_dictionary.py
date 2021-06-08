# Specifications
# User Input: User inputs a word, Returns definition
# Returns multiple definition if the word has multiple
# If user mistypes a word that is similar, ask the user if it meant
# X word. 
# If user types jumbles, return word is not an word
# 1st Revision. Does not do mistyping finding
import json
import difflib
from difflib import get_close_matches
data = json.load(open('english_dictionary/data.json'))

def definition(word):
    word = word.lower()
    if word in data:
        return ' '.join(data.get(word))
    else:
        return word + ' is not a word.'


while True:
    user_input = input("Say word: ")
    if user_input == '\end':
        break
    else:
        print(definition(user_input))
