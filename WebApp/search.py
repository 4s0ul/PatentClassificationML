import heapq
from most_similar import find_most_similar


def search(class_of_doc, search_text, nlp, data):
    if class_of_doc != 'None':
        result = find_most_similar(nlp(search_text), data['nlp_docs'][data['label'] == class_of_doc])
    else:
       result = find_most_similar(nlp(search_text), data['nlp_docs'])
    most_similar_texts = heapq.nlargest(5, result, key=result.get)
    return most_similar_texts, result