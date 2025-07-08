from . import pdf_reader
from pathlib import Path



def documents_content(document_directory):
    dict_doc_words = {} 
    document_directory = Path(document_directory)
    for file in document_directory.iterdir():
        file_name = file.name
        dict_doc_words[file_name] = pdf_reader.clean_words_pdf(file)
  
#FALTA OCURRENCIAS GENERALES POR PALABRA

#FALTA EL INDICE INVERTIDO CON TODO EL CORPUS
