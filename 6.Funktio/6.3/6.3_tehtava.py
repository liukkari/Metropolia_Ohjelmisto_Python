# Tehtävä 6.3

'''Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
    ja palauttaa paluuarvonaan vastaavan litramäärän.
    Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
    Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
    kunnes käyttäjä syöttää negatiivisen gallonamäärän.
    Yksi gallona on 3,785 litraa.'''


def gallons_to_litre(maara):

    while True:
        litre = maara * 3.785
        print(f"{maara} gallonmäärä on {litre} litraa.")
        print()

        maara = float(input("Anna gallonmäärä. Negatiivinen luku lopettaa toiminnon.\n"))
        if maara < 0:
            break


def main():
    gallons = float(input("Anna gallonmäärä. Negatiivinen luku lopettaa toiminnon.\n"))
    print()
    if gallons < 0:
        print("Et antanut ollenkaan positiivista gallon määrää!")
    else:
        gallons_to_litre(gallons)

    print()
    print("Toiminto lopetetaan.")


main()
