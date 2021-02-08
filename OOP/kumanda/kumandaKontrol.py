import random
import time

class kumanda():
    def __init__(self,durum="KAPALI",ses=17,kanalListe=["TRT","TRT MÜZİK","ATV","SHOW TV","STAR TV","FOX TV","TV8"],kanal="TRT"):
        self.durum=durum
        self.ses=ses
        self.kanalListe=kanalListe
        self.kanal=kanal

    def ac(self):
        print("Televizyon açılıyor..")
        time.sleep(1)
        self.durum="AÇIK"

    def kapat(self):
        print("Televizyon kapatılıyor..")
        time.sleep(1)
        self.durum="KAPALI"

    def sesDegistir(self):
        while True:
            n=input("Sesi azaltmak için -'ye, arttırmak için +'ya, çıkmak için q'ya basınız: ")
            if n=="-":
                if self.ses!=0:
                    self.ses-=1
                    time.sleep(0.5)
                    print("Ses azaltıldı.")
            elif n=="+":
                if self.ses!=31:
                    self.ses+=1
                    time.sleep(0.5)
                    print("Ses arttırıldı.")
            elif n=="q":
                break
            else:
                print("Lütfen geçerli bir karakter giriniz.")
        print("Ses seviyesi güncellendi: {}".format(self.ses))

    def kanalDegistir(self,kanal):
        while True:
            n=input("Bir sonraki kanal için +'ya, bir önceki kanal için -'ye, çıkmak için q'ya basınız: ")
            if n=="+":
                a=self.kanalListe.index(self.kanal)
                self.kanal=self.kanalListe[a+1]
            elif n=="-":
                a=self.kanalListe.index(self.kanal)
                self.kanal=self.kanalListe[a+1]
            elif n=="q":
                break
            else:
                print("Lütfen geçerli bir karakter giriniz.")
        print("Kanal güncellendi. Şimdiki kanal: {}".format(self.kanal))

    def rastgeleKanalAc(self):
        rastgele=random.randint(0,len(self.kanalListe)-1)
        self.kanal=self.kanalListe[rastgele]
        print("Şimdiki kanal: {}".format(self.kanal))

    def kanalEkleSil(self,kanal):
        n=input("Kanal eklemek için +'ya, silmek için -'ye, çıkmak için q'ya basınız: ")
        while True:
            if n=="+":
                print("Kanal eklendi: {}".format(kanal))
                self.kanalListe.append(kanal)
                break
            elif n=="-":
                print("Kanal silindi: {}".format(kanal))
                self.kanalListe.remove(kanal)
                break
            elif n=="q":
                break
            else:
                print("Lütfen geçerli bir karakter giriniz.")
                break

    def bilgileriGoster(self):
        print("TV Durumu: {}\nKanal Listesi: {}\nŞimdiki Kanal: {}\nToplam Kanal Sayısı: {}\nSes Seviyesi: {}".format(self.durum,self.kanalListe,self.kanal,len(self.kanalListe),self.ses))


kumanda1=kumanda()

print("* * * * * MENÜ * * * * * *")
print("*  1. TV AÇ              *\n"
      "*  2. TV KAPA            *\n"
      "*  3. KANAL DEĞİŞTİR     *\n"
      "*  4. SES AZALT/ARTTIR   *\n"
      "*  5. RASTGELE KANAL AÇ  *\n"
      "*  6. KANAL EKLE/SİL     *\n"
      "*  7. BİLGİLERİ GÖSTER   *")
print("* * * * *      * * * * * *")

while True:
    islem=input("\nİşlem numarasını giriniz [Çıkmak için q'ya basınız]: ")
    if islem=="q":
        break
    elif islem=="1":
        if kumanda1.durum=="KAPALI":
            kumanda1.ac()
        else:
            print("Televizyon zaten açık.")
    elif islem=="2":
        if kumanda1.durum!="KAPALI":
            kumanda1.kapat()
        else:
            print("Televizyon zaten kapalı.")
    elif islem=="7":
            kumanda1.bilgileriGoster()
    if kumanda1.durum!="KAPALI":
        if islem=="3":
            kumanda1.kanalDegistir(kumanda1.kanal)
        elif islem=="4":
            kumanda1.sesDegistir()
        elif islem=="5":
            kumanda1.rastgeleKanalAc()
        elif islem=="6":
            kanallar = input("Eklemek/Silmek istediğiniz kanalları ',' ile ayırarak giriniz: ")
            eklenecekler = kanallar.split(",")
            for i in eklenecekler:
                kumanda1.kanalEkleSil(i)
            print("Kanal listesi güncellendi: {}".format(kumanda1.kanalListe))
        elif islem!="q" and islem!="1" and islem!="2" and islem!="7":
            print("Lütfen geçerli bir değer giriniz.")
    else:
        if islem!="7":
            print("Televizyon kapalı.")
