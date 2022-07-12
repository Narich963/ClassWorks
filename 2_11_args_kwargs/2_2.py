# Напишите функцию которая спрашивает у пользователя число и
# выводит ему на экран именно столько строк самой себя как текст.

def ret_string(a):
    if a == 1:
        return f'{a}'
    if a <= 0:
        return 'Error'
    if a > 1:
        return f'{a}\n' * a

print(ret_string(9))