dict={}
key=[]
value=[]
n=int(input("Enter number of pairs: "))
for i in range(n):
    k=input(f"Enter key {i+1} : ")
    v=input(f"Enter value {i+1} : ")
    key.append(k)
    value.append(v)
dict={key[i]:value[i] for i in range(n)}
for i in range (n):
    print(key[i], ":", value[i])