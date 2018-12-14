a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
for i in range(1,a+1):
    if (a%i==0 and b%i==0):
        print (i)

