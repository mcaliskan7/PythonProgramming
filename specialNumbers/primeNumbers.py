print("            **********IS IT PRIME?**********")

def prime(x):
    temp=1
    for i in range(2,x):
        if x>2:
            if x%i==0:
                temp=0
                break
    if x<=1:
        temp=0
    return temp

while True:
    n=input("\nEnter an integer to see whether it's a prime number or not: ")
    if n=="q":
        break
    else:
        n=int(n)
        if prime(n)==1:
            print("It's a prime number!")
        else:
            print("It's not a prime number.")
