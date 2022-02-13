import numpy as np
from config import dataset

def markov(length=np.random.randint(30), dataset=dataset):

    chatbot = open(dataset, encoding='utf8').read().split()

    word_dict = {}

    def make_pairs(chatbot):
        for i in range(len(chatbot)-1):
            yield (chatbot[i], chatbot[i+1])

    pairs = make_pairs(chatbot)

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(chatbot)

    while first_word.islower():
        first_word = np.random.choice(chatbot)

    chain = [first_word]

    for i in range(length):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    return ' '.join(chain)