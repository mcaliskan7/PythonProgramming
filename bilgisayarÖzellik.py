import time

class Bilgisayar():

    def __init__(self,islemci,ram,harddisk,ekran,fiyat):

        self.__islemci = islemci
        self.__ram = ram
        self.__harddisk = harddisk
        self.__ekran = ekran
        self.__fiyat = fiyat

    def yukselt(self,y_islemci,y_ram,y_harddisk,y_ekran): #varsayılan değer atanamıyor...

        self.__islemci = y_islemci
        self.__ram = y_ram
        self.__harddisk = y_harddisk
        self.__ekran = y_ekran
        print("Yükseltiliyor...")
        time.sleep(1)
        print(bilgisayar)


    def __str__(self):

        return ("""
        Yeni Bilgisayarın Özellikleri
        
        işlemci : {}
        Ram : {}
        Harddisk : {}
        Ekran : {}
        Fiyat : {}
        """.format(self.__islemci,self.__ram,self.__harddisk,self.__harddisk,self.__fiyat))




    def fiyatGuncelle(self,fiyat):

        print("Fiyat güncelleniyor..")
        time.sleep(1)
        self.__fiyat = fiyat
        print(bilgisayar)

bilgisayar = Bilgisayar("75Mhz","8mb","1.2Gb","15inç","1200$")

print(bilgisayar)
bilgisayar.fiyatGuncelle(fiyat="1350$")
