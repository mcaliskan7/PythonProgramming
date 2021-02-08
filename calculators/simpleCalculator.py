print("**************CALCULATOR**************")
print("1. ADDITION\n"
      "2. SUBTRACTION\n"
      "3. MULTIPLICATION\n"
      "4. DIVISION\n"
      "5. EXPONENTIATION\n"
      "6. ROOT\n")

x=int(input("Enter the number of operation: "))

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

if x==1:
    print("The result: {}".format(a+b))
elif x==2:
    print("The result: {}".format(a-b))
elif x==3:
    print("The result: {}".format(a*b))
elif x==4:
    print("The result: {}".format(a/b))
elif x==5:
    print("The result: {}".format(a**b))
elif x==6:
    print("The result: {}".format(a**(1/b)))
else:
    print("Please enter a valid operation number![1,2,3,4,5,6]")
