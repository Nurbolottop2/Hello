# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")
# print("Hello world")

# for, while

# for num in range(1000):
#     print("Hello world")

# numbers = []
# print(numbers)
# for num in range(1,1001):
#     numbers.append(num)
# print(numbers)

# users = ["Nurbolot", "Bektemir","Asan", "Berksultan", "Aman"]
# for name in users:
#     print(f"{name} - {len(name)} букв")
# #Nurbolot - 6 букв    

#NURBOLOT
#BEKTEMIR
#ASAN
#BERKSULTAN
#AMAN

# n = 0 
# while True:
#     n+=100000000000
#     print(n)

# Запросите у пользовтеля его имя и возраст
#Если ему меньше 18 лет выводите "Вы подросток"
# Если ему больше 18 но меньше 35 лет выводите, "Вы взрослый."
# Если ему больше 35 но меньше 75  лет выводите, "Вы старик."
# Иначе выводите, "Вас нет в живых"

# Используйте while

while True:
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    if age <18:
        print("Вы подросток")
    elif age >=18 and age <35:
        print("Вы взрослый")
    elif age>=35 and age <75:
        print("Вы старик")
    else:
        print("Вас нет в живых!")

# users = [1,"dshbd",24.53]
# numbers = (1,"dshbd",24.53,[1,2,3,4])   #Первое отличие: Создается с помощью круглых скобок
# print(type(users))
# print(type(numbers))
# users.append("Apple")
# numbers.append("Apple")         #Второе отличие: Не изменямый тип данных
# print(users)
# print(numbers)

# list_1 = ["Nurbolot"]
# print(type(list_1))

# tuple_1 = ("Nurbolot",)
# print(type(tuple_1))



