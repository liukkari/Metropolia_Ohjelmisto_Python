# Tehtävä 11.1

'''Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
    Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
    Kirjoita luokkiin myös tarvittavat alustajat.

    Tee aliluokkiin metodi tulosta_tiedot,joka tudostaa kyseisen julkaisun kaikki tiedot.
    Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
    ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
    Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.'''


class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}.\nKirjailija: {self.kirjoittaja}.\nSivumäärä: {self.sivumaara}.\n")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}.\nPäätoimittaja: {self.paatoimittaja}.\n")


def main():
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    lehti.tulosta_tiedot()
    kirja.tulosta_tiedot()


main()
