# users = ['Nurbolot', 'Geeks']

# student = {'name': "Geeks", 'age': 18, 'hobby': "Football"}

# # Создается {}  скобками.
# # Всегда хранит в себе ключ и значение
# # Мы не можем использовать индексы(используем ключи для получения значений)

# # print(student["name"])
# # print(student['hobby'])
# print(student)
# student['city'] = "Osh"
# print(student)
# student['age'] = 19
# print(student)
# student.pop('hobby')
# print(student)


# # del student['hobby']
# # print(student)

# "Привет меня зовут Geeks, мне 19 лет. Я живу в городе Osh"
# print(f"Привет меня зовут {student['name']},  мне {student['age']}. Я живу в городе {student['city']} ")

# 'name, age, city'

# key = student.keys()
# print(key)

# values = student.values()
# print(values)


# result = {"num1":12, 23: 43}
# print(result)


#set, frozenset
# Создается  с помощью фигурных скобок
# Не имеют структуры и порядка и по этому меняются местами
# Не можем использовать индексы и срезы
# set() -  Изменямый тип данных
# frozenset() -  Неизменяемый тип данных

# user = {"Nurbolot", "Musu", "Kutbuhan", "Beksultan", "Islam", "Geeks"}
# print(user)
# # print(user[0])  не работает 

# user.add("Nurai")
# print(user)

# # user.remove("Musu")
# # print(user)

# user.discard("Musulmankul")
# print(user)

# users = frozenset(["Nurbolot", "vlad", "Kutbuhan", "Kutia", "Kutkubak"])
# print(users)
# users.add("Geeks")


# 1) Сделайте игру Камень, Ножницы, Бумага .Добавьте туда цикл while, также у пользователя должно быть 5 попыток и каждый раз вы должны отнимать попытки по 1. Если попытки закончятся цикл должен остоновится и программа должна вывести  текст <<Игра окончена, у вас осталось 0 попыток>>

import random

users_health = 5
bot_health = 5
while True:
    if users_health ==0:
        print("Игра окончена, у вас осталось 0 попыток")
        break
    elif bot_health ==0:
        print("Игра окончена, у бота осталось 0 попыток")
        break
    else:
        bot = random.choice(["Камень", "Ножницы", "Бумага"])
        user = input("Введите ваш выбор: ")
        if user == "Камень":
            if bot == "Камень":
                print(f"Ничья.У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot == "Ножницы":
                bot_health -=1
                print(f"Вы выиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot =="Бумага":
                users_health -=1
                print(f"Вы проиграли. У вас: {users_health} попыток, у бота: {bot_health}")
        elif user =="Ножницы":
            if bot == "Камень":
                users_health -=1
                print(f"Вы проиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot == "Ножницы":
                print(f"Ничья.У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot =="Бумага":
                bot_health -=1
                print(f"Вы выиграли. У вас: {users_health} попыток, у бота: {bot_health}")
        elif user =="Бумага":
            if bot == "Камень":
                bot_health -=1
                print(f"Вы выиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot == "Ножницы":
                users_health -=1
                print(f"Вы проиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot =="Бумага":
                print(f"Ничья.У вас: {users_health} попыток, у бота: {bot_health}")
        else:
            print("Неверный вариант, введи снова!!!")