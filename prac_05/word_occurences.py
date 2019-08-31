
WORD_COUNT = {}

user_input = input("Please enter a sentence: ")
words = user_input.split()

for word in words:
    amount_of_word = WORD_COUNT.get(word, 0)
    WORD_COUNT[word] = amount_of_word + 1

words = list(WORD_COUNT.keys())
words.sort()

max_word_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_word_length, WORD_COUNT[word]))


