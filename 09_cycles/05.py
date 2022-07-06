# 5 zadanie
for i in range(11):
    print(i, end=' ')
    for j in range(9, -1, -1):
        if i >= 10:
            print(j, end=' ')