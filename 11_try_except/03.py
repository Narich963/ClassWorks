# 3 zadanie
# Перенесите к себе код #2 и исправьте все ошибки,
# сделайте так чтобы работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.
'''
lst = []

for i in renge(10):
lst.apend(i)
a = list(revesed(lst))
sls_obj = slice('0','8')
print(а[sls_obj])
'''
try:
    lst = []
    for i in range(10):
        lst.append(i)
        a = list(reversed(lst))
        sls_obj = slice(0, 8)
        print(a[sls_obj])
except TypeError:
    print('Ошибка приведения типов ')
