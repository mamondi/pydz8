text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
sentence_count = 0

#Вибір методу підрахунку
act = int(input("Choose the method of counting[1/2]: "))

#Цей метод ураховує останню крапку в тексті, через що показує невірний результат
if act == 1:
    for i in text:
        i = text.split(".")
        count = len(i)
        print("The number of sentences in the text is: ", count)
        break


if act == 2:
    for char in text:
        if char == "." or char == "!" or char == "?":
            sentence_count += 1
            while sentence_count == 4:
                print("The number of sentences in the text is: ", sentence_count)
                break