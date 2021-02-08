import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa Sayısı INT)")
    con.commit()

tablo_olustur()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplık values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplık values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("Select * from kitaplık")
    liste = cursor.fetchall()
    print(liste)

def verileri_al2():
    cursor.execute("select isim,yazar from kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def verileri_al3(yayinevi):
    cursor.execute("select * from kitaplık where yayınevi=?",(yayinevi,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def verileri_guncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("Update kitaplık set Yayınevi=? where Yayınevi=?",(yeni_yayinevi,eski_yayinevi))
    con.commit()

def verileri_sil(yazar):
    cursor.execute("Delete from kitaplık where Yazar=?",(yazar,))
    con.commit()

"""isim = input("İsim: ")
yazar = input("Yazar: ")
yayinevi = input("Yayınevi: ")
sayfa_sayisi = input("Sayfa Sayısı: ")

veri_ekle()

veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi)"""

verileri_al()
verileri_al2()
verileri_al3("Kabalcı")

verileri_guncelle("Metis Edebiyat","Everest")
verileri_sil("Tess Gerritsen")

con.close()
