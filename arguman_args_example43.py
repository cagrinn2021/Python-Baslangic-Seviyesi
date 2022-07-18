def ortalama(*args):
    """

    :type args: object
    """
    sonuc=0
    for i in args:
        sonuc=sonuc+i
        sonuc2=float(sonuc/len(args))
    return round(sonuc2,4)


print(ortalama(15,10,13.412312313451,14.1,33.53))


def ortalamaa(*args,x):
    sonuc=0
    for i in args:
        sonuc=sonuc+i
        sonuc2=sonuc/len(args)
    if sonuc2>x:
        print("{} sayisi ortalamadan kücüktür".format(x))
    else:
        print("{} sayisi ortalamadan büyüktür".format(x))
    return sonuc2

ortalamaa(44,45,x=44)


def araba(**kwargs):
    for key,value in kwargs.items():
        if value>250000:
            print("{} marka araba biraz pahalı".format(key))
        else:
            print("{} marka araba biraz ucuz".format(key))

araba(bmw=500000,audi=10000000,mercedees=1000,ford=2501)

##sevdim ben bunu cok lazim olur burası 