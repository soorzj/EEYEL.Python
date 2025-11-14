def check(str,pattern,i):
    if len(str)<len(pattern):
        return -1
    elif pattern==str[:len(pattern)]:
        return i
    else:
        return check(str[1:], pattern, i+1)

str=input("Enter a string: ")
pattern=input("Enter the pattern to find: ")
pos=check(str,pattern,0)
if pos==-1:
    print("Pattern not found")
else:
    print("Pattern found at position:", (pos+1))