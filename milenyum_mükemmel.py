n = 1
while True:

    p=0
    for i in range(1,n):
        if n%i==0:
            p+=i

    if p == n:
        if n % 2 != 0:
            print("found:",n)
            break

    n += 1
