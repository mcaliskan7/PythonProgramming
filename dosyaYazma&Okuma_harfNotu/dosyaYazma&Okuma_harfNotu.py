def harfNotu(ogrenci):
    ogrenci = ogrenci[:-1]
    liste = ogrenci.split(", ")
    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])

    ortalama = (vize1 * 3 + vize2 * 3 + final * 4)/10
    liste.append(str(ortalama))

    if ortalama>=90:
        harf = "AA"
    elif ortalama>=85:
        harf = "BA"
    elif ortalama>=80:
        harf = "BB"
    elif ortalama>=75:
        harf = "CB"
    elif ortalama>=70:
        harf = "CC"
    elif ortalama>=65:
        harf = "DC"
    elif ortalama>=60:
        harf = "DD"
    elif ortalama>=50:
        harf = "FD"
    else:
        harf = "FF"

    liste.append(harf)
    ogrenci1 = ""
    for i in liste:
        ogrenci1 += i + "  "

    return ogrenci1

with open("harfnotu.txt","w",encoding="utf-8") as file:
    file.write("Ayşe Yılmaz, 60, 70, 80\nAhmet Şahin, 75, 87, 45\nElif Sevgi, 23, 38, 62\nNazlı Ilıcak, 91, 65, 83\n")

with open("harfnotu.txt","r",encoding="utf-8") as file:
    liste2 = []
    for i in file:
        liste2.append(harfNotu(i))
    with open("harfnotu.txt","w",encoding="utf-8") as file:
        for j in liste2:
            file.write(j)
            file.write("\n")
