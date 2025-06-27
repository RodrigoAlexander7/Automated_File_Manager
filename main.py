
from app.pdf_reader import get_words_pdf
from app.pdf_reader import get_file_names
from app.indexer import create_inverted_index 


if __name__ == "__main__":
    route = "test_files"
    list_pdf = get_file_names(route)
    for name in list_pdf:
        dictionary = get_words_pdf(name)
        print(create_inverted_index(dictionary))  
    
    