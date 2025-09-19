#program to find fibonacci series upto n numbers
n=int(input("Enter the number of fibbonacci numbers required: "))
if(n>0):
    print(1,end=", ")
a=0
b=1
count=0
while(count<=n):
    c=a+b
    print(c,end=", ")
    a=b
    b=c
    count=count+1