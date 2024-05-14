with open("текст 4.txt", "r") as file:
    text = file.read()
    words_list = text.split()
    word_count = len(words_list)
print(word_count)