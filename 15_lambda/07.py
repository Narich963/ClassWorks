# Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА.
# Простое число - это число которое делится только на себя и на 1.

def Is_Simple(n):
    d = 2
    while d < n:
        if n % d == 0:
            return f'{n} - Составное число '
        d += 1
    return f'{n} - Простое число '
print(Is_Simple(23))
