def findGcd(x,y):
    i=1
    gcd=1
    while i<=x and i<=y:
        if x%i==0 and y%i==0:
            gcd=i
        i+=1
    return gcd

def findLcm(x,y):
    if x>y:
        i=x
    else:
        i=y
    lcm=1
    while i>=x and i>=y:
        if i%x==0 and i%y==0:
            lcm=i
            break
        i+=1
    return lcm

while True:
    a=input("\nEnter first number to see their GCD and LCM: ")
    if a=="q":
        break
    else:
        b=int(input("Enter second number to see their GCD and LCM: "))
        a=int(a)
        print("GCD: {}    LCM: {}".format(findGcd(a,b),findLcm(a,b)))
