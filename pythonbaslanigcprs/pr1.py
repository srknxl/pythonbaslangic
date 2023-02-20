import random
a = random.randint(1,20)
tahmin = int(input("tahmininizi giriniz"))

if tahmin > a:
        print("tahmininiz sayıdan daha yüksek")
if tahmin < a:
        print("tahmininiz sayıdan daha düşük")
elif tahmin == a:
        print("tebrikler tahmininiz doğru")
if a < tahmin or a > tahmin :
    tahmin2 = int(input("2. tahminizi giriniz"))
if tahmin2 > a:
        print("tahmininiz sayıdan daha yüksek")
if tahmin2 < a:
        print("tahmininiz sayıdan daha düşük")
elif tahmin2 == a:
        print("tebrikler tahmininiz doğru")
tahmin3 = int(input("3.tahmininizi giriniz"))
if tahmin3 > a:
        print("tahmininiz sayıdan daha yüksek")
if tahmin3 < a:
        print("tahmininiz sayıdan daha düşük")
elif tahmin3 == a:
        print("tebrikler tahmininiz doğru")


