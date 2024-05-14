#кэширование лемм
import nltk
from functools import lru_cache
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

@lru_cache(maxsize=None)
def lemmatize_cached(word):
    return lemmatizer.lemmatize(word)

word = input("Введите слово для лемматизации: ")
print(lemmatize_cached(word))

word = input("Введите еще одно слово для лемматизации: ")
print(lemmatize_cached(word))



