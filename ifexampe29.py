name=str(input("please enter your name"))
age=int(input("please enter your age"))
egitim=str(input("please enter your education"))
egitimversus=("ilkokul","lise","ortaokul","üniversite")

if egitim not in egitimversus:
    print("enter your valid====(ilkokul,lise,ortaokul,üniversite")
elif (age>=18) and (egitim=="lise" or egitim=="üniversite"):
    print("Ehliyet şartlarını karşılamaktasınız")
else:
    print("ehliyet şartları gerçekleşmiyor")
