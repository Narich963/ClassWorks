# 2 zadanie
n1 = int(input('Enter num 1 '))
n2 = int(input('Enter num 2 '))
n3 = int(input('Enter num 3 '))
if n1 > n2 and n1 > n3:
	print(n1 , ' больше остальных ')
elif n2 > n1 and n2 > n3:
	print(n2, ' больше остальных ')
elif n3 > n1 and n3 > n1:
	print(n3 , ' больше остальных ')
else:
	print('они все равны ')

