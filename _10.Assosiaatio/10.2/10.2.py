import random

# Tehtävä 10.2

'''Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
    Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
    Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.

    Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
    Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.'''


class Hissi:
    def __init__(self, alin_kerros=1, ylin_kerros=5):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen = alin_kerros

    def siirry_kerrokseen(self, kerros):

        nykyinen_kerros = self.nykyinen
        if nykyinen_kerros == kerros:
            print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
        elif kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print(f"Valitsemaasi kerrosta ei löydy välillä {self.alin_kerros} - {self.ylin_kerros}. Hissi ei liiku.\n")
        else:
            print(f"Olemme kerroksessa {nykyinen_kerros}.")
            print(f"Siirrymme kerrokseen {kerros}.\n")
            if kerros < nykyinen_kerros:
                while kerros < nykyinen_kerros:
                    nykyinen_kerros = self.kerros_alas()
            elif kerros > nykyinen_kerros:
                while kerros > nykyinen_kerros:
                    nykyinen_kerros = self.kerros_ylos()

    def kerros_ylos(self):
        self.nykyinen += 1
        nykyinen_kerros = self.nykyinen
        print(f"Kerros {nykyinen_kerros}.")

        return nykyinen_kerros

    def kerros_alas(self):
        self.nykyinen -= 1
        nykyinen_kerros = self.nykyinen
        print(f"Kerros {nykyinen_kerros}.")

        return nykyinen_kerros


class Talo:
    def __init__(self, hisseja):
        self.hisseja = []
        for i in range(hisseja):
            hissi = Hissi()
            self.hisseja.append(hissi)

    def aja_hissia(self, hissinumero, matka):
        hissi = self.hisseja[hissinumero - 1]
        hissi.siirry_kerrokseen(matka)


def main():
    montako_hissia = int(input("Montako hissiä luodaan taloon?\n"))
    talo = Talo(montako_hissia)
    print(f"Hissejä luontiin {montako_hissia}.\n")

    pituus = len(talo.hisseja)
    suorita = True
    while suorita:
        milla_hissilla = int(input(f"Millä hissillä haluaisit kulkea? 1 - {pituus}. \n"))

        hissin_alin = talo.hisseja[0].alin_kerros
        hissin_ylin = talo.hisseja[0].ylin_kerros
        minne_matka = int(input(f"Mihin kerrokseen haluaisit mennä? {hissin_alin} - {hissin_ylin}.\n"))
        print()

        talo.aja_hissia(milla_hissilla, minne_matka)
        print()
        for i in range(pituus):
            print(f"Hissi {i+1} on {talo.hisseja[i].nykyinen} kerroksessa.")

        print()
        vastaus = input("Haluatko jatkaa? Tyhjä syöte lopettaa.\n")
        if vastaus == "":
            suorita = False
            print("Toiminto lopetetaan..")


main()
