import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer('[A-Za-z]+')

def find_most_similar(text, docs):
  index_score = {}
  for i, doc in enumerate(docs):
    similarity_score = text.similarity(doc)
    index_score[i] = similarity_score
  return index_score