# 4 zadanie
# Перенесите к себе код #3 и исправьте все ошибки,
# сделайте так чтобы код работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.
# a = (0)
# b = (1,)
#
# numbers = []
# while b > a:
# numbers += b
# b += 1
try:
    a = (0)
    b = (1,)

    numbers = []
    i = 0
    while b[i] > a[i]:
        i += 1
        numbers.append(b)
        b += 1
except TypeError:
    print('Type Error')
    "C:\Users\azizb\Desktop\NariWork\11_try_except"