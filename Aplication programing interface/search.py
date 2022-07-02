

def search_by_name(res):
    name = input("Enter name of character... ")
    for item in res:    
        if  item['firstName'] == name:
              print(str(item['id']) + "\n" + item['firstName'] + 
                  "\n" + item['lastName'] + "\n" + item['fullName'] + item['title'] + "\n" + item['family'])
    print("Operation complited succcessful")

def search_by_family(res):
    family = input("Enter name of character... ")
    for item in res:    
        if  item['family'] == family:
              print(str(item['id']) + "\n" + item['firstName'] + 
                  "\n" + item['lastName'] + "\n" + item['fullName'] + item['title'] + "\n" + item['family'])