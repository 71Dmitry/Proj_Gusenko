'''2. Дана строка, содержащая полное имя файла, то есть имя диска,
 список каталогов (путь), собственно имя и расширение.
  Выделить из этой строки расширение файла (без предшествующей точки).
'''


file_name = "C:/Users/username/Documents/file.txt"
r = file_name.split('.')[-1]
print(r)