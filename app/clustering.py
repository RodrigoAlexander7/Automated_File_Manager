from app import pdf_reader 
from app import constant
from pathlib import Path

from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def documents_content(document_directory):
    dict_doc_words = {} 
    document_directory = Path(document_directory)
    for file in document_directory.iterdir():
        file_name = file.name
        dict_doc_words[file_name] = pdf_reader.clean_words_pdf(file)
    #GLOBAL OCURRENCES BY WORDS FROM LISTS "doc" : [palabras]
    return dict_doc_words

def count_ocurrences(dict_doc_words:dict):
    corpus = defaultdict(int)
    for word_list in dict_doc_words.values():
        for words in word_list:
            corpus[words] += 1
    # DICTIONARY WITH COUNTER OF WORDS
    return corpus


def create_corpus_inverted_index_umbral(dict_doc_words:dict, corpus:defaultdict):
    inverted_index = defaultdict(set)
    TOTAL = 0
    for word_list in dict_doc_words.values():
        TOTAL += len(word_list)
    UMBRAL = 0.01 * TOTAL

    for file_name, word_list in dict_doc_words.items():
        for words in word_list:
            if(corpus[words] >= UMBRAL):
                inverted_index[words].add(file_name)
    return inverted_index

def create_corpus_inverted_index(dict_doc_words:dict, corpus:defaultdict):
    inverted_index = defaultdict(set)
    for file_name, word_list in dict_doc_words.items():
        for words in word_list:
            inverted_index[words].add(file_name)
    return inverted_index


def dict_to_text_list(dict_doc_words):
    doc_names = []
    corpus_texts = []
    for file_name, word_list in dict_doc_words.items():
        doc_names.append(file_name)
        corpus_texts.append(" ".join(word_list))
    return doc_names, corpus_texts
                
def build_tfidf(corpus_texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus_texts)
    return tfidf_matrix, vectorizer

def group_documents(tfidf_matrix, k=5):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(tfidf_matrix)
    return model.labels_

def show_groups(doc_names, labels):
    groups_dic = {}
    for name, group in zip(doc_names, labels):
        if group not in groups_dic:
            groups_dic[group] = []
        groups_dic[group].append(name)
    
    for group, docs in groups_dic.items():
        print(f"\n-> Group {group}:")
        for doc in docs:
            print(f"   - {doc}")

def group_by_topics(dict_doc_words, k=5):
    doc_names, corpus_texts = dict_to_text_list(dict_doc_words)
    tfidf_matrix, vectorizer = build_tfidf(corpus_texts)
    labels = group_documents(tfidf_matrix, k)
    show_groups(doc_names, labels)


"""
a = documents_content(constant.PATH_DIRECTORY)
b = count_ocurrences(a)
print(create_corpus_inverted_index(a,b))

group_by_topics(a)
"""