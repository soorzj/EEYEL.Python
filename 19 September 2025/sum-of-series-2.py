#sum of series2
x=int(input("Enter a number: "))
n=int(input("Enter number of terms: "))
sum=1
for i in range(1,n):
    if (i%2==0):
        sum+=x**(2*i)/(2*i)
    else:
        sum-=x**(2*i)/(2*i)
print("The sum of series is ",sum)