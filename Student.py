from tokenize import group


class Student:
    def __init__(self, name, surname, age, birthday, city, country, group_number):
        
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__birthday = birthday
        self.__city = city
        self.__country = country
        self.__group_number = group_number
        
    
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname
    
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
    def birthday(self):
        return self.__birthday
    
    
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        self.__city = new_city
    
    
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, new_country):
        self.__city = new_country
    
    
    @property
    def group_number(self):
        return self.__group_number

    @group_number.setter
    def group_number(self, new_group_number):
        if new_group_number <=0 or  new_group_number > 30:    
            print ("Out of range. '1-30'")
        else:
            self.__group_number = new_group_number
    
    def show_student_info(self):
        print("{}, {} , {} , {} \n".format(self.__name,self.__surname,self.__age, self.__birthday))
        print("{}, {}, {} \n============\n".format(self.__city,self.__country,self.__group_number))

#def __init__(self, name, surname, age, birthday, city, country, group_number)
daenerys = Student("Daenerys", "Targaryen", 27 ,"27.05.1995","Lviv","Ukraine",15)
samwell = Student("Samwell", "Tarly", 34 ,"24.04.1988","Ternopil","Ukraine",13)
jon = Student("Jon", " Snow", 33 ,"23.01.1989","Lublin","Poland",12)
arya = Student("Arya", "Stark", 23 ,"20.01.1998","Rivne","Ukraine",12)
sansa  = Student("Sansa", "Stark", 24 ,"22.08.1997","Rivne","Ukraine",12)
brandon = Student("Brandon", "Stark", 31 ,"12.08.1990","Rivne","Ukraine",12)
ned = Student("Ned", "Stark", 29 ,"14.05.1993","Rivne","Ukraine",12)
robert = Student("Robert", "Baratheon", 40 ,"10.04.1982","Berlin","German",11)
jamie = Student("Jamie", "Lannister", 21 ,"29.03.2001","London","Great Britain",14)
cersei = Student("Cersei", "Lannister", 22 ,"14.02.2000","London","Great Britain",14)

student_list =[]

student_list.append(daenerys)
student_list.append(samwell)
student_list.append(jon)
student_list.append(arya)
student_list.append(sansa)
student_list.append(brandon)
student_list.append(ned)
student_list.append(robert)
student_list.append(jamie)
student_list.append(cersei)

for student in student_list:
    student.show_student_info()

