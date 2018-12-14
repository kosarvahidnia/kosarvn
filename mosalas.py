import math
x1=int(input("Enter x1 : "))
y1=int(input("Enter y1 : "))
x2=int(input("Enter x2 : "))
y2=int(input("Enter y2 : "))
x3=int(input("Enter x3 : "))
y3=int(input("Enter y3 : "))
a=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
b=math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
c=math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
p=a+b+c
print(p)
s=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
if s<0 :
    s=-1*s
print(s)