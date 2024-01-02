to_do_list = []

def gorev_ekle():
    gorev = str(input("Bir Görev Girin : "))
    to_do_list.append(gorev)
    print("Görev Girildi.")

def gorev_goster():
    print("---Görevler---")
    for gorev in to_do_list:
        print(gorev)

def gorev_sil():
    gorev = int(input("Kaçıncı görevi sileceksin : "))
    to_do_list.remove(to_do_list[gorev-1])
    print(f"{gorev} .cı görev silindi")

def cikis():
    exit()
    
#ana program
while True:
    print("\n To Do List Uygulamasına Hoş Geldiniz..")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çıkış")
    secim = int(input("\nBir Seçim Yapınız ( 1/2/3/4 ) : "))

    if secim == 1 :
        gorev_ekle()
    elif secim == 2 :
        gorev_goster()
    elif secim == 3 :
        gorev_sil()
    elif secim == 4 :
        cikis()
    else :
        print("1-4 arası seçim yapmadınız!")

