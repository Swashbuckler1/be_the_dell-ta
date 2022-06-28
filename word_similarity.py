import nltk
from IO import open_file

nltk.download('wordnet')
from nltk.corpus import wordnet as wn

# syn = []

# data_terms = open_file('data_terms.txt')
# ll_terms = open_file('low_level_terms.txt')
#
# print(data_terms)
# print(ll_terms)
#
# for data_term in data_terms:
#     syn.append(wn.synsets(data_term))
#
# print(syn)