pienin_luku = ""
suurin_luku = ""

while True:
    syote = input("Anna lukuja. Tyhjä syöte lopettaa toiminnon.\n")
    if syote == '':
        if pienin_luku != '' and suurin_luku != '':
            print(f"Pienin luku syötteistäsi on {pienin_luku}")
            print(f"Suurin luku syötteistäsi on {suurin_luku}")

        print()
        print("Toiminto lopetetaan.")
        break
    else:
        syote_numeroksi = float(syote)

        if pienin_luku == '':
            pienin_luku = syote_numeroksi
        if suurin_luku == '':
            suurin_luku = syote_numeroksi

        if syote_numeroksi < pienin_luku:
            pienin_luku = syote_numeroksi
        if syote_numeroksi > suurin_luku:
            suurin_luku = syote_numeroksi