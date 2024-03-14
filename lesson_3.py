# name = [1,2,3,4,5,6,7,8,9,10]
# print(type(name))

# users = ['Geeks','Beksultan', 'Nurbek', 'Anton']
# print(users)

# print(users[1])
# print(users[0:3])


# type_data = [5,"Пять", 5.5, True, [1,2,3,4,5], 5]
# print(type_data)

# users = ['Geeks','Beksultan','Geeks', 'Nurbek', 'Anton']
# user_list = ["Nurai", 'Geeks', "Kutbuhan", "Muha",'Geeks']
# print(users)
# users.append("Aigul")   # Для добавления в конец списка
# print(users)
# users.insert(1, "Musu") # Для добавления по индексу
# print(users)
# users.remove("Nurbek")  # Для удаления из списка
# print(users)
# users.pop(3)        # Для удаление из списка по индексу
# print(users)
# users.extend(user_list) #Для объеденения двух списков
# print(users)

# # print(users.index("Nurai")) # Что бы узнать индекс элемента 
# print(users.count("Geeks"))   #Что бы узнать количество элементов
# # users.reverse()   # Что бы перевернуть список
# # print(users
# print(users[::-1])   # Что бы перевернуть список с помощью индексов
# users.sort()    #Что бы сделать сортировку
# print(users)
# users.clear()       # Что бы очистить список 
# print(users)


#Запросите у пользователя его имя и возраст, и сделайте проверку на возраст.
# Если ему есть 18 лет, вы должны: вывести текст "Добро пожаловать", добавить пользователя в список и вывести список. 

# Если ему нет 18 лет, вы должны: Вывести текст "Доступ запрещен" и вывети список

# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# geeks = []

# if age >=18:
#     print("Добро пожаловать")
#     geeks.append(name)
#     print(f"Список пользователей: {geeks}")
# else:
#     print("Доступ запрещен")
#     print(f"Список пользователей: {geeks}")
    


# У вас есть список машин, Вы должны у пользователя запросить его имя и машину которую он хочет купить. 

# Если машина пользователя есть в списке, вы должны вывести текст
# "Уважаемый <<Имя>>, Ваш выбор у нас есть в наличии. Ваш выбор <<Название машины>>"

# А если его нет, Вы должны вывести,
# "Уважаемый <<Имя>>, Ваш выбор  у нас нет  в наличии. Ваш выбор: <<Название машины>>"


cars = ["Mersedes", "BMW", "Kia", "Tayota", "Supra", "Nissan", "Huandai", "Tiko", "Matiz"]
name = input("Введите имя: ")
car = input("Введите машину: ")
if  car in cars:
    print(f"Уважаемый {name}, Ваш выбор у нас есть в наличии. Ваш выбор {car}")
else:
    print(f"Уважаемый {name}, Ваш выбор у нас нет в наличии. Ваш выбор {car}")
    