'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''
n = int(input('Введите количество элементов первого списка: '))
m = int(input('Введите количество элементов второго списка: '))

list_1 = list()
for _ in range(n):
    n1 = int(input('Введите число, для добавления в первый список: '))
    list_1.append(n1)

list_2 = list()
for _ in range(m):
    m1 = int(input('Введите число, для добавления во второй список: '))
    list_2.append(m1)

list_1, list_2 = set(list_1), set(list_2)
print(sorted(list(list_1 & list_2)))