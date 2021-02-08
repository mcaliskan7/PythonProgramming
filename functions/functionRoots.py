print("Program is starting.. Enter the values for ax^2+bx+c function.")

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

delta=b**2-4*a*c
x1=(-b-delta**0.5)/2
x2=(-b+delta**0.5)/2

if(x1!=x2):
    print("The first root: {}       The second root: {}".format(x1,x2))

else:
    print("The only root: {}".format(x1))


