#generate a dictornay of numbers and their squares
a=int(input("Enter numbers required:"))
dict={}
for i in range(1,a+1):
    dict[i]=i**2
print("Number\t Square")
for key in dict:
    print(key ,"\t", dict[key])
