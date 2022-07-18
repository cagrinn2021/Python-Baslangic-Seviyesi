# # break istediğimiz noktada kesebilmemize yarar
# #continue bazı adımları atlayıp adımlara devam etmemiz gerekmektedir bunun için kullanılır
#
# x="Cagri Esen"
# for i in x:
#     if i==" ":
#         break ## bosluğu gördükten sonra koşulu bozuyor for döngüsündeki bu yüzden bosluga kadar olan hepsini yazıyor
#     print(i)
#
# for i in x:
#     if i==" ":
#         continue ##boşluğu görünce atlıcak ve devam edecek
#
#     print(i)


##kullanicidan belli bir sayida veri almak

sayac=2

for i in range(0,3):
    kullaniciadi=input("kullanici adininizi giriniz ")
    kullanicisifresi=input("kullanici sifrenizi giriniz ")
    SistemKullanici="cagriesenn"
    SistemSifre="12345"

    if kullaniciadi==SistemKullanici and kullanicisifresi==kullanicisifresi:
        print("Giris basarili...")
        break
    elif (kullaniciadi!=SistemKullanici or kullanicisifresi!=SistemSifre) and sayac!=0:
        print("hatali giris tekrar deneyiniz...\n kalan giris hakkiniz {}".format(sayac))
        sayac=sayac-1
    else:
        print("3 kere hatali girdiniz sistem kapatiliyor...")

##break ile döngüyü istediğim yerde kapattim