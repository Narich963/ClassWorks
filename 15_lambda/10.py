# Создайте функцию которая генерирует 10 чисел Фибоначчи:
#
# 1,1,2,3,5,8,13,21,34,...

def fibonacci(n):
    fi_prev = 1
    fi_new = fi_prev
    for i in range(n):
        fi_prev, fi_new = fi_new, fi_prev + fi_new
        print(fi_new)
fibonacci(10)

