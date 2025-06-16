import fitz
from typing import List

def get_text_pdf(path_pdf: str, max_pag: int = 200)->str:
    full_text = ""
    try:
        with fitz.open(path_pdf) as doc:
            len_pag = min(len(doc), max_pag)
            for i in range(len_pag):
                full_text += doc[i].get_text()
        return full_text
    except Exception as e:
        print(f"Error in lecture {path_pdf}:{e}")
        return ""