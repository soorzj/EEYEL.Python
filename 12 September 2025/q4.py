#wap to check if input is a prime
a=int(input("Enter a number : "))
flag=0
if(a==0):
    print("Number is Zero ")
elif (a==1):
    print("Number is 1 ")
else:
    for i in range (2,a-1):
        if (a%i==0):
            flag=1 
if (flag ==1):
    print("number is composite")
else:
     print("number is prime")
