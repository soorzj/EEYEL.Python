def isprime(n):
    if n<=1:
        return False
    else:
        for i in range (2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
def reverse (n,x):
    if n==0:
        return x
    else:
        return  reverse(n//10, x*10 +n%10)

n=int(input("Enter a number:"))
m=reverse(n,0)
if isprime(n) and isprime(m):
    print("Number is a Twisted prime")
else:
    print("Number is not a Twisted prime")