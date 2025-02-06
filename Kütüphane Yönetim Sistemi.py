class Kitap:
    def __init__(self, kitap_adi, yazar, sayfa_sayisi, isbn):
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.isbn = isbn

    def __str__(self):
        return f"{self.kitap_adi} - {self.yazar}/ {self.sayfa_sayisi} sayfa (ISBN: {self.isbn})"
class Kutuphane():

    def __init__(self):
        self.__kitaplar = {}
    def kitap_ekle(self, kitap):

        if kitap.isbn in self.__kitaplar:
            raise Exception(f"'{kitap.kitap_adi}' kitabı zaten kütüphanede mevcut!")
        else:
            self.__kitaplar[kitap.isbn] = kitap
            print(f"{kitap.kitap_adi} kütüphaneye eklendi")

    def kitap_sil(self,isbn):
        if isbn in self.__kitaplar:
            kitap = self.__kitaplar.pop(isbn)
            print(f"{kitap.kitap_adi} kütüphaneden silindi." )
        else:
            raise Exception(f"ISBN: {isbn} numaralı kitap kütüphanede bulunamadı.")

    def tum_kitaplari_goster(self):
        if not self.__kitaplar:
            print("Kütüphanede hiç kitap bulunmamaktadır.")
        else:
            print("Kütüphanedeki kitaplar:")
            for kitap in self.__kitaplar.values():
                print(kitap)
try:
    Kutuphane = Kutuphane()
    kitap1 = Kitap("Şeker Portakalı", "José Mauro de Vasconcelos", 200, 679)
    kitap2 = Kitap("Tutunamayanlar", "Oğuz Atay", 700, 345)
    kitap3 = Kitap("Martin Eden", "Jack London", 480, 213)
    kitap4 = Kitap("Martin Eden", "Jack London", 480, 213 )

    Kutuphane.kitap_ekle(kitap1)
    Kutuphane.kitap_ekle(kitap2)
    Kutuphane.kitap_ekle(kitap3)
    Kutuphane.kitap_ekle(kitap4)
except Exception as e:
    print(f"Hata: {e}")

    Kutuphane.tum_kitaplari_goster()

try:
    Kutuphane.kitap_sil(679)
    Kutuphane.kitap_sil(999)
except Exception as e:
    print(f"Hata: {e}")

    Kutuphane.tum_kitaplari_goster()



