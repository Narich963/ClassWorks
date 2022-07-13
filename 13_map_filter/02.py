# Спросите у пользователя 5 чисел добавьте их в SET и скажите какое самое маленькое число он ввел.

def min_set():
    num_set = set()
    while len(num_set) < 5:
        num = int(input('Введите 5 чисел '))
        num_set.add(num)
    return min(num_set)
print(f'{min_set()} самое маленькое число ')
