import sys

text = sys.stdin.read()

result = text.replace(". ", ". \n")

sys.stdout.write(result)