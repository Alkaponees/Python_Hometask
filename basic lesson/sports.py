def print_speed (distence,t):
    return distence /t

def enter_number():
    num=float(input("Enter number "))
    return num

distence = enter_number()
t = enter_number() 

print("Speed m/s := {}".format(print_speed))