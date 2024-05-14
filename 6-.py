with open("текст 6.txt", "r") as file:
    text = file.read()
    clean_text = ""
    for word in text.split():
        clean_word = ''.join(filter(str.isalpha, word))
        if clean_word:
            clean_text += clean_word + ""
print(clean_text)