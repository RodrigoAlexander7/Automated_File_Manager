import constant
import pymupdf
from typing import List


def get_words_pdf(path_pdf: str, max_pag: int = 200)->str:
    dict_words = {} 
    try:
        with pymupdf.open(path_pdf) as doc:
            len_pag = min(len(doc), max_pag)
            for i in range(len_pag):
                words = doc[i].get_text("words")
                for word_info in words:
                    _,_,_,_,word,_,_,_ = word_info
                    word = word.lower()
                    if not (word in constant.STOPWORDS_EN or 
                           word in constant.STOPWORDS_ES or  
                           word in constant.SYMBOLS):
                        dict_words[word] = dict_words.get(word,0) + 1
                    

        return dict_words 
    
    except Exception as e:
        print(f"Error in lecture {path_pdf}:{e}")
        return ""
    

