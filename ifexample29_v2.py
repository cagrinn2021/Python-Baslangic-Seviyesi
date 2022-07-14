sayi=int(input("please enter a number"))
kontrol=sayi>0 and sayi%2==1
if kontrol==True:
    print("{} pozitif bir tek sayidir".format(sayi))
else:
    print("{} pozitif bir tek sayil değildir".format(sayi))