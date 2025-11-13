def multiply(a,b):
    return a * b
def divide(a,b):
    return a//b, a%b
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
choice=0
print("MENU OF OPERATIONS")
print(" 1.ADD \n 2.SUBTRACT \n 3.MULTIPLY \n 4.DIVIDE")
while choice<5 :
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("The sum is:", add(a,b))
    elif choice==2:
        print("The difference is:", subtract(a,b))
    elif choice==3:
        print("The product is:", multiply(a,b))
    elif choice==4:
        ans=divide(a,b)
        print("The quotient is:", ans[0], "with a remainder of", ans[1])
    else:
        print("Invalid choice")
