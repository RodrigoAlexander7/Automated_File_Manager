from collections import defaultdict
import app.constant as constant
import json

save_path = constant.JSON_INVERTED_INDEX_PATH
inverted_index = defaultdict(list)

def create_inverted_index(words_dict,file_name):
    TOTAL = len(words_dict)
    UMBRAL = 0.01 * TOTAL
    for word in words_dict.keys():
        if words_dict[word] > UMBRAL:
            inverted_index[word].append(file_name)
    return inverted_index

#creation of a inverted index just for one specific document
def create_single_inverted_index_(words_dict,file_name):
    doc_inverted_index = {}
    TOTAL = len(words_dict)
    UMBRAL = 0.01 * TOTAL
    for word in words_dict.keys():
        if words_dict[word] > UMBRAL:
            doc_inverted_index[word].append(file_name)
    return doc_inverted_index
# Left specify the filename as constant but the idea is here


# High DF Threshold
# method to remove words that appears on the 90% of the total documents 

# Low DF Threshold
# method to remove tha words that only apears on the 1% of the documents 
# or when the ocurrences are < 1 per document

def save_inverted_index(inverted_index):
    try:
        with open(save_path, "w") as save_file:
            json.dump(inverted_index, save_file,indent = 4)
        print(f"Inverted index saved to {save_path} on Json")
    except Exception as e:
        print(f"Exeption: {e}")

def read_from_json():
    inverted_index_dict = {}
    try:
        with open(save_path, "r") as json_file:
            inverted_index_dict = json.load(json_file)
            return inverted_index_dict
    except Exception as e:
        print(f"Exeption: {e}")