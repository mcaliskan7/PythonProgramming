import sys

"modülün tüm fonksiyonlarını gösterir"
print(dir(sys))

"ekrana (hata yazısı) yazdırır/kırmızı"
sys.stderr.write("Bu bir hata mesajıdır")

"ekrana anında yazdırır"
sys.stderr.flush()

"ekrana normal bir yazı yazdırır"
sys.stdout.write("Bu normal bir yazıdır\n")

"dizini gösterir"
print(sys.argv)
for i in sys.argv:
    print(i)

def kok_bulma(a,b,c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Reel kök yoktur.")
    else:
        x1 = ( - b - delta ** 0.5 ) / ( 2 * a )
        x2 = ( - b + delta ** 0.5 ) / ( 2 * a )
        return x1,x2

if len(sys.argv) == 4:
    print("Kök Bulma",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin.")
    sys.stderr.flush()

"programı sonlandırır, altındaki işlemler çalışmaz"
sys. exit()
