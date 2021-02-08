from kütüphanem import *

print("                                                       \n"
      "                    * * * * * * * * * * * * * * * * * *\n"
      "                    *                                 *\n"
      "                    *    Kütüphanem'e hoşgeldiniz.    *\n"
      "                    *                                 *\n"
      "                    *      1. Kitapları Göster        *\n"
      "                    *      2. Kitap Sorgula           *\n"
      "                    *      3. Kİtap Ekle              *\n"
      "                    *      4. Kitap Sil               *\n"
      "                    *      5. Baskı Yükselt           *\n"
      "                    *                                 *\n"
      "                    *    Çıkmak için q'ya basınız.    *\n"
      "                    *                                 *\n"
      "                    * * * * * * * * * * * * * * * * * *")

kutuphane1 = kutuphane()

while True:
      islem = input("\nYapacağınız İşlem: ")

      if islem=="q":
            print("Program Sonlandırılıyor..")
            time.sleep(1)
            print("Yine bekleriz..")
            break

      elif islem=="1":
            kutuphane1.kitaplari_goster()

      elif islem=="2":

            isim = input("Hangi kitabı arıyorsunuz?: ")
            print("Kitap sorgulanıyor..")
            time.sleep(1)
            kutuphane1.kitap_sorgula(isim)

      elif islem=="3":

            isim = input("İsim: ")
            yazar = input("Yazar: ")
            yayinevi = input("Yayınevi: ")
            tur = input("Tür: ")
            baski = int(input("Baskı: "))
            sayfasayisi = int(input("Sayfa Sayısı: "))

            yeni_kitap = kitap(isim,yazar,yayinevi,tur,baski,sayfasayisi)
            print("Kitap ekleniyor..")
            time.sleep(1)

            kutuphane1.kitap_ekle(yeni_kitap)
            print("Kitap eklendi.")

      elif islem=="4":
            isim = input("Hangi kitabı silmek istiyorsunuz?: ")

            while True:
                  onay = input("{} kitabını silmek istediğinize emin misiniz?[E/H]: ".format(isim))
                  if onay == "E" or onay == "e":
                        print("Kitap siliniyor..")
                        time.sleep(1)

                        kutuphane1.kitap_sil(isim)
                        break

                  elif onay == "H" or onay == "h":
                        break

                  else:
                        print("Lütfen geçerli bir değer giriniz.")

      elif islem=="5":
            isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz?: ")
            print("Baskı yükseltiliyor..")
            time.sleep(1)

            kutuphane1.baski_yukselt(isim)

      else:
            print("Lütfen geçerli bir değer giriniz.")
            time.sleep(1)
            print("İşlem sayfasına yönlendiriliyorsunuz..")
            time.sleep(1)
