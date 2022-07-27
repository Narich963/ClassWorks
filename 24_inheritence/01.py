# Нужно создать класс который принимает Data #2 данные.
#
# И внутри класса создать несколько методов:
#
# Метод который вернёт все имена отелей.
#
# Метод который из собирает все name в один Tuple и locations в другой и возвращает dictionary c двумя ключами списками со всеми значениями.
#
#  3.Метод который добавит к каждому элементу в markers поле
#
# status_id: 1

DATA = {"MARKERS":
    [
        {
            "NAME": "RIXOS THE PALM DUBAI",
            "LOCATION": [25.1212, 55.1535],
        },
        {
            "NAME": "SHANGRI-LA HOTEL",
            "LOCATION": [25.2084, 55.2719]
        },
        {
            "NAME": "GRAND HYATT",
            "LOCATION": [25.2285, 55.3273]
        }
    ]
}
class Data:
    def __init__(self, data):
        self.data = data

    def get_names(self):
        return [i['NAME'] for i in self.data['MARKERS']]

    def get_names_and_locations(self):
        return {
            'NAME': tuple(i['NAME'] for i in self.data['MARKERS']),
            'LOCATION': tuple(i['LOCATION'] for i in self.data['MARKERS'])
        }

    def add_new_attr(self):
        for i in range(len(self.data['MARKERS'])):
            self.data['MARKERS'][i]['status_id'] = i

    def print(self):
        print(self.data)
data = Data(DATA)
data.add_new_attr()
print(data.get_names())
print(data.get_names_and_locations())
data.print()
