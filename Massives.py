# Завдання 2. У функцію передається масив випадкових
# чисел у діапазоні від -20 до +20. Необхідно знайти пози-
# ції крайніх від’ємних елементів (найлівішого від’ємного
# елемента і найправішого від’ємного елемента) і впоряд-
# кувати елементи, що знаходяться між ними.




# from array import array
# from itertools import count
# import random

 

import random

massive =[]
count_first_min=0
count_last_min=0
array = []


# Функція для виведення значень
def print_value(value):
    print(value)

# Функція для заповнення першого масиву
def fill_massive(massive, size):
    i=0
    while i < size:
        massive.append(random.randrange(-20,20))
        i+=1  
    return massive

# Функція для знаходження першого від'ємного елемента
def check_first_min(massive,size):
    
    i=0
    while i < size:
        if (massive[i] < 0):
            count_first_min = i
            if count_first_min != None:
                break
        i+=1  
    return  count_first_min

# Функція для знаходження останнього від'ємного елемента
def check_last_min(massive,size):
    
    count_1=count_first_min
    while  count_1 < size:
        if massive[count_1]< 0 :
            count_last_min = count_1
        count_1 +=1
    return count_last_min

# Функція для заповнення другого масиву
def fill_arrray (array):
    i=0
    count_2=count_first_min
    while i < count_last_min:
        array.append(massive[count_2]) 
        count_2 += 1
        i += 1
    return array

# Функція для роботи з масивами    
def work_with_massive(massive,size):

    fill_massive(massive , size) # Заповнюємо перший масив
    print_value(massive)# Виводимо перший масив
    # Знаходимо перший від'єиний елемент і вносимо значення у змінну 
    count_first_min= check_first_min(massive , size)   
    print_value(count_first_min)# Виводимо значення змінної
    # Знаходимо останній від'єиний елемент і вносимо значення у змінну 
    count_last_min=check_last_min(massive,size)
    print_value(count_last_min)# Виводимо значення змінної
    fill_arrray(array)# Заповнюємо другий масив
    print_value(array)# Виводимо другий масив
    array.sort()# Сортуємо другий масив
    print_value(array) # Виводимо другий масив

# Меню програми
def menu():

    print("Welcome to massive")
    size=int(input("Enter value of size of massive "))
    work_with_massive(array,size)

# Викликаємо меню
menu()


# massive=[]

# def print_value(massive):
#     print(massive)

# def enter_value_in_massive(massive,size):
#     i= 0
#     while i < size:
#         massive.append(random.randrange(1,100))
#         i += 1
#     return massive

# def average_masive(massive,size):
#     i= 0
#     average = 0
#     sum = 0
#     while i < size:
#         sum+=massive[i]
#         i+=1
#     average= sum / size
#     return average

# def menu():
#     enter_value_in_massive(massive,10)
#     print_value(massive) 
#     avarege=average_masive(massive,10)
#     print_value(avarege)

# menu()

# massive=[]

# def print_value(massive):
#     print(massive)

# def enter_value_in_massive(massive,size):
#     i= 0
#     while i < size:
#         massive.append(random.randrange(-100,100))
#         i += 1
#     return massive

# def plus_element(massive,size):
#     i= 0
#     count = 0
#     while i < size:
#         if (massive[i]>0):
#             count += 1
#         i+=1
#     return count

# def minus_element(massive,size):
#     i= 0
#     count = 0
#     while i < size:
#         if (massive[i]<0):
#             count += 1
#         i+=1
#     return count

# def zero_element(massive,size):
#     i= 0
#     count = 0
#     while i < size:
#         if (massive[i]==0):
#             count += 1
#         i+=1
#     return count

# def menu():
#     enter_value_in_massive(massive,10)
#     print_value(massive)
#     plus=plus_element(massive,10)
#     minus=minus_element(massive,10)
#     zero=zero_element(massive,10)
#     print_value(plus)
#     print_value(minus)
#     print_value(zero)

# menu()