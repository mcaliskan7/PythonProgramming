def findGcd(x,y,z):
    i=1
    gcd=1
    while i<=x and i<=y and i<=z:
        if x%i==0 and y%i==0 and z%i==0:
            gcd=i
        i+=1
    return gcd

def findPytha():
    pythaList = list()
    for i in range(1,101):
        for j in range(1,101):
            k = (i ** 2 + j ** 2) ** 0.5
            if (k == int(k) ):
                if findGcd(i,j,k)>1:
                    continue
                pythaList.append((i,j,int(k)))
    return pythaList

for i in findPytha():
    print(i)
