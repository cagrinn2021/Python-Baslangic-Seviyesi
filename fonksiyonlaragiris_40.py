# def toplam():
#     sonuc=10+11
#     print(sonuc)
#
# toplam()

# def toplam(x,y):
#     sonuc=x+y
#     print(sonuc)
# toplam(31,32)
# x=44
# toplam(x,22)
def usalma(x,y):
    sonuc=x**y
    print(sonuc)

usalma(9,6)
print(pow(9,6))

def resitlikhesapla(x):
    yas=int(2022-x)
    if yas>=18:
        print("Yasiniz {}  reşitsinizdir".format(yas))
    else:
        print("resit degilisiniz {}".format(yas))

kullanicidogum=int(input("lutfen yasinizi giriniz"))
resitlikhesapla(kullanicidogum)