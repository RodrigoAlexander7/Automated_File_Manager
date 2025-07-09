from app import pdf_reader 
from app import constant
from pathlib import Path

from collections import defaultdict

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


def create_corpus_inverted_index(dict_doc_words:dict, corpus:defaultdict):
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
                
a = documents_content(constant.PATH_DIRECTORY)
b = count_ocurrences(a)
print(create_corpus_inverted_index(a,b))
