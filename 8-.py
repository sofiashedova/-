import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')
stemmer = PorterStemmer()
word ="listening"
stemmer_word = stemmer.stem(word)
print(stemmer_word)