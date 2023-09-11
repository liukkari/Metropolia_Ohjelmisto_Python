from random import randint


def noppa():
    heittoja = 0
    while True:
        luku = randint(1, 6)
        heittoja += 1
        if luku == 6:
            break
    return heittoja


def main():
    kertoja = noppa()
    print(f"Tarvittiin {kertoja} heittoa, että saatiin silmäluku 6.")


main()
