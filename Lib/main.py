text = input("Введіть текст: ")
text = text.lower()
text = text.replace(" ", "")
if text == text[::-1]:
    print("Це паліндром")
else:
    print("Це не паліндром")