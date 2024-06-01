'''
7. Создайте класс «Матрица», который имеет атрибуты количества
строк и столбцов. Добавьте методы для сложения, вычитания и умножения матриц.
'''
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def add(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            return "Матрицы имеют разные размеры и не могут быть сложены"

    def subtract(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] - other.data[i][j]
            return result
        else:
            return "Матрицы имеют разные размеры и не могут быть вычтены"

    def multiply(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] += self.data[i][j] * other.data[i][j]
            return result
        else:
            return "Умножение невозможно из-за неправильных размеров матриц"


matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

print(matrix1.add(matrix2).data)
print(matrix1.subtract(matrix2).data)
print(matrix1.multiply(matrix2).data)
