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
    return dict_doc_words

#OCURRENCIAS GENERALES POR PALABRA A PARTIR DE LAS LISTAS "doc" : [palabras]
def count_ocurrences(dict_doc_words:dict):
    corpus = defaultdict(int)
    for word_list in dict_doc_words.values():
        for words in word_list:
            corpus[words] += 1
    print(corpus)
    return corpus



#FALTA EL INDICE INVERTIDO CON TODO EL CORPUS


count_ocurrences(documents_content(constant.PATH_DIRECTORY))