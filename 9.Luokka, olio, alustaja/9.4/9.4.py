import random

# Tehtävä 9.4

'''Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
    Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
    Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
    Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.

    Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
    Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
    Tämä tehdään kutsumalla kiihdytä-metodia.
    Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
    Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
    Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.'''


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


def main():
    lista_autoja = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        kilpa_auto = Auto(rekisteritunnus, huippunopeus)
        lista_autoja.append(kilpa_auto)

    kisa_kaynnissa = True
    while kisa_kaynnissa:
        for auto in lista_autoja:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
        for auto in lista_autoja:
            auto.kulje(1)
            if auto.matka_kuljettu >= 10000:
                kisa_kaynnissa = False
                break

    print("\t\t\t\t\t\t\t\tResult")
    print("------------------------------------------------------------------------------------------------")
    for auto in lista_autoja:
        print(f"|Auto: {auto.rekisteritunnus:6s} | Huippunopeus: {auto.huippunopeus:3d} km/h | "
              f"Hetkellinen Nopeus: {auto.nopeus_nyt:3d} km/h | Kuljettu Matka {auto.matka_kuljettu:5d}km |")
        print("------------------------------------------------------------------------------------------------")


main()
