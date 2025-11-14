n=int(input("Enter a number of rows: "))
n+=1
for i in range (n):
    for a in range(i):  
        print(" ",end="")
    for j in range(2*(n-i-1)-1):
        print("*",end="")
    print()
