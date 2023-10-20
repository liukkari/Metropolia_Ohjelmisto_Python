# Tehtävä 9.1

'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
    tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
    joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
    Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
    Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
    Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.'''


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus_nyt=0, matka_kuljettu=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = nopeus_nyt
        self.matka_kuljettu = matka_kuljettu


def main():
  uusi_auto = Auto("ABC-123", 142)

  print(f"Uuden auton rekisteritunnus on: {uusi_auto.rekisteritunnus} ja huippunopeus: {uusi_auto.huippunopeus} km/h.\n"
        f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h ja"
        f" kuljettu matka eteenpäin: {uusi_auto.matka_kuljettu}km.")


main()
