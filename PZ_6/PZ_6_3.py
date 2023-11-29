'''
3. Дан список размера N. Возвести
в квадрат все его локальные минимумы
(то есть числа, меньшие своих соседей).
'''

from random import randint
i = 0
while i == 0:
    try:
        N = int(input('Сколько элементов в списке? '))
        a = []
        b = []
        bb = []
        for i in range(0, N):
            a.append(randint(0, 100))
        print(a)
        for o in range(len(a)):
            if o == 0 and a[o] < a[o+1]:
                b.append(a[o])

            if o == len(a)-1 and a[o] < a[o-1]:
                b.append(a[o])

            elif a[o] < a[o-1] and a[o] < a[o+1]:
                b.append(a[o])

        for i in range(len(b)):
            bb.append(b[i]*b[i])

        print(f'Локальные минимумы: {b}')
        print(f'Квадраты локальных минимумов: {bb}')
        i = 1
    except:
        print('Надо ввести число')

