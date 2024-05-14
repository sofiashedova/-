import pymorphy2
import matplotlib.pyplot as plt
from collections import Counter


morph = pymorphy2.MorphAnalyzer()


with open("текст 10.txt", "r") as file:
    text = file.read()


words = text.split()
lemmas = [morph.parse(word)[0].normal_form for word in words]


word_freq = Counter(lemmas)

top_words = word_freq.most_common(10)


top_words, freq = zip(*top_words)


plt.figure(figsize=(10, 6))
plt.bar(top_words, freq, color='skyblue')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('Наиболее частотные слова в тексте')
plt.xticks(rotation=45)
plt.show()
