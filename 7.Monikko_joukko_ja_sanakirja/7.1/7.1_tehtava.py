# Tehtävä 7.1

'''Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
    jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
    Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
    Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
    että joulukuu on ensimmäinen talvikuukausi.'''


Kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu",
             "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

kuukauden_numero = int(input("Anna kuukauden numero.\n"))
if kuukauden_numero == 12:
    koodi_numero = 11
else:
    koodi_numero = kuukauden_numero - 1
kuukausi = Kuukaudet[koodi_numero]
print()

if kuukauden_numero <= 2 or kuukauden_numero == 12:
    print(f"{kuukausi}:n vuodenaika on Talvi.")
elif 2 < kuukauden_numero <= 5:
    print(f"{kuukausi}:n vuodenaika on Kevät.")
elif 5 < kuukauden_numero <= 8:
    print(f"{kuukausi}:n vuodenaika on Kesä.")
else:
    print(f"{kuukausi}:n vuodenaika on Syksy.")
