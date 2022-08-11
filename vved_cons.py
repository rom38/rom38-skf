#%%
import datetime as dt
from collections import defaultdict
import json
import os.path

def greet():
    print("Приветствуем вас в приложении")
    print("-----------------------------")
    print("------- Учёт финансов -------")
    print("-----------------------------")
    print("        Режимы работы:       ")
    print("-----------------------------")
    print("   1.  Добавить зачисление   ")
    print("   2.  Добавить трату        ")
    print("   3.  Получить статистику   ")
    print("   4.  Выйти из программы    ")
    print("-----------------------------")
    print(" Формат ввода даты: YY-MM-DD ")

def ask_mode():
    print("-----------------------------")
    return input("    Выберите режим работы:   ")

def wrong():
    print("-----------------------------")
    print(" Вы ввели некорректный режим ")

def ask_cost(ask_str):
    number = None
    while number is None:
        num_str =  input("  Введите сумму:             ")
        if num_str.isdigit():
            number = int(num_str)
        else:
            print(" Вы ввели некорректное число!")
            continue
    return number

def ask_date(ask_str):
    date = None
    while date is None:
        date_str = input(ask_str)
        splitted = date_str.split("-")
        
        if len(splitted)!= 3:
            print(" Введена некорректная дата!  ")
            continue
        
        check = [] 
        for string in splitted:
            check.append(string.isdigit())
        
        if not(all(check)):
            print(" Часть даты- не число!       ")
            continue
        
        splitted[0] = "20"+splitted[0]
        year, month, day = map(int, splitted)
        date = dt.date(year, month, day)
    return date

def ask_income():
    print("-----------------------------")
    cat = input("  Введите категорию:         ")
    cost = ask_cost("  Введите сумму поступления:")
    date = ask_date("  Введите дату поступления: ")
    return ["+",cat, date, cost]

def ask_spend():
    print("-----------------------------")
    cat = input("  Введите категорию:         ")
    cost = ask_cost("  Введите сумму траты:      ")
    date = ask_date("  Введите дату траты:       ")
    return ["-",cat, date, cost]

def ask_interval():
    date1 = ask_date("  Введите начало интервала:")
    date2 = ask_date("  Введите конец интервала: ")
    return (date1,date2)

def stat(data, date1, date2):
    income_stat = defaultdict(list)
    spend_stat = defaultdict(list)
    
    for typ, cat, date, cost in data:
        if date >= date1 and date <= date2:
            if typ == "+":
                income_stat[cat].append(cost)
            if typ == "-":
                spend_stat[cat].append(cost)
    
    print("-----------------------------")
    print("  Статистика поступлений:    ")
    print("-----------------------------")
    for cat, cost_list in income_stat.items():
        print(f"  {cat:20} - {sum(cost_list)}")
    print("-----------------------------")
    print("  Статистика трат:           ")
    print("-----------------------------")
    for cat, cost_list in spend_stat.items():
        print(f"  {cat:20} - {sum(cost_list)}")

def loop(data):
    greet()
    
    while True:
        mode = ask_mode()
        if mode == "1":
            data.append(ask_income())
        elif mode == "2":
            data.append(ask_spend())
        elif mode == "3":
            beg, end = ask_interval()
            stat(data, beg, end)
        elif mode == "4":
            break
        else:
            wrong()
    
    print("-----------------------------")
    print("      Данные сохранены!      ")
    print("-----------------------------")
    return data

def save(data, FILENAME):
    for rec in data:
        rec[2] = str(rec[2])
    with open(FILENAME, "w") as f:
        json.dump(data, f)

def read(FILENAME):
    if os.path.isfile(FILENAME):
        with open(FILENAME) as f:
            data = json.load(f)
    else:
        data = []
    
    for rec in data:
        date_ints = map(int, rec[2].split("-"))
        rec[2] = dt.date(*date_ints)
    return data

def main(FILENAME):
    data = read(FILENAME)
    data = loop(data)
    save(data, FILENAME)

main("journal.json") 
# %%
