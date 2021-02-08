list1 = [1,1,2,4,5,5,6,1,5,7,4,8,9,1,3,8,9]
print(set(list1))
print(set("Python Programlama Dili"))

for i in set(list1):
    print(i**2,end=" ")

print("\n")
set1 = {0,1,2,3,4,5,6,7,8}
set2 = {1,3,5,7,9}

set1.add(9)
print(set1,end=" ")
print(set2)

print(set1.difference(set2))

set1.difference_update(set2)
print(set1,end=" ")
print(set2)

set1.discard(2)
print(set1,end="\n\n")

set3 = {0,1,2,3,4,5,6,7,8}
set4 = {1,3,5,7,9}
print(set3.intersection(set4))

set3.intersection_update(set4)
print(set3,end=" ")
print(set4,end="\n\n")

set5 = {0,2,4,6,8}
set6 = {1,3,5,7,9}
print(set5.union(set6))

set5.update(set6)
print(set5,end=" ")
print(set6)
