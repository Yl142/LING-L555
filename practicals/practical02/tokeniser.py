import sys
import nltk

nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = sys.stdin.read()
listOfWords = word_tokenize(text)

result = ""
for i in listOfWords:
    result += i + "\n"

sys.stdout.write(result)

    