# Tehtävä 3.3

'''Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
    Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

    Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.'''

sukupuoli = input("Mikä on biologinen sukupuolesi? (M/N)\n")
hemo_arvo = float(input("Mikä on hemoglobiiniarvosi?\n"))

if sukupuoli == "M":
    if hemo_arvo < 134:
        print("SOS! Hemoglobiiniarvo alhainen!")
    elif hemo_arvo > 195:
        print("SOS! Hemoglobiiniarvo korkea!")
    else:
        print("Kaikki hyvin! Hemoglobiiniarvo normaali!")

elif sukupuoli == "N":
    if hemo_arvo < 117:
        print("SOS! Hemoglobiiniarvo alhainen!")
    elif hemo_arvo > 175:
        print("SOS! Hemoglobiiniarvo korkea!")
    else:
        print("Kaikki hyvin! Hemoglobiiniarvo normaali!")
else:
    print("Oletko taisteluhelikopteri vai mikä?!")
