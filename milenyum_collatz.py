i = 2

while True:
    sayi = i
    while True:
        if sayi % 2 != 0:
            sayi = sayi * 3 + 1
        else:
            sayi = sayi / 2

        if sayi == 1:
            break
    print(i)

    i += 1
