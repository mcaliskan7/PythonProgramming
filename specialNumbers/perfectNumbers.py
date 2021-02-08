print("     **********PERFECT NUMBERS**********")

while True:
    n=input("\nEnter a number to see whether it's a perfect number or not: ")
    if n=="q":
        break
    else:
        n=int(n)
        p=0
        for i in range(1,n):
            if n%i==0:
                p+=i
        if p==n:
            print("{} is a perfect number!".format(n))
        else:
            print("{} is not a perfect number.".format(n))
        print("\nPress q to quit...")
