class kare_al():
    def __init__(self,max):
        self.sayi = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi <= self.max:
            sonuc = self.sayi ** 2
            self.sayi += 1
            return sonuc
        else:
            self.sayi = 1
            raise StopIteration

kareal = kare_al(45)

for i in kareal:
    print(i,end=" ")
