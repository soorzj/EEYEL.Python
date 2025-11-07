def fibonacci(n,a,b):
    if n==0:
        return b
    else:
        return fibonacci(n-1,b,a+b)
n=int(input("enter the number of fibonacci terms you want:"))
print("nth fibonacci number is:", fibonacci(n,0,1))