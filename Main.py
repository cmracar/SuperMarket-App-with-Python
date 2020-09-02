from MarketStok import *
from Kasa import Kasa

depo = Depo()
kasa = Kasa()

def entrance():
    while (True):
        print("""

        * * * * * * * Welcome to SuperMarket App * * * * * * * 

         1 - ) Depo İşlemleri
         2 - ) Yazar Kasa İşlemleri
         3 - ) Çıkış


        """)
        islem = input("İşlemi Seçiniz : ")

        if int(islem) == 1:
            print("Depo İşlemlerine Bağlanıyorsunuz ...")
            time.sleep(2)
            depo_gorsel()
        elif int(islem) == 2:
            print("Yazar Kasa İşlemlerine Bağlanıyorsunuz ...")
            time.sleep(2)
            kasa_gorsel()
        elif int(islem) == 3:
            print("Çıkış Yapılıyor ...")
            time.sleep(1)
            break
        else:
            print("Geçersiz İşlem Girdiniz !")
def depo_gorsel():
    while(True):
        print("""

                * * * * * * * SuperMarket Depo İşlemleri * * * * * * * 

                 1 - ) Yeni Ürün Ekle
                 2 - ) Ürünleri Listele
                 3 - ) Ürün Sorgula(Ürün Kodu İle)
                 4 - ) Ürünü Kaldır
                 5 - ) Çıkış


                    """)
        islem = input("İşlemi Seçiniz : ")

        if int(islem) == 1:
            adi = input("Ürün Adını Girin : ")
            kodu = input("Ürün Kodunu Girin : ")
            fiyati = input("Ürün Fiyatını Girin : ")
            adedi = input("Ürün Adedini Girin : ")

            yeni_urun = Urun(adi, kodu, fiyati, adedi)
            print("Yeni Ürün Ekleniyor ...")
            time.sleep(2)
            depo.urun_ekle(yeni_urun)
            print("Ürün Eklendi !")
        elif int(islem) == 2:
            depo.urunleri_listele()

        elif int(islem) == 3:
            islem = input("Aranan Ürünün Kodu : ")
            depo.urun_sorgula(islem)

        elif int(islem) == 4:
            islem = input("Kaldırılacak Ürünün Ürün Kodunu Girin : ")
            time.sleep(3)
            depo.urun_kaldir(islem)
        elif int(islem) == 5:
            print("Çıkış Yapılıyor...")
            time.sleep(2)
            break
        else:
            print("Geçersiz İşlem !")
def kasa_gorsel():

    while (True):
        print("""

                    * * * * * * * SuperMarket Yazar Kasa İşlemleri * * * * * * * 

                     1 - ) Ürün Satış
                     2 - ) Ürün İade
                     3 - ) Çıkış

                                """)
        islem = input("İşlemi Seçiniz : ")

        if int(islem) == 1:
            print("Satış İşlemini Sonlandırmak ve Toplam Ücreti Yansıtmak İçin Kod Giriş Kısmına Yalnızca 'q' / 'Q' Giriniz !")

            while(True):
                kod = input("|||||000")
                kasa.urun_satis(kod)

                if kod.upper()=="Q":
                    print("Toplam Tutar : {}".format(kasa.toplam))
                    input("\nÖdeme İşlemini Bitirmek İçin Bir Tuşa Basın ...\n")
                    break


        elif int(islem) == 2:
            while (True):
                islem = input("İade Edilecek Ürün Kodu : ")
                kasa.urun_iade(islem)

                if islem.upper() == "Q":
                    print("Toplam Tutar : {}".format(kasa.toplam))
                    input("\nGeri Ödeme İşlemini Bitirmek İçin Bir Tuşa Basın ...\n")
                    break

        elif int(islem) == 3:
            print("Çıkış Yapılıyor...")
            time.sleep(2)
            break

        else:
            print("Geçersiz İşlem !")

entrance()







