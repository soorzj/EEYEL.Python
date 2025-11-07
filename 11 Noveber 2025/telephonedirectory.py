directory={}
print("TELEPHONE DIRECTORY - MENU OF OPERATIONS")
choice=0
while(choice!=6):
    print(" 1.ADD CONTACT \n 2.UPDATE CONTACT \n 3.DELETE CONTACT \n 4.SEARCH CONTACT \n 5.DISPLAY ALL CONTACTS \n 6.EXIT")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter name:")
        number=input("Enter number:")
        directory[name]=number
        print("Contact added...")
    elif choice==2:
        name=input("Enter name of contact:")
        if name in directory:
            print("Given Phone:", directory.get(name, "Not found"))
            number=input("Enter new phone:")
            directory[name]=number
            print("Contact updated...")
        else:
            print("Contact Not found")
    elif choice==3:
        name=input("Enter name of contact:")
        if name in directory:
            print("Given Phone:", directory.get(name, "Not found"))
            del(directory[name])
        else:
            print("Contact Not found...")
    elif choice==4:
        name=input("Enter name of contact:")
        print("Given Phone:", directory.get(name, "Contact Not found"))
    elif choice==5:
        print("Name  \t  Number")
        for key in directory:
            print(key,":", directory[key])
        print()
    elif choice==6:
        print("Exiting")
    else:
        print("Invalid code")
