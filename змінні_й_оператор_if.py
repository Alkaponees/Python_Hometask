#Task 1. User has entered number. Is number steamed ?

number =int(input("Enter your number "))
if number%2 == 0:
    print("Your number is steam ")
else:
    print("Your number is odd ")

#Task 2.User has entered two numbers. We must show on the screen less number

number1=int(input("Enter your first number "))
number2=int(input("Enter your second number "))

if number1 < number2:
    print("First number is less than second number")
    print(number1)
elif number1 > number2:
    print("Second number is less than first number")
    print(number2)
else:
    print("First number equals second number")
    print( number1, number2)
"""
Task 3.User has entered number.Is your number equal 0, or more than zero,
or less than 0 ?
"""
number4 =int(input("Enter your number "))
if number4 == 0:
    print("Your number equals 0 ")
elif number4 < 0:
    print("Your number is less than zero ")
else:
    print("Your number is more than zero ")
"""
Task 4. User has entered two numbers. Are your numbers equal 0, or more than zero,
or less than 0 (show number in growing's order) ?
"""
number5=int(input("Enter your first number "))
number6=int(input("Enter your second number "))

if number5 < number6:
    print("First number is less than second number")
    print(number6)
    print(number5)

elif number1 > number2:
    print("Second number is less than first number")
    print(number5)
    print(number6)
else:
    print("First number equals second number")
