bash = ""

with open("edgar_allan_poe.txt","r",encoding="utf-8") as file:
    for satir in file:
        bash += satir[0]
print(bash)
