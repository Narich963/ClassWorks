# Создайте класс Factory и внутри создайте 2 метода:
# Метод engine который возвращает строку "Двигатель создан"
# Метод bridge который возвращает строку "Ходовая часть создана"

# Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе Toyota создайте методы wheels и windows.
# Метод wheels возвращает строку "Колёса готовы"
# Метод windows возвращает строку "Стёкла готовы"
# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
# Результат каждого метода вставьте в лист

class Factory:
    def engine(self):
        return 'Двигатель создан'
    def bridge(self):
        return 'Ходовая часть создана'

class Toyota(Factory):
    def wheels(self):
        return 'Колеса готовы'
    def windows(self):
        return 'Стекла готовы'

camry = Toyota()
car = [camry.engine(), camry.bridge(), camry.wheels(), camry.windows()]
print(car)