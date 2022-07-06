# 3 zadanie
list1 = [
    'JACK', 'JIMMY1', 'JACKSON2',
    'JHON1', 'JACKSON2', 'JHON1',
    'JIMMY2', 'JACKSON1', 'JHON2',
    'JACK1', 'JIMMY2', 'JACK1',
    'JACKSON2', 'JHON1', 'JACK2',
    'JIMMY1', 'JACK2', 'JACKSON1', 'JHON2'
]
n = 0
while n < 5:
    if n % 2 == 0:
        list1.pop(n)
    if n % 2 == 1:
        list1.pop(n)
    n += 1
print(list1)