#listelere göre daha hızlıdır yazilimda içerisinde bir şey değişmicek ise demet kullanilmali
#veriler saklanir ve değişmez içerisi  index 0 dan başlanır iç içe kullanım vardır

liste =["Ahmet",23]
print(type(liste))

demet=("Ahmet",42)
print(type(demet))

demet2=("cagri")
print(type(demet)) ## visualda  tek değişken varsa str olarak gösteriyordu bende ikiside tuple oldu
liste[0]="sukran"
print(liste)
#demet[1]="Cagri" tuple is not change
print(demet[0])


