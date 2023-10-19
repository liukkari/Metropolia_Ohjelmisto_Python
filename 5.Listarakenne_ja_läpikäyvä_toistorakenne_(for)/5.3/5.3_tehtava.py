# Tehtävä 5.2

'''Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
    Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
    Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
    Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.'''

kokonaisluku = int(input("Anna kokonaisluku.\n"))
print()

if kokonaisluku > 1:
    lista = [1, kokonaisluku]

    for luku in range(2, kokonaisluku):
        if kokonaisluku % luku == 0:
            lista.append(luku)

    listan_pituus = len(lista)
    if listan_pituus == 2:
        print(f"{kokonaisluku} on alkuluku.")
    else:
        print(f"{kokonaisluku} ei ole alkuluku.")

else:
    print(f"{kokonaisluku} ei ole alkuluku, koska alkuluvut ovat suurempia kuin luku 1!")

