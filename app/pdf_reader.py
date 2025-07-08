import app.constant as constant 
import pymupdf

from collections import defaultdict
from typing import List
from pathlib  import Path


def get_words_pdf(path_pdf: str, max_pag: int = 700)->str:
    dict_words = {} 
    try:
        with pymupdf.open(path_pdf) as doc:
            len_pag = min(len(doc), max_pag)
            for i in range(len_pag):
                words = doc[i].get_text("words")
                for word_info in words:
                    _,_,_,_,word,_,_,_ = word_info
                    word = word.lower()
                    if not (constant.is_stopword(word)):
                        dict_words[word] = dict_words.get(word,0) + 1
        return dict_words 
    except Exception as e:
        print(f"Error in lecture {path_pdf}:{e}")
        return ""
    
# return a list of all the words in a doc
def clean_words_pdf(path_pdf: str, max_pag: int = 700)->str:
    list_words = [] 
    try:
        with pymupdf.open(path_pdf) as doc:
            len_pag = min(len(doc), max_pag)
            for i in range(len_pag):
                words = doc[i].get_text("words")
                for word_info in words:
                    _,_,_,_,word,_,_,_ = word_info
                    word = word.lower()
                    if not (constant.is_stopword(word)):
                        list_words.append(word)
        return list_words
    except Exception as e:
        print(f"Error in lecture {path_pdf}:{e}")
        return ""   

"""
def get_corpus(directory_pdf):
    path_list = get_file_names(directory_pdf)
    corpus = defaultdict(int)
    dict_list = []
    for path in path_list:
        dict_list.append(get_words_pdf(path))
    for dict_words in dict_list:
        for word,count in dict_words.items():
            corpus[word] += count
    return corpus   
"""
def get_file_names(directory_path):
    file_list = []
    try:
        for file in Path(directory_path).iterdir():
            if file.is_file():
                file_list.append(file)
        return file_list
    except FileNotFoundError:
        print("Directory not found in: '{directory_path}")
        return []
    except Exception as e :
        print("exption found: {e}")
        return []
