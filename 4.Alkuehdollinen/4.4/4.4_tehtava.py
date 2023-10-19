import random

# Tehtävä 4.4

'''Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
    Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
    Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
    Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.'''


arvottu_luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku 1-10.\n"))
    print()
    if arvaus == arvottu_luku:
        print("Oikein!")
        break
    elif arvaus < arvottu_luku:
        print("Liian pieni arvaus.")
        print()
    else:
        print("Liian suuri arvaus.")
        print()
