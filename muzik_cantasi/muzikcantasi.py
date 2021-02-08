import sqlite3
import time

class muzik():
    def __init__(self,sarkiadi,sarkici,sure,tur,cikisyili,dinlenmesayisi):
        self.sarkiadi = sarkiadi
        self.sarkici = sarkici
        self.sure = sure
        self.tur = tur
        self.cikisyili = cikisyili
        self.dinlenmesayisi = dinlenmesayisi

    def __str__(self):
        return "\nŞarkı Adı: {}\nŞarkıcı: {}\nSüre: {}\nTür: {}\nÇıkış Yılı: {}\nDinlenme Sayısı: {}".format(self.sarkiadi,self.sarkici,self.sure,self.tur,self.cikisyili,self.dinlenmesayisi)


class muzikcantasi():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("muzikcantasi.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("Create table if not exists muzikler (Şarkı_Adı TEXT,Şarkıcı TEXT,Süre INT,Tür TEXT,Çıkış_Yılı INT,Dinlenme_Sayısı INT)")
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def muzikleri_goster(self):
        self.cursor.execute("Select * from muzikler")
        muzikler = self.cursor.fetchall()

        if len(muzikler)==0:
            print("\nMüzik Çantası'nda müzik bulunmuyor.")
        else:
            for i in muzikler:
                muzik1 = muzik(i[0],i[1],i[2],i[3],i[4],i[5])
                print(muzik1)

    def muzik_sorgula(self,sarkiadi):
        self.cursor.execute("Select * from muzikler where Şarkı_Adı = ?",(sarkiadi,))
        muzikler = self.cursor.fetchall()

        if len(muzikler)==0:
            print("Müzik Çantası'nda böyle bir müzik bulunmuyor.")
        else:
            muzik1 = muzik(muzikler[0][0],muzikler[0][1],muzikler[0][2],muzikler[0][3],muzikler[0][4],muzikler[0][5])
            print(muzik1)

    def muzik_ekle(self,muzik):
        self.cursor.execute("Insert into muzikler values(?,?,?,?,?,?)",(muzik.sarkiadi,muzik.sarkici,muzik.sure,muzik.tur,muzik.cikisyili,muzik.dinlenmesayisi))
        self.baglanti.commit()

    def muzik_sil(self,sarkiadi):
        self.cursor.execute("Select * from muzikler where Şarkı_Adı = ?",(sarkiadi,))
        muzikler = self.cursor.fetchall()

        if len(muzikler)==0:
            print("Müzik Çantası'nda böyle bir müzik yok.")
        else:
            self.cursor.execute("Delete from muzikler where Şarkı_Adı = ?",(sarkiadi,))
            self.baglanti.commit()
            print("Müzik silindi: {}".format(sarkiadi))

    def dinlenme_sayisi_yukselt(self,sarkiadi):
        self.cursor.execute("Select * from muzikler where Şarkı_Adı = ?",(sarkiadi,))
        muzikler = self.cursor.fetchall()

        if len(muzikler)==0:
            print("Müzik Çantası'nda böyle bir müzik yok.")
        else:
            dinlenmesayisi = muzikler[0][5]
            dinlenmesayisi += 1
            self.cursor.execute("Update muzikler set Dinlenme_Sayısı = ?",(dinlenmesayisi,))
            self.baglanti.commit()
            print("Dinlenme sayısı yükseltildi: {}".format(dinlenmesayisi))
