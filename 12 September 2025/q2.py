#wap to find roots of a quad expression
import cmath,math
print("Quadratic equation is of the form ax2 + bx + c = 0")
a=float(input("enter value a: "))
b=float(input("enter value b: "))
c=float(input("enter value c: "))
D=b*b-4*a*c #discrimnent
if(D>0):
    rd=math.sqrt(D)
else:
    rd=cmath.sqrt(D) #root of disicrimnent
x1=(-b+rd)/(2*a) 
x2=(-b-rd)/(2*a)
print("Quadratic equation  ax2 + bx +c = 0 has solutions ",x1,"and", x2)