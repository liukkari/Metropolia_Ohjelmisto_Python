# Tehtävä 6.5

'''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
    Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
    paitsi että siitä on karsittu pois kaikki parittomat luvut.
    Kirjoita testausta varten pääohjelma,jossa luot listan, kutsut funktiota ja tulostat
    sen jälkeen sekä alkuperäisen että karsitun listan.'''


def filtteri(listaa):
    uusi_lista = []
    for luku in listaa:
        if luku == 0:
            continue
        elif (luku % 2) == 0:
            uusi_lista.append(luku)
    return uusi_lista


def main():

    lista = []
    while True:
        syote = input("Anna kokonaislukuja. Tyhjä lopettaa toiminnon.\n")
        print()
        if syote == "":
            muutettu_lista = filtteri(lista)
            break
        else:
            kokonaisluku = int(syote)
            lista.append(kokonaisluku)

    print("Alkuperäinen listasi on:")
    print(lista)
    print()
    print("Editoitu listasi ilman parittomia lukuja on:")
    print(muutettu_lista)


main()
