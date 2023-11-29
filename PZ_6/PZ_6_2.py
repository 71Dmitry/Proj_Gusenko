'''
2. Дан список размера N. Найти минимальный
из его локальных максимумов (локальный
минимум это элемент, который меньше
любого из своих соседей).
'''

from random import randint
i = 0
while i == 0:
    try:
        N = int(input('Сколько элементов в списке? '))
        a = []
        b = []
        bb = 0
        i = 0
        for i in range(0, N):
            a.append(randint(0, 100))
        print(a)
        for o in range(len(a)):
            if o == 0 and a[o] > a[o+1]:
                b.append(a[o])

            if o == len(a)-1 and a[o] > a[o-1]:
                b.append(a[o])

            elif a[o] > a[o-1] and a[o] > a[o+1]:
                b.append(a[o])

        bb = min(b)
        print(b)
        print(f'Минимум из локальных максимумов: {bb}')
        i = 1
    except:
        print('Надо ввести число')