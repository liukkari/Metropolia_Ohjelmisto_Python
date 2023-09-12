lentoasema_pankki = {}


def lisaa():
    lisattava_icao_koodi = input("Lisää nelikirjainen ICAO-koodi. (Esim. EFHK)\n")
    if len(lisattava_icao_koodi) != 4:
        print("ICAO-koodi pitäisi olla nelikirjainen")
        return
    lisattava_icao_koodi = lisattava_icao_koodi.upper()

    lisattava_lentoasema = input("Anna lisättävä lentoaseman nimi. (Esim. Helsinki-Vantaan lentoasema)\n")

    if lisattava_icao_koodi not in lentoasema_pankki:
        if lisattava_lentoasema in lentoasema_pankki.values():
            print("Lisäys epäonnistui!")
            print("Lisäämäsi lentoasema on jo tietopankissa!")
        else:
            lentoasema_pankki[lisattava_icao_koodi] = lisattava_lentoasema
            print("Lisäys onnistui!")

    else:
        print("Lisäys epäonnistui!")
        if lisattava_icao_koodi in lentoasema_pankki:
            print("Lisäämäsi ICAO-koodi on jo tietopankissa!")


def hae():
    haettava_icao_koodi = input("Anna nelikirjainen ICAO-koodi (esim. EFKH),\n"
                                "lentoaseman tiedon hakua varten.\n")
    if len(haettava_icao_koodi) != 4:
        print("ICAO-koodi pitäisi olla nelikirjainen")
        return
    haettava_icao_koodi = haettava_icao_koodi.upper()

    if haettava_icao_koodi in lentoasema_pankki:
        print(f"Haettava tieto löytyi!"
              f" {haettava_icao_koodi} on {lentoasema_pankki[haettava_icao_koodi]}.")
    else:
        print("Ei löytynyt haettava tieto!")


suorita = True

while suorita:

    print()
    syote = input("Haluatko: lisätä (lis), hakea (hae) vai lopettaa (lop) toiminnon?\n")
    syote = syote.upper()
    print()

    if syote == "LIS":
        lisaa()
    elif syote == "HAE":
        hae()
    elif syote == "LOP":
        suorita = False
    else:
        print("Kirjoita joko lis, hae tai lop")

print("Toiminto lopetetaan.")