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

def print_value(value):
    print(value)

def fill_massive(massive, size):
    i=0
    while i < size:
        massive.append(random.randrange(-20,20))
        i+=1  
    return massive
def check_first_min(massive,size):
    
    i=0
    while i < size:
        if (massive[i] < 0):
            count_first_min = i
            if count_first_min != None:
                break
        i+=1  
    return  count_first_min

def check_last_min(massive,size):
    
    count_1=count_first_min
    while  count_1 < size:
        if massive[count_1]< 0 :
            count_last_min = count_1
        count_1 +=1
    return count_last_min

def fill_arrray (array):
    
    count_1=count_first_min
    while count_1 < count_last_min:
        array.append(massive[count_1]) 
        count_1 += 1
    return array
    
def work_with_massive(massive,size):

    fill_massive(massive , size)
    print_value(massive)
    count_first_min= check_first_min(massive , size)    
    print_value(count_first_min)
    count_last_min=check_last_min(massive,size)
    print_value(count_last_min)
    fill_arrray(array)
    print_value(array)
    array.sort()
    print_value(array)


    

def menu():
    print("Welcome to massive")
    size=int(input("Enter value of size of massive "))
    work_with_massive(array,size)
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