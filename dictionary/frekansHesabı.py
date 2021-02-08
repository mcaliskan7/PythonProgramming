dizi = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
dizisozluk = dict()
for harf in dizi:
    if harf in dizisozluk:
        dizisozluk[harf] += 1
    else:
        dizisozluk[harf] = 1

for i,j in dizisozluk.items():
    print(i,"->",j)
