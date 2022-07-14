# Создайте функцию которая принмает тип данных dictionary,
# но возвращает два Tuple в одном из них все ключи, в другом только значения.

def return_tuples(dict1):
    values_tuple = tuple(dict1.values())
    keys_tuple = tuple(dict1.keys())

    return values_tuple, keys_tuple


all_tuple = list(return_tuples({1:963, 963:1}))

print(all_tuple)