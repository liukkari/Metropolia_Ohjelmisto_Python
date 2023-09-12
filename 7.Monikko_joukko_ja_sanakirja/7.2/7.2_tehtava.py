joukko = set()
nimi = ""
suorita = True

while suorita:
    syote = input("Anna nimiä. Tyhjä lopettaa toiminnon\n")
    print()
    if syote == "":
        suorita = False
    else:
        if syote in joukko:
            print(f"{syote} ei lisätty tietorakenteeseen.")
            print(f"{nimi} oli viime syöte, joka lisättiin tietorakenteeseen.")
            continue
        else:
            nimi = syote
            joukko.add(nimi)
            print(f"{nimi} lisättiin tietorakenteeseen.")

print("Tietorakenne sisältää:")
print()
for nimet in joukko:
    print(nimet)
