import random

# Tehtävä 10.4

'''Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka,
    jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
    Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne
    ominaisuuksille arvoiksi.
    Luokassa on seuraavat metodit:

    tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli
    arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
    tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
    kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli
    se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

    Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
    Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
    Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
    jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
    Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein
    sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.'''


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt=0, matka_kuljettu=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.matka_kuljettu = matka_kuljettu

    def kiihdyta(self, nopeuden_muutos):
        if nopeuden_muutos > 0:
            self.nopeus_nyt += nopeuden_muutos
            if self.nopeus_nyt > self.huippunopeus:
                self.nopeus_nyt = self.huippunopeus
        else:
            self.nopeus_nyt += nopeuden_muutos
            if self.nopeus_nyt < 0:
                self.nopeus_nyt = 0

    def kulje(self, tuntimaara):
        lisaa_matkaa = self.nopeus_nyt * tuntimaara
        self.matka_kuljettu += lisaa_matkaa


class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_kilometreina, kilpailijat):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_kilometreina = pituus_kilometreina
        self.autoja = kilpailijat

    def tunti_kuluu(self):
        kilpa_autot = self.autoja
        for auto in kilpa_autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        kilpa_autot = self.autoja
        print("------------------------------------------------------------------------------------------------")
        for auto in kilpa_autot:
            print(f"|Auto: {auto.rekisteritunnus:6s} | Huippunopeus: {auto.huippunopeus:3d} km/h | "
                  f"Hetkellinen Nopeus: {auto.nopeus_nyt:3d} km/h | Kuljettu Matka {auto.matka_kuljettu:5d}km |")
            print("------------------------------------------------------------------------------------------------")

    def kilpailu_ohi(self):
        kilpa_autot = self.autoja
        maali = self.pituus_kilometreina
        for auto in kilpa_autot:
            auto_ajanut = auto.matka_kuljettu
            if auto_ajanut >= maali:
                return True


def main():
    lista_autoja = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        kilpa_auto = Auto(rekisteritunnus, huippunopeus)
        lista_autoja.append(kilpa_auto)

    kilpailu = Kilpailu("Suuri romuralli", 8000, lista_autoja)

    ohi = True
    while ohi:
        for i in range(10):
            kilpailu.tunti_kuluu()
            if kilpailu.kilpailu_ohi():
                ohi = False
                break
        print()
        kilpailu.tulosta_tilanne()

    print("\t\t\t\t\t\t\t\tResult")
    for voittaja in kilpailu.autoja:
        if voittaja.matka_kuljettu >= 8000:
            print("\t\t\t\t\t\t----------------------")
            print(f"\t\t\t\t\t\t*|Voittaja on: {voittaja.rekisteritunnus}|*")
            print("\t\t\t\t\t\t----------------------")
            break


main()
