def palindrome(str,rev,i):
    if i==len(str):
        if str==rev:
            return True
        else:
            return False
    else:
        return palindrome(str, rev + str[-(i+1)], i+1)

str=input("Enter the string: ")
count=len(str)
if palindrome(str,"",0) == True:
    print("The number is palindrome")
else:

    print("The number is not palindrome")
