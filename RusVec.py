from gensim.models import KeyedVectors


model_path = 'C:/Users/sofia/Downloads/212/model.ckpt' 
model = KeyedVectors.load_word2vec_format(model_path, binary=True)


words = ['автомобиль', 'кот', 'дом', 'книга', 'путешествие']

for word in words:
    similar_words = model.most_similar(word, topn=10)
    print(f"Ближайшие соседи для слова '{word}':")
    for neighbor, similarity in similar_words:
        print(f"{neighbor}: {similarity:.4f}")
