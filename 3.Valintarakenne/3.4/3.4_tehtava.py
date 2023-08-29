vuosiluku = int(input("Anna vuosiluku.\n"))

if (vuosiluku % 100) == 0:
    if (vuosiluku % 400) == 0:
        print(f"{vuosiluku} on karkausvuosi.")
    else:
        print(f"{vuosiluku} ei ole karkausvuosi.")

else:
    if (vuosiluku % 4) == 0:
        print(f"{vuosiluku} on karkausvuosi.")
    else:
        print(f"{vuosiluku} ei ole karkausvuosi.")
