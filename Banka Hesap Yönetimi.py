class Hesap:

    def __init__(self,hesap_sahibinin_adi, hesap_numarasi, bakiye = 0) :
        self.hesap_sahibinin_adi = hesap_sahibinin_adi
        self.hesap_numarasi = hesap_numarasi
        self.__bakiye = bakiye

    def get_bakiye(self):
        return self.__bakiye
    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} Tl yatırıldı. Güncel bakiye: {self.__bakiye} TL")
        else:
            print("Geçersiz miktar")

    def para_cek(self, miktar):
        if 0 < miktar <= self.__bakiye :
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel bakiye: {self.__bakiye} TL")
        else:
            print("Yetersiz bakiye")
    def bakiye_goster(self):
        print(f"Hesaptaki bakiye: {self.__bakiye} TL")

class Vadesiz_Hesap(Hesap):
    pass

class Vadeli_Hesap(Hesap):
    def faiz_hesapla(self,faiz_orani,gun):
        bakiye = self.get_bakiye()
        faiz = (bakiye/ 100) * (faiz_orani/365) * gun
        print(f"{gun} gün için hesaplanan faiz: {faiz} TL")
        return faiz
    def para_cek(self, miktar):
        print("Vadeli hesaptan para çekiliyor.")
        super().para_cek(miktar)

hesap1 = Vadesiz_Hesap( "Ali Kılıç", "123456789", 3500)
hesap1.bakiye_goster()
hesap1.para_yatir(300)
hesap1.para_cek(100)

Vadeli_Hesap = Vadeli_Hesap("Meryem Yılmaz", "345678912", 7000)
Vadeli_Hesap.faiz_hesapla(0.3,60)
Vadeli_Hesap.para_cek(900)