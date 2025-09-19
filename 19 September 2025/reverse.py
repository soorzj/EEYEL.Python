a=int(input("Enter a number: "))
temp=a
count=0 #digitcount
while temp>0:
    temp=temp//10
    count=count+1
temp=a
rev=0
for i in range (count):
    rev = rev*10+temp%10
    temp=temp//10

print("Reverse of ", a ," is ",rev)
