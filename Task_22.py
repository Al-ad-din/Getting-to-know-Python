"""Задача 22. Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов 
второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
"""

n, m = map(int, input(
    'Введите количество элементов 1 и 2 набора чисел через пробел: ').split())

list_1 = []
print('Введите первый набор чисел через enter: ')
for i in range(n):
    list_1.append(int(input()))

list_2 = []
print('Введите второй набор чисел через enter: ')
for i in range(m):
    list_2.append(int(input()))

uniq_1 = set(list_1)
uniq_2 = set(list_2)

uniq_inter=uniq_1.intersection(uniq_2)
print('Во введенных наборах встречаются числа: ', end='')
print(*sorted(uniq_inter))
