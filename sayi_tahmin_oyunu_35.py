sayi=25
hak=10
while hak>0:
    tahmin=int(input("pozitif bir tam sayi giriniz"))
    if tahmin<0:
        print("Pozitif tam sayi giriniz")
        continue
    if sayi==tahmin:
        print("Tebrikler doğru bildiniz")
        break
    elif sayi>tahmin:
        print("Yukari  = Kalan hakkiniz {}".format(hak-1))
    else:
        print("Asagiya = Kalan hakkiniz {}".format(hak-1))
    hak = hak - 1
if hak==0:
    print("Hakkiniz bitmiştir kapatiliyor...")