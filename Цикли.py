
# exit = False
# while exit != True:
#     a = int(input("0, Exit"))
#     if a == 0:
#         exit = True


# count =10
# for i in range(1, count):
#     for j in range(1,count):
#         print(i*j,end="\t")
#     print("\n")

# days = 0
# counter = 0

# while days <= 7:
#     a=random.randrange(-50,50)
#     print("Random Number => ", a)
#     if a > 10:
#         counter +=1
#     days+=1
# print(counter)
"""
Написати програму, яка перевіряє користувача на знання таблиці множення. Програма виводить
на екран два числа, користувач має ввести їхній добуток. Розробити кілька рівнів складності (відрізняються
складністю та кількістю питань). Вивести користувачеві
оцінку його знань.
"""
import random


choice = int(input("Choice level of dificulty (5,15,20) "))
i=0
true_answer=0
# When choice equals 5
if choice == 5:
    while i !=5:
        number_1 = random.randrange(0,10)
        number_2 = random.randrange(0,10)
        result=int(input("Enter result of operation {} * {} ").format(number_1,number_2))
        if result == number_1*number_2:
            true_answer+=1
        i+=1
# When choice equals 15
elif choice == 15:
    while i !=15:
        number_1 = random.randrange(0,10)
        number_2 = random.randrange(0,10)
        result=int(input("Enter result of operation {} * {} ").format(number_1,number_2))
        if result == number_1*number_2:
            true_answer+=1
        i+=1
# When choice equals 20        
elif choice == 20:
    while i !=20:
        number_1 = random.randrange(0,10)
        number_2 = random.randrange(0,10)
        result=int(input("Enter result of operation {} * {} ").format(number_1,number_2))
        if result == number_1*number_2:
            true_answer+=1
        i+=1
else:
    print("You entered wrong number for choice. See you later!!!")
# Show value of true answer for user
print("Count of true answer {}".format(true_answer))
