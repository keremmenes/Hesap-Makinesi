giriş="""
(1) topla
(2) çıkar
(3) çarp
(4) böl 
(5) karesini hesapla
(6) karekökünü al
(7) çıkış
"""

print(giriş)

soru=input("Yapmak istediğniz işlemin numarasını girin")

if soru==1:
    sayi1 = int(input("1. sayıyı girin"))
    sayi2 = int(input("2. sayıyı girin"))
    print(sayi1+"+"+sayi2+" = "+sayi2+sayi1)
elif soru==2:
    sayi1 = int(input("1. sayıyı girin"))
    sayi2 = int(input("2. sayıyı girin"))
    print(sayi1 + "-" + sayi2 + " = " + sayi2 - sayi1)
elif soru==3:
    sayi1 = int(input("1. sayıyı girin"))
    sayi2 = int(input("2. sayıyı girin"))
    print(sayi1 + "*" + sayi2 + " = " + sayi2 * sayi1)
elif soru==4:
    sayi1 = int(input("1. sayıyı girin"))
    sayi2 = int(input("2. sayıyı girin"))
    print(sayi1 + "/" + sayi2 + " = " + sayi2 / sayi1)
elif soru==5:
    sayi1=int(input("karesi alıncak sayıyı girin"))
    print(sayi1+"karesi = "+sayi1**2)
elif soru==6:
    sayi=int(input("karekökü alıncak sayıyı girin"))
    print(sayi+"karekökü = "+sayi**0.5)
elif soru==7:
    print("Sistemden çıkılıyor")
else:
    print("yanlış işlem aşağıdakilerden birini giriniz ",giriş)
