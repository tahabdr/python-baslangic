vt={}
def ekle():
   print("Ad soyad ve numara ekle")
   ad= input("Ad-Soyad: ")
   numara= int(input("Numara: "))
   vt[ad]= numara
   print(vt)

def sil():
   ad= input("silmek istediğiniz ismi yazın: ")
   if ad in vt:
      del vt[ad]
      print("Başarı ile silindi")
      print(vt)
   else:
      print(ad,"Bulunamadı")

def ara():
    arananKelime= input("Aramak İstediğiniz Kişi: ")
    if arananKelime in vt:
        print(arananKelime,vt[arananKelime])
    else:
        print(arananKelime," Bulunamadı")

def listele():
    for i in vt:
        print(i,vt[i])

while True:
   print("Telefon Rehberi")
   print("1 - Ekle")
   print("2 - Sil")
   print("3 - Ara")
   print("4 - Listele")
   print("5 - Çıkış")
   menusec= int(input("Seçim Yapınız : "))
   if menusec==1:
      ekle()
   elif menusec==2:
      sil()
   elif menusec==3:
      ara()
   elif menusec==4:
       listele()     
   elif menusec==5:
       break
   else:
      print("1-5 arası sayı giriniz")

