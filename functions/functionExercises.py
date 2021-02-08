print("******************************")
list1 = [(3,4),(10,3),(5,6),(1,9)]

def area(tuple):
    return tuple[0] * tuple[1]

print(list(map(area,list1)))

print("******************************")
list2 = [(3,4,5),(8,15,17),(4,7,10),(7,24,25),(9,45,62)]

def triangle(tuple):
    if tuple[0] + tuple[1] > tuple[2] and tuple[1] + tuple[2] > tuple[0] and tuple[0] + tuple[1] > tuple[2]:
        return True
    else:
        return False

print(list(filter(triangle,list2)))

print("******************************")
list3 = [1,2,3,4,5,6,7,8,9,10]

def even(x):
    if x%2==0:
        return True
    else:
        return False

list3_ = list(filter(even,list3))
print(list3_)

result=0
for i in list3_:
    result+=i
print(result)

print("******************************")
name = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surname =["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(name,surname):
    print(i,j)
