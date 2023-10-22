import random

# Tehtävä 11.2

'''Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
    Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
    Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat.
     Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
      Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.

       Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
        ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
        Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran
        ja tulosta autojen matkamittarilukemat.'''


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt=0, matka_kuljettu=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.matka_kuljettu = matka_kuljettu

    def aja(self, aika):
        huippunopeus = self.huippunopeus
        nopeus = random.randint(1, huippunopeus)
        self.nopeus_nyt = nopeus
        print(f"Auto ajaa: {self.nopeus_nyt} km/h.")
        print(f"{aika} tunnin päästä...")
        self.matkamittarilukema(aika)

    def matkamittarilukema(self, aika):
        kulkenut = self.nopeus_nyt * aika
        self.matka_kuljettu = kulkenut
        print(f"Matkamittarinlukema: {self.matka_kuljettu}km")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)


def main():

    sahkoAuto = Sahkoauto("ABC-15", 180, 52.5)
    polttoMoottoriAuto = Polttomoottoriauto("ACD-123", 165, 32.3)

    print("Sähköauto menee liikkeelle!\n")
    sahkoAuto.aja(3)
    print()

    print("Polttomoottoriauto menee liikkeelle!\n")
    polttoMoottoriAuto.aja(3)





main()
