print("**********FORM YOUR LIST**********")

while True:
    a=input("Enter your first number: ")
    if a=="q":
        break
    else:
        a=int(a)
        i=int(input("Enter your increment value: "))
        b=int(input("Enter your last number:" ))
        n=int(input("Enter a number to display numbers that are multiple of it in list: "))

        list = [a for a in range (a,b+1,i) if a%n==0]

    print("\n")
    print(list)
    print("\nPress q to quit...")
