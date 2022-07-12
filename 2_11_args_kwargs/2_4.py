# Напишите функцию которая спрашивает число N и
# генерирует вам List состоящий из N разных элементов.
from random import choice
def make_rand(n):
    rand_list = [True, '963', 963, 963.963, False, 123, 'wdwad', 1, 0, 'adwadwa', 4213, 42.42]
    list1 = []
    for i in range(n):
        list1.append(choice(rand_list))
    return list1
print(make_rand(7))


