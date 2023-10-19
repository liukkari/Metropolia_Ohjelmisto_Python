# Tehtävä 4.2

'''Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
    kunnes käyttäjä antaa negatiivisen tuumamäärän.
    Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm'''

while True:
    syote = float(input("Anna tuumia,jotka muutetaan senttimetreiksi. Negatiivinen luku lopettaa toiminnon\n"))
    print()
    if syote < 0:
        print("Negatiivinen luku syötetty.Toiminto lopetetaan.")
        break
    else:
        syote_to_cm = syote * 2.54
        print(f"{syote} tuumaa on {syote_to_cm:.2f} senttimetriä.")
        print()

