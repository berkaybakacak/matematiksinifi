from matematik import Matematik as mat

def main():
    formüller = mat(True)
    çizgiler = "\n------------------------------\n"

    print(formüller.basamaksayısı(3751), end=çizgiler) # 4
    print(formüller.tekmi(7), end=çizgiler) # 7 % 2 = 1         -> True
    print(formüller.çiftmi(8), end=çizgiler) # 8 % 2 = 0        -> True
    print(formüller.tekmiçiftmi(18), end=çizgiler) # 18 % 2 = 0 -> Çift sayı
    print(formüller.karekökü(9), end=çizgiler) # √9 = 3.0       -> 3.0
    print(formüller.karesi(9), end=çizgiler) # 9² = 81          -> 81
    print(formüller.küpü(9), end=çizgiler) # 9³ = 729           -> 729
    print(formüller.kuvvet(5, 5), end=çizgiler) # 5⁵ = 3125     -> 3125
    print(formüller.çarpanlarıal(8), end=çizgiler) # {8, 1, 2, 4}
    print(formüller.asalmı(11), end=çizgiler) # 11 %(2...10) = 1-> True
    print(formüller.asalçarpanlarıal(27), end=çizgiler) # {3}
    print(formüller.fibonacci(1, 8), end=çizgiler) # 21
    print(formüller.faktoriyel(5), end=çizgiler) # 120
    print(formüller.ebob(18, 24), end=çizgiler) # 6
    print(formüller.ekok(18, 24), end=çizgiler) # 72
    print(formüller.armstrongmu(1634)) # True

if __name__ == "__main__":
    main()