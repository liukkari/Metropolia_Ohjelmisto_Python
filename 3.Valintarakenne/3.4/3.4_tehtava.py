# Tehtävä 3.4

'''Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
    Vuosi on karkausvuosi, jos se on jaollinen neljällä.
    Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.'''

vuosiluku = int(input("Anna vuosiluku.\n"))
print()

if (vuosiluku % 100) == 0:
    if (vuosiluku % 400) == 0:
        print(f"Vuosi {vuosiluku} on karkausvuosi.")
    else:
        print(f"Vuosi {vuosiluku} ei ole karkausvuosi.")

else:
    if (vuosiluku % 4) == 0:
        print(f"Vuosi {vuosiluku} on karkausvuosi.")
    else:
        print(f"Vuosi {vuosiluku} ei ole karkausvuosi.")
