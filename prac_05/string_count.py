

individual_words = {}
text = input('Text: ')

# text: we were dressed in potential now we're draped in sorrow

words = text.split()
for word in words:
    frequency = individual_words.get(word, 0)
    if frequency is None:
        individual_words[word] = 1
    else:
        individual_words[word] = frequency + 1

words = list(individual_words.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print('{:{}} : {}'.format(word, max_length, individual_words[word]))
