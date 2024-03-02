"""
    В матрице элементы последнего столбца заменить на -1.
"""
from random import randint
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

matrix = [[randint(1,20) for j in range(n)] for i in range(m)]

print("Исходная матрица:")
for i in matrix:
    print(i)

matrix = [[matrix[i][j] if j < n-1 else -1 for j in range(n)] for i in range(m)]

print("Конечная матрица:")
for i in matrix:
    print(i)