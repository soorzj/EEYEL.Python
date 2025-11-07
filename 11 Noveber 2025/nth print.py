def isprime(n):
    if n<=1:
        return False
    else:
        for i in range (2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
n=int(input("to find nth prime number, enter n:"))
x=1
while n>0:
    x=x+1
    if isprime(x):
        n=n-1
print("nth prime number is:", x)

