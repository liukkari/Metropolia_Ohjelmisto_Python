# Tehtävä 2.4

'''Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
 Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.'''

kokonaisluku1 = int(input("Anna ensimmäinen kokonaisluku.\n"))
kokonaisluku2 = int(input("Anna toinen kokonaisluku.\n"))
kokonaisluku3 = int(input("Anna kolmas kokonaisluku.\n"))

summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
keskiarvo = summa/3

print()
print(f"Kokonaislukujen summa on: {summa}.")
print(f"Kokonaislukujen tulo on: {tulo}.")
print(f"Kokonaislukujen keskiarvo on: {keskiarvo}.")