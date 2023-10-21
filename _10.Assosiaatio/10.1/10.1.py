# Tehtävä 10.1

'''Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
    Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.

    Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
    tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.

    Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
    missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten,
    että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja
    sen jälkeen takaisin alimpaan kerrokseen.'''


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


def main():
    h = Hissi()
    print("Valitsit kerros 5.\n")
    tapahtuma = h.siirry_kerrokseen(5)

    if tapahtuma == 1:
        print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
    elif tapahtuma == 2:
        print(f"Valitsemaasi kerrosta ei löydy välillä {h.alin_kerros} - {h.ylin_kerros}. Hissi ei liiku.\n")
    else:
        print(f"Olemme kerroksessa {h.nykyinen}.")

    print("Valitisit kerros 5.\n")
    tapahtuma = h.siirry_kerrokseen(5)
    if tapahtuma == 1:
        print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
    elif tapahtuma == 2:
        print(f"Valitsemaasi kerrosta ei löydy välillä {h.alin_kerros} - {h.ylin_kerros}. Hissi ei liiku.\n")
    else:
        print(f"Olemme kerroksessa {h.nykyinen}.")

    print("Valitisit kerros 7.\n")
    tapahtuma = h.siirry_kerrokseen(7)
    if tapahtuma == 1:
        print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
    elif tapahtuma == 2:
        print(f"Valitsemaasi kerrosta ei löydy välillä {h.alin_kerros} - {h.ylin_kerros}. Hissi ei liiku.\n")
    else:
        print(f"Olemme kerroksessa {h.nykyinen}.")

    print("Valitisit kerros 3.\n")
    tapahtuma = h.siirry_kerrokseen(3)
    if tapahtuma == 1:
        print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
    elif tapahtuma == 2:
        print(f"Valitsemaasi kerrosta ei löydy välillä {h.alin_kerros} - {h.ylin_kerros}. Hissi ei liiku.\n")
    else:
        print(f"Olemme kerroksessa {h.nykyinen}.")

    print("Valitisit kerros -1.\n")
    tapahtuma = h.siirry_kerrokseen(-1)
    if tapahtuma == 1:
        print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
    elif tapahtuma == 2:
        print(f"Valitsemaasi kerrosta ei löydy välillä {h.alin_kerros} - {h.ylin_kerros}. Hissi ei liiku.\n")
    else:
        print(f"Olemme kerroksessa {h.nykyinen}.")

    print("Valitisit kerros 1.\n")
    tapahtuma = h.siirry_kerrokseen(1)
    if tapahtuma == 1:
        print("Valitsemasi kerros on nykyinen kerros. Hissi ei liiku.\n")
    elif tapahtuma == 2:
        print(f"Valitsemaasi kerrosta ei löydy välillä {h.alin_kerros} - {h.ylin_kerros}. Hissi ei liiku.\n")
    else:
        print(f"Olemme kerroksessa {h.nykyinen}.")


main()
