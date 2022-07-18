# #dir yapının içindeki methodları gösterir
# print(dir(list))##listin methodlarını görmek istiyoruz
# ##divmod kalan kismi yazdirir
# print(divmod(10,6))## 1,4 cıktısı veriyor 1 kere iicinde var ve 4 kalan
#
# #x="Cagri esen"
# print(*enumerate(x))##her bir degere karşı gelen object numarası veriyor listelemek istiyorsak * koy
# for i in enumerate(x):
#     print(i)
#
# #help(dir)## ne işe yaradığını gösteriyor
#
# #input() # her zaman string tipi veriyi alir rakamlari cevirmeyi unutma
# #len fonksiyonu listenin uzanlığı ##stringde tüm kelimeleri sayar listede listedei ürünleri sayar
#
# print("ankara","istanbul","izmir",sep="--",end="...\n")
# ##sep komutu geçişlerin arasina ekleme yapmak için end sonuna koymak için
# print(list(range(1,101,2)))

#reserverd tersten yazar
y=["a","b","c",14]
print(list(reversed(y))) ##ters yazdirir :: çift noktada ters yapar

x=[1,2,3,4]
y=["a","b","c","d"]
print(*zip(y,x))