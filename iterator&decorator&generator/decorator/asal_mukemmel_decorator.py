def ekstra(fonk):

    def ekstra_ozellik():
        print("Mükemmel Sayılar...")
        for sayı in range(1,1001):
            toplam = 0
            i = 1
            while (i < sayı):
                if (sayı % i == 0):
                    toplam += i
                i +=1
            if (toplam == sayı):
                print(sayı,end=" ")
        fonk()

    return ekstra_ozellik



@ekstra
def asal_sayilar():
    print("\nAsal Sayılar...")
    for sayi in range(2,1001):
        i = 2
        say = 0
        while (i < sayi):
            if (sayi % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(sayi,end=" ")

asal_sayilar()
