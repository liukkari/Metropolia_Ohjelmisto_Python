# Tehtävä 3.2

'''Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
    ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
    Tehtävässä on käytettävä if/elif/else-toistorakennetta.

    LUX on parvekkeellinen hytti yläkannella.
    A on ikkunallinen hytti autokannen yläpuolella.
    B on ikkunaton hytti autokannen yläpuolella.
    C on ikkunaton hytti autokannen alapuolella.
    Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.'''

hyttiluokka = input("Mikä on laivan hyttiluokka? (LUX, A, B vai C)\n")
hyttiluokka = hyttiluokka.upper()
print()

if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")