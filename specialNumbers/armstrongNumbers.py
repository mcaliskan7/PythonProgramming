print("         **********ARMSTRONG NUMBERS**********")

while True:
    n=input("\nEnter a number to see whether it's an armstrong number or not: ")
    if n=="q":
        break
    else:
        a=len(n)
        n=int(n)
        result=0
        temp=n
        step=0
        while temp>0:
            step=int(temp%10)
            result+=step**a
            temp/=10
        if result==n:
            print("{} is an armstrong number!".format(n))
        else:
            print("{} is not an armstrong number.".format(n))
    print("Press q to quit...")
