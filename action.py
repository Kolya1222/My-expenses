'''
    Файл для добавления новых пунктов меню и написание их функционала
'''

from os import system
import sys
import datetime

def Balance():                                              #Функция отображения баланса
    system('cls')
    file = open('main.txt')
    text = file.readlines()  
    balance = 0                                             #Баланс
    incglob = 0                                             #Отдельно доходы
    expenglob = 0                                           #Отдельно расходы
    i=0
    for row in text:
        if "Income" in row:
            type, inc = map(str, text[i+1].split(':'))      #Доход для расчета баланса
            incglob += int(inc) 
        if "Expenses" in row:
            type, expen = map(str, text[i+1].split(':'))    #Расходы для баланса
            expenglob += int(expen)
        i+=1  
    file.close() 
    balance = incglob - expenglob
    print(f"You balance:{balance}") 
    print(f"You income:{incglob}") 
    print(f"You expenses:{expenglob}") 
    input("Press Enter to Continue\n")
    system('cls') 

def New_entry():                                #Добавление записи
    system('cls') 
    date_entry = input('Enter a date in YYYY-MM-DD format:')
    year, month, day = map(int, date_entry.split('-'))
    date = datetime.date(year, month, day)      #Дата в формате год-месяц-день
    category = input('Income or Expenses:')     #Категории в формате Income or Expenses
    sum = int(input('Sum:'))                    #Деньги
    description = input('Description:')         #Описание
    file = open('main.txt','at')
    file.write(f"date:{date}\n")
    file.write(f"category:{category}\n")
    file.write(f"sum:{sum}\n")
    file.write(f"description:{description}\n")
    file.close()
    input("Press Enter to Continue\n")
    system('cls') 

def Edit_entry():                                                   #Редактирование
    system('cls') 
    print("Edit")
    file = open('main.txt')
    text = file.readlines()
    textout = dict(enumerate(text, start=1))                        #Для окуратного вывода в консоль
    for key, value in textout.items():
        print("{0}: {1}".format(key,value))
    editid = int(input('Line number to edit:'))-1                   #Номер строки для изменения
    edittext = input (f'replace the current text {text[editid]}')   #Измененая строка
    text[editid] = edittext+'\n'
    file.close()
    file = open('main.txt','w')
    file.writelines(text)
    file.close()
    input("Press Enter to Continue\n")
    system('cls') 

def Search_sum():                                               #Поиск по сумме 
    system('cls')
    print("Search")
    seach=int(input("Sum:"))                                    #Значение которое нужно найти
    file = open('main.txt')
    text = file.readlines()
    i=0
    for row in text:
        if "sum" in row:
            type, value = map(str, text[i].split(':'))          #Значение для поиска
            if seach == int(value):
                print(text[i-2],text[i-1],text[i],text[i+1])
        i+=1       
    input("Press Enter to Continue\n")
    file.close()
    system('cls') 

def Search_category():      #Поиск по категориям
    system('cls')
    print("Search")
    seach = input("Category:")
    file = open('main.txt')
    text = file.readlines()
    i=0
    for row in text:
        if seach in row:
            print(text[i-1],text[i],text[i+1],text[i+2])
        i+=1       
    input("Press Enter to Continue\n")
    file.close()
    system('cls') 

def Search_date():                                                          #Поиск по дате
    system('cls')
    print("Search")
    date_entry = input('Enter a date in YYYY-MM-DD format:')
    year, month, day = map(int, date_entry.split('-'))
    date = datetime.date(year, month, day)
    file = open('main.txt')
    text = file.readlines()
    i=0
    for row in text:
        if "date" in row:
            type, value = map(str, text[i].split(':')) 
            year_text, month_text, day_text = map(int, value.split('-'))
            date_text = datetime.date(year_text, month_text, day_text)      #Дата из файла
            if date == date_text:
                print(text[i],text[i+1],text[i+2],text[i+3])
        i+=1       
    input("Press Enter to Continue\n")
    file.close()
    system('cls') 

def Done():         #Завершение работы
    system('cls') 
    print("Goodbye")
    sys.exit()