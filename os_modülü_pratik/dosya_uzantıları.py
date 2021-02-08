import os

txt_dosyalari = list()
pdf_dosyalari = list()
jpg_dosyalari = list()
digerleri = list()

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/Büşra/Desktop"):

    for i in dosya_isimleri:
        if i.endswith(".txt") or i.endswith(".TXT"):
            txt_dosyalari.append(i)
        elif i.endswith(".pdf") or i.endswith(".PDF"):
            pdf_dosyalari.append(i)
        elif i.endswith(".jpg") or i.endswith(".JPG"):
            jpg_dosyalari.append(i)
        else:
            digerleri.append(i)

with open("txt_dosyaları.txt","w",encoding="utf-8") as file:
    for txt in txt_dosyalari:
        file.write(txt)
        file.write("\n")

with open("pdf_dosyaları.txt","w",encoding="utf-8") as file1:
    for pdf in pdf_dosyalari:
        file1.write(pdf)
        file1.write("\n")

with open("jpg_dosyaları.txt","w",encoding="utf-8") as file2:
    for jpg in jpg_dosyalari:
        file2.write(jpg)
        file2.write("\n")

with open("diger_dosyalar.txt","w",encoding="utf-8") as file3:
    for diger in digerleri:
        file3.write(diger)
        file3.write("\n")
