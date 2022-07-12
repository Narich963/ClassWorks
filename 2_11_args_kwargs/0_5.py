# Создайте функцию которая принимает слово
# и создаёт файл с таким именем в той же директории, где был запущен Ваш .py файл.

def make_file(word):
    with open('word.txt', 'w') as file:
        file.write(word)
