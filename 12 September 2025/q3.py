#wap to find factorial of a number using for loop

a=int(input("Enter a number: "))
b=1
fact=1
for i in range(a):
    fact=fact*b
    b+=1
print ("Factorial of the number: ",fact)