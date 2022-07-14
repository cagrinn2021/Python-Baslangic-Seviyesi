liste=[1,2,3,3,4,11,23,51,23,41,3.1234]
liste.append("xD")
print(liste)
liste.insert(1,3215)
print(liste)
liste.remove(2)#belirlenen değeri bulur ve siler
print(liste)
liste.pop()#eğer içerisine veri girilmezse en sonuncuyu siler yoksa girileni siler
liste.pop(0)#bulunan değerin endeksdekini siler
print(liste)
liste2=liste.copy() # kopyalama için kullanilir[
print(liste2)
liste3= ["a","b","c","d"]
liste3.extend(liste2) # iki listeyi birleştiriyoruz
print(liste3)
liste3+=liste # dediğimizde yine iki liste birleşmektedir
print(liste3)

liste.sort()##kücükten büyüğe
print(liste)

#count methodu kac adet veri bulunduğunu geri döndürür
print(liste.count(3))
liste.sort(reverse=True)
print(liste)
liste.reverse()
print(liste)
liste.clear()
print(liste )