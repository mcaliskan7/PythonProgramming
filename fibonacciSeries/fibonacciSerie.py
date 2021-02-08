print("         **********FIBONACCI SERIES**********")

while True:
    n=input("\nEnter a number to show the fibonacci series until the number: ")
    if n=="q":
        break
    else:
        n=int(n)
        i=1
        j=0
        print(i+j,end="  ")
        while i+j<=n:
            k=i+j
            print("{}".format(k),end="  ")
            j=i
            i=k
    print("\n")

"""
i=1
j=1
fibonacci =[j,i]

n=int(input("\nEnter a number to show the fibonacci series until the number: "))
while i<=n:
    i,j = i+j,i
    fibonacci.append(i)
print(fibonacci)
"""
