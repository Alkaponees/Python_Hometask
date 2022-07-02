import requests

from search import search_by_family
from search import search_by_name
from show import show_all_characters

 
URL="https://thronesapi.com/api/v2/Characters"

res= requests.get(URL)
res=res.json()

       
def menu():
    print("Welcome to Game of Throne")
    run = False
    while run != True:
        choice=int(input("Make your choose (1.All charaters 2.Search by name 3.Search by family  0.Exit )\n"))
        if choice == 1:
            show_all_characters(res)
        elif choice == 2:   
            search_by_name(res)
        elif choice == 3:   
            search_by_family(res)
        elif choice==0:
            run =True
        else:
            print("You enter a valid value!!!!\n Try again!!!")

menu()