from collections import Counter

with open("текст 5.txt", "r") as file:
    text = file.read()
    words_list = text.split()
    word_counts = Counter(words_list)
print("Количество слов")
for word, count in word_counts.items():
    print(f"{word}: {count}")
    