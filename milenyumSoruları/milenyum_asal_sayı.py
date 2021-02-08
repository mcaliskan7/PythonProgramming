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

i=1
while True:

    nkare = i ** 2
    narti1kare = (i+1) ** 2

    a = nkare
    temp = 0

    while a <= narti1kare:
        if  prime(a) == 1:
            temp +=1
        a += 1

    if temp == 0:
        print(i)
        print(i)
        print(i)
        break

    print(i)

    i += 1
