import en_core_web_lg
from IO import open_file, read_data
import itertools

def load_model():
    nlp = en_core_web_lg.load()
    return nlp

def pair_interns():
    nlp = load_model()
    pairs = []
    df = read_data()
    interests = list(df['TechnologiesOfInterest'].values)

    for i in range(len(interests)):
        interests[i] = interests[i].split(',')
        for j in range(len(interests[i])):
            interests[i][j] = interests[i][j].strip()

    df['Full Name'] = df['FirstName'] + ' ' + df['LastName']
    names = df['Full Name'].values

    for item1, item2 in itertools.product(interests, interests):
        term_1 = nlp.vocab[item1[0]]
        term_2 = nlp.vocab[item2[0]]
        sim = term_1.similarity(term_2)
        if sim >= 0.45 and sim != 1:
            index_1 = interests.index(item1)
            index_2 = interests.index(item2)
            pairs.append((names[index_1], names[index_2]))

    return pairs

# data_terms = open_file('data_terms.txt')
# ll_terms = open_file('low_level_terms.txt')

# pairs = []
#
# for element in itertools.product(data_terms, ll_terms):
#     term_1 = nlp.vocab[element[0]]
#     term_2 = nlp.vocab[element[1]]
#     if term_1.similarity(term_2) >= 0.3:
#         pairs.append(element)
#
# print(pairs)

