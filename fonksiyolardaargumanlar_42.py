# def toplam(x,y,z=0):
#     sonuc=x+y+z
#     return sonuc
# print(toplam(4,5,11)) ## 3. de vermesek olur

##sinirssiz değişken göndermemiz gerekiyorsa


def toplamm(*x):
    return x

def toplam(*x):
    sayac=0
    for i in x:
        print(i)
        sayac=sayac+i

    return sayac

print(toplamm(5,2,1,4))
print(toplam(1,4,2,4,5,5754534))

def isim(*x):
    return "merhaba benim adim {}, soy adım {}.".format(x[0],x[1])

print(isim("123",41))

##yukarisi sinirsiz arguman lazım ise tek yildiz varsa, keyfi argüman kitaplarda agrs olarak görürüz
##şimdi argüman yapısı lazım olursa ** yıldız kullancaz kitaplarda **kwarg olarak geçer

def kalori(**meyve):
    return meyve
print(kalori(Elma=45,armut=50,sebze=30))

def kimlik(**bilgi):
    for i in bilgi.items():
        print(i)
    for i in bilgi.keys():
        print(i)
    for i in bilgi.values():
        print(i)
kimlik(Ad="Cagri",Soyad="Esen",Yas=26)