from cmath import inf
from dis import dis
# Функція для додавання двох чисел
def added(num1,num2):
    return num1+num2
# Функція для множення двох чисел
def multiple(num1,num2):
    return num1*num2
# Функція для ділення двох чисел
def divide(num1,num2):
    if num2 == 0:
        return inf;
    else:
        return num1/num2
# Функція для віднімання двох чисел
def subtract(num1,num2):
    return num1-num2

def enter_number():
    num=int(input("Enter number "))
    return num
# Меню
def menu():
        print("Welcome To Calculator!!!")
        exit = False
        while exit != True:
            choice = int(input("Enter number of operation (1 => +,2 => -,3 => *,4 => /,0 => Exit) "))
            
            if choice == 1:
                num1= enter_number()
                num2= enter_number()
                res = added(num1,num2)
                print("Result => {}".format(res))
            elif choice == 2:
                num1= enter_number()
                num2= enter_number()
                res = subtract(num1,num2)
                print("Result => {}".format(res))
            elif choice == 3:
                num1= enter_number()
                num2= enter_number()
                res = multiple(num1,num2)
                print("Result => {}".format(res))
            elif choice == 4:
                num1= enter_number()
                num2= enter_number()
                res = divide(num1,num2)
                print("Result => {}".format(res))
            elif choice == 0:
                exit = True
            else :
                exit = False

menu()
print("\t\tCreated by Serhii Vysotskyi")