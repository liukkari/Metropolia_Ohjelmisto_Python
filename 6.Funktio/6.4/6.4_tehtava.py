def laskin(listaa):
    yhteensa = 0
    for kokonaisluku in listaa:
        yhteensa += kokonaisluku
    return yhteensa


def main():
    lista = []
    while True:
        lukuja = input("Anna kokonaislukuja. Tyhjä syöte lopettaa toiminnon.\n")
        if lukuja == '':
            break
        lukuja = int(lukuja)
        lista.append(lukuja)

    summa = laskin(lista)
    print(f"Kokonaislukujen summa on {summa}.")


main()