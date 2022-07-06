# 9 zadanie
n = 1
k = 1
for i in range(-100, 100):
    if i % 13 == 0 and i % 2 == 0:
        n += 1
        i = i ** 2
    if i % 7 == 0 and i % 2 != 0:
        k += 1
        i = i ** 2
print(n)
print(k)
