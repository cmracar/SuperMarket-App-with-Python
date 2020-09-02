import sqlite3
import time

class Urun():
    def __init__(self,urun_adi,urun_kodu,urun_fiyati,urun_adedi):
        self.urun_adi = urun_adi
        self.urun_kodu = urun_kodu
        self.urun_fiyati = urun_fiyati
        self.urun_adedi = urun_adedi

    def __str__(self):
        return "Ürün Adı : {}\nÜrün Kodu : {}\nÜrün Fiyatı : {} ₺\nÜrün Adedi : {} Adet".format(self.urun_adi,self.urun_kodu,self.urun_fiyati,self.urun_adedi)

class Depo():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("supermarket.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS Market (urun_adi TEXT,urun_kodu TEXT,urun_fiyati INT,urun_adedi INT)"

        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()

    def urunleri_listele(self):
        sorgu = "SELECT * FROM Market"

        self.cursor.execute(sorgu)

        Urunler = self.cursor.fetchall()
        if (len(Urunler) == 0):
            time.sleep(2)
            print("Stoklarda Hiç Ürün Yok !")
        else:
            for i in Urunler:
                urun = Urun(i[0],i[1],i[2],i[3])
                print(urun)
                print()

    def urun_sorgula(self,urun_kodu):
        sorgu = "Select * From Market where urun_kodu = ?"

        self.cursor.execute(sorgu,(urun_kodu,))
        Urunler = self.cursor.fetchall()

        if (len(Urunler) == 0):
            print("Bu İsimde Bir Ürün Bulunmuyor !")
        else:
            urun = Urun(Urunler[0][0],Urunler[0][1],Urunler[0][2],Urunler[0][3])
            print(urun)

    def urun_ekle(self,urun):
        sorgu = "Insert into Market Values(?,?,?,?)"

        self.cursor.execute(sorgu,(urun.urun_adi,urun.urun_kodu,urun.urun_fiyati,urun.urun_adedi))
        self.baglanti.commit()

    def urun_kaldir(self,urun_kodu):
        sorgu1 = "Select * From Market where urun_kodu = ?"
        sorgu = "Delete From Market where urun_kodu = ?"

        self.cursor.execute(sorgu1,(urun_kodu,))
        Urunler = self.cursor.fetchall()

        if (len(Urunler) == 0):
            print("Bu Koda Sahip Bir Ürün Bulunmuyor !")
        else:

            self.cursor.execute(sorgu, (urun_kodu,))

            self.baglanti.commit()
            print("Ürün Başarıyla Kaldırıldı !")


















