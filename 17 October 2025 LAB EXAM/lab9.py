n=int(input("Enter a number: "))
num=2
count=0
i=2
while(n>0):
    factcount=0
    for j in range (2,i):
        if(i%j==0):
            factcount+=1
    if(factcount==0):
        count+=1
        if(count==n):
            print(i)
            n=0
    i+=1
        
