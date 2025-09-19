a=int(input("Enter a number: "))
temp=a
n1=0 #digit count
while temp>0:
    temp=temp//10
    n1=n1+1
temp=a
rev=0
for i in range (n1):
    n2=temp%10
    rev = rev*10+n2
    temp=temp//10
print("Reverse of ", a ," is ",rev)