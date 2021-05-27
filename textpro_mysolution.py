# 1. Output "Say Something"
# 2. take an input, store it into a list
# 3. end if user inputs /end
# 4. Capitalise first letter. End in a question mark if it starts with who, what, when, where, why, how
# 5. Print out each input. 


inputs = []
word = ''
fullstop = '.'
sentence = ''

while True:
    if word != "\end.":
        word = input("Say something: ")
        word = str(word)
        word = word.capitalize()

        if word.startswith('Who') or word.startswith('What') or word.startswith('When') or word.startswith('Why') or word.startswith('How'):
            word = word + '?'

        else:
            word = word + '.'

        inputs.append(word)

        continue
    else:
        inputs.remove('\end.')
        print(' '.join(inputs))
        
        break
