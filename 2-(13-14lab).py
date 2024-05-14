import re

with open("текст 2.txt", "r") as file:
    text = file.read()
    tokens = re.findall(r'\w+|[^\w\s]', text)
print(tokens)
