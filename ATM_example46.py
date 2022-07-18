print("""\t Merhaba ESENBANK'A HOŞGELDİNİZ........
\t\t Lütfen Kartınızı Takınız....""")

veritabani={
    "AhmetHesap":{
    "isim":"Ahmet",
    "soyisim":"esen",
    "kartsifre":"1234",
    "hesapbakiye":5000,
    "kredikartborc":4200,
    "kredikartborctarihi":"20/11/2021"},
    "mehmetHesap":{
    "isim":"mehmet",
    "soyisim":"tepe",
    "kartsifre":"1234",
    "hesapbakiye":5000,
    "kredikartborc":4200,
    "kredikartborctarihi":"28/11/2021"
}}

takilankart=dict(veritabani["AhmetHesap"])
hak=2
for i in range(0,3):
    sifre=input("lütfen 4 haneli sifreinizi giriniz")
    if sifre==takilankart.get("kartsifre"):
        print("""Merhaba hoşgeldiniz SAyın {} {}""".format(takilankart.get("isim"),takilankart.get("soyisim")))
        sec=input("""lütfen yapmak istediginiz işlemi seçiniz
        [1] Bakiye Sorgulama
        [2] Kredi Kart borcu
        [3] para cekme
        [4] para yatırma
        [Q] çıkış\n""")
        break
    elif sifre!=takilankart.get("kartsifre") and hak!=0:
        print("hatali sifre girdiniz kalan hakkiniz {}".format(hak))
        hak=hak-1
    elif sifre!=takilankart.get("kartsifre") and hak==0:
        print("sifrenizi 3 kere yanlis girdiiniz ve kartiniz bloke olmustur\n en Yakın subemize basvuruunuz")
        exit()
if sec=="1":
    print("Hesap bakiyeniz = {}".format(takilankart.get("hesapbakiye")))
elif sec=="2":
    print("Kredi karti borcunuz = {} son ödeme tarihi ise = {}".format(takilankart.get("kredikartborc"),takilankart.get("kredikartborctarihi")))
elif sec=="3":
    cekmekistenilen=int(input("cekmek istediginiz tutari giriniz"))
    if takilankart.get("hesapbakiye")<cekmekistenilen:
        print("yetersiz bakiye")
    else:
        print("Lutfen paranizi kontrol ederek aliniz")
        yenibakiye=takilankart.get("hesapbakiye")-cekmekistenilen
        print("yeni bakiyeniz {}TL".format(yenibakiye))
elif sec=="4":
    yatirilanpara=int(input("yatiricak tutari giriniz"))
    print("paraniz yatirilmistir")
    yatirilanyeni=takilankart.get("hesapbakiye")+yatirilanpara
    print("yeni bakiyeniz {}".format(yatirilanyeni))

elif sec=="Q" or sec=="q":
    print("Teşekkür eder iyi günler")
    exit()
else:
    print("lütfen geçerli bir değer giriniz")
    help(set)

