'''
    1. Средствами языка Python сформировать текстовый файл (.txt),
    содержащий последовательность из целых положительных и отрицательных чисел.
    Сформировать новый текстовый файл (.txt) следующего вида, предварительно
    выполнив требуемую обработку элементов:
    Исходные данные:
    Количество элементов:
    Среднее арифметическое элементов:
    Положительные четные элементы:
    Сумма положительных четных элементов:
    Среднее арифметическое положительных четных элементов:
'''
from random import randint
elem = 0
sr = 0
pol = []
sr = []
pol_sum = 0
sum = 0
with open('counts.txt', 'w') as f:
    with open('results.txt', 'w') as ff:
        ff.write('Исходные данные: ')
        for i in range(20):
            chislo = randint(-100, 100)
            f.write(str(chislo) + ' ')
            ff.write(str(chislo) + ' ')
            elem += 1
            sum += chislo
            sr.append(chislo)
            if chislo > 0 and chislo % 2 == 0:
                pol.append(chislo)
                pol_sum += chislo
        sr_vse = sum/len(sr)
        sr_pol = pol_sum/len(pol)
        ff.write('\n')
        ff.write('Количество элементов: ' + str(elem) + '\n')
        ff.write('Среднее арифметическое элементов: ' + str(sr_vse) + '\n')
        ff.write('Положительные четные элементы: ' + str(elem) + '\n')
        ff.write('Сумма положительных четных элементов: ' + str(pol_sum) + '\n')
        ff.write('Среднее арифметическое положительных четных элементов: ' + str(elem))
























