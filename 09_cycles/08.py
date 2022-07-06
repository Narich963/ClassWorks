# 8 zadanie
num = 963
if len(str(num)) == 2:
    print('3 значное число ')
if num > 0 and num % 2 == 0:
    print('Положительное четное число ')
if num % 31 == 0:
    print('делится на 31 без остатка ')
if num > 100 and num % 17 == 0 or num > 150 and num == 13**2:
    print(num)