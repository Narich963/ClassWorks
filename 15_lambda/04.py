# Создайте функцию которая принимает слово и
# создаёт файл с таким именем в той же директории,
# где был запущен Ваш .py файл.

def make_file(word):
    txt = f'{word}.txt'
    with open(txt, 'w') as file:
        file.write(word)
make_file('Haleluyah')