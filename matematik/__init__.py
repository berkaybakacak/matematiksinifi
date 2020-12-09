class Matematik:
    def __init__(self, ekranabas=False):
        self.ekranabas = ekranabas
        self.sürüm = 1.0
    
    basamaksayısı = lambda self, x: len(str(x))

    def tekmi(self, n):
        if self.ekranabas:
            print(n, "% 2 =", n%2)

        return n%2 != 0

    def çiftmi(self, n):
        if self.ekranabas:
            print(n, "% 2 =", n%2)

        return n%2 == 0

    def tekmiçiftmi(self, n):
        if self.tekmi(n):
            return "Tek sayı"
        else:
            return "Çift sayı"

    def karekökü(self, x):
        sonuç = x ** 0.5
        if self.ekranabas:
            print("√",x," = ",sonuç, sep="")
        return sonuç

    def karesi(self, x):
        sonuç = x ** 2
        if self.ekranabas:
            print(x,"² = ",sonuç,sep="")
        return sonuç

    def küpü(self, x):
        sonuç = x ** 3
        if self.ekranabas:
            print(x,"³ = ",sonuç,sep="")
        return sonuç

    def kuvvet(self, x, y):
        sonuç = x ** y
        if self.ekranabas:
            y = str(y).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
            print( x,y," = ",sonuç,sep="")
        return sonuç

    def çarpanlarıal(self, x):
        çarpanlar = set()
        for i in range(1, x+1):
            if x % i == 0:
                if self.ekranabas:
                    print(i,"x",x//i,"=",x)
                çarpanlar.add(i)
        
        return çarpanlar

    def asalmı(self, n):
        if n < 2:
            return False

        for i in range(2, n):
            kontrol = n % i
            if self.ekranabas:
                print(n, "%", i, "=", kontrol)
            if kontrol == 0:
                return False
        
        return True

    def asalçarpanlarıal(self, x):
        çarpanlar = list(self.çarpanlarıal(x))
        çarpanlar = [x for x in çarpanlar if self.asalmı(x)]
        
        if not len(çarpanlar):
            return "Ø"

        return set(çarpanlar)

    def fibonacci(self, ilk, tekrar_sayısı):
        ilksayi = ilk
        ikincisayi = ilk
        toplam = 0
        for tekrar in range(1, tekrar_sayısı + 1):
            ilksayi, ikincisayi = ikincisayi, toplam
            toplam = ilksayi + ikincisayi
            if self.ekranabas:
                print(toplam)
        
        return toplam

    def faktoriyel(self, n):
        çarpım = 1
        for i in range(çarpım, n + 1):
            çarpım = çarpım * i
            if self.ekranabas:
                print(çarpım)
        
        return çarpım

    def ebob(self, x, y):
        r = x % y
        while r != 0:
            x = y
            y = r
            r = x % y

        return y

    def ekok(self, x, y):
        return (x * y) // self.ebob(x, y)

    def armstrongmu(self, sayı):
        toplam = 0
        for rakam in str(sayı):
            toplam += int(rakam) ** len(str(sayı))
        
        if toplam == sayı:
            return True
        else:
            return False