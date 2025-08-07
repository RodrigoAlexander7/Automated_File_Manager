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

"""
def make TF():
    N = len(docs)  # número total de documentos
    idf = {t: math.log(N / len(indice_invertido[t])) for t in indice_invertido}

def make_IDF():
    for doc_nombre, palabras in docs.items():
    conteo = Counter(palabras)  # frecuencia en el documento
    total_palabras = len(palabras)

    vector_doc = []

    for t in vocabulario:
        tf = conteo[t] / total_palabras if t in conteo else 0
        vector_doc.append(tf * idf[t])

    tfidf_matrix.append(vector_doc)

"""    