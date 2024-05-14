from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt

with open("текст 1.txt", "r") as file:
    text1 = file.read()
with open("текст 2.txt", "r") as file:
    text2 = file.read()
with open("текст 3.txt", "r") as file:
    text3 = file.read()

corpus = [text1, text2, text3]

tfidf_vectorizer = TfidfVectorizer()

tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

feature_names = tfidf_vectorizer.get_feature_names_out()
for i, text in enumerate(corpus):
    scores = tfidf_matrix[i].toarray().flatten()
    key_words = [feature_names[j] for j in scores.argsort()[::-1][:5]]  # Выбираем топ-5 ключевых слов
    print(f"Ключевые слова для текста {i+1}: {key_words}")

plt.figure(figsize=(12, 6))
plt.bar(key_words, tfidf_matrix[0].toarray().flatten()[tfidf_matrix[0].toarray().argsort()[0]][::-1][:5], color='skyblue')
plt.xlabel('Ключевые слова')
plt.ylabel('TF-IDF Score')
plt.title('TF-IDF ключевых слов для текста 1')
plt.xticks(rotation=45)
plt.show()
