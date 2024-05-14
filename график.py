#график частотных слов
import matplotlib.pyplot as plt
from collections import Counter

with open("текст 8.txt", "r") as file:
    text = file.read()

words = [word for word in text.split() if len(word) >= 3]

word_freq = Counter(words)

# Получение наиболее часто встречающихся слов (можно изменить значение n на нужное количество)
n = 10
most_common_words = word_freq.most_common(n)

# Разделение слов и их частот для построения графика
words, freq = zip(*most_common_words)

# Построение графика
plt.figure(figsize=(12, 6))
plt.bar(words, freq, color='skyblue')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('Частотные слова (без слов короче 3 букв)')
plt.xticks(rotation=45)
plt.show()
