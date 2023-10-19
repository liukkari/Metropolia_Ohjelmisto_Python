# Tehtävä 7.2

'''Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
    kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa
    joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
    syötettiinkö nimi ensimmäistä kertaa.
    Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
    Käytä joukkotietorakennetta nimien tallentamiseen.'''


joukko = set()
nimi = ""
suorita = True

while suorita:
    syote = input("Anna nimiä. Tyhjä lopettaa toiminnon\n")
    print()
    if syote == "":
        suorita = False
    else:
        if syote in joukko:
            print(f"{syote} ei lisätty tietorakenteeseen.")
            print(f"{nimi} oli viime syöte, joka lisättiin tietorakenteeseen.")
        else:
            nimi = syote
            joukko.add(nimi)
            print(f"{nimi} lisättiin tietorakenteeseen.")
    print()

print("Tietorakenne sisältää:")
print()
for nimet in joukko:
    print(nimet)
