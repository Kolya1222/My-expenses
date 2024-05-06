'''
    Вывод на экран списка доступных пунктов меню
'''

from os import system
#Функция вывода в консоль
def display_menu(menu):
    system('cls') 
    for k, function in menu.items():
        print(k, function.__name__)