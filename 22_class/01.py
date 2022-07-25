# Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...) и возвращает полную комплектацию ноутбука со всеми характеристиками.
#
# В характеристики должны входить:
# Процессор
# Оперативная Память
# Видео карта
# Жёсткий Диск
# Материнская плата
# Размер экрана

# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены:
# Модель Ноутбука и его Характеристики.

class Laptop:
    proc = None
    ozu = 0
    video = None
    hdd = 0
    motherboard = None
    size = 0
    def __init__(self, model):
        self.model = model
        if self.model == 'Acer':
            self.proc = 'Inter i5-10000 2.44Hz'
            self.ozu = '8Gb DDR4'
            self.video = 'Intel i5HD'
            self.hdd = 1024
            self.motherboard = 'MSI ACRGA-1214'
            self.size = '1920x1080 Full HD'
        elif self.model == 'Asus':
            self.proc = 'AMD RYZEN 5'
            self.ozu = '12GB DDR4'
            self.video = 'NVidia GeForse 230'
            self.hdd = 1024
            self.motherboard = 'CODEC ASDWF-9224'
            self.size = '1344x977'
        elif self.model == 'MacBook':
            self.proc = 'Govno 2'
            self.ozu = '2'
            self.video = 'Potato'
            self.hdd = '256'
            self.motherboard = 'Navoz ADAW-2412'
            self.size = '500x500 mm'

    def get_dict(self):
        return {
            'Model': self.model,
            'Processor': self.proc,
            'OZU': self.ozu,
            'Video': self.video,
            'Hard Driver': self.hdd,
            'Motherboard': self.motherboard,
            'Size': self.size
        }

acer = Laptop('MacBook')
print(acer.get_dict())