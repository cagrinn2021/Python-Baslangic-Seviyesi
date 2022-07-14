# kullaniciadi=input(" kullanici adi girin")
# kullanicisifresi=input(" kullanici sifresi giriniz")
#
# dataadi="cagriiesen"
# datasifresi="Yemek123!"
#
# if kullaniciadi==dataadi and kullanicisifresi==datasifresi:
#     print("Merhaba {} Hoşgeldin sisteme".format(dataadi))
# elif kullaniciadi!=dataadi and kullanicisifresi==datasifresi:
#     print("Kullanici adiniz yanlis lütfen dogru giriniz {}".format(kullaniciadi))
# elif kullaniciadi==dataadi and kullanicisifresi!=datasifresi:
#     print("sifren yanlis abicim düzelt gel {}".format(dataadi))
# else:
#     print("ikiside yanlis ")

print("merhaba, vucut kitle endeksi hesaplama uygulamasina hosgeldiniz")
boy=int(input("boyunuzu cm cinsinden gir"))
kilo=int(input("kilonuzu kg cinsinden girin"))
endeks=round(((kilo)/(boy/100)**2),9)
print(endeks)
if endeks<=18.5:
    print("vucut kitle endeksiniz {}, düşük kilolu".format(endeks))
elif endeks>18.5 and endeks<=24.9:
    print("vucut kitle endeksiniz {}, normal kilolu".format(endeks))
elif endeks>=25 and endeks<=29.9:
    print("vucut kitle endeksiniz {}, fazla kilolu".format(endeks))
elif endeks>=30 and endeks<=45:
    print("obezsiniz, lütfen en kısa sürede veriniz")
else:
    print("düzgün degerler giriniz")