import pickle
from preprocess import preprocess_tokenize


def upload_doc(upload_publication_number, upload_abstract, upload_application_number, upload_description, upload_award, data, nlp):
    with open('./models/SVM.pkl', 'rb') as svm, open('./models/TFIDF.pkl', 'rb') as tfidf:
        SVM = pickle.load(svm)
        TFIDF = pickle.load(tfidf)
    label = SVM.predict(TFIDF.transform([upload_abstract]))[0]
    new_row = {'publication_number': upload_publication_number, 'abstract': upload_abstract, 'application_number': upload_application_number, 'description': upload_description, 'label': label, 'award': int(upload_award), 'nlp_docs': nlp(upload_abstract)}
    updated_data = data.append(new_row, ignore_index = True)
    return updated_data