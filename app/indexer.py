from app.constant import STOPWORDS_EN
from app.constant import STOPWORDS_ES

inverted_index = {}

def create_inverted_index(words_dict):
    TOTAL = len(words_dict)
    UMBRAL = 0.1 * TOTAL
    for word in words_dict.keys():
        if words_dict[word] > UMBRAL:
            inverted_index[word] = 'file_name'
# Left specify the filename as constant but the idea is here


# High DF Threshold
# method to remove words that appears on the 90% of the total documents 

# Low DF Threshold
# method to remove tha words that only apears on the 1% of the documents 

