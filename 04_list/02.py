# 2 zadanie
list1 = [
    'JACK', 'JIMMY1', 'JACKSON2',
    'JHON1', 'JACKSON2', 'JHON1',
    'JIMMY2', 'JACKSON1', 'JHON2',
    'JACK1', 'JIMMY2', 'JACK1',
    'JACKSON2', 'JHON1', 'JACK2',
    'JIMMY1', 'JACK2', 'JACKSON1', 'JHON2'
]
k = 0
for i in list1:
    if i == 'JACK':
        k += 1
print(f'JACK встретилось {k} раз')
