import nltk
from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from gensim.parsing.preprocessing import remove_stopwords
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw-1.4')

tokenizer = RegexpTokenizer('[A-Za-z]+')
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None
    
def preprocess_tokenize(row):
  lowered_row = row.lower() # Переводим в нижний регистр все слова в строке
  tokens = tokenizer.tokenize(remove_stopwords(lowered_row)) # Убираем стоп слова и токенизируем строку
  filtered_tokens = []
  for token in tokens: # Осоновываясь на части речи производим лемматизацию                
    postag = get_wordnet_pos(pos_tag([token])[0][1])
    if postag == None:
      lem = lemmatizer.lemmatize(token)
      if len(lem) > 1: # Не используем слово, если его длина меньше двух символов
        filtered_tokens.append(lem)
    else:
      lem = lemmatizer.lemmatize(token, postag)
      if len(lem) > 1:
        filtered_tokens.append(lem)
  return(filtered_tokens)