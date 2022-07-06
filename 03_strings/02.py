# 2 zadanie
str8 = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"
list_str8 = str8.split(' ')
for i in list_str8:
    if i == type(int):
        print(f'{i} имеет тип данных int ')
    if i == type(float):
        print(f'{i} имеет тип данных float')
    if i == type(str):
        print(f'{i} имеет тип данных string ')
