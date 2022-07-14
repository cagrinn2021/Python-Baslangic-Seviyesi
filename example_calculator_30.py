print("""
1=toplama
2=çıkarma
3=çarpma
4=bölme
5=üs alma
q=çıkış
""")
islem=input("lütfen işlemi seçin")
if islem=="1":
    sayi1=float(input("1.sayiyi girin"))
    sayi2 = float(input("2.sayiyi girin"))
    sonuc=sayi1+sayi2
    print(sonuc)
elif islem=="2":
    sayi1 = float(input("1.sayiyi girin"))
    sayi2 = float(input("2.sayiyi girin"))
    sonuc = sayi1 - sayi2
elif islem=="3":
    sayi1 = float(input("1.sayiyi girin"))
    sayi2 = float(input("2.sayiyi girin"))
    sonuc = sayi1 * sayi2
elif islem=="4":
    sayi1 = float(input("bölümü girin"))
    sayi2 = float(input("böleni girin"))
    sonuc = sayi1 / sayi2
elif islem=="2":
    sayi1 = float(input("sayiyi girin"))
    sayi2 = float(input("üssü girin"))
    sonuc = sayi1 ** sayi2
