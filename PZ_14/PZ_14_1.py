"""
    7. В исходном текстовом файле (Dostoevsky.txt) найти все годы 
    деятельности писателя (например, 1821 года, 1837 год, 1843 году 
    и так далее по всему тексту). Посчитать количество полученных элементов.
"""


import re

# Открываем файл и считываем его содержимое
with open("Dostoevsky.txt", "r") as file:
    text = file.read()

# Используем регулярное выражение для поиска всех годов
years = re.findall(r'\b\d{4}\b', text)

# Выводим все найденные годы
print('Найденные годы деятельности писателя:')
for year in years:
    print(year, end= ' ')
print('\n')
# Подсчитываем количество найденных годов
count = len(years)
print(f'Всего найдено {count} годов деятельности писателя.')

# \d любая цифра
# \D любой символ, кроме цифры.
# . 1 любой символа, кроме символа новой строки
# \s любой пробельный символ
# \S любой не пробельный символ
# \w любая буква, цифра, нижнее подчеркивание
# \W любая не буква, не цифра, не нижнее подчеркивание(то есть знаки, пробелы)
# \b начало или конец слова
# [5-7] символ, в диапазоне от 5 до 7 включительно.
# [^5-7] символ, который не входит в этот диапазон включительно.
# search(r"D|k", s) выведет на выбор, что найдет быстрее.
# search(r"\d{5}", s) выведет 5 повторений.
# search(r"\d{1-5}", s) выведет в диапазоне от 1 до 5 повторений.
# search(r"\d{5,}", s) выведет не меньше 5 повторений.
