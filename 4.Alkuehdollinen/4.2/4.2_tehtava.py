while True:
    syote = float(input("Anna senttimetrejä, joka muutetaan tuumiksi. Negatiivinen luku lopettaa toiminnon\n"))
    if syote < 0:
        print("Toiminto lopetettu.")
        break
    else:
        syote_tuumaksi = syote / 2.54
        print(f"{syote} senttimetriä on {syote_tuumaksi:.2f} tuumaa ")

