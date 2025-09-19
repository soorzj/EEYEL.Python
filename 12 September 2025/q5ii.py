#sum of series1
import math
x=int(input("Enter a number: "))
n=int(input("Enter number of terms: "))
sum=1
i=2
counter=1
while counter<n:
    if (counter%2==0):
        sum+=math.pow(x,i)/i
    else:
        sum-=math.pow(x,i)/i
    i=i+2
    counter+=1
print("The sum of series is ",sum)