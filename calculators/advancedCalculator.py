print("**********WELCOME**********")
print("\n1.  ADDITION"
      "\n2.  SUBTRACTION"
      "\n3.  MULTIPLICATION"
      "\n4.  DIVISION"
      "\n5.  EXPONENTIATION"
      "\n6.  SQUARE ROOT"
      "\n7.  ROUND UP"
      "\n8.  ROUND DOWN"
      "\n9.  COMBINATION"
      "\n10. PERMUTATION"
      "\n11. COSINE"
      "\n12. SINE"
      "\n13. ABSOLUTE VALUE"
      "\n14. FACTORIAL"
      "\n15. GCD"
      "\n16. LOGARITHM"
      "\n17. TANGENT")

import math

while True:
    n=input("\nEnter the number of operation: ")
    if n=="q":
        break
    else:
        x=float(input("Enter a number: "))
        if n=="1":
            y=float(input("Enter other number: "))
            print(x+y)
        elif n=="2":
            y=float(input("Enter other number: "))
            print(x-y)
        elif n=="3":
            y=float(input("Enter other number: "))
            print(x*y)
        elif n=="4":
            y=float(input("Enter other number: "))
            print(x/y)
        elif n=="5":
            y=float(input("Enter other number: "))
            print(math.pow(x,y))
        elif n=="6":
            print(math.sqrt(x))
        elif n=="7":
            print(math.ceil(x))
        elif n=="8":
            print(math.floor(x))
        elif n=="9":
            x=int(x)
            y=int(input("Enter other number: "))
            print(math.comb(x,y))
        elif n=="10":
            x=int(x)
            y=int(input("Enter other number: "))
            print(math.perm(x,y))
        elif n=="11":
            print(math.cos(x))
        elif n=="12":
            print(math.sin(x))
        elif n=="13":
            print(math.fabs(x))
        elif n=="14":
            print(math.factorial(x))
        elif n=="15":
            x=int(x)
            y=int(input("Enter other number: "))
            print(math.gcd(x,y))
        elif n=="16":
            y=float(input("Enter the base: "))
            print(math.log(x,y))
        elif n=="17":
            print(math.tan(x))
        else:
            print("Please enter a valid operation number!")
