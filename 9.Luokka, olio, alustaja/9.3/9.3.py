# Tehtävä 9.3

'''Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
    Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
    Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
    Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.'''


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
    uusi_auto = Auto("ABC-123", 142)

    print(f"Uuden auton rekisteritunnus on: {uusi_auto.rekisteritunnus} ja huippunopeus: {uusi_auto.huippunopeus} km/h.\n"
        f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h ja"
        f" kuljettu matka eteenpäin: {uusi_auto.matka_kuljettu}km.")
    print()

    print("Auto kiihdyttää +30 km/h!")
    uusi_auto.kiihdyta(30)
    uusi_auto.kulje(1.5)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h ja"
          f" kuljettu matka eteenpäin: {uusi_auto.matka_kuljettu}km.\n")

    print("Auto kiihdyttää +70 km/h!")
    uusi_auto.kiihdyta(70)
    uusi_auto.kulje(1.5)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h ja"
          f" kuljettu matka eteenpäin: {uusi_auto.matka_kuljettu}km.\n")

    print("Auto kiihdyttää +50 km/h!")
    uusi_auto.kiihdyta(50)
    uusi_auto.kulje(1.5)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h ja"
          f" kuljettu matka eteenpäin: {uusi_auto.matka_kuljettu}km.\n")

    print("Auto hätäjarruttaa -200 km/h!")
    uusi_auto.kiihdyta(-200)
    uusi_auto.kulje(1.5)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h ja"
          f" kuljettu matka eteenpäin: {uusi_auto.matka_kuljettu}km.")


main()
