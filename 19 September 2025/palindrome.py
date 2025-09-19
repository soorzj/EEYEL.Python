#wap to check if a number input is palindrome
a=int(input("Enter a number: "))
temp=a
n1=0
while temp>0:
    temp=temp//10
    n1=n1+1
temp=a
rev=0
for i in range (n1):
    n2=temp%10
    rev = rev*10+n2
    temp=temp//10
if(rev==a):
    print(a," is Palindrome")
else:
     print(a," is not Palindrome")