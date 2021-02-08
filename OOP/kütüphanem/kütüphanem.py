import sqlite3
import time

class kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski,sayfasayisi):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
        self.sayfasayisi = sayfasayisi

    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\nSayfa Sayısı: {}".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski,self.sayfasayisi)

class kutuphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect(("kütüphanem.db"))
        self.cursor = self.baglanti.cursor()
        sorgu = "Create table if not exists kitaplar (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Tür TEXT,Baskı INT,Sayfa Sayısı INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):
        self.cursor.execute("Select * from kitaplar")
        kitaplar = self.cursor.fetchall()

        if len(kitaplar)==0:
            print("Kütüphanede kitap bulunmuyor.")
        else:
            for i in kitaplar:
                kitap1 = kitap(i[0],i[1],i[2],i[3],i[4],i[5])
                print(kitap1)

    def kitap_sorgula(self,isim):
        self.cursor.execute("Select * from kitaplar where İsim = ?",(isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar)==0:
            print("Böyle bir kitap bulunmuyor.")
        else:
            kitap1 = kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4],kitaplar[0][5])
            print(kitap1)

    def kitap_ekle(self,kitap):
        self.cursor.execute("Insert into kitaplar values(?,?,?,?,?,?)",(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski,kitap.sayfasayisi))
        self.baglanti.commit()

    def kitap_sil(self,isim):
        self.cursor.execute("Select * from kitaplar where İsim = ?",(isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar)==0:
            print("Böyle bir kitap bulunmuyor.")
        else:
            self.cursor.execute("Delete from kitaplar where İsim = ?",(isim,))
            self.baglanti.commit()
            print("Kitap silindi.")

    def baski_yukselt(self,isim):
        self.cursor.execute("Select * from kitaplar where İsim = ?",(isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar)==0:
            print("Böyle bir kitap bulunmuyor.")
        else:
            baski = kitaplar[0][4]
            baski += 1
            self.cursor.execute("Update kitaplar set Baskı = ?",(baski,))
            self.baglanti.commit()
            print("Baskı yükseltildi.")
