# Tehtävä 2.5

'''Kirjoita ohjelma, joka kysyy käyttäjältä massan
    keskiaikaisten mittojen mukaan
    leivisköinä, nauloina ja luoteina.
    Ohjelma muuntaa syötteen täysiksi kilogrammoiksi
    ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

    Yksi leiviskä on 20 naulaa.
    Yksi naula on 32 luotia.
    Yksi luoti on 13,3 grammaa.'''

leiviskat = input("Anna leiviskät.\n")
naulat = input("Anna naulat.\n")
luodit= input("Anna luodit.\n")

annetut_leiviskat_luodeiksi = float(leiviskat) * 20 * 32
annetut_naulat_luodeiksi = float(naulat) * 32
massa = (annetut_leiviskat_luodeiksi + annetut_naulat_luodeiksi + float(luodit)) * 13.3

kiloja = int(massa//1000)
grammat = massa - kiloja * 1000

print()
print("Massa nykymittojen mukaan:")
print("{:d} kilogrammaa ja {:.2f} grammaa.".format(kiloja, grammat))