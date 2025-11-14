n=int(input("Enter a number of rows: "))
for i in range(n):
    for a in range(n-i):
        print(" ",end="")
    for a in range(i+1):
        print("* ",end="")
    print()
