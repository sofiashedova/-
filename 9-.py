import pymorphy2

morph = pymorphy2.MorphAnalyzer()

with open("текст 9.txt", "r") as file:
    text = file.read()


words = text.split()


lemmas = [morph.parse(word)[0].normal_form for word in words]

lemmatized_text = ' '.join(lemmas)

print("Исходный текст:", text)
print("Лемматизированный текст:", lemmatized_text)
