# Представьте Вы хотите взять какой-то набор данных и переконвертировать его в SET для удаления дубликатов,
# возьмите values и проверьте каждый ли элемент доступен для конвертации.
# Создайте список. Проитерируйте values.
# Если объект в списке можно переконвертировать добавьте True в новый список иначе добавьте False.
# После, с помощью функции all() скажите можно ли конвертировать values в SET?

def convert(values):
    bool_list = []
    for i in values:
        if isinstance(i, int) or isinstance(i, str) or isinstance(i, bool) or isinstance(i, tuple) or isinstance(i, float):
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list

values = ("TURUSBEKOVA 109/1", 10, 1005, ["TABLES", "CHAIRS"], 23.00)
if all(convert((values))) == True:
    print('Списко можно конвертировать ')
else:
    print('Список нельзя конвертировать ')