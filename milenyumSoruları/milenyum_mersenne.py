i = 2
while True:
    sayi = 2 ** i - 1

    prime = 1
    for j in range(2,sayi):
        if sayi % j == 0:
            prime = 0
            break

    if prime == 1:
        print(i,"found:",sayi)

    i += 1
