# Завдання 2. У функцію передається масив випадкових
# чисел у діапазоні від -20 до +20. Необхідно знайти пози-
# ції крайніх від’ємних елементів (найлівішого від’ємного
# елемента і найправішого від’ємного елемента) і впоряд-
# кувати елементи, що знаходяться між ними.




# from array import array
# from itertools import count
# import random

 


# def work_with_massive(massive,size):
#     i=0
#     count_first_min=0
#     count_last_min=0
#     while i < size:
#         massive.append(random.randrange(-20,20))
#         i+=1  
#     print_massive(massive)

#     i=0
#     while i < size:
#         if (massive[i] < 0):
#             count_first_min = i
#             if count_first_min != None:
#                 break
#         i+=1   
        
#     print(count_first_min)

#     count_1=count_first_min
#     while  count_1 < size:
#         if massive[count_1]< 0 :
#             count_last_min = count_1
#         count_1 +=1

#     print(count_last_min)
#     i=0
#     count_1=count_first_min
#     array=[]
#     while i < count_last_min:
#         array.append(massive[count_1]) 
#         i += 1
#         count_1 += 1
    
#     print_massive(array)
#     array.sort()
#     print_massive(array)


    
# def print_massive(massive):
#     print(massive)

# def menu():
#     print("Welcome to massive")
#     work_with_massive(arr,10)

# arr = []
# menu()

import random

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

massive=[]

def print_value(massive):
    print(massive)

def enter_value_in_massive(massive,size):
    i= 0
    while i < size:
        massive.append(random.randrange(-100,100))
        i += 1
    return massive

def plus_element(massive,size):
    i= 0
    count = 0
    while i < size:
        if (massive[i]>0):
            count += 1
        i+=1
    return count

def minus_element(massive,size):
    i= 0
    count = 0
    while i < size:
        if (massive[i]<0):
            count += 1
        i+=1
    return count

def zero_element(massive,size):
    i= 0
    count = 0
    while i < size:
        if (massive[i]==0):
            count += 1
        i+=1
    return count

def menu():
    enter_value_in_massive(massive,10)
    print_value(massive)
    plus=plus_element(massive,10)
    minus=minus_element(massive,10)
    zero=zero_element(massive,10)
    print_value(plus)
    print_value(minus)
    print_value(zero)

menu()