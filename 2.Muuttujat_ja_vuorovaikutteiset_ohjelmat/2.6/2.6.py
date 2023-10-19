import random

# Tehtävä 2.6

'''Kirjoita ohjelma, joka arpoo ja tulostaa
    kaksi erilaista numerolukon koodia:
    kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
    nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
    Vihje: tutustu random.randint()-funktion käyttöön.'''

kolmi_koodi = ""
neli_koodi = ""

print("Generoidaan kolmenumeroisesi koodisi..")
for i in range(3):
    kolmi_koodi_generointi = random.randint(0, 9)
    kolmi_koodi += str(kolmi_koodi_generointi)

print(f"Kolmenumeroisesi koodisi on: {kolmi_koodi}.")
print()

print("Generoidaan nelinumeroisesi koodisi..")
for i in range(4):
    neli_koodi_generointi = random.randint(1, 6)
    neli_koodi += str(neli_koodi_generointi)

print(f"Nelinumeroisesi koodisi on: {neli_koodi}.")