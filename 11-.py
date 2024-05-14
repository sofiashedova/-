import nltk
nltk.download('gutenberg')
from nltk.book import text1

with open("текст_11.txt", "r") as file:
    text_from_file = file.read()

nltk.download('book')
nltk.download('genesis')

text = nltk.Text(text_from_file.split())

corpus_path = nltk.data.find('corpora/genesis')
nltk.data.path.append(corpus_path)

text.dispersion_plot(["whale", "ocean", "ship"])

