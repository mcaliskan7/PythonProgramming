def evenorodd(x):
    if x%2==0:
        return x
    else:
        raise ValueError

list=[0,1,7,9,4,2,3,11,16,17,21]

for i in list:
    try:
        print(evenorodd(i))
    except ValueError:
        pass
print("\n")
for i in list:
    try:
        evenorodd(i)==i
    except ValueError:
        print(i)
