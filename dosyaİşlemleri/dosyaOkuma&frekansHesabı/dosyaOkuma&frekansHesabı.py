class dosya():
    def __init__(self):
        with open("istiklal_marşı.txt","r",encoding="utf-8") as file:
            icerik = file.read()
            kelimeler = icerik.split()
            self.safKelimeler = list()
            for i in kelimeler:

                i = i.strip("\n")
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip("?")
                i = i.strip(";")
                i = i.strip("-")
                i = i.strip(":")
                i = i.strip("'")
                i = i.strip("!")

                self.safKelimeler.append(i)

    def tumKelimeler(self):
        kelimelerKumesi = set()
        for i in self.safKelimeler:
            kelimelerKumesi.add(i)
        print("Tüm kelimeler:\n")
        for i in kelimelerKumesi:
            print(i)

    def kelimeFrekansi(self):
        kelime_sozluk = dict()
        kelimesayisi=0
        harfsayisi=0
        for i in self.safKelimeler:
            kelimesayisi+=1
            harfsayisi+=len(i)
            if i in kelime_sozluk:
                kelime_sozluk[i]+=1
            else:
                kelime_sozluk[i]=1
        encokgecenkelimeninfrekansi = 0
        encokgecenkelime=0
        for kelime,frekans in kelime_sozluk.items():
            print("{} ---> {}".format(kelime,frekans))
            if frekans>encokgecenkelimeninfrekansi:
                encokgecenkelimeninfrekansi=frekans
                encokgecenkelime=kelime
        print("\nToplam {} harf var.".format(harfsayisi))
        print("\nToplam {} kelime geçiyor.".format(kelimesayisi))
        print("\nEn çok {} kelimesi geçiyor.[{} kere]".format(encokgecenkelime,encokgecenkelimeninfrekansi))

dosya1 = dosya()
dosya1.tumKelimeler()
dosya1.kelimeFrekansi()
