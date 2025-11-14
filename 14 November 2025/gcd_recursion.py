def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
gcd=gcd(a,b)
lcm=(a*b)//gcd
print("GCD of", a ,"and", b ,"is:", gcd)
print("LCM of", a ,"and", b ,"is:", lcm)