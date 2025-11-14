def list_sum(list, i):
    if i == len(list):
        return 0
    else:
        return list[i]+ list_sum(list, i+1)
n=int(input("Enter number of terms of the list:"))
list=[]
for i in range (n):
    a=int(input("Enter element:"))
    list.append(a)
print("Sum of elements of the list is: ",list_sum(list,0))
