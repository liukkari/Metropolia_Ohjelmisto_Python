from random import randint

# Tehtävä 6.2

"""Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
    Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
    Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
    kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa."""

def noppa_luoja(puolia):
    lista = []
    while puolia > 0:
        lista.append(puolia)
        puolia -= 1

    lista.sort()
    return lista


def main():
    tahkoja = int(input("Monenko tahkon noppaa haluaisit heittää?\n"))
    print()
    noppa = noppa_luoja(tahkoja)

    maksimisilmaluku = noppa[-1]
    heittoja = 0

    while True:
        luku = randint(1, maksimisilmaluku)
        print(luku)
        heittoja += 1
        if luku == maksimisilmaluku:
            print()
            break

    print(f"Tarvittiin {heittoja} heittoa, että saatiin silmäluku {maksimisilmaluku}.")


main()


