with open("tüm_futbolcular.txt","r",encoding="utf-8") as file:
    fb_oyuncular = list()
    gs_oyuncular = list()
    bjk_oyuncular = list()
    kaleciler = list()
    defanslar = list()
    ortasahalar = list()
    forvetler = list()

    for oyuncuBilgisi in file:
        oyuncuBilgisi  = oyuncuBilgisi[:-1]
        bilgiler = oyuncuBilgisi.split(" - ")
        if bilgiler[2]=="Galatasaray":
            gs_oyuncular.append(oyuncuBilgisi + "\n")
        elif bilgiler[2]=="Fenerbahce":
            fb_oyuncular.append(oyuncuBilgisi + "\n")
        else:
            bjk_oyuncular.append(oyuncuBilgisi + "\n")

        if bilgiler[1]=="Kaleci":
            kaleciler.append(oyuncuBilgisi + "\n")
        elif bilgiler[1]=="Defans":
            defanslar.append(oyuncuBilgisi + "\n")
        elif bilgiler[1]=="Orta Saha":
            ortasahalar.append(oyuncuBilgisi + "\n")
        else:
            forvetler.append(oyuncuBilgisi + "\n")

    with open("gs_tümoyuncular.txt","w",encoding="utf-8") as file1:
        for i in gs_oyuncular:
            file1.write(i)
    with open("fb_tümoyuncular.txt","w",encoding="utf-8") as file2:
        for i in fb_oyuncular:
            file2.write(i)
    with open("bjk_tümoyuncular.txt","w",encoding="utf-8") as file3:
        for i in bjk_oyuncular:
            file3.write(i)
    with open("tümkaleciler.txt","w",encoding="utf-8") as file4:
        for i in kaleciler:
            file4.write(i)
    with open("tümdefanslar.txt","w",encoding="utf-8") as file5:
        for i in defanslar:
            file5.write(i)
    with open("tümortasahalar.txt","w",encoding="utf-8") as file6:
        for i in ortasahalar:
            file6.write(i)
    with open("tümforvetler.txt","w",encoding="utf-8") as file7:
        for i in forvetler:
            file7.write(i)
