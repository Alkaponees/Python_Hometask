#Завдання 1. Дан масив чисел розмірністю 10 елементів.
# Написати функцію, яка сортує масив за зростанням або за
# спаданням, залежно від третього параметра функції. Якщо
# він дорівнює true, сортування йде за спаданням, якщо
# false, то за зростанням. Перші 2 параметри функції — це
# масив і його розмір, третій параметр за замовчуванням
# дорівнює false.


import random




def work_with_massive(massive,size,b=False):
    i=0
    while i < size:
        massive.append(random.randrange(1,100))
        i +=1

    
    print_massive(massive)
    
    if b==True:
        massive.sort()
    else:
        massive.sort(reverse=True)

    print_massive(arr)

    return massive


    
def print_massive(massive):
    print(massive)

def menu():
    print("Welcome to massive")
    work_with_massive(arr,10,True)

arr = []
menu()
    
