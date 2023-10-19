from random import randint

# Tehtävä 6.1

"""Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun
    väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
    Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun."""


def noppa():
    heittoja = 0
    while True:
        luku = randint(1, 6)
        print(luku)
        heittoja += 1
        if luku == 6:
            print()
            break
    return heittoja


def main():
    kertoja = noppa()
    print(f"Tarvittiin {kertoja} heittoa, että saatiin silmäluku 6.")


main()
