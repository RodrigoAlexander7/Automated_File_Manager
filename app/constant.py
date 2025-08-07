import string
import re

SUPPORTED_FILE_EXTENSIONS = {'.txt', '.md', '.doc', '.docx', '.pdf'}
PATH_DIRECTORY = "test_files"
JSON_INVERTED_INDEX_PATH = "inverted_index.json"

MIN_WORD_LENGTH = 2  
MAX_WORD_LENGTH = 14

DOC_EXTENSION:frozenset[str] = frozenset({
  '.doc', '.txt', '.docx', '.md'
})

MEDIA_EXTENSION:frozenset[str] = frozenset({
  '.jpg', '.png', '.img', '.svg', '.gif', '.jpeg', '.mkv', '.mpg4', '.mp4', '.MOV'
})

SLIDE_EXTENSION:frozenset[str] = frozenset({
  '.ppt', '.pptx'
})

CODE_EXTENSION:frozenset[str] = frozenset({
  '.cpp', '.java', '.py', '.pl', '.js', '.ts', '.ini', '.accdb', '.sql', '.mermaid'
})

COMPRESS_EXTENSION:frozenset[str] = frozenset({
  '.zip', '.rar', '.7z', '.gz' , '.tgz', '.izo', '.tar'
})

PDF_EXTENSION:frozenset[str] = frozenset({
  '.pdf'
})

EXECUTABLE_EXTENSION:frozenset[str] = frozenset({
  '.exe', '.msi'
})

SHEET_EXTENSION:frozenset[str] = frozenset({
  '.xls', '.xlsx', '.csv'
})


STOPWORDS_EN:frozenset[str] = frozenset({
    'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'also', 
    'am', 'an', 'and', 'any', 'are', 'aren', "aren't", 'as', 'at', 'be', 
    'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 
    'by', 'can', 'cannot', 'could', 'couldn', "couldn't", 'd', 'did', 'didn', 
    "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don', "don't", 
    'down', 'during', 'each', 'et', 'al', 'etc', 'few', 'for', 'from', 'further', 
    'had', 'hadn', "hadn't", 'has', 'hasn', "hasn't", 'have', 'haven', 
    "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 
    'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 
    'it', "it's", 'its', 'itself', 'just', 'll', 'm', 'ma', 'me', 'might', 
    'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 
    'needn', "needn't", 'no', 'nor', 'not', 'now', 'o', 'of', 'off', 'on', 
    'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 
    'own', 're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should', 
    "should've", 'shouldn', "shouldn't", 'so', 'some', 'such', 't', 'than', 
    'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 
    'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 
    'until', 'up', 've', 'very', 'was', 'wasn', "wasn't", 'we', 'were', 
    'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 
    'whom', 'why', 'will', 'with', 'won', "won't", 'would', 'wouldn', 
    "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've", 'your', 
    'yours', 'yourself', 'yourselves'
})

