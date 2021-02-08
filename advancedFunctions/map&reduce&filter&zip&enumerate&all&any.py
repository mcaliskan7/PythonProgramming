print("**********MAP FONKSİYONU**********")
liste1 = [1,2,7,9,4,6,5]
liste2 = [4,5,6,7,3,1,2]
liste3 = [2,4,9,3,8,7,5]
print(list(map(lambda x,y,z : x*y/z,liste1,liste2,liste3)))

print("**********FILTER FONKSİYONU**********")
def asalSayı(x):
    i=2
    if x==1:
        return False
    elif x==2:
        return True
    else:
        while i<x:
            if x%i==0:
                return False
            i+=1
        return True
print(list(filter(asalSayı,liste1)),end=" ")
print(list(filter(asalSayı,liste2)),end=" ")
print(list(filter(asalSayı,liste3)))

print("**********ZIP FONKSİYONU**********")
liste4 = []
i=0
while i<len(liste1) and i<len(liste2) and i<len(liste3):
    liste4.append((liste1[i],liste2[i],liste3[i]))
    i+=1
print(liste4)

print(list(zip(liste1,liste2,liste3)))

for i,j,k in zip(liste1,liste2,liste3):
    print(list(str(i)+str(j)+str(k)),end=" ")
    print("----->",end=" ")
    print(i+j+k)

print("**********ENUMERATE FONKSİYONU**********")
print(list(enumerate(liste4)),end="\n\n")
for i,j in enumerate(liste4):
    print(i,j)

print("\n**********ALL & ANY FONKSİYONLARI**********")
print(all([True,False,True,True]))
print(all([True,True,True,True]))
print(any([True,False,False,True]))
print(any([False,False,False,False]))
print(all([1+5==6,2+7==5,4-9==2]))
print(any([1+5==6,2+7==5,4-9==2]))
