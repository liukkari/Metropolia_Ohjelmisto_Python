# Tehtävä 5.2

'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
    kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
    Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
    Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.'''


lista = []

syote = input("Anna lukuja. Tyhjä lopettaa toiminnon. \n")

if syote == "":
    print("Et antanut ollenkaan lukuja!")
    print("Toiminto lopetetaan.")

else:
    syote = int(syote)
    lista.append(syote)

    while True:
        syote = input("Anna lukuja. Tyhjä lopettaa toiminnon. \n")
        if syote == "":

            lista.sort(reverse=True)
            listan_pituus = len(lista)

            if listan_pituus < 5:
                for i in range(listan_pituus):
                    print(lista[i])
            else:
                for i in range(0, 5):
                    print(lista[i])
                    i += 1

            print()
            print("Toiminto lopetetaan.")
            break
        else:
            syote = int(syote)
            lista.append(syote)