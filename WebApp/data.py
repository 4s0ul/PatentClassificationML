import numpy as np
import pandas as pd
import spacy
from spacy.tokens import DocBin

def process_data():
    data = pd.read_csv('C:/Users/lil4sxvl/Desktop/VKRO_O/search/data/df_res.csv', sep='\t')
    data['award'] = pd.DataFrame(np.random.randint(500,10000,size=(len(data), 1)))

    nlp = spacy.load('en_core_web_lg')
    nlp_data = DocBin()
    nlp_data.from_disk('C:/Users/lil4sxvl/Desktop/VKRO_O/search/data/db')
    nlp_docs = list(nlp_data.get_docs(nlp.vocab))

    data['nlp_docs'] = nlp_docs
    return data, nlp