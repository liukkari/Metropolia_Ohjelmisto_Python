
kokonaisluku = int(input("Anna kokonaisluku.\n"))

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
    print(f"{kokonaisluku} ei ole alkuluku, koska alkuluvut ovat suurempia kuin luku 1 !")

