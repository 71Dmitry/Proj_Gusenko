'''
   2. Из предложенного текстового файла (text18-7.txt) вывести
   на экран его содержимое, количество букв в нижнем регистре.
   Сформировать новый файл, в который поместить текст в стихотворной
   форме предварительно поставив последнюю строку между второй и третьей.
'''
with open("text18-7.txt", "r", encoding='utf-16') as file:
    text = file.read()
    word = sum(1 for char in text if char.islower())
    print("Содержимое файла:")
    print(text)
    print(f"Количество букв в нижнем регистре: {word}")

lines = text.split("\n")
if len(lines) >= 3:
    new_text = "\n".join(lines[:2] + [lines[-1]] + lines[2:-1])

    with open("poem.txt", "w") as new_file:
        new_file.write(new_text)

