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
