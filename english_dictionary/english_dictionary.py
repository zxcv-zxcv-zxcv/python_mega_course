# Specifications
# User Input: User inputs a word, Returns definition
# Returns multiple definition if the word has multiple
# If user mistypes a word that is similar, ask the user if it meant
# X word. 
# If user types jumbles, return word is not an word TO_DO

import json
import difflib
from difflib import get_close_matches
data = json.load(open('english_dictionary/data.json'))

def definition(word):
    word = word.lower()
    if word in data:
        return ' '.join(data.get(word))
    elif get_close_matches(word, data.keys()):
        most_similar = get_close_matches(word, data.keys())[0]
        while True:
            inputa = input("Did you mean this word?: " + most_similar + 
                        " \nType 'Y' or 'N': ")
            if inputa.lower() == 'y':
                word = most_similar
                return definition(word)
            elif inputa.lower() == 'n':
                return 'This word doesn''t exist'
            else:
                print('Please say Y or N. \n')
    else:
        return 'This word doesn''t exist'

while True:
    user_input = input("Say word: ")
    if user_input == '\end':
        break
    else:
        print(definition(user_input))
