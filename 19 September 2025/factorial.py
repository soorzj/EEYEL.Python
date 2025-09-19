# factorial of a number using while loop
a=int(input("Enter a number: "))
b=1
fact=1
while b<=a:
    fact=fact*b
    b=b+1
print ("Factorial of the number: ",fact)
