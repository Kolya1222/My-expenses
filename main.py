'''
    Файл для создания меню, путем импорта из файла 
action.py ссылки на функцию. Добавления ее в список 
имен для последующего вывода в бесконечном цикле при
помощи способа из файла show.py и ожидания получения 
ключа в числовом формате для вызова нужной функции.
'''

from action import *
from show import display_menu
from os import system

#Функция для отображения и взаимодействия с пунктами меню
def Main():
    #Назавания функций для перехода к ним
    functions_names = [Balance, New_entry, Edit_entry, Search, Done]
    #Создание словаря для отображения меню выбора
    menu_items = dict(enumerate(functions_names, start=1))
    system('cls')
    while True:
        #Функция вывода в консоль меню
        display_menu(menu_items)
        #Переменная-индекс выбора для переключения на нужную функцию
        selection = int(input("Please enter your selection number: "))
        #Имя нужной функции
        selected_value = menu_items[selection]  
        #Вызов нужной функции
        selected_value()  
        
#Функция для меню выбора способа поиска
def Search():
    functions_names = [Search_sum, Search_category, Search_date, Main]
    menu_items = dict(enumerate(functions_names, start=1))
    system('cls')
    while True:
        display_menu(menu_items)
        selection = int(input("Please enter your selection number: ")) 
        selected_value = menu_items[selection]  
        selected_value()  

if __name__ == "__main__":
    Main()