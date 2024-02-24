"""
        1. Организовать и вывести последовательность из N случайных целых чисел. 
        Из исходной последовательности организовать первую последовательность, 
        содержащую четные числа, и вторую для всех остальных. Найти среднее 
        арифметическое в полученных последовательностях.1.
"""
from random import randint

all_list = [randint(-100,100) for i in range(20)]
print(f'Изначальный список: {all_list}')

del_2 = [num for num in all_list if num % 2 == 0]
print(f'Список четных значений: {del_2}')
sr_del_2 = sum(del_2)/len(del_2)
print(f'среднее арифметическое: {round(sr_del_2,1)}')

ne_del_2 = [num for num in all_list if num % 2 != 0]
print(f'Список четных значений: {ne_del_2}')
sr_ne_del_2 = sum(ne_del_2)/len(ne_del_2)
print(f'среднее арифметическое: {round(sr_ne_del_2,1)}')