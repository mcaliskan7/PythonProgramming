print("**********WELCOME**********")
print("   Factorial Calculator")

while True:
    n=input("\nEnter a positive integer to calculate its factorial: ")
    if n=="q":
      break
    else:
        n=int(n)
        fact=1
        for i in range(1,n+1):
            fact*=i
    print("\n{}! = {}".format(n,fact))

    print("Press q to quit...")
