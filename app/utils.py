from . import pdf_reader
from . import indexer

def create_from_route(route):
    list_pdf = pdf_reader.get_file_names(route)
    for file_path in list_pdf:
        dictionary = pdf_reader.get_words_pdf(file_path)
        index = indexer.create_inverted_index(dictionary,file_path.name)
    print(index)
    indexer.save_inverted_index(index)
    
    loaded_inverted_index = indexer.read_from_json()
    print(loaded_inverted_index)