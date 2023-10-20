# Tehtävä 9.2

'''Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
    Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
    Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.

    Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
    Tulosta tämän jälkeen auton nopeus.
    Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
    Kuljettua matkaa ei tarvitse vielä päivittää.'''


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


def main():
    uusi_auto = Auto("ABC-123", 142)

    print(f"Uuden auton rekisteritunnus on: {uusi_auto.rekisteritunnus} ja huippunopeus: {uusi_auto.huippunopeus} km/h.\n"
        f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h ja"
        f" kuljettu matka eteenpäin: {uusi_auto.matka_kuljettu}km.\n")

    print("Auto kiihdyttää +30 km/h!")
    uusi_auto.kiihdyta(30)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h.\n")

    print("Auto kiihdyttää +70 km/h!")
    uusi_auto.kiihdyta(70)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h.\n")

    print("Auto kiihdyttää +50 km/h!")
    uusi_auto.kiihdyta(50)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h.\n")

    print("Auto hätäjarruttaa -200 km/h!")
    uusi_auto.kiihdyta(-200)
    print(f"Auton tämän hetkinen nopeus: {uusi_auto.nopeus_nyt} km/h.")


main()
