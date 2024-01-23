'''Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16,
отражающая продажи продукции по дням в кг.
Преобразовать информацию из строки в словари, с использованием
функции найти минимальные продажи по каждому виду продукции, результаты вывести на экран.'''

data = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
items = data.split()

first_ch = items[1:6]
first_ch = list(first_ch)
for i in range(len(first_ch)):
    first_ch[i] = int(first_ch[i])
m1 = min(first_ch)

two_ch = items[7:]
two_ch = list(two_ch)
for i in range(len(two_ch)):
    two_ch[i] = int(two_ch[i])
m2 = min(two_ch)

fr1 = items[0]
fr2 = items[6]

d = {}
d[fr1] = m1
d[fr2] = m2
print(d)