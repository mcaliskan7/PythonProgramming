list1 = [1,2,3,4,5,6,7]
list1.append(8)
print(list1)

list2 = [9,0]
list1.extend(list2)
print(list1)

list1.insert(0,"Numbers")
print(list1)

list1.pop()
print(list1)

list1.insert(1,0)
print(list1)

list1.remove("Numbers")
print(list1)

print(list1.index(7))

list1.append(3)
print(list1)
print(list1.count(3))

list3 = {-5,0,4,-9,7,3,-8,-1,5}
print(sorted(list3))

list4 = ["araba","kayak","salıncak","balkon","mahalle","yağmur"]
print(sorted(list4))
print(sorted(list4,reverse=True))

