# 2 zadanie
# Возьмите код #1 и создайте для него try... except...
# Создайте несколько except выражений для разных типов ошибок.
try:
    at = 10
    in1 = 15
    wo = 20

    for e in range(-at, at):
    print(wo / e)
    if at > '5':
    print("at > 5)
except IndentationError:
    print('Табуляция ')
except SyntaxError:
    print('Ошибка синтаксиса ')
except NameError:
    print('Ошибка названия ')
except TypeError:
    print('Ошибка типа данных ')
