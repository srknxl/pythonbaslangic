sayi = int(input("faktöriyelini bulmak istediniz sayıyı giriniz: "))
fac = 1
for i in range(1,sayi+1):
    fac = i * fac
print(fac)
