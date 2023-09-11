def gallons_to_litre(maara):

    while True:
        litre = maara * 3.785
        print(f"{maara} gallonmäärä on litroina {litre}.")
        print()

        maara = float(input("Anna gallonmäärä. Negatiivinen luku lopettaa toiminnon.\n"))
        if maara < 0:
            break

def main():
    gallons = float(input("Anna gallonmäärä. Negatiivinen luku lopettaa toiminnon.\n"))
    if gallons < 0:
        print("Et antanut ollenkaan positiivista gallon määrää!")
    else:
        gallons_to_litre(gallons)

    print()
    print("Toiminto lopetetaan.")


main()