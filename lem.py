#лемматизация и морфоанализ
import spacy

# Загружаем языковую модель
nlp = spacy.load("en_core_web_sm")

with open("текст 12.txt", "r") as file:
    text = file.read()

doc = nlp(text)

for token in doc:
    print(token.text)