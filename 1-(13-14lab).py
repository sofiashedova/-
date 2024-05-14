with open("текст.txt", "r") as file:
    text = file.read()
    tokens = text.split()
print(tokens)
