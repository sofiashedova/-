import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words('russian'))

with open("текст 7.txt", "r") as file:
    text = file.read()
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    clean_text = ''.join(filtered_words)
print(clean_text)
