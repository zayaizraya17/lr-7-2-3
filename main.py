import json 
count = 0 
with open('dump.json', 'r', encoding='utf-8') as file: 
        data = json.load(file) 
while True:           
    print(" 1 Вывести все записи\n 2 Вывести запись по полю\n 3 Добавить запись\n 4 Удалить запись по полю\n 5 Выйти из программы") 
    choise = input("Что выберете? ") 
 
    if choise == "1": 
        print("----------Все записи----------") 
        for i in data: 
            print(f"""Номер цветка: {i["id"]}  
        Название: {i["name"]} 
        Латинское название: {i["latin_name"]} 
        Краснокнижный цветок? {i["is_red_book_flower"]} 
        Цена: {i["price"]} BYN\n""") 
        count +=1 
 
    elif choise == "2": 
        print("----------Запись по полю----------") 
        item = int(input("Введите поле которое вывести ")) 
        for i, flower in enumerate(data): 
            if flower['id'] == item: 
                print(f"""Номер цветка: {flower["id"]}  
        Название: {flower["name"]} 
        Латинское название: {flower["latin_name"]} 
        Краснокнижный цветок? {flower["is_red_book_flower"]} 
        Цена: {flower["price"]} BYN\n""") 
        count +=1 
         
 
    elif choise == "3": 
        print("----------Добавить запись----------")  
        newDct = {} 
        newDct["id"] = max(item["id"] for item in data) + 1 
        while True:
            newDct["name"] = input("Введите названия цветка ")
            if newDct["name"] != "":
                break
            else:
                print("Вы не ввели")

        while True:
            newDct["latin_name"] = input("Введите латинское имя цветка ")
            if newDct["latin_name"] != "":
                break
            else:
                print("Вы не ввели")

        while True:
            newDct["is_red_book_flower"] = input("Введите краснокнижный ли цветок True/False ")
            if newDct["is_red_book_flower"].lower() in ["true", "false"]:
                newDct["is_red_book_flower"] = newDct["is_red_book_flower"].lower() == "true"
                break
            else:
                print("Некорректный ввод")

        while True: 
            try: 
                newDct["price"] = float(input("Введите цену цветка ")) 
                break 
            except ValueError: 
                print("Некорректный ввод") 
        data.append(newDct) 
        print("----------Запись добавлена----------")  
        count +=1 
    elif choise == "4": 
        print("----------Удалить запись----------")  
        itemDel = int(input("Введите поле которое хотите удалить ")) 
        found = False
        for i, item in enumerate(data):
            if item["id"] == itemDel:
                del data[i]
                print("----------Запись удалена----------")
                found = True
                break
        if not found:
            print("Запись по полю не найдена")
        count += 1
 
 
    elif choise == "5": 
        print("Количество выполненных операций с записями ", count)  
        print("----------Пока----------") 
        break