"""
    В матрице элементы строки N (N задать с клавиатуры) увеличить 3 раза
"""
from random import randint
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

matrix = [[randint(1,20) for j in range(n)] for i in range(m)]

print(f"Исходная матрица:")
for i in matrix:
    print(i)

row_number = int(input("Введите номер строки, которую нужно увеличить в 3 раза: ")) - 1

matrix[row_number] = [elem * 3 for elem in matrix[row_number]]

print("Измененная матрица:")
for row in matrix:
    print(row)
