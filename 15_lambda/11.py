# Создайте lambda функцию которая принимает одно число и возвращает это число умноженное на 1.185.
# Вам дан список
# [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
# пройдите по списку и примените функцию к каждому числу.
nums = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
list1 = []
lam = lambda i :i * 1.185
for i in nums:
    list1.append(lam(i))
print(list1)

