list=["123","c","python","17","java","programming","719"]

for i in list:
    try:
        i=int(i)
        print(i)
    except:
        pass
print("\n")
for i in list:
    try:
        i=int(i)
    except:
        print(i)
