# Tehtävä 5.4

'''Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
    (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
    Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
    käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.'''

lista = []

print("Syötä 5 kaupungin nimeä.")
print()

for i in range(5):
    kaupunki = input("Syötä kaupungin nimi.\n")
    print()
    lista.append(kaupunki)

print()
print("Syötit:\n")

for tulostus in lista:
    print(tulostus)
