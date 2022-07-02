
def show_all_characters(res):
    for item in res:
            print(str(item['id']) + "\n" + item['firstName'] + 
                  " " + item['lastName'] + "\n" + item['fullName'] + " " + item['title'] + "\n" + item['family'])