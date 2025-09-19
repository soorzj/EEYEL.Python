f=0
while f!=6:
    a=int(input("Enter 1st Number: "))
    b=int(input("Enter 2nd Number: "))
    print("Menu for operations with the two numbers:\n 1. Sum \n 2. Difference \n 3. Product \n 4. Quotient \n 5. Reminder \n 6. Quit")
    f=int(input("Required Funtion No: "))
    if f==1:
        sum=a+b
        print("Sum of 2 no:s is = " ,sum)
    elif f==2:
        diff=a-b
        print("Difference of 2 no:s is = " ,diff)
    elif f==3:
        product=a*b
        print("Product of 2 no:s is = "  , product)
    elif f==4: 
        quotient=a//b
        print("Quotient of 2 no:s is = "  , quotient)
    elif f==5:
        reminder=a%b
        print("Reminder of division is = " , reminder)
    elif f==6:
        print("Program Exit")
        break;
    else:
        print("Wrong choice")



