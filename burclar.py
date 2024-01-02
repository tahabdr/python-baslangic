#Ay giriniz
ay = int(input("Kaçıncı Ayda Doğdunuz? 1...12 "))
#Gün giriniz
gun = int(input("Kaçıncı Günde Doğdunuz? 1...31 "))

#eğer 23 kasım-22 aralık arasında ise Yay Burcudur
if (ay==11 and gun>=23) or (ay==12 and gun <=22):
        print("Yay Burcusunuz")
    #aksi takdirde eğer 23 aralık-20 ocak arasında ise Oğlak Burcudur
elif (ay==12 and gun>=23) or (ay==1 and gun<=20):
        print("Oğlak Burcusunuz")
    #aksi takdirde eğer 21 ocak-19 şubat arasında ise Kova Burcudur
elif (ay==1 and gun>=21) or (ay==2 and gun<=19):
        print("Kova Burcusunuz")
    #aksi takdirde eğer 20 şubat-20 mart arasında ise Balık Burcudur
elif (ay==2 and gun>=20) or (ay==3 and gun<=20):
        print("Balık Burcusunuz")
    #aksi takdirde eğer 21 mart-20 nisan arasında ise Koç Burcudur
elif (ay==3 and gun>=21) or (ay==4 and gun<=20):
        print("Koç Burcusunuz")
#Aksi takdirde Başka Burçtur
else:
    print("Başka bir burçsunuz")