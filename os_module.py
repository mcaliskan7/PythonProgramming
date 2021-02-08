import os
import datetime

"tüm fonksiyonlarını gösterir"
print(dir(os))

"os modülünün hangi dizinde olduğunu gösterir"
print(os.getcwd())

"dizini değiştirir"
os.chdir("C:/Users/Büşra/Desktop")
print(os.getcwd())

"bulunduğu dizindeki klasörleri gösterir"
print(os.listdir())

for i in os.listdir():
    print(i)
"""
//yeni klasör oluşturur
os.mkdir("deneme1")
os.remove("deneme1")
"""

"bir klasör ve içine yeni bir klasör oluşturur"
os.makedirs("deneme2/deneme3")

"bir klasörün içindeki bir klasörü siler"
os.rmdir("deneme2/deneme3")

os.makedirs("deneme2/deneme3")

"hem klasörü hem içindeki klasörü siler"
os.removedirs("deneme2/deneme3")

"""
"dosya isimlerini değiştirir"
os.rename("xx.txt","yy.txt")

"dosyanın tüm özelliklerini gösterir"
print(os.stat("xx.txt"))

"dosyanın son değiştirilme tarihini gösterir/saniye cinsinden"
print(os.stat("xx.txt").st_mtime)

print(datetime.fromtimestamp(os.stat("xx.txt").st_mtime))
"""

"dizindeki tüm klasörleri gezer"
print(os.walk("C:/Users/Büşra/Desktop"))

for i in os.walk("C:/Users/Büşra/Desktop"):
    print(i)

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/Büşra/Desktop"):
    for i in dosya_isimleri:
        if i.endswith(".txt"):
            print(i)
