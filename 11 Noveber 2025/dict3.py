#geberate histogram for a string
str=input("Enter a string: ")
histogram={}
for c in str:
    if c in histogram:
        histogram[c]+=1
    else:
        histogram[c]=1
print("Histogram of the string:")
for key in histogram:
    print(key,":", histogram[key])