from random import randint


def noppa_luoja(puolia):
    lista = []
    while puolia > 0:
        lista.append(puolia)
        puolia -= 1

    lista.sort()
    return lista


def main():
    tahkoja = int(input("Monenko tahkon noppaa haluaisit heittää?\n"))
    noppa = noppa_luoja(tahkoja)

    maksimisilmaluku = noppa[-1]
    heittoja = 0

    while True:
        luku = randint(1, maksimisilmaluku)
        heittoja += 1
        if luku == maksimisilmaluku:
            break

    print(f"Tarvittiin {heittoja} heittoa, että saatiin silmäluku {maksimisilmaluku}.")


main()


