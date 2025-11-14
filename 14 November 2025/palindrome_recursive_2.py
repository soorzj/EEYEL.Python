str=input("Enter the string: ")
count=len(str)
def palindrome(str):
    l=len(str)
    if l==1:
        return True
    if str[0] != str[l-1]:
        return False
    else:
        return palindrome(str[1:l-1])
if palindrome(str) == True:
    print("The number is palindrome")
else:
    print("The number is not palindrome")