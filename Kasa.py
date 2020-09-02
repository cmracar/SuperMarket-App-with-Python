from MarketStok import *

class Kasa:
    def __init__(self):
        self.baglanti_olustur()
        self.toplam = 0

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("supermarket.db")

        self.cursor = self.baglanti.cursor()

    def urun_satis(self,urun_kodu):
        sorgu = "Select * From Market where urun_kodu = ?"

        self.cursor.execute(sorgu, (urun_kodu,))
        liste = self.cursor.fetchall()
        for i in liste:
            print("{} - {} Türk Lirası".format(i[0],i[2]))
            self.toplam +=i[2]
            adet = i[3]-1
            guncelle = "UPDATE Market SET urun_adedi=? where urun_kodu=?"
            self.cursor.execute(guncelle,(adet,urun_kodu,))
            self.baglanti.commit()

    def urun_iade(self,urun_kodu):
        sorgu = "Select * From Market where urun_kodu = ?"

        self.cursor.execute(sorgu, (urun_kodu,))
        liste = self.cursor.fetchall()
        for i in liste:
            print("İade Edilen : {} - {} Türk Lirası".format(i[0], i[2]))
            self.toplam -= i[2]
            adet = i[3] + 1
            guncelle = "UPDATE Market SET urun_adedi=? where urun_kodu=?"
            self.cursor.execute(guncelle, (adet, urun_kodu,))
            self.baglanti.commit()