STOPWORDS_ES:frozenset[str] = frozenset({
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'este', 'esta', 
    'estos', 'estas', 'ese', 'esa', 'esos', 'esas', 'aquel', 'aquella', 
    'aquellos', 'aquellas', 'todo', 'toda', 'todos', 'todas', 'otro', 'otra', 
    'otros', 'otras', 'mismo', 'misma', 'mismos', 'mismas', 'tal', 'tales',
    
    'a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 
    'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 
    'sin', 'so', 'sobre', 'tras', 'versus', 'vía', 'del', 'al',
    
    'y', 'e', 'ni', 'o', 'u', 'pero', 'mas', 'sino', 'aunque', 'como', 
    'cuando', 'donde', 'mientras', 'que', 'si', 'porque', 'pues', 'luego',
    
    'yo', 'tú', 'él', 'ella', 'nosotros', 'nosotras', 'vosotros', 'vosotras', 
    'ellos', 'ellas', 'me', 'te', 'se', 'nos', 'os', 'le', 'les', 'lo', 'los', 
    'la', 'las', 'mi', 'mis', 'tu', 'tus', 'su', 'sus', 'nuestro', 'nuestra', 
    'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 
    'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 
    'suya', 'suyos', 'suyas', 'quien', 'quienes', 'cual', 'cuales', 'cuyo', 
    'cuya', 'cuyos', 'cuyas',
    
    'muy', 'más', 'menos', 'poco', 'mucho', 'tanto', 'tan', 'también', 
    'tampoco', 'sí', 'no', 'ya', 'aún', 'todavía', 'siempre', 'nunca', 
    'jamás', 'aquí', 'ahí', 'allí', 'allá', 'acá', 'donde', 'adonde', 
    'cuando', 'entonces', 'ahora', 'antes', 'después', 'luego', 'pronto', 
    'tarde', 'temprano', 'hoy', 'ayer', 'mañana', 'bien', 'mal', 'mejor', 
    'peor', 'así', 'cómo', 'quizá', 'quizás', 'acaso', 'apenas',
    
    'soy', 'eres', 'es', 'somos', 'sois', 'son', 'era', 'eras', 'éramos', 
    'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 
    'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería', 'serías', 
    'sería', 'seríamos', 'seríais', 'serían', 'sea', 'seas', 'seamos', 
    'seáis', 'sean', 'fuera', 'fueras', 'fuéramos', 'fuerais', 'fueran', 
    'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen', 'ser', 'siendo', 'sido',
    
    'estoy', 'estás', 'está', 'estamos', 'estáis', 'están', 'estaba', 'estabas', 
    'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 
    'estuvimos', 'estuvisteis', 'estuvieron', 'estaré', 'estarás', 'estará', 
    'estaremos', 'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos', 
    'estaríais', 'estarían', 'esté', 'estés', 'estemos', 'estéis', 'estén', 
    'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 
    'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 
    'estar', 'estando', 'estado',
    
    'he', 'has', 'ha', 'hemos', 'habéis', 'han', 'había', 'habías', 'habíamos', 
    'habíais', 'habían', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 
    'hubieron', 'habré', 'habrás', 'habrá', 'habremos', 'habréis', 'habrán', 
    'habría', 'habrías', 'habríamos', 'habríais', 'habrían', 'haya', 'hayas', 
    'hayamos', 'hayáis', 'hayan', 'hubiera', 'hubieras', 'hubiéramos', 
    'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos', 'hubieseis', 
    'hubiesen', 'haber', 'habiendo', 'habido', 'hay',
    
    'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen', 'tenía', 'tenías', 
    'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 
    'tuvisteis', 'tuvieron', 'tendré', 'tendrás', 'tendrá', 'tendremos', 
    'tendréis', 'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais', 
    'tendrían', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tuviera', 
    'tuvieras', 'tuviéramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 
    'tuviésemos', 'tuvieseis', 'tuviesen', 'tener', 'teniendo', 'tenido',
    
    'algo', 'alguien', 'algún', 'alguna', 'algunos', 'algunas', 'nada', 'nadie', 
    'ningún', 'ninguna', 'ningunos', 'ningunas', 'cosa', 'cosas', 'parte', 
    'partes', 'lugar', 'lugares', 'momento', 'momentos', 'tiempo', 'tiempos', 
    'año', 'años', 'día', 'días', 'vez', 'veces', 'forma', 'formas', 'manera', 
    'maneras', 'modo', 'modos', 'caso', 'casos', 'tipo', 'tipos', 'ejemplo', 
    'ejemplos', 'etc', 'etcétera'
})

SYMBOLS = {
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', 
    '}', '~', '¡', '¿', '“', '”', '‘', '’', '«', '»', '—', '–',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','et','al.'
}

PUNCTUATION_CHARS = frozenset(string.punctuation + '¡¿«»""''—–„‚‹›‚''""…•·‰†‡§¶†‡•‰¿¡')

#REGEX EXPRESION
NON_ALPHABETIC_PATTERN = re.compile(r'[^a-zA-Z]') 


def is_stopword(word):
  if len(word) <= MIN_WORD_LENGTH or len(word)>=(MAX_WORD_LENGTH):
    return True
  if NON_ALPHABETIC_PATTERN.search(word):
    return True
  if (word in STOPWORDS_EN or
      word in STOPWORDS_ES or
      word in SYMBOLS or
      word in PUNCTUATION_CHARS):
    return True
  return False
