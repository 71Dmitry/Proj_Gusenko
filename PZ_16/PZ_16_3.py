'''
Для задачи из блока 1 создать две функции, save_def и load_def,
которые позволяют сохранять информацию из экземпляров класса (3 шт.)
в файл и загружать ее обратно. Использовать модуль pickle для
сериализации и десериализации объектов Python в бинарном формате.
'''
import pickle

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

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
            return obj

# Пример использования
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

# Сохранение матрицы в файл
matrix1.save('matrix_data.pkl')

# Загрузка матрицы из файла
loaded_matrix = Matrix.load('matrix_data.pkl')

print(loaded_matrix.add(matrix2).data)  # Сложение матриц
print(loaded_matrix.subtract(matrix2).data)  # Вычитание матриц
print(loaded_matrix.multiply(matrix2).data)  # Умножение матриц
