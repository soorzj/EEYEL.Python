#sum of series1
x=int(input("Enter a number: "))
n=int(input("Enter number of terms: "))
sum=1
for i in range(1,n):
    sum+=x**(2*i)/(2*i)
print("The sum of series is ",sum)