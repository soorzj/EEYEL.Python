#Sum of numbers eneted by user till exit code 999 entered
print("Enter numbers to add to sum or enter 999 to exit")
sum=0
num=int(input("Enter a number: "))
while num!=999:
    sum=sum+num
    num=int(input("Enter a number: "))
print("Exit code occured")
print("Sum of numbers= ", sum)
