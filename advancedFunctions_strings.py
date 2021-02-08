print("********** UPPER & LOWER FUNCTIONS **********")
print("Merve Çalışkan".upper())
print("Merve Çalışkan".lower())

print("********** REPLACE FUNCTION **********")
print("Sen çok biliyorsun!".replace("e","i").replace("o","i").replace("u","i"))
print("Sen çok biliyorsun!".replace("e","o").replace("i","o").replace("u","o"))
print("Evet, benim.".replace("et","im").replace(",","").replace(".",":)"))

print("********** STARTSWITH & ENDSWITH FUNCTIONS **********")
print("Aynen.".startswith("A"))
print("Hayır".endswith("ır"))

print("********** SPLIT FUNCTION **********")
print("Python Programlama Dili".split(" "))

print("********** STRIP & LSTRIP & RSTRIP FUNCTIONS **********")
print("\-\-\-\-\-MERVE ÇALIŞKAN-/-/-/-/-/".strip("\-").strip("-/"))
print("\-\-\-\-\-MERVE ÇALIŞKAN-/-/-/-/-/".lstrip("\-"))
print("\-\-\-\-\-MERVE ÇALIŞKAN-/-/-/-/-/".rstrip("-/"))
print("          MERVE ÇALIŞKAN          ".strip())

print("********** JOIN FUNCTION **********")
list1 = ["16","08","1999"]
print(".".join(list1))

print("********** COUNT FUNCTION **********")
print("Ankara'dan üstü kapalı araba aldım.".count("a"))
print("Ankara'dan üstü kapalı araba aldım.".count("a",11))

print("********** FIND & RFIND FUNCTION **********")
print("Ankara'dan üstü kapalı araba aldım.".find("a"))
print("Ankara'dan üstü kapalı araba aldım.".rfind("a"))
print("Ankara'dan üstü kapalı araba aldım.".find("y"))
