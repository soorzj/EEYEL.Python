n=int(input("Enter a number: "))
sumdig,count=0,0
temp=n
while temp>0:
    temp=temp//10
    count+=1
temp=n
while temp>0:
    sumdig+=((temp%10)**count)
    temp=temp//10
if(sumdig==n):
    print("Number is Armstrong")
else:
    print("Number is not armstrong")
