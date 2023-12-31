'''
Вариант 3. Скорость лодки в стоячей воде Ѵ км/ч, скорость течения реки U км/ч (UV).
 Время движения лодки по озеру Т1 ч, а по реке (против течения) - Т2 ч. Определить путь 5,
пройденный лодкой (путь - время скорость). Учесть, что при движении против течения
 скорость лодки уменьшается на величину скорости течения.
'''
# обработка исключений с помощью конструкции try, except.
 try:
   # Запрашиваем ввод данных пользователем
   V = float(input('Введите скорость лодки: '))
   U = float(input('Введите скорость течения: '))
   T1 = float(input('Введите время, которая лодка плыла по озеру: '))
   T2 = float(input('Введите время, которое лодка плыла по реке: '))
   # производим вычисления.
   S1 = V*T1
   S2 = (V-U)*T2
   S = S1 + S2
   # Вывод данных
   print(f'Время, за которое лодка прошла путь: {S}')
# ветвь работает в случае ошибки в первой ветви.
 except ValueError:
    print('Надо ввести число')