# Tehtävä 2.3

'''Kirjoita ohjelma, joka kysyy suorakulmion kannan
 ja korkeuden. Ohjelma tulostaa suorakulmion piirin
ja pinta-alan. Suorakulmion piiri tarkoittaa
 sen neljän sivun yhteispituutta.'''

suorakulmion_kanta = input("Mikä on suorakulmion kannan pituus? (cm)\n")
suorakulmion_korkeus = input("Mikä on suorakulmion korkeus? (cm)\n")

suorakulmion_piiri = float(suorakulmion_korkeus) * 2 + float(suorakulmion_kanta) * 2
suorakulmion_ala = float(suorakulmion_kanta) * float(suorakulmion_korkeus)

print()
print(f"Suorakulmion piiri on: {suorakulmion_piiri:.0f}cm.")
print(f"Suorakulmion pinta-ala on: {suorakulmion_ala:.0f}cm.")