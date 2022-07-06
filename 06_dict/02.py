# 2 zadanie
login = {}
for i in range(3):
    name = input('введите имя ')
    password = input('Введите пароль ')
    login[f'{name}'] = password
print(login)