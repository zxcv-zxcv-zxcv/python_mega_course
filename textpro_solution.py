def sentence_maker(phrase):
    interrogatives = ('how', 'what', 'why')
    capitalised = phrase.capitalize()

    if phrase.startswith(interrogatives):
        return "{}?".format(capitalised)
    else:
        return "{}.".format(capitalised)

results = []

while True:
    user_input = input("Say something: ")
    if user_input =="\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(' '.join(results))