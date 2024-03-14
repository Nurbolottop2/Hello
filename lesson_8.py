# numbers = [1,2,3,4,5,6,7,8,9,10]

# result = lambda x: x[::-1]
# print(result(numbers))


# users = ["Anton","Vlad", "Geeks", "Mirbek"]
# #Anton - 5 букв
# #Vlad - 4 букв
# # result = list(map(lambda num: f"{num} -  {len(num)} букв ",users))
# # for res in result:
# #     print(res)

# # A,V,G,M

# result = list(map(lambda x: x[0], users))
# print(result)

# #ANTON,VLAD,GEEKS,MIRBEKz

# result = list(map(lambda x: x.upper(), users))
# print(result)


# file_write = open("geeks.txt", "w")
# file_write.write("Привет, меня зовут Антон")


# file_read = open("test.txt", "r")
# result = file_read.read()
# print(result)

# nurbo.txt  внутри есть текст "Что такое лямбда в Python?"
# Ваша задача прочитать содержимое файла nurbo.txt и написать его в новом вайле kani.txt

names = ["Mergul", "Erbol", "Yryskeldi", "Beishen", "Omonboi", "Nurai", "Bakai"]

# file_read = open("test.txt", "r")
with open("names.txt","w") as file_write:
    for i in names:
        file_write.write(f"Имя: {i} \n")

with open("test.txt", "r") as reader:
    result = reader.read()
    print(result)