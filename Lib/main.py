text = input("Enter a string: ")
reserve = input("Enter a list of reserved words: ").split()

for word in reserve:
    text = text.replace(word, word.upper())

print(text)

