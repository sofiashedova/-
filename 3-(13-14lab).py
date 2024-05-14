import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

with open("текст 3.txt", "r") as file:
    text = file.read()
    tokens = word_tokenize(text)
print(tokens)
