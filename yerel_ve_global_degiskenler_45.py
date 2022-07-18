a="merhaba2"
def merhaba():
    a="merhaba"
    print(a)## yerel fonksiyon dışarda kullanamayız
merhaba()
print(a)

##globaldeki fonksiyonda değiştirebiliyoruz ama fonksiyondakini globelde değiştiremeyiz


print("global degisim ")
def anahtar():
    global a
    a="merhaba11"


print(a)
anahtar()
print(a)