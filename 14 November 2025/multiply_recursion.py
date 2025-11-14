def mult(a,b):
    if b==0:
        return 0
    else:
        return a + mult(a,b-1)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("the product of the numbers is ", mult(a,b))