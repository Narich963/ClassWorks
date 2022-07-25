# 1. Создать телеграм бота который парсит ноутбуки на сайте kivano.kg по следущим фильтрам
# цена
# объем оперативной памяти
# процессор
# объем SSD
# производитель (Apple, Xiaomi, HP и т.д.)
# тип матрицы
# размер экрана
from requests import get
from bs4 import BeautifulSoup
from pprint import pprint



def get_data(url):
    r = get(url).content
    soup = BeautifulSoup(r, 'html.parser')
    items = soup.findAll('div', class_='pull-right rel')
    return items
def get_parse(items):
    result = []
    info = []
    k = 0
    for item in items:
        info .append(item.find('div', class_='product_text pull-left').get_text().replace('\n', '').strip().split(' '))
        size = []
        matrix = []
        for i in info:
            for j in range(len(i)):
                if 'экрана:' not in i and 'экран' not in i:
                    size.append('Отсутствует информация')
                elif i[j] == 'экрана:':
                    size.append(f'{i[j + 1]} {i[j + 2]} {i[j + 3][0:2]}')
                    matrix.append('Отсутствует информация')
                elif i[j] == 'экран':
                    size.append(f'{i[j + 1]} {i[j + 2]} {i[j + 3]}')
                    matrix.append(f'{i[j + 2]}')

        result.append({
            'Производитель':item.find('div', class_='product_text pull-left').get_text().replace('\n', '').strip().split(' ')[1],
            'Размер экрана': size[k],
            'Тип матрицы': matrix[k]
        })
        k += 1
    return result
url = 'https://www.kivano.kg/noutbuki'
items = get_data(url)
pprint(get_parse(items))