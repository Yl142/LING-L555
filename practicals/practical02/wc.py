import sys

spaceCounter = 0
lineCounter = 0
charCounter = 0
for c in sys.stdin.read():
	if c == ' ':
        spaceCounter += 1
    elif c == '\n':
        lineCounter += 1
    else:
        charCounter += 1

print("# of lines: " + lineCounter)
print("# of tokens: " + spaceCounter)
print("# of characters: " + charCounter)