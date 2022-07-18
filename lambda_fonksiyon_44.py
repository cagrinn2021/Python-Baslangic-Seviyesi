## az kullanilan fonksiyonlarda kullanacağız def ile sürekli calısması gerekiyor lamba tek satılrık ve bir defaya mahsustur
##map fonksiyonu var o işi daha kolay kılıyor


toplam=lambda x,y:x+y
print(toplam(2,4))

kare=lambda sayi:sayi**4
liste=[1,3,5,3,1,2,43,2,31,21,14]
sonuc=list(map(kare,liste)) ## kare yeri fonksiyonu yaziyoruz sağ tarafta ise verileri nereden alacagini söylüyoruz

print(sonuc)

##asiri kullanisli map verileri cekiyor fonksiyonu atıyor lambda tek satilrlik kod olustutruyor