# Написать lambda которая принимает 3 параметра и
# умножает все параметры между собой.
# Функция должна вернуть строку: "Объём бассейна " и
# значение которое получилось.
a = 5
b = 6
c = 9
print((lambda a, b, c: f'Обьем бассейна {a * b * c}')(a, b, c))
