import math
import random

#Tehtävä1

nimi = input("Mikä on nimesi?\n")
print("Terve,", nimi + "!")

print()

#Tehtävä2

sade = input("Anna ympyrän säde. (cm)\n")
ympyran_pinta_ala = math.pi * float(sade)**2
print(f"Ympyrän pinta-ala on : {ympyran_pinta_ala:.2f}cm")

print()

#Tehtävä3

suorakulmion_kanta = input("Mikä on suorakulmion kannan pituus? (cm)\n")
suorakulmion_korkeus = input("Mikä on suorakulmion korkeus? (cm)\n")

suorakulmion_piiri = float(suorakulmion_korkeus) * 2 + float(suorakulmion_kanta) * 2
suorakulmion_ala = float(suorakulmion_kanta) * float(suorakulmion_korkeus)

print(f"Suorakulmion piiri on : {suorakulmion_piiri}")
print(f"Suorakulmion pinta-ala on: {suorakulmion_ala} ")

print()

#Tehtävä4

kokonaisluku1 = int(input("Anna ensimmäinen kokonaisluku.\n"))
kokonaisluku2 = int(input("Anna toinen kokonaisluku.\n"))
kokonaisluku3 = int(input("Anna kolmas kokonaisluku.\n"))

summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
keskiarvo = summa/3

print(f"Numeroiden summa on : {summa}")
print(f"Numeroiden tulo on : {tulo}")
print(f"Numeroiden keskiarvo on : {keskiarvo}")

print()

#Tehtävä5

leiviskat = input("Anna leiviskät.\n")
naulat = input("Anna naulat.\n")
luodit= input("Anna luodit.\n")

annetut_leiviskat_luodeiksi = float(leiviskat) * 20 * 32
annetut_naulat_luodeiksi = float(naulat) * 32
massa = (annetut_leiviskat_luodeiksi + annetut_naulat_luodeiksi + float(luodit)) * 13.3

kiloja = int(massa//1000)

grammat = massa - kiloja * 1000

print("Massa nykymittojen mukaan:")
print("{} kilogrammaa ja {:.2f} grammaa.".format(kiloja, grammat))

print()

#Tehtävä6

kolmi_koodi = ""
neli_koodi = ""

for i in range(3):
    kolmi_koodi_generointi = random.randint(0, 9)
    kolmi_koodi += str(kolmi_koodi_generointi)

for i in range(4):
    neli_koodi_generointi = random.randint(1, 6)
    neli_koodi += str(neli_koodi_generointi)

print(f"Kolmenumeroisesi koodisi on: {kolmi_koodi}")
print(f"Nelinumeroisesi koodisi on: {neli_koodi}")