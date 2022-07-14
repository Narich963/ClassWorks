# Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить.
# А затем записывает это всё в файл на рабочем столе menu.txt

def add_menu():
    food = input('Что покушать ')
    drink = input('что попить ')
    with open(r'C:/users/azizb/Desktop/menu.txt', 'w') as file:
        file.write(food)
        file.write(drink)