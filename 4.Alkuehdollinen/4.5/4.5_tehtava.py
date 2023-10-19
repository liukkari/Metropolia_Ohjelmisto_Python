# Tehtävä 4.5

'''Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
    Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
    Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
    Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
    (Oikea käyttäjätunnus on python ja salasana rules).'''

kayttajatunnus = "python"
salasana = "rules"
kertoja = 5

while kertoja != 0:

    syote_tunnus = input("Anna käyttäjätunnus.\n")
    syote_salasana = input("Anna salasana.\n")
    print()

    if syote_tunnus == kayttajatunnus and syote_salasana == salasana:
        print("Tervetuloa.")
        break
    else:
        print("Pääsy evätty.")
        print()

    kertoja -= 1

if kertoja == 0:
    print("Liian monta yritystä! Tili on väliaikaisesti lukittu.")
