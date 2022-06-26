from webbrowser import get


class Person:   
    def __init__(self, name , age):
        self.__name= name
        self.__age = age
    def show_person_info(self): 
         print(self.__name, " : ",self.__age )
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age <= 18 or new_age >= 120:    
            print ("Out of range. '18-120'")
        else:
            self.__age = new_age

    @property
    def name (self):
        return self.__name

jimmy = Person('Jimmy Fellton', 46)
john = Person('John Romero', 46)
adam = Person('Adam Tentis', 46)
janes = Person('Janes Katerlin', 46)
print(jimmy.age)
print(jimmy.name)
jimmy.age = 86
print("================")
print(jimmy.age)
print(jimmy.name)

person_list = []
person_list.append(jimmy)
person_list.append(john)
person_list.append(adam)
person_list.append(janes)
for person in person_list:
  jimmy.show_person_info()  
# jimmy.show_person_info()