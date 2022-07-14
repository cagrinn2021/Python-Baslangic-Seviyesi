kullaniciadi="cagri3"
kullanicisifre="12345"

if kullanicisifre=="12345"and kullaniciadi=="cagri":
    print("giris basarili")
elif kullanicisifre=="12345" and kullaniciadi!="cagri":
    print("kullanici adi hatili")
elif kullanicisifre!="12345"and kullaniciadi=="cagri":
    print("sifreniz yanlıs")
else:
    print("ikiside yanlis abicim")