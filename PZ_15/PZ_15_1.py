'''
    Приложение АПТЕКА для автоматизации работы аптечных пунктов.
    Таблица Лекарственные Средства должна содержать следующую информацию:
    Код, Пазвание препарата, Применение, Количество, Цена, Страна-производитель.
'''
import sqlite3 as sq

# Создаем подключение к базе данных
conn = sq.connect('apteka.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS лекарства")


cur.execute('''
    CREATE TABLE IF NOT EXISTS лекарства (
        Код INTEGER PRIMARY KEY,
        Название_препарата TEXT,
        Применение TEXT,
        Количество INTEGER,
        Цена REAL,
        Страна_производитель TEXT
    )
''')


zap = [
    (1, 'Аспирин', 'Противовоспалительное', 1000, 10.5, 'Россия'),
    (2, 'Аспирин', 'Противовоспалительное', 10, 10, 'Россия'),
    (3, 'Аспирин', 'Противовоспалительное', 1700, 18.5, 'Россия'),
    (4, 'Аспирин', 'Противовоспалительное', 100, 13.5, 'Россия'),
    (5, 'Аспирин', 'Противовоспалительное', 1003, 1, 'Россия'),
    (6, 'Аспирин', 'Противовоспалительное', 1003, 5, 'Россия'),
    (7, 'Аспирин', 'Противовоспалительное', 1020, 100, 'Россия'),
    (8, 'Аспирин', 'Противовоспалительное', 1050, 150, 'Россия'),
    (9, 'Аспирин', 'Противовоспалительное', 100, 50, 'Россия'),
    (10, 'Аспирин', 'Противовоспалительное', 1010, 2, 'Россия')
]


with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO лекарства VALUES (?, ?, ?, ?, ?, ?)", zap)


with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM лекарства")
    result = cur.fetchall()
    print(f'Полное содержание таблицы "лекарства":\n{result}')

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM лекарства WHERE Цена < 15")
    result = cur.fetchall()
    print(f'Содержание таблицы "лекарства", где Цена меньше 15:\n{result}')

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM лекарства WHERE Цена > 15")
    result = cur.fetchall()
    print(f'Содержание таблицы лекарства, где Цена больше 15:\n{result}')

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE лекарства SET Цена = Цена+4 WHERE Количество=100")

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE лекарства SET Цена = Цена+1 WHERE Количество!=1010")

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE лекарства SET Цена = Цена+2 WHERE Количество>1030")

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM лекарства WHERE Количество=100")

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM лекарства WHERE Цена=150")

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM лекарства WHERE Цена>20")

with sq.connect('apteka.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM лекарства")
    result = cur.fetchall()
    print(f'Итоговое содержание таблицы "лекарства":\n{result}')