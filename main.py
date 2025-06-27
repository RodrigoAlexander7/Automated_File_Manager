import app.pdf_reader as pdf_reader
import app.indexer as indexer  

import app.constant as constant

if __name__ == "__main__":
    route = constant.PATH_DIRECTORY
    list_pdf = pdf_reader.get_file_names(route)
    for file_path in list_pdf:
        dictionary = pdf_reader.get_words_pdf(file_path)
        index = indexer.create_inverted_index(dictionary,file_path.name)
    print(index)
    indexer.save_inverted_index(index)
    #WEEEEEEE NEED TO CONVERT FROM DEFAULT DICTIONARY TO A NORML DICT