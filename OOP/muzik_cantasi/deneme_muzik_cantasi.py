from muzikcantasi import *

print("                                                           \n"
      "                    * * * * * * * * * * * * * * * * * * * *\n"
      "                    *                                     *\n"
      "                    *    Müzik Çantası'na hoşgeldiniz.    *\n"
      "                    *                                     *\n"
      "                    *      1. Müzikleri Göster            *\n"
      "                    *      2. Müzik Sorgula               *\n"
      "                    *      3. Müzik Ekle                  *\n"
      "                    *      4. Müzik Sil                   *\n"
      "                    *      5. Dinlenme Sayısını Yükselt    *\n"
      "                    *                                     *\n"
      "                    *    Çıkmak için q'ya basınız.        *\n"
      "                    *                                     *\n"
      "                    * * * * * * * * * * * * * * * * * * * *")

muzikcantam = muzikcantasi()

while True:
      islem = input("\nYapacağınız İşlem: ")

      if islem=="q":
            print("Program Sonlandırılıyor..")
            time.sleep(1)
            print("Yine bekleriz..")
            break

      elif islem=="1":
            muzikcantam.muzikleri_goster()

      elif islem=="2":

            sarkiadi = input("\nHangi müziği arıyorsunuz?: ")
            print("Müzik sorgulanıyor..")
            time.sleep(1)
            muzikcantam.muzik_sorgula(sarkiadi)

      elif islem=="3":

            sarkiadi = input("\nŞarkı Adı: ")
            sarkici = input("Şarkıcı: ")
            sure = int(input("Süre: "))
            tur = input("Tür: ")
            cikisyili = int(input("Çıkış Yılı: "))
            dinlenmesayisi = int(input("Dinlenme Sayısı: "))

            yeni_muzik = muzik(sarkiadi,sarkici,sure,tur,cikisyili,dinlenmesayisi)
            print("Müzik ekleniyor..")
            time.sleep(1)

            muzikcantam.muzik_ekle(yeni_muzik)
            print("Müzik eklendi: {}".format(sarkiadi))

      elif islem=="4":
            sarkiadi = input("\nHangi müziği silmek istiyorsunuz?: ")

            while True:
                  onay = input("{} müziğini silmek istediğinize emin misiniz?[E/H]: ".format(sarkiadi))
                  if onay == "E" or onay == "e":
                        print("Müzik siliniyor..")
                        time.sleep(1)

                        muzikcantam.muzik_sil(sarkiadi)
                        break

                  elif onay == "H" or onay == "h":
                        break

                  else:
                        print("Lütfen geçerli bir değer giriniz.")

      elif islem=="5":
            sarkiadi = input("\nHangi müziğin dinlenme sayısını yükseltmek istiyorsunuz?: ")
            print("Dinlenme sayısı yükseltiliyor..")
            time.sleep(1)

            muzikcantam.dinlenme_sayisi_yukselt(sarkiadi)

      else:
            print("\nLütfen geçerli bir değer giriniz.")
            time.sleep(1)
            print("İşlem sayfasına yönlendiriliyorsunuz..")
            time.sleep(1)
