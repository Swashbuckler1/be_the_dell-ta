import en_core_web_lg
from IO import open_file
import itertools

def load_model():
    nlp = en_core_web_lg.load()
    return nlp

nlp = load_model()

data_terms = open_file('data_terms.txt')
ll_terms = open_file('low_level_terms.txt')
pairs = []

for element in itertools.product(data_terms, ll_terms):
    term_1 = nlp.vocab[element[0]]
    term_2 = nlp.vocab[element[1]]
    if term_1.similarity(term_2) >= 0.3:
        pairs.append(element)

print(pairs)

