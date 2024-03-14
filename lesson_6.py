# print("Hello world")
# num1 = input("")

# def print_world():
#     print("Hello world")

# print_world()


# num1 = 8
# num2 = 2
# print(num1/num2)

def result(geeks1,geeks2):
    print(geeks1/geeks2)
    
result(10,5)


# Создайте функцию user, и запросите имя, фамилия, возраст, номер пользователя вне функции. Далее выведите текст:    "ФИО: Эркинбаев Нурболот, возраст: 18, тел.ном: 09999999"


# def user(age,name,surname,phone):
#     print(f"ФИО: {name} {surname}, возраст: {age}, тел.номер: {phone}")
# name = input("Введите имя: ")
# surname = input("Введите фамилию: ")
# age = int(input("Введите возраст: "))
# phone = input("Введите номер: ")

# user(name,surname,age,phone)

# user("geeks", "Osh", )

def age_user():
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
            
            