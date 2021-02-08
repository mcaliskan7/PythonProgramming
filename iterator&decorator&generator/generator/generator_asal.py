def asal_sayi(sayi):
    i = 2

    while i < sayi:
        if sayi % i == 0:
            return False
        i += 1
    return True

def asal_generator():
    i = 2

    while True:
        if asal_sayi(i):
            yield i
        i += 1

for sayi in asal_generator():
    if sayi > 1000:
      break
    print(sayi,)
