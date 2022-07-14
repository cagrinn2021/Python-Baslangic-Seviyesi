# # # # # x="SelAm CicEQ MerhAbA"
# # # # # y=x.lower()
# # # # # print(y)
# # # # # z=x.upper()
# # # # # print(z)
# # # # # c=x.islower()
# # # # # d=x.isupper()
# # # # # print(c)
# # # # # print(d)
# # # # # e=x.isnumeric()
# # # # # print(e)
# # # # #
# # # # # stringleri kontrol etmek için kullanılır
# # # # x="sdfsfs"
# # # # y="mEhaba?"
# # # # a=x.isalnum()
# # # # print(a)
# # # # a=y.isalnum() ##sadece metin ve sayi varmi diye bakıyoruz
# # # # print(a)
# # #
# # # x="anlasilir yapi"
# # # y=x.capitalize()
# # # z=x.title()
# # # print(y+" "+ z)
# # # y=x.count("a")
# # # print(y)
# #
# # x= "   Anlasilir Matematik    "
# # y=x.strip(" ") #soldan ve sağdan tarama yapar ilk gördüğünü alır sadece
# # print(y)
# # y=y.lstrip("Anlas") # soldan tarama yapar
# # print(y)
# # y=y.rstrip(("tik"))
# # print(y) ## güzelmiş heee :DD
#
# x="Merhaba Ben Cagri ESEn, Naber, iyiyim Sen, Peki abla"
# y=x.split(("i"))
# print(y)
#
# y="i".join((y))
# print(y)
#
# y=x.find(("Benxxx"))
# print(y) ## başlangıç indexini geri döndürüyor eğer bulamazsa -1 döndürür
# y=x.replace("e","AAA") # #soldaki yerine sağdakini koyuyor
# print(y)

ad="cagri"
soyad="esen"
gorevi="coder"
bilgi=[ad,soyad,gorevi]
print("Kişinin adı:{}, Soyadı:{}, Gorevi=:{}".format(bilgi[0],bilgi[1],bilgi[2]))