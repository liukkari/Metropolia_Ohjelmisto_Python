# Tehtävä 10.3

'''Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
    joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.'''


class Hissi:
    def __init__(self, alin_kerros=1, ylin_kerros=5):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen = alin_kerros

    def siirry_kerrokseen(self, kerros):

        nykyinen_kerros = self.nykyinen
        if nykyinen_kerros == kerros:
            return 1
        elif kerros < self.alin_kerros or kerros > self.ylin_kerros:
            return 2
        else:
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
        tapahtuma = hissinumero.siirry_kerrokseen(matka)
        return tapahtuma

    def palohalytys(self):
        for i in range(len(self.hisseja)):
            hissi = self.hisseja[i]
            hissi.siirry_kerrokseen(1)
            print(f"Hissi {i + 1} on pohjakerroksessa.\n")


def main():
    montako_hissia = int(input("Montako hissiä luodaan taloon?\n"))
    talo = Talo(montako_hissia)
    print(f"Hissejä luontiin {montako_hissia}.\n")

    pituus = len(talo.hisseja)
    suorita = True
    while suorita:
        milla_hissilla = int(input(f"Millä hissillä haluaisit kulkea? 1 - {pituus}. \n"))
        hissi = talo.hisseja[milla_hissilla-1]

        hissin_alin = hissi.alin_kerros
        hissin_ylin = hissi.ylin_kerros
        minne_matka = int(input(f"Mihin kerrokseen haluaisit mennä? {hissin_alin} - {hissin_ylin}.\n"))
        print()

        tapahtuma = talo.aja_hissia(hissi, minne_matka)
        if tapahtuma == 1:
            print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
        elif tapahtuma == 2:
            print(f"Valitsemaasi kerrosta ei löydy välillä {hissin_alin} - {hissin_ylin}. Hissi ei liiku.\n")
        else:
            nykyinen = hissi.nykyinen
            print(f"Olemme kerroksessa {nykyinen}.\n")
        for i in range(pituus):
            print(f"Hissi {i+1:3d} on {talo.hisseja[i].nykyinen} kerroksessa.")

        print()
        palo = input("Laukastaanko palohältys? (N/Y)\n").upper()
        if palo == "Y":
            print()
            talo.palohalytys()

        print()
        vastaus = input("Haluatko jatkaa? Tyhjä syöte lopettaa.\n")
        if vastaus == "":
            suorita = False
            print("Toiminto lopetetaan..")


main()
